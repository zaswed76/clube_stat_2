from bs4 import BeautifulSoup

class User:
    def __init__(self, title):
        print(333)
        self.title = title
        if self.title:
            self.soup = BeautifulSoup(self.title)
            print(self.soup.findAll("strong")[0].text)
            self.soup.strong.decompose()
            self.soup.br.decompose()
            self.soup.br.decompose()
            self.soup.br.decompose()
            print(self.soup.find_all("body")[0].text)



if __name__ == '__main__':
    line = "<strong>VirusKrolika</strong><br/>Уровень: 23 <br/>Скидка: 11.50% <br/>2017-12-15T09:03:48"
    user = User(line)