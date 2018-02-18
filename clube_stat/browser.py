import datetime
import os
import time
from selenium import common
import selenium.webdriver.chrome.service as service
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select



ignored_exceptions = (common.exceptions.NoSuchElementException,
                      common.exceptions.StaleElementReferenceException,)
from clube_stat.clubs.user import User


# log = lg.log(os.path.join(pth.LOG_DIR, "scr_web.log"))


class Browser:
    def __init__(self, driver_pth, binary_pth, adr, login_id,
                 password_id, submit_name,
                 login, password, log=None):
        self.log = log
        self.adr = adr
        self.password = password
        self.login = login
        self.submit_name = submit_name
        self.password_id = password_id
        self.login_id = login_id
        self.binary_pth = binary_pth
        self.driver_pth = driver_pth

        # self.service = service.Service(self.driver_pth)
        # self.service.start()
        self.driver = self.get_driver()


    def hide_window(self):
        self.driver.set_window_position(-5000, 0)

    def get_driver(self):
    #     capabilities = {'chrome.binary': self.binary_pth,
    #                     'chrome.switches': ['--disable-logging']}
    #     #
    #     #
    #     driver = webdriver.Remote(self.service.service_url,
    #                               capabilities)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--ignore-certificate-errors")
        driver = webdriver.Chrome(executable_path=self.driver_pth,
                                  chrome_options=chrome_options)
        return driver

    def get_page(self):
        self.driver.get(self.adr)

    def log_in(self):
        username = self.driver.find_element_by_id(self.login_id)
        username.send_keys(self.login)
        passw = self.driver.find_element_by_id(self.password_id)
        passw.send_keys(self.password)
        m = self.driver.find_element_by_class_name(self.submit_name)
        m.click()

    def get_table(self):
        table = []
        text = self.driver.page_source
        soup = BeautifulSoup(text, "lxml")
        soup_table = soup.find('table', id="map")
        for tr in soup_table.find_all('tr'):
            for i in tr:
                r = i.findAll("span")
                if r:
                    tag = r[0]
                    # if tag["class"][1] != 'bg_off':
                    title = tag["title"]
                    if title:
                        usr = User(title)
                        login = usr.login
                        level = usr.level
                        discount = usr.discount
                        subscription = usr.subscription
                        time_start = usr.time_start
                    else:
                        login, level, discount, subscription, time_start = (
                            None, None, None, None, None)
                    line = (
                        tag.text,
                        tag["class"][1],
                        tag["data-id"],
                        tag["data-ip"],
                        tag["data-mac"],
                        tag["data-unauth"],
                        tag["id"],
                        login, level, discount, subscription,
                        time_start)
                    table.append(line)
        return table

    def select_club(self, club: str):
        select = Select(self.driver.find_element_by_id('club_id'))
        select.select_by_value(club)

    def select_club_by_name(self, club_name):
        select = Select(self.driver.find_element_by_id('club_id'))
        select.select_by_visible_text(club_name)

    def get_data(self, field):
        get_data_error_limit = 10
        while True:
            try:
                res = self.driver.find_element_by_id(field).text
            except Exception as ex:
                if get_data_error_limit:
                    get_data_error_limit -= 1
                    time.sleep(1)
                    self.get_page()
                    self.log.error(ex)
                    continue
                else: return "none"
            else:
                return res

    def close(self):
        self.driver.quit()


if __name__ == '__main__':
    from clube_stat import service as sv
    from clube_stat import pth
    from clube_stat.db import sql_tables, sql_keeper
    from clube_stat.clubs.club import Club, Clubs
    import time

    clubs = Clubs()
    clubs.add_club(Club(Club.LES, 40))
    clubs.add_club(Club(Club.TROYA, 40))
    adr = "http://adminold.itland.enes.tech/index.php/map"
    login_id = 'enter_login'
    password_id = 'enter_password'
    submit_name = 'but_m'
    login = "zaswed"
    password = "fasadAQ9"

    cfg = sv.load(pth.CONFIG_PATH)

    driver_pth = os.path.join(pth.DRIVERS_DIR,
                              cfg["driver"])
    binary_pth = os.path.abspath(cfg["binary_browser_pth"])
    driver = Browser(driver_pth, binary_pth, adr, login_id,
                     password_id, submit_name,
                     login, password)
    driver.get_page()
    driver.log_in()

    # driver.select_club("4")
    time.sleep(5)
    driver.select_club_by_name(clubs["troya"].field_name)
    select = Select(driver.driver.find_element_by_id('club_id'))
    selected_option = select.first_selected_option
    print(selected_option.text.strip())

    #
    # table = driver.get_table()
    # # #
    # keeper = sql_keeper.Keeper(
    #     os.path.join(pth.DATA_DIR, cfg["sql_data"]))
    # keeper.open_connect()
    # keeper.open_cursor()
    # keeper.create_table(map_sql_table.table())
    # #
    # date_time = datetime.datetime.now()
    # date = date_time.date()
    # h = date_time.time().hour
    # minute = date_time.time().minute
    # club = clubs["les"].field_name
    #
    # seq = []
    # s = [date, date_time, h, minute, club]
    # temp_lst = []
    # for line in table:
    #     # print(line)
    #     # print("--------------")
    #     temp_lst.extend(s)
    #     temp_lst.extend(line)
    #     seq.append(temp_lst.copy())
    #     temp_lst.clear()
    #
    # keeper.add_lines(sql_keeper.ins_table_stat(), seq)
    # keeper.commit()
    # keeper.close()
    # driver.close()
