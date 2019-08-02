import time
import datetime


#   publish_time is stored and retrieved from a database or object.
#   now = times.right_now()
#   pub = story.publish_time
#   sentence = decorate_time(pub, now)
#   print(sentence)
#       >> '6 hours ago'


def right_now():
    return datetime.datetime.now()


def decorate_time(*args):
    return render_time(*elapsed_time(*args))


def days_hours_minutes(td):
    #   /   => Integer
    #   //  => Float
    days = td.days
    hours =  td.seconds//3600
    minutes = (td.seconds//60)%60
    # seconds = td.seconds
    return days, hours, minutes # ,seconds


def elapsed_time(*args, as_dict=False):
    if len(args) is 1:
        td = args[0]
    else:
        td = args[-1] - args[0]
    d, h, m = days_hours_minutes(td)
    if not as_dict:
        return d, h, m
    else:
        return dict(
            day=d,
            hour=h,
            min=m,
        )


def render_time(day, hour, minute):
    '''
    Examples:
        (0, 0, 16)    =>  "16 minutes ago"
        (0, 1, 8)     =>  "1 hour ago"
        (1, 10, 45)   =>  "1 day ago"
        (8, 3, 51)   =>  "1 week ago"

    >>  td = datetime.timedelta(days=1, seconds=22345)
    >>  d, h, m = elapsed_time(td)
    >>  sentence = render_time(d, h, m)

        1 day ago

    '''
    plural = 's'
    num = 0
    label = ''

    if (day is 0) and (hour is 0) and (minute is 0):
        return 'Just Now'

    elif day > 6:
        num = day//7
        if num is 1:
            plural = ''
        label = 'week'

    elif day > 0:
        num = day
        if num is 1:
            plural = ''
        label = 'day'

    elif hour > 0:
        num = hour
        if num is 1:
            plural = ''
        label = 'hour'

    else:
        num = minute
        if num is 1:
            plural = ''
        label = 'minute'

    return f'{num} {label}{plural} ago'



if __name__ == '__main__':
    def main0():
        t1 = datetime.datetime.now()
        time.sleep(2)
        t2 = datetime.datetime.now()
        d, h, m = elapsed_time(t2 - t1)
        sentence = render_time(d, h, m)
        print(sentence)
    def main1():
        td = datetime.timedelta(days=1, seconds=22345)
        d, h, m = elapsed_time(td)
        sentence = render_time(d, h, m)
        print(sentence)
    def main2():
        td = datetime.timedelta(days=0, seconds=345)
        d, h, m = elapsed_time(td)
        sentence = render_time(d, h, m)
        print(sentence)
    def main3():
        td = datetime.timedelta(days=8, seconds=29345)
        d, h, m = elapsed_time(td)
        sentence = render_time(d, h, m)
        print(sentence)
    def main4():
        td = datetime.timedelta(days=8, seconds=29345)
        sentence = decorate_time(td)
        print(sentence)

    main0()
    main1()
    main2()
    main3()
    main4()
