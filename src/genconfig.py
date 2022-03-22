#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import getpass
import json
import os
import sys


def genconfig(file_name=None):
    config = dict()
    if not file_name:
        save_file = "config.json"
    else:
        save_file = "%s.json" % file_name

    print("Generate new file %s" % save_file)
    config['gateway_ip'] = input("enter network login address: ")
    config['user_id'] = input("enter your campus id: ")
    config['user_passwd'] = getpass.getpass("enter your password: ")
    config['isp_name'] = input("enter your isp name (campus/telecom/unicom/mobile): ")

    if os.path.exists(save_file):
        print("Configure file was existd, Overwrite? (y/n): ", end='')
        op = input()
        if op == 'Y' or op == 'y':
            pass
        else:
            print("cancel.")
            sys.exit(0)

    try:
        with open(save_file, 'w', encoding='utf-8') as file:
            json.dump(config, file, ensure_ascii=False)
    except IOError as e:
        print(e)
        print("[ERROR] Configure file generated faild.")
        sys.exit(1)

    print("Configure file generated successful.",
          "Use: %s up to login network." % sys.argv[0],
          "Use: %s down to logout network." % sys.argv[0],
          "or, Use: '%s --config=' option to specify a configure file.", sep='\n')
