
import os
import time
from clubestat import service, pth
from clubestat.log.log import log
from clubestat.browser import Browser

_cfg = service.load(pth.CONFIG_PATH)






def main():
    login_id = 'enter_login'
    password_id = 'enter_password'
    submit_name = 'but_m'
    adr = _cfg["web_adr"]
    driver_pth = os.path.join(pth.DRIVERS_DIR, _cfg["driver"])
    binary_pth = os.path.abspath(_cfg["binary_browser_pth"])

    browser = Browser(driver_pth, binary_pth)
    browser.get_page(adr)
    assert "Shell" in browser.driver.title
    browser.hide_window()
    while True:
        login = service.get_log()
        password = service.get_pass()
        browser.log_in(login_id, password_id, submit_name, login, password)
        if "Карта клуба" in browser.driver.title:
            print("вошли в карту клуба")
            break




if __name__ == '__main__':
    main()