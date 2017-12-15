from bs4 import BeautifulSoup


def user(title):
    if title:
        soup = BeautifulSoup(title, 'html.parser')

        login = soup.find("strong").get_text()

        soup.strong.decompose()
        soup.br.decompose()
        soup.br.decompose()
        soup.br.decompose()
        title = soup.get_text()
        return {"login": login, "title": title}


if __name__ == '__main__':
    line = "<strong>VirusKrolika</strong><br/>Уровень: 23 <br/>Скидка: 11.50% <br/>2017-12-15T09:03:48"

    line2 = "&lt;strong&gt;kristich&lt;/strong&gt;&lt;br/&gt;Уровень: 46 &lt;br/&gt;Скидка: 23.00% &lt;br/&gt;2017-12-15T13:59:36"
    usr = user(line)