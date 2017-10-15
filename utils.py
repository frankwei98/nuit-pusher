import json
from datetime import date

import config

order_to_time = {
    1: '08:40-10:00',
    3: '14:10-15:30',
    4: '15:50-17:10',
    5: '18:30-19:50',
    2: '10:20-11:40',
    6: '20:10-21:30',
}

list_of_common_weekday_str = [
    {'星期一': 1}, {'周一': 1},
    {'星期二': 2}, {'周二': 2},
    {'星期三': 3}, {'周三': 3},
    {'星期四': 4}, {'周四': 4},
    {'星期五': 5}, {'周五': 5},
    {'星期六': 6}, {'周六': 6},
    {'星期日': 7}, {'周日': 7}
]


def get_id_by_weekday(_str):
    def get_element(elem):
        if _str in elem:
            return elem[_str]

    res = list(filter(get_element, list_of_common_weekday_str))
    return res[0][_str]


def int2cn(s):
    """

    :param s:
    :return:
    """
    s = str(s)
    d = {
        '1': '一',
        '2': '二',
        '3': '三',
        '4': '四',
        '5': '五',
        '6': '六',
        '7': '日',
    }
    return d[s]


def get_time(array_of_order):
    actual_order = int(array_of_order[1] / 2)
    return order_to_time[actual_order]


def get_date_from_week(week=0, weekday=0):
    """

    :param week: the weekly_data that need located
    :param weekday: the day start from monday
    :return: A date object indicate the date itself
    """
    week_diff = config.timedelta(weeks=week - 1, days=weekday)  # because weekly_data start from 0, not 1
    return config.FIRST_DAY + week_diff


def get_today_week_weekday_from_date():
    """

    :return:
    """
    return get_week_weekday_from_date(date.today())


def get_week_weekday_from_date(_date):
    """

    :param _date:
    :return:
    """
    week_diff = _date - date(2017, 9, 18)
    weeks = int(week_diff.days / 7) + 1
    days = (week_diff.days % 7) + 1
    return {'weeks': weeks, 'weekdays': days}


def diff_from_today(week=0, weekday=0):
    """

    :param week:
    :param weekday:
    :return:
    """
    return config.date.today() - config.timedelta(weeks=week - 1, days=weekday)


def get_simple(lesson):
    """

    :param lesson: a lesson
    :return: User-reading-friendly information about lesson
    """
    return {
        '课程名称': lesson['name'],
        '教室': lesson['classRoom'],
        # 'translate': int2cn(str(lesson['weekday'])),
        '时间': order_to_time[lesson['order']],
    }


def get_reply_lesson_msg(lesson):
    return '**{name}** *@{location}* {time}'.format(
        name=lesson['name'],
        location=lesson['classRoom'],
        time=order_to_time[lesson['order']]
    )


def days_left():
    """

    :return: A countdown message
    """
    return '离最后一节课还有 {} 天'.format(
        (config.LAST_DAY - date.today()).days
    )


# for test
if __name__ == '__main__':
    print(get_date_from_week(week=4, weekday=5).weekday())  # 4 weeks later
    print(get_date_from_week(week=4, weekday=1))  # 4 weeks later
    print(config.LAST_DAY)
    print(days_left())
