#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import re
import sys
import urllib.error
import urllib.request

login_api = "http://%s/drcom/login?callback=dr1647823658089" \
            "&DDDDD=%s&upass=%s&0MKKey=123456&R1=0&R3=%d&R6=0&para=00&v6ip="
status_api = "http://%s/drcom/chkstatus?callback=dr1648011656431&v=6113"


def request(lip, uid, passwd, isp, msg_list):
    # login network
    try:
        res = urllib.request.urlopen(login_api % (lip, uid, passwd, isp), timeout=5)
        data = str(res.read().decode('gbk')).strip()
    except urllib.error.URLError as e:
        print(e)
        res = data = None

    # show status
    if res.status == 200:
        msg = json.loads(re.findall(r'{.*}', data)[0])
        if msg['result']:
            print("[OK] uid: %s, name: %s" % (msg['uid'], msg['NID']))
            print("[INFO] client: %s, start_time: %s" % (msg['v46ip'], msg['stime']))
        else:
            print("[ERROR] %s" % msg_list[msg['msga']])
            print("[INFO] client: %s, server: %s" % (msg['ss5'], msg['ss6']))
    else:
        print(res.status)
        print(data)


def login(config, isp=None):
    # load response file and isp file
    try:
        with open("resource/error_info.json", 'r', encoding='utf-8') as file:
            msg_list = json.load(file)
        with open("resource/isp_info.json", 'r', encoding='utf-8') as file:
            isp_list = json.load(file)
    except FileNotFoundError as e:
        print(e)
        sys.exit(1)

    # test connection 3 times for gateway
    counts = 0
    print("connection for %s" % config['gateway_ip'])
    while counts < 3:
        try:
            res = urllib.request.urlopen("http://%s" % config['gateway_ip'], timeout=20)
            if res.status == 200:
                break
        except Exception:
            print("try connected again: %d" % (counts + 1))
            counts += 1

    if counts == 3:
        raise ConnectionError("[ERROR] Campus network %s has unavaliable." % config['gateway_ip'])

    # test login status
    print("check login status: ", end='')
    try:
        res = urllib.request.urlopen(status_api % config['gateway_ip'])
        data = str(res.read().decode('gbk')).strip()
        status = json.loads(re.findall(r'{.*}', data)[0])
        is_login = status['result']
    except urllib.error.HTTPError as e:
        print(e)
        sys.exit(1)

    if is_login:
        print(status['uid'], status['NID'])
        print("[ERROR] This account has logged, Please logout it and retry.")
        sys.exit(1)
    else:
        print("no login, ok")

    # isp vaildity
    if config['isp_name'] not in isp_list or (isp and isp not in isp_list):
        print("[ERROR] Specified ISP not exists.")
        sys.exit(1)

    # login network if test was successful
    if isp:
        request(config['gateway_ip'], config['user_id'],
                config['user_passwd'], isp_list[isp], msg_list)
    else:
        request(config['gateway_ip'], config['user_id'],
                config['user_passwd'], isp_list[config['isp_name']], msg_list)
