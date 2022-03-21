#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import os
import sys

import src.genconfig as genconfig
import src.login as login
import src.logout as logout

if __name__ == "__main__":
    flag = False
    # load response file
    with open("resource/error_info.json", 'r', encoding='utf-8') as file:
        msg_list = json.load(file)

    if len(sys.argv) > 1:
        # generate configure
        if sys.argv[1] == "gen":
            genconfig.genconfig()
            print("Configure file generated successful.",
                  "Use: %s up to login network." % sys.argv[0],
                  "Use: %s down to logout network." % sys.argv[0], sep='\n')

        # login network
        elif sys.argv[1] == "up":
            if os.path.exists("config.json"):
                # load configure file
                isp_list = {'campus': 0, 'telecom': 1, 'unicom': 2, 'mobile': 3}
                with open("config.json", 'r', encoding='utf-8') as file:
                    config = json.load(file)

                # choose isp
                if len(sys.argv) == 3:
                    if sys.argv[2] in isp_list:
                        login.login(config, msg_list, isp=isp_list[sys.argv[2]])
                    else:
                        print("invaild option '%s'" % sys.argv[2])
                        flag = True

                # normal
                elif len(sys.argv) == 2:
                    login.login(config, msg_list)

            else:
                genconfig.genconfig()
                print("Configure file generated successful.",
                      "Use: %s up to login network." % sys.argv[0],
                      "Use: %s down to logout network." % sys.argv[0], sep='\n')

        # logout network
        elif sys.argv[1] == 'down':
            if os.path.exists("config.json"):
                # load configure file
                with open("config.json", 'r', encoding='utf-8') as file:
                    config = json.load(file)

                logout.logout(config, msg_list)
            else:
                genconfig.genconfig()
                print("Configure file generated successful.",
                      "Use: %s up to login network." % sys.argv[0],
                      "Use: %s down to logout network." % sys.argv[0], sep='\n')

    if flag or len(sys.argv) == 1:
        print("Use: %s [gen] [down] [up][campus|telecom|unicom|mobile]" % sys.argv[0])
        sys.exit(1)
