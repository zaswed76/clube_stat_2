
import os
from clubestat import service, pth
from clubestat.log.log import log
from clubestat.browser import Browser

_cfg = service.load(pth.CONFIG_PATH)

class Main(Browser):
    def __init__(self, driver_pth, binary_pth):
        super().__init__(driver_pth, binary_pth)



    def get_page(self, adr):
        Browser.get_page(self, adr)
        assert "Shell" in self.browser.driver.title
        log.debug(self.browser.driver.title)




def main():
    adr = _cfg["web_adr"]
    driver_pth = os.path.join(pth.DRIVERS_DIR, _cfg["driver"])
    binary_pth = os.path.abspath(_cfg["binary_browser_pth"])

    browser = Main(driver_pth, binary_pth)




if __name__ == '__main__':
    main()