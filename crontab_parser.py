
from time_calc import validate_hour_min, time_difference_calculation


def parse_config(filename):
    crontab_list = []
    for line in filename:
        crontab_list.append(line.strip('\n').split(' '))

    return crontab_list


def next_crontab_time(current_time, crontab_list):
        for line in crontab_list:
            crontab_hour = line[1]
            crontab_minute = line[0]
            crontab_command = line[2]
            crontab_validated_time = crontab_time_validator(
                [crontab_minute, crontab_hour])
            if crontab_validated_time:
                result = time_difference_calculation(
                    crontab_validated_time, current_time)
                print(f'{result} - {crontab_command}')


def crontab_time_validator(crontab):
    try:
        # * validate crontab time

        for time_value in crontab:
            if not time_value == '*' and not time_value.isdigit():
                raise ValueError

        crontab_hour = crontab[1]
        crontab_minute = crontab[0]

        # * validate crontab time in digits
        if crontab_hour.isdigit() and crontab_minute.isdigit():
            validate_hour_min(int(crontab_hour), int(crontab_minute))

        elif crontab_hour.isdigit():
            validate_hour_min(int(crontab_hour), 0)

        elif crontab_minute.isdigit():
            validate_hour_min(0, int(crontab_minute))

        else:
            pass

        return {'hour': crontab_hour, 'minute': crontab_minute}

    except:
        print('❗️ Incorrect time format in config file ❗️')
