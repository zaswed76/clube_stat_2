from bs4 import BeautifulSoup


def user(title):
    if title:
        soup = BeautifulSoup(title, "lxml")


        login = soup.find("strong").get_text()

        soup.strong.decompose()
        # soup.br.decompose()
        # soup.br.decompose()
        # soup.br.decompose()
        title = soup.get_text()
        return {"login": login, "title": title}


if __name__ == '__main__':
    line = "<strong>VirusKrolika</strong><br/>Уровень: 23 <br/>Скидка: 11.50% <br/>2017-12-15T09:03:48"

    title="&lt;strong&gt;075668171040&lt;/strong&gt;&lt;br/&gt;Уровень: 0 &lt;br/&gt;2017-12-15T23:51:24"
    #

    import re

    result = re.sub(r'&lt;', '<', line)
    result2 = re.sub(r'&gt;', '>', result)
    # print(result2)
    usr = user(result2)
    print(usr)


