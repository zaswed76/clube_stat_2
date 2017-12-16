import datetime
import re
line2 = 'Уровень: 0 2017-12-16T19:58:11'
line = """Уровень: 22 Скидка: 03.326% 2017-12-16T15:51:08 (абонемент) """




def get_level(line):
    p = re.compile('(Уровень:)\s*(\d+)', re.IGNORECASE)
    res = p.search(line)
    if res:
        return res.group(2)

def get_discount(line):
    p = re.compile('(Скидка:)\s*(\d+[.,]?\d*[%]?)', re.IGNORECASE)
    res = p.search(line)
    if res:
        return res.group(2)

def get_date_start(line):
    lst = line.split(" ")

    for d in lst:
        try:
            dt = datetime.datetime.strptime(d, "%Y-%m-%dT%H:%M:%S")
        except Exception as er:
            pass
        else:
            return {"line": d, "datetime": dt}

def get_subscription(line):
    p = re.compile('абонемент', re.IGNORECASE)
    res = p.search(line)
    if res:
        return res.group()



# print(datetime.datetime.strptime("2017-12-16T15:51:08", "%Y-%m-%dT%H:%M:%S"))
print(get_subscription(line2))