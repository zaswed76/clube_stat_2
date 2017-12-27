# import arrow
#
# start = arrow.Arrow(2017, 12, 27, 9, 0)
# end = arrow.Arrow(2017, 12, 30, 9, 0)
# for r in arrow.Arrow.range('hour', start, end):
#      print(r.hour)

import prettytable

table = prettytable.PrettyTable(["x", "y"])
table.add_row([1, 2])
print(table)