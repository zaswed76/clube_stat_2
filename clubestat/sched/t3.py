import datetime

date_time = datetime.datetime.now()
print(date_time)
print(type(date_time))



d = "2017-12-15T23:51:24"

dt = datetime.datetime.strptime(d, "%Y-%m-%dT%H:%M:%S")

print("----------------------")
print(dt)
print(type(dt))