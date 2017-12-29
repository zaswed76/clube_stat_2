import yaml


def get_data(path):
    with open(path, "r") as obj:
        return yaml.load(obj)

class Table:
    def __init__(self, name, table, queries):
        self.queries = queries
        self.table = table
        self.name = name


class Tables:
    def __init__(self):
        self.tables = {}

    def add_table(self, table, name, queries):
        lst = []
        for c, td in table.items():
            lst.append("{} {}".format(c, td))

        tab = ",\n".join(lst)
        res = """
        {quer} {name}\n(\n{tab}\n);""".format(quer=queries, name=name,
                                         tab=tab)
        return res


if __name__ == '__main__':
    t = Tables()
    stat_table = dict(
        dt="DATA",
        data_time="TIMESTAMP",
        mhour="HOUR",
        mminute="MINUTE",
        club="TEXT",
        ncomp="TEXT",
        class_="TEXT",
        data_id="TEXT",
        data_ip="TEXT",
        data_mac="TEXT",
        data_unauth="TEXT",
        id="TEXT",
        login="TEXT",
        level="TEXT",
        discount="TEXT",
        subscription="TEXT",
        time_start="TIMESTAMP"

    )
    r = t.add_table(stat_table, "stat", "CREATE TABLE IF NOT EXISTS")

    print(r)
