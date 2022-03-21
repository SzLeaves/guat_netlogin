#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import getpass
import json
import os
import sys


def genconfig():
    if os.path.exists("config.json"):
        print("Configure file was existd, Overwrite? (y/n): ", end='')
        op = input()
        if op == 'N' or op == 'n':
            print("Bye.")
            sys.exit(0)

    config = dict()
    print("Generate new file.")
    config['gateway_ip'] = input("enter network login address: ")
    config['user_id'] = input("enter your campus id: ")
    config['user_passwd'] = getpass.getpass("enter your password: ")
    config['isp_name'] = input("enter your isp name (campus/telecom/unicom/mobile): ")

    try:
        with open("config.json", "w") as file:
            json.dump(config, file, ensure_ascii=False)
    except IOError as e:
        print(e)
        print("Configure file generated faild.")
        sys.exit(1)
