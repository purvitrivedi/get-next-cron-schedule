#!/usr/bin/env python3

import sys
import select

from time_calc import validate_time_format
from crontab_parser import parse_config, next_crontab_time



def main():
    try:
        if len(sys.argv) != 2:
            raise IndexError

        if not select.select([sys.stdin, ], [], [], 0.0)[0]:
            raise IndexError

        current_time = sys.argv[1]
        validated_current_time = validate_time_format(current_time)

        if validated_current_time:
            crontab_list = parse_config(sys.stdin)
            return next_crontab_time(validated_current_time, crontab_list)

    except IndexError:
        if len(sys.argv) != 2:
            print('''
            ❗️ Error: Please input the current time as HH:MM❗️

            Your command line input should follow the following format:
            ​./application.py HH:MM < config

            Example command line 👇

            ​./application.py 17:30 < config

            ''')
        else:
            print('''
            ❗️ Error: Please provide standard input ❗️

            Your command line input should follow the following format to provide STDIN:
            ​./application.py HH:MM < config

            Example command line 👇

            ​./application.py 17:30 < config

            ''')


if __name__ == '__main__':
    main()
