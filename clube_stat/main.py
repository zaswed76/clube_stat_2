import os
import time

import sys

import datetime

import collections
from apscheduler.schedulers.blocking import BlockingScheduler
import win32gui, win32con

from clube_stat import service, pth
from clube_stat.log import log as lg
from clube_stat.browser import Browser
from clube_stat.db import sql_keeper, sql_tables
from clube_stat.clubs.club import Club, Clubs

_cfg = service.load(pth.CONFIG_PATH)
log = lg.log(os.path.join(pth.LOG_DIR, "scr.log"))
HIDE = False
LIMIT_ERROR = 3


# def hide_browser(v):
#     if v:
#         win32gui.ShowWindow(win32gui.GetForegroundWindow(),
#                             win32con.SW_MINIMIZE)
class Main:
    def __init__(self):
        self.clubs = self.get_clubs()

        self.adr = _cfg["web_adr"]
        self.driver_pth = os.path.join(pth.DRIVERS_DIR,
                                       _cfg["driver"])
        self.binary_pth = os.path.abspath(_cfg["binary_browser_pth"])
        self.login = service.get_log()
        self.password = service.get_pass()

        self.browser = Browser(self.driver_pth, self.binary_pth)
        # self.browser.hide_window()
        log.warning("\n    ##### - START PROGRAM - ######\n")

        self.args = [self.browser, self.adr, self.clubs, self.login,
                     self.password]
        self.scr_run(*self.args)

    def log_in(self, browser, login, password):
        login_id = 'enter_login'
        password_id = 'enter_password'
        submit_name = 'but_m'
        browser.log_in(login_id, password_id, submit_name, login,
                       password)
        time.sleep(2)
        if "Карта клуба" in browser.driver.title:
            log.warning("open map")
        else:
            log.error("не правильная пара логин - пароль")
            input("нажмите  < ENTER > что бы выйти")
            print("программа будет закрыта")
            time.sleep(1)
            browser.close()
            sys.exit(1)

    def get_clubs(self):
        clubs = Clubs()
        clubs.add_club(
            Club(Club.LES, 50, pro_comps=_cfg["pro_comps"]["les"]))
        clubs.add_club(Club(Club.TROYA, 50))
        clubs.add_club(Club(Club.AKADEM, 50))
        clubs.add_club(Club(Club.DREAM, 50))
        return clubs



    def get_map_table(self, browser, club, dt):
        """
        получить данные карты клуба
        :param browser: browser.driver
        :param club: Club
        :param dt: {date, date_time, h, minute}
        :return: list <- [[data...], [data...]]
        """
        table = browser.get_table()
        club_name = club.field_name
        seq = []
        s = [dt["date"], dt["date_time"], dt["h"], dt["minute"],
             club_name]
        temp_lst = []
        for line in table:
            temp_lst.extend(s)
            temp_lst.extend(line)
            seq.append(temp_lst.copy())
            temp_lst.clear()
        return seq

    def get_stat_table(self, browser, club, dt):
        """
        получить данные статистики клуба
        :param browser: browser.driver
        :param club: Club
        :param dt: {date, date_time, h, minute}
        :return: list <- [[data...], [data...]]
        """
        stat = collections.OrderedDict()
        stat_names = ["load", "taken", "free", "guest",
                      "resident", "admin", "workers", "school"]
        try:
            for opt in stat_names:
                stat[opt] = browser.get_data(opt)
            stat["visitor"] = sum(
                [int(x) for x in
                 (stat["guest"], stat["resident"],
                  stat["school"])])
        except Exception as er:
            log.error(er)
        seq = [dt["date"], dt["date_time"], dt["h"], dt["minute"],
               club.field_name]
        seq.extend(stat.values())
        return seq

    def get_data_tables(self, browser, clubs, data_time_objects):
        """
        получить данные клуба (статистика и карта)
        :param browser: browser.driver
        :param club: Club
        :param dt: {date, date_time, h, minute}
        :return: dict <- {data1, data2 ...}
        data = {'IT Land Troya': table, 'IT Land Les': table, ...}
        """
        map_tables = {}
        stat_tables = {}
        for club in clubs.values():
            if browser.driver.title != "Карта клуба":
                log.error("club card is not open")
                log.debug("browser close")
                time.sleep(2)
                return False
            try:
                browser.select_club_by_name(club.field_name)
            except Exception as er:
                log.error(er)
                time.sleep(2)
                return False
            else:

                time.sleep(4)

                table_map = self.get_map_table(browser, club,
                                               data_time_objects)
                map_tables[club.field_name] = table_map

                table_stat = self.get_stat_table(browser, club,
                                                 data_time_objects)
                stat_tables[club.field_name] = table_stat

        else:
            return {"map_tables": map_tables, "stat_tables": stat_tables}

    def create_table(self, keeper, table):
        keeper.open_connect()
        keeper.open_cursor()
        keeper.create_table(table)
        keeper.commit()
        keeper.close()

    def get_data_time(self):
        dt = {}
        dt["date_time"] = datetime.datetime.now()
        dt["date"] = dt["date_time"].date()
        dt["h"] = dt["date_time"].time().hour
        dt["minute"] = dt["date_time"].time().minute
        return dt

    def scr_run(self, browser, adr, clubs, login, password):
        keeper = sql_keeper.Keeper(
            os.path.join(pth.DATA_FILE))

        self.create_table(keeper, sql_tables.map_table())
        self.create_table(keeper, sql_tables.stat_table())

        while True:
            # зайти на страницу
            browser.get_page(adr)
            time.sleep(1)
            #  залогинится
            if "Shell" in browser.driver.title:
                self.log_in(browser, login, password)
            time.sleep(2)

            data_time_objects = self.get_data_time()

            # получить статистику и таблицы карт клубов
            club_data = self.get_data_tables(browser, clubs,
                                               data_time_objects)




            # данные получены без ошибок
            keeper.open_connect()
            keeper.open_cursor()

            club_map = club_data["map_tables"]
            self.write_tables(keeper, club_map,
                                  sql_keeper.ins_club_map())
            keeper.commit()

            club_stat= club_data["stat_tables"]

            self.write_table(keeper, club_stat,
                                  sql_keeper.ins_club_stat())
            keeper.commit()
            keeper.close()

    def write_table(self, keeper, data, sql_scr):
        keeper.add_lines(sql_scr, data.values())
        log.warning("write stat - ok")

    def write_tables(self, keeper, data, sql_scr):
        for tb in data.values():
            keeper.add_lines(sql_scr, tb)
        log.warning("write maps - ok\n---------------------")

def main():
    script = Main()
    sched = BlockingScheduler()
    sched.add_job(script.scr_run, 'interval', script.args, minutes=1,
                  start_date="2017-12-20 07:00:00")

    sched.start()
    log.warning("\n    ##### - END PROGRAM - ######")


if __name__ == '__main__':
    main()
