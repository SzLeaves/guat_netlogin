#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os
import sys

import src.genconfig as genconfig
import src.login as login
import src.logout as logout


def read_config(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            config = json.load(file)
    except FileNotFoundError as e:
        print("[ERROR] %s: %s" % (e.strerror, path))
        sys.exit(1)

    return config


if __name__ == "__main__":
    error = False
    is_config = os.path.exists("config.json")
    parms = sys.argv[1:]  # read parameters

    # up/down/gen
    if len(parms) == 1:
        if not is_config and parms[0] != 'gen':
            print("There is no configure file.",
                  "Use: '%s gen' option to create new one." % sys.argv[0],
                  "or, Use: '%s --config=' option to specify one." % sys.argv[0], sep='\n')
            sys.exit(1)

        if parms[0] == 'up':
            login.login(read_config("config.json"))
        elif parms[0] == 'down':
            logout.logout(read_config("config.json"))
        elif parms[0] == 'gen':
            genconfig.genconfig()
        else:
            error = True

    # up/down/gen --isp/--config/file_name
    elif len(parms) == 2:
        if not is_config and parms[1][:9] != "--config=":
            print("There is no configure file.",
                  "Use: '%s gen' option to create new one." % sys.argv[0],
                  "or, Use: '%s --config=' option to specify one." % sys.argv[0], sep='\n')
            sys.exit(1)

        if parms[0] == 'up':
            if parms[1][:6] == "--isp=":
                login.login(read_config("config.json"), isp=parms[1][6:])
            elif parms[1][:9] == "--config=":
                login.login(read_config(parms[1][9:]))
            else:
                error = True

        elif parms[0] == 'down' and parms[1][:9] == '--config=':
            logout.logout(read_config(parms[1][9:]))

        elif parms[0] == 'gen':
            genconfig.genconfig(file_name=parms[1])

        else:
            error = True

    # up --isp --config
    elif len(parms) == 3:
        if parms[0] == 'up':
            if parms[1][:6] == "--isp=" and parms[2][:9] == "--config=":
                login.login(read_config(parms[2][9:]), isp=parms[1][6:])
            elif parms[1][:9] == "--config=" and parms[2][:6] == "--isp=":
                login.login(read_config(parms[1][9:]), isp=parms[2][6:])
            else:
                error = True

        else:
            error = True

    # wrong options
    if len(sys.argv) == 1 or error:
        print("Invaild options.")
        print("Use: %s [gen][GEN_FILE_NAME] [up][down][--isp=ISP_NAME][--config=FILE_NAME]" % sys.argv[0])
        sys.exit(1)
