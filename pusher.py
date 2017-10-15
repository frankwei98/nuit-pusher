import requests
import schedule
import time

import config
import search


def push(key=config.DEFAULT_SENDKEY, title='Empty Title', message=None):
    """

    :param key: Channel Key, default Value is config.DEFAULT_SENDKEY
    :param title: Title of the message
    :param message: Full-Message,Markdown supported, default Value is None
    """
    request_json = {
        'sendkey': key,
        "text": title,
        "desp": message,
    }
    print(request_json)
    resp = requests.get(
        url=config.API,
        params=request_json
    )
    resp = resp.json()
    return True if resp['code'] == 200 else False


def push_daily():
    push(
        title='每日课表推送',
        # message=search.get_today_msg()
        message=search.get_msg_of_the_day(5, 1)
    )


if __name__ == '__main__':
    schedule.every().day.at("07:30").do(push_daily)
    while True:
        schedule.run_pending()
        time.sleep(1)
