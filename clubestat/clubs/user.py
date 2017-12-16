import copy
import datetime
import re

from bs4 import BeautifulSoup

LEVEL_PATTERN = re.compile('(Уровень:)\s*(\d+)', re.IGNORECASE)
DISCOUNT_PATTERN = re.compile('(Скидка:)\s*(\d+[.,]?\d*[%]?)',
                              re.IGNORECASE)
SUBSCRIPTION_PATTERN = re.compile('абонемент', re.IGNORECASE)


def norm(line):
    return re.sub(r'&gt;', '>', re.sub(r'&lt;', '<', line))


def get_level(line, p):
    res = p.search(line)
    if res:
        return res.group(2)


def get_discount(line, p):
    res = p.search(line)
    if res:
        return res.group(2)


def get_date_start(line):
    """

    :param line: str title
    :return: dict(str, datetime) or None
    """
    lst = line.split(" ")
    for d in lst:
        try:
            dt = datetime.datetime.strptime(d, "%Y-%m-%dT%H:%M:%S")
        except Exception as er:
            pass
        else:
            return {"line": d, "datetime": dt}


def get_subscription(line, p):
    res = p.search(line)
    if res:
        return res.group()


class User:
    def __init__(self, title):
        if title:
            self.title = norm(title)
            self.soup = BeautifulSoup(title, "lxml")
            self.soup_copy = copy.deepcopy(self.soup)
            self.soup_copy.strong.decompose()
            self.title = self.soup_copy.get_text()

    @property
    def login(self):
        return self.soup.find("strong").get_text()

    @property
    def level(self):
        return get_level(self.title, LEVEL_PATTERN)

    @property
    def discount(self):
        return get_discount(self.title, DISCOUNT_PATTERN)

    @property
    def subscription(self):
        return get_subscription(self.title, SUBSCRIPTION_PATTERN)

    @property
    def time_start(self):
        return get_date_start(self.title)

    def __repr__(self):
        return "{}; {}, {}; {}, {}".format(self.login, self.level,
                                           self.discount,
                                           self.time_start,
                                           self.subscription)


if __name__ == '__main__':
    pass
    line = "<strong>VirusKrolika</strong><br/>Уровень: 23 <br/>Скидка: 11.50% <br/>2017-12-15T09:03:48"

    title = "&lt;strong&gt;075668171040&lt;/strong&gt;&lt;br/&gt;Уровень: 0 &lt;br/&gt;2017-12-15T23:51:24"
    # #
    #
    # import re
    #

    # # print(result2)
    usr = User(line)
    print(usr)
