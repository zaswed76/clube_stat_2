import collections
import datetime
import os
import sys
import time
import urllib

from apscheduler.schedulers.blocking import BlockingScheduler

from clube_stat import service, pth
from clube_stat.browser import Browser
from clube_stat.clubs.club import Club, Clubs
from clube_stat.db import sql_keeper, sql_tables
from clube_stat.log import log as lg

_cfg = service.load(pth.CONFIG_PATH)
log = lg.log(os.path.join(pth.LOG_DIR, "scr.log"))
HIDE = False

class ExitException(Exception):
    pass

class Main:
    def __init__(self, key):
        self.clubs = self.get_clubs()
        self.keeper = sql_keeper.Keeper(r"D:/save/serg/drop/Dropbox/data_off_on.sql")
        self.create_table(self.keeper, sql_tables.map_table())
        self.create_table(self.keeper, sql_tables.stat_table())
        adr = _cfg["web_adr"]
        driver_pth = os.path.join(pth.DRIVERS_DIR,
                                  _cfg["driver"])
        binary_pth = os.path.abspath(_cfg["binary_browser_pth"])
        login = service.get_log()
        password = service.get_pass(key, os.path.join(pth.ROOT, "etc/uls.pl"))
        login_id = 'enter_login'
        password_id = 'enter_password'
        submit_name = 'but_m'
        self.browser = Browser(driver_pth, binary_pth, adr, login_id,
                               password_id, submit_name, login,
                               password, log=log)
        if HIDE:
            self.browser.hide_window()

        log.warning("\n    ##### - START PROGRAM - ######\n")

        self.args = [self.clubs]

    def scr_run(self, clubs):

        # зайти на страницу
        try:
            self.browser.get_page()
        except urllib.error.URLError:
            log.error("аварийный выход")
            sys.exit()
        time.sleep(1)
        #  залогинится
        self.log_in()
        time.sleep(2)
        self.keeper.open_connect()
        self.keeper.open_cursor()
        data_time_objects = self.get_data_time()
        # получить статистику и таблицы карт клубов
        club_data = self.get_data_tables(clubs, data_time_objects)
        # данные получены без ошибок
        if club_data:
            club_map = club_data["map_tables"]
            self.write_tables(self.keeper, club_map,
                              sql_keeper.ins_club_map())
            self.keeper.commit()
        else:
            log.error("not club_data")

        try:
            club_stat = club_data["stat_tables"]
        except TypeError:
            log.error("закрыт браузер")
            raise Exception("закрыт браузер")
        if club_stat:
            self.write_table(self.keeper, club_stat,
                             sql_keeper.ins_club_stat())
            self.keeper.commit()
            self.keeper.close()
        else:
            log.error("not club_stat")

    def log_in(self):
        if "Shell" in self.browser.driver.title:
            self.browser.log_in()
            time.sleep(2)
            if "Карта клуба" in self.browser.driver.title:
                log.warning("open map")
            else:
                log.error("не правильная пара логин - пароль")
                input("нажмите  < ENTER > что бы выйти")
                print("программа будет закрыта")
                time.sleep(1)
                self.browser.close()
                sys.exit(1)

    def get_clubs(self):
        clubs = Clubs()
        clubs.add_club(
            Club(Club.LES, 50, pro_comps=_cfg["pro_comps"]["les"]))
        clubs.add_club(Club(Club.TROYA, 50))
        clubs.add_club(Club(Club.AKADEM, 50))
        clubs.add_club(Club(Club.DREAM, 50))
        return clubs

    def get_map_table(self, club, dt):
        """
        получить данные карты клуба
        :param browser: browser.driver
        :param club: Club
        :param dt: {date, date_time, h, minute}
        :return: list <- [[data...], [data...]]
        """
        table = self.browser.get_table()
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

    def get_stat_table(self, club, dt):
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

        for opt in stat_names:
            stat[opt] = self.browser.get_data(opt)
        stat["visitor"] = sum(
            [int(x) for x in
             (stat["guest"], stat["resident"],
              stat["school"]) if x != "none"])
        seq = [dt["date"], dt["date_time"], dt["h"], dt["minute"],
               club.field_name]
        seq.extend(stat.values())
        return seq

    def get_data_tables(self, clubs, data_time_objects):
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
            if self.browser.driver.title != "Карта клуба":
                log.error("club card is not open")
                log.debug("browser close")
                time.sleep(2)
                return False
            try:
                self.browser.select_club_by_name(club.field_name)
            except Exception as er:
                log.error(er)
                time.sleep(2)
                return False
            else:
                time.sleep(4)

                try:
                    table_map = self.get_map_table(club,
                                                   data_time_objects)
                    map_tables[club.field_name] = table_map

                    table_stat = self.get_stat_table(club,
                                                     data_time_objects)
                    stat_tables[club.field_name] = table_stat
                except urllib.error.URLError:
                    log.error("аварийный выход")
                    raise Exception

                log.debug("get data on club - {}".format(club.name))


        else:
            return {"map_tables": map_tables,
                    "stat_tables": stat_tables}

    def create_table(self, keeper, table):
        keeper.open_connect()
        keeper.open_cursor()
        keeper.create_table(table)
        keeper.commit()
        keeper.close()

    def get_data_time(self):
        """

        :return: {date_time, date, h, minute}
        """
        dt = {}
        dt["date_time"] = datetime.datetime.now()
        dt["date"] = dt["date_time"].date()
        dt["h"] = dt["date_time"].time().hour
        dt["minute"] = dt["date_time"].time().minute
        return dt

    def write_table(self, keeper, data, sql_scr):
        keeper.add_lines(sql_scr, data.values())
        log.warning("write stat - ok\n---------------------")

    def write_tables(self, keeper, data, sql_scr):
        for tb in data.values():
            keeper.add_lines(sql_scr, tb)
        log.warning("write maps - ok")


def main():
    try:
        key = sys.argv[1]
    except IndexError:
        raise Exception("нужен ключ")

    script = Main(key)
    while True:
        script.scr_run(*script.args)
        time.sleep(300)
    log.warning("\n    ##### - END PROGRAM - ######")

    # sched = BlockingScheduler()
    # sched.add_job(script.scr_run, 'interval', script.args, minutes=5,
    #               start_date="2017-12-20 07:00:00")
    #
    # sched.start()



if __name__ == '__main__':
    main()
