#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import re
import urllib.error
import urllib.request

logout_api = "http://%s/drcom/logout?callback=dr1647825375804"


def request(lip, msg_list):
    try:
        res = urllib.request.urlopen(logout_api % lip, timeout=5)
        data = str(res.read().decode('gbk')).strip()
    except urllib.error.URLError as e:
        print(e)
        res = data = None

    msg = json.loads(re.findall(r'{.*}', data)[0])
    if res.status == 200:
        if msg['result']:
            print("[OK] uid: %s" % msg['uid'])
            print("[INFO] client: %s, server: %s" % (msg['ss5'], msg['ss6']))
        else:
            print("[ERROR] %s" % msg_list[msg['msga']])
            print("[INFO] client: %s, server: %s" % (msg['ss5'], msg['ss6']))
    else:
        print(res.status)
        print(data)


def logout(config, msg_list):
    counts = 0

    # test connection 5 times for gateway
    print("connection for %s" % config['gateway_ip'])
    while counts < 5:
        try:
            res = urllib.request.urlopen("http://%s" % config['gateway_ip'], timeout=15)
            if res.status == 200:
                break
        except Exception:
            print("try connected again: %d" % (counts + 1))
            counts += 1

    # login network if test was successful
    if counts == 5:
        raise ConnectionError("[ERROR] Campus network %s has unavaliable." % config['gateway_ip'])
    else:
        request(config['gateway_ip'], msg_list)
