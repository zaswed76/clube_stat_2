import yaml
import collections
CREATE_TABLE_QUERIES = "CREATE TABLE IF NOT EXISTS"

def get_data(path):
    with open(path, "r") as obj:
        return yaml.load(obj)


class Table:
    def __init__(self, name: str, table: dict, queries: str,
                 sql_line: str):
        """

        :param name: имя базы данных
        :param table: колонки {name: type}
        :param queries: созданный запрос
        :param sqlqer: текст sql запроса
        """
        self.sql_line = sql_line
        self._queries = queries
        self._table = table
        self.name = name

    @property
    def header(self):
        return tuple(self.table.keys())

    @property
    def table(self):
        return self._table

    @property
    def queries(self):
        return self._queries

class Tables(collections.MutableMapping):
    def __init__(self):
        self._data = {}

    def add_table(self, table, name, queries_sql=CREATE_TABLE_QUERIES):
        lst = []
        for c, td in table.items():
            lst.append("{} {}".format(c, td))

        tab = ",\n".join(lst)
        res = """
        {quer} {name}\n(\n{tab}\n);""".format(quer=queries_sql, name=name,
                                              tab=tab)
        self._data[name] = Table(name, table, res, queries_sql)

    def __getitem__(self, item) -> Table:
        return self._data[item]

    def __setitem__(self, item, value):
        self._data[item] = value

    def __delitem__(self, item):
        del(self._data[item])

    def __iter__(self):
        for x in self._data:
            yield x

    def __len__(self):
        return len(self._data)


if __name__ == '__main__':
    tab = Tables()
    tab.add_table({"name": "text", "num": "integer"}, "stat", "CREATE TABLE IF NOT EXISTS")
    print(tab["stat"].queries)
