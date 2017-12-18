import os
import time
from clube_stat import service, pth
from clube_stat.log import log as lg
from clube_stat.browser import Browser
from clube_stat.clubs.club import Club, Clubs
import win32gui, win32con

_cfg = service.load(pth.CONFIG_PATH)
log = lg.log(os.path.join(pth.LOG_DIR, "scr.log"))


def log_in(browser):
    login_id = 'enter_login'
    password_id = 'enter_password'
    submit_name = 'but_m'
    while True:
        login = service.get_log()
        password = service.get_pass()
        log.debug("log - {}, pass - {}".format(login, password))
        browser.log_in(login_id, password_id, submit_name, login,
                       password)
        time.sleep(2)
        if "Карта клуба" in browser.driver.title:
            print("вошли в карту клуба")
            break
        else:
            log.error("не правильная пара логин - пароль")

def get_clubs():
    clubs = Clubs()
    clubs.add_club(Club(Club.LES, 50))
    clubs.add_club(Club(Club.TROYA, 50))
    clubs.add_club(Club(Club.AKADEM, 50))
    clubs.add_club(Club(Club.DREAM, 50))
    return clubs

def main():
    clubs = get_clubs()
    adr = _cfg["web_adr"]
    driver_pth = os.path.join(pth.DRIVERS_DIR, _cfg["driver"])
    binary_pth = os.path.abspath(_cfg["binary_browser_pth"])

    #открыть браузер
    browser = Browser(driver_pth, binary_pth)
    # зайти на страницу
    browser.get_page(adr)
    assert "Shell" in browser.driver.title
    # скрыть браузер
    win32gui.ShowWindow(win32gui.GetForegroundWindow(),
                        win32con.SW_MINIMIZE)
    #  залогинится
    log_in(browser)

    for club in clubs.values():
        browser.select_club_by_name(club.field_name)
        log.debug("select by {}".format(club.field_name))
        log.error("select by {}".format(club.field_name))
        time.sleep(2)

    # table = browser.get_table()

if __name__ == '__main__':
    main()
