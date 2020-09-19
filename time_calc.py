import sys


def validate_time_format(time):
    try:
        # * check the length
        if len(time) < 4:
            raise ValueError
        time = time.split(':')

        # * check if the split was correct
        if len(time) < 2:
            raise ValueError

        # * check if values can be converted to int

        time_to_int = [int(item) for item in time]


        hour = time_to_int[0]
        minute = time_to_int[1]

        # * check if hour and minute are in the correct range
        
        if validate_hour_min(hour, minute):
            return {'hour': hour, 'minute': minute}

    except ValueError:
        if len(time) < 2:
            print('''

            ❗️ Error: ':' missing from your current time input ❗️

            Time should be provided in HH:MM format, eg: 17:30

            Example command line 👇

            ​./application.py 17:30 < config

            ''')
        else:
            print('''

            ❗️ Error: Please use the format provided below to input current time ❗️

            Time should be provided in HH:MM format, eg: 01:30

            Example command line 👇

            ./application.py 01:30 < config

            ''')


def validate_hour_min(hour, minute):
    time_min = 00
    hour_max = 23
    minute_max = 59
    try:
        if not (time_min <= hour <= hour_max and time_min <= minute <= minute_max):
            raise ValueError

        return True
    except:
        if not time_min <= hour <= hour_max:
            print(f'''
            ❗️ Error: Hour value {hour} is out of bounds in command line input or config file ❗️
            
            👉 The value of hour must be within {time_min} and {hour_max}
            ''')
        if not time_min <= minute <= minute_max:
            print(f'''
            ❗️ Error: Minute value {minute} is out of bounds in command line input or config file ❗️
            👉 The value of minute must be within {time_min} and {minute_max}
            ''')
        sys.exit()


def time_difference_calculation(crontab_time, current_time):
    today = 'today'
    tomorrow = 'tomorrow'

    current_time['minute'] = str(current_time['minute']).zfill(2)
    current_time['hour'] = str(current_time['hour']).zfill(2)

    if crontab_time['hour'].isdigit():
        difference = int(crontab_time['hour']) - int(current_time['hour'])

        if difference < 0:
            if crontab_time['minute'].isdigit():
                return f'{crontab_time["hour"]}:{crontab_time["minute"]} {tomorrow}'
            else:
                return f'{crontab_time["hour"]}:00 {tomorrow}'

        elif difference > 0:
            if crontab_time['minute'].isdigit():
                return f'{crontab_time["hour"]}:{crontab_time["minute"]} {today}'
            else:
                return f'{crontab_time["hour"]}:00 {today}'

        elif difference == 0:
            if crontab_time['minute'].isdigit():
                minute_difference = int(crontab_time['minute']) - int(current_time['minute'])
                if minute_difference == 0:
                    return f'{current_time["hour"]}:{current_time["minute"]} {today}'
                elif minute_difference < 0:
                    return f'{current_time["hour"]}:{crontab_time["minute"]} {tomorrow}'
                else:
                    return f'{current_time["hour"]}:{crontab_time["minute"]} {today}'
            elif not crontab_time['minute'].isdigit() and  crontab_time['hour'].isdigit():
                return f'{crontab_time["hour"]}:{current_time["minute"]} {today}'
            else:
                return f'{crontab_time["hour"]}:00 {tomorrow}'


    elif crontab_time['minute'].isdigit():
        difference = int(crontab_time['minute']) - int(current_time['minute'])

        if difference > 0:
            return f'{current_time["hour"]}:{crontab_time["minute"]} {today}'
        elif difference < 0:
            if int(current_time['hour']) < 23:
                return f'{str(int(current_time["hour"]) + 1).zfill(2)}:{crontab_time["minute"]} {today}'
            else:
                return f'00:{crontab_time["minute"]} {tomorrow}'
        else:
            return f'{current_time["hour"]}:{current_time["minute"]} {today}'

    else:
        return f'{current_time["hour"]}:{current_time["minute"]} {today}'
