import json
from functools import reduce

import utils


def search(week, weekday):
    """

    :param week: the order of week, like 1 to 16
    :param weekday: the order of weekday, like Mon is 1, Sun is 7
    :return: lessons schedule
    """
    with open(
            './weekly_data/{}.json'.format(week),
            'r',
            encoding='utf-8'
    ) as f:
        file = json.load(f)
        lessons = file['lessons']

        def filter_lesson(lesson):
            """
            对 lessons 的元素 lesson 做 filter_lesson(),
            若成立则进入filtered_result
            :param lesson: lessons 的元素 lesson
            :return: Boolean: True or False
            """
            return weekday == lesson['weekday']

        filtered_result = filter(
            filter_lesson,
            lessons
        )

    return sorted(
        filtered_result,
        key=lambda l: l['order']
    )


def get_msg_of_the_day(week, weekday):
    """

    :param week: week
    :param weekday: weekday
    :return: The message that user-reading-friendly
    """
    result = list(
        search(week, weekday)
    )
    if not result:
        # For sequences, (strings, lists, tuples),
        # use the fact that empty sequences are false.
        return_str = '今天星期{} 没课! 一起出去耍吧～'.format(utils.int2cn(str(weekday)))
    else:
        return_str = '今天是第{}周星期{}，一共有{}节课，课程如下 \n\n'.format(
            week,
            utils.int2cn(str(weekday)),
            len(result),
        )
        return_str += reduce(
            lambda x, y: '{}\n\n{}'.format(x, y),
            map(utils.get_reply_lesson_msg, result)
        )

    return return_str


def get_today_msg():
    schedule = utils.get_today_week_weekday_from_date()
    return get_msg_of_the_day(schedule['weeks'], schedule['weekdays'])


if __name__ == '__main__':
    # print today's schedule
    print(get_today_msg())
    search_week = int(input('请输入第几周(阿拉伯数字)'))
    search_weekday = int(input('请输入星期几(阿拉伯数字)'))
    print(get_msg_of_the_day(search_week, search_weekday))
