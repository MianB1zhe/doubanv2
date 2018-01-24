# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import datetime

def str2date(date_str):
    if len(date_str.split(' ')) >1 :
        dates = [int(i) for i in date_str.split(' ')[0].split('-')]
        times = [int(i) for i in date_str.split(' ')[1].split(':')]
        date = datetime.datetime(dates[0], dates[1], dates[2], times[0], times[1], times[2])
    elif len(date_str.split('-')) == 3:
        dates = [int(i) for i in date_str.split(' ')[0].split('-')]
        date = datetime.datetime(dates[0], dates[1], dates[2])
    else:
        dates = [int(i) for i in date_str.split(' ')[0].split('-')]
        date = datetime.datetime(dates[0], dates[1], 1)

    return date

if __name__ == '__main__':
    print str2date('2017-03-17 16:32:43')
    print str2date('2013-03-12')
    print str2date('2013-12')