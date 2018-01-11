import datetime
import os


import sqlite3


def ins_club_stat():
    return 'insert into club values (?,?,?,?,?,?,?,?,?,?,?,?,?,?)'

def ins_club_map():
    return 'insert into club_tab values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'

def seq_line():
    d = datetime.datetime.now().date()
    dt = datetime.datetime.now()
    return (d, dt, "les", 1, 1, 1, 1, 1, 1, 1, 1)


def seq_line_date(date):
    d = datetime.datetime.strptime(date, "%d.%m.%Y").date()
    dt = datetime.datetime.strptime(date, "%d.%m.%Y")
    return (d, dt, "les", 1, 1, 1, 1, 1, 1, 1, 1)

def seq_line_date_time(date_time):
    dt = datetime.datetime.strptime(date_time, "%d.%m.%Y %H:%M")
    d = dt.date()
    return (d, dt, "les", 1, 1, 1, 1, 1, 1, 1, 1)

def pretty(table, seq):
    # table = PrettyTable(["животное", "свирепость"])
    print(table)




def dates():
    lst = []
    d = (1, 2, 3, 4, 5)
    for i in d:
        strdate = "{}.09.2017".format(i)
        lst.append(datetime.datetime.strptime(strdate, "%d.%m.%Y").date())
    return lst

class Akm(list):
    def __init__(self):
        super().__init__()

    def __contains__(self, item):
        for line in self:
            if item[0] == line[2] and item[1] == line[3]:
                return True


def sort_seq(lst):
    akm = Akm()
    for line in lst:
        if not (line[2], line[3]) in akm:
            akm.append(line)
    return akm

class Keeper():
    def __init__(self, path):
        self.path = path
        data_dir = os.path.dirname(self.path)
        if not os.path.isdir(data_dir):
            os.makedirs(data_dir)
        print(path)


    def create_table(self, table):
        try:
            self.cursor.executescript(table)
        except sqlite3.OperationalError as er:
            print(er)

    def add_line(self, ins, seq):
        self.cursor.execute(ins, seq)

    def add_lines(self, ins, seq):
        self.cursor.executemany(ins, seq)

    def open_connect(self):
        self.connect = sqlite3.connect(self.path)

    def open_cursor(self):
        self.cursor = self.connect.cursor()

    def commit(self):
        self.connect.commit()

    def close(self):
        self.cursor.close()
        self.connect.close()

    @staticmethod
    def seq_print(seq):
        for i in seq:
            print(i)

    def samp_date(self, date):
        d = datetime.datetime.strptime(date, "%d.%m.%Y").date()
        self.cursor.execute("SELECT data_time, taken FROM club WHERE dt = ?", (d,))
        return self.cursor.fetchall()

    @staticmethod
    def str_to_date(line):
        return datetime.datetime.strptime(line, "%d.%m.%Y").date()

    @staticmethod
    def str_to_date_time(line):
        return datetime.datetime.strptime(line, "%d.%m.%Y %H:%M:%S")

    def sample_range_date(self, date_start , date_end, club_name):

        """

        :param date_start : datetime.datetime
        :param date_end: datetime.datetime
        """


        req = "SELECT * FROM club WHERE (club = ?) AND (data_time BETWEEN ? AND ?) AND mminute = 0"
        self.cursor.execute(req, (club_name, date_start, date_end))
        r1 = self.cursor.fetchall()
        return r1

    def sample_range_date_2(self, date_start , date_end, time_step, club_name, selected=None):

        """

        :param date_start : datetime.datetime
        :param date_end: datetime.datetime
        """
        req = {}
        req["step1"] = "SELECT dt FROM club WHERE (club = ?) AND (data_time BETWEEN ? AND ?) AND mminute = 0"

        req["step30"] = "SELECT * FROM club WHERE(club = ?) AND (data_time BETWEEN ? AND ?) AND (mminute = 0 OR mminute = 30)"

        self.cursor.execute(req[time_step], (club_name, date_start, date_end))
        r1 = self.cursor.fetchall()
        return r1

    def sample_all(self):
        self.cursor.execute("SELECT * FROM club")
        return self.cursor.fetchall()

    def sample_range_time(self, start, end, sample_hour=False):
        res = []
        start_date_time = self.str_to_date_time(start)
        start_date = start_date_time.date()
        end_date_time = self.str_to_date_time(end)
        end_date = end_date_time.date()

        start_time = self.str_to_date_time(start).time()
        end_time = self.str_to_date_time(end).time()

        range_date = self.sample_range_date(start_date, end_date)

        for line in range_date:
            sql_date = datetime.datetime.strptime(line[0], "%Y-%m-%d %H:%M:%S.%f")
            sql_time = sql_date.time()
            #
            # if (sql_time <
            #         datetime.datetime.strptime("23:59:59", "%H:%M:%S").time()):
            #     print(start_time, sql_time, end_time)
            if start_date_time <= sql_date <= end_date_time:
                if sample_hour:
                    if sql_time.minute == 0:
                        res.append(line)
                else:
                    res.append(line)
        print(res)
        return tuple(res)

    def sample_hour(self, start, end):
        return self.sample_range_time(start, end, sample_hour=True)




if __name__ == '__main__':
    # region открыть базу
    # path = "data.db"
    # region Description
    import os
    import prettytable
    from clube_stat import pth, service
    from clube_stat.clubs.club import Clubs, Club
    from clube_stat.db import queries
    from clube_stat.db import sql_tables
    # endregion
    path = os.path.join(pth.DATA_FILE)
    kp = Keeper(path)
    kp.open_connect()
    kp.open_cursor()

    _cfg = service.load(pth.CONFIG_PATH)
    clubs = Clubs()
    clubs.add_club(Club(Club.LES, 50, pro_comps=_cfg["pro_comps"]["les"]))
    pro_les = clubs["les"].pro_comps
    pretty(sql_tables.stat_table(), [])

    # kp.sample_range_date()
    # # print(pro_les)
    # # запрос на про зону
    # # sql_="select * from club_tab where ncomp in ({seq}) and club = 'IT Land Les'".format(
    # #     seq=','.join(['?']*len(pro_les)))
    # sql_="select * from club where club = 'IT Land Les'"
    #
    #
    # kp.cursor.execute(sql_)
    # res = kp.cursor.fetchall()
    # for i in res:
    #     print(i)
    #     print("--------------")
    # print(len(res))

    # Keeper.seq_print(kp.sample_all())
    # region Description
    # r = kp.sample_hour("28.09.2017 09:00:00", "28.09.2017 23:00:00")
    # print(r)

    # lst = []
    # for line in r:
    #     ln = list(line)
    #     st = ln[0]
    #     t = datetime.datetime.strptime(st, "%Y-%m-%d %H:%M:%S.%f").time()
    #     new_t = t.strftime("%H")
    #     ln[0] = new_t
    #     lst.append(ln)
    #
    # import pandas as pd
    # df = pd.DataFrame(lst)
    #
    # writer = pd.ExcelWriter('output2.xlsx')
    # df.to_excel(writer,'Sheet1')
    # writer.save()
    # endregion
    # endregion

    # s = kp.sample_range_time("24.09.2017 12:00", "24.09.2017 18:00")
    # Keeper.seq_print(s)
    # Keeper.seq_print(kp.sample_range_date("24.09.2017", "26.09.2017"))

    # start_date = Keeper.str_to_date("27.12.2017")
    # end_date = Keeper.str_to_date("29.12.2017")
    # r = queries.sample_range_date(kp.cursor, start_date, end_date,'IT Land Les')
    # Keeper.seq_print(r)
    # Keeper.seq_print(kp.sample_range_date(start_date, end_date))

    # Keeper.seq_print(kp.sample_all())

    # res = kp.samp_date("23.09.2017")
    # Keeper.seq_print(res)
    # date = "23.09.2017"
    # tm = "11:39:24"
    # t = datetime.datetime.strptime(tm, "%H:%M:%S").time()
    # d = datetime.datetime.strptime(date, "%d.%m.%Y").date()
    # kp.cursor.execute("select * from club")
    # for i in kp.cursor.fetchall():
    #     dt_t = i[1]
    #     sql_time = datetime.datetime.strptime(dt_t, "%Y-%m-%d %H:%M:%S.%f").time()
    #     print(dt_t)

    # region добавить даты
    # kp.add_line(table.ins_club_stat(), seq_line_date("24.09.2017"))
    # kp.add_line(table.ins_club_stat(), seq_line_date("25.09.2017"))
    # kp.add_line(table.ins_club_stat(), seq_line_date("26.09.2017"))
    # kp.add_line(table.ins_club_stat(), seq_line_date("27.09.2017"))
    # endregion

    # region добавить даты + вермя
    # times = (9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
    # for t in times:
    #     kp.add_line(table.ins_club_stat(),  seq_line_date_time("28.09.2017 {}:00".format(t)))

    # endregion

    # kp.create_table(table())
    kp.close()

