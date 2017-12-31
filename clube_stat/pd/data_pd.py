
from datetime import datetime
from pandas import Series, to_datetime


def to_date_time(dates_line):
    res = []
    for dl in dates_line:
        res.append(datetime.strptime(dl, '%Y-%m-%d %H:%M:%S'))
    return res



dates = ['2017-12-30 09:30:12',
         '2017-12-30 09:35:12',
         '2017-12-30 09:40:12',
         '2017-12-30 09:45:12',
         '2017-12-30 09:50:12',
         '2017-12-30 09:55:12',
         '2017-12-31 1:00:12',
         '2017-12-31 2:00:12',
         '2017-12-31 3:00:12']



pds = to_datetime(Series(dates))

st = '2017-12-30 09:45:00'
end = '2017-12-31 2:00:59'


print(pds[pds >= st][pds <= end])