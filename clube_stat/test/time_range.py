import arrow
from datetime import datetime

start = datetime(2017, 12, 27, 9, 0)
end = datetime(2017, 12, 30, 9, 0)
for r in arrow.Arrow.span_range('hour', start, end):
     print(r[0].hour)