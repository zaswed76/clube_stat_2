import os
import time

import sys
import selenium
import win32gui, win32con

from clube_stat import service, pth
from clube_stat.log import log as lg
from clube_stat.browser import Browser
from clube_stat.db import sql_keeper, map_sql_table
from clube_stat.clubs.club import Club, Clubs


_cfg = service.load(pth.CONFIG_PATH)
log = lg.log(os.path.join(pth.LOG_DIR, "scr.log"))
HIDE = False
LIMIT_ERROR = 3
def hide_browser(v):
    if v:
        win32gui.ShowWindow(win32gui.GetForegroundWindow(),
                        win32con.SW_MINIMIZE)

def log_in(browser, login, password):
    login_id = 'enter_login'
    password_id = 'enter_password'
    submit_name = 'but_m'


    log.debug("log - {}, pass - {}".format(login, password))
    browser.log_in(login_id, password_id, submit_name, login,
                   password)
    time.sleep(2)
    if "Карта клуба" in browser.driver.title:
        print("вошли в карту клуба")
    else:
        log.error("не правильная пара логин - пароль")
        input("нажмите  < ENTER > что бы выйти")
        print("программа будет закрыта")
        time.sleep(1)
        browser.close()
        sys.exit(1)

def get_clubs():
    clubs = Clubs()
    clubs.add_club(Club(Club.LES, 50))
    clubs.add_club(Club(Club.TROYA, 50))
    clubs.add_club(Club(Club.AKADEM, 50))
    clubs.add_club(Club(Club.DREAM, 50))
    return clubs

def write_data():
    pass

def read_data(browser, clubs):
    for club in clubs.values():
        try:
            browser.select_club_by_name(club.field_name)
        except Exception as er:
            log.error(er)
            browser.close()
            log.debug("browser close")
            time.sleep(2)
            return False
        else:
            table = browser.get_table()
            log.debug("right in data - OK")
            time.sleep(4)
    else:
        return True
def scr_run(driver_pth, binary_pth, adr, clubs, login, password):
    errors = 0
    keeper = sql_keeper.Keeper(
        os.path.join(pth.DATA_DIR, _cfg["sql_data"]))
    keeper.open_connect()
    keeper.open_cursor()
    keeper.create_table(map_sql_table.table())
    while True:
        browser = Browser(driver_pth, binary_pth)
        hide_browser(HIDE)
        # зайти на страницу
        browser.get_page(adr)

        assert "Shell" in browser.driver.title
        time.sleep(1)
        # скрыть браузер

        #  залогинится
        log_in(browser, login, password)
        time.sleep(1)
        # получить данные
        result = read_data(browser, clubs)
        # данные получены без ошибок
        if result:
            log.debug("end; count error - {}".format(errors))
            return
        # при ошибке повторить чтение данных если не исчерпан лимит ошибок
        elif errors < LIMIT_ERROR:
            errors += 1
            log.error("error; count error - {}".format(errors))
            continue

        # данные получены потому что лимит исчерпан
        else:
            log.debug("end; limit end - {}".format(errors))
            return


def main():
    log.warning("\n    ##### - START PROGRAM - ######\n")
    clubs = get_clubs()
    adr = _cfg["web_adr"]
    driver_pth = os.path.join(pth.DRIVERS_DIR, _cfg["driver"])
    binary_pth = os.path.abspath(_cfg["binary_browser_pth"])

    #открыть браузер
    login = service.get_log()
    password = service.get_pass()



    scr_run(driver_pth, binary_pth, adr, clubs, login, password)
    log.warning("\n    ##### - END PROGRAM - ######")




if __name__ == '__main__':
    main()
