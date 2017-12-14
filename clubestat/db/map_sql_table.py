
def table():
    table = """\
    CREATE TABLE club
    (
    dt DATA,
    data_time TIMESTAMP,
    mhour HOUR,
    mminute MINUTE,
    club TEXT,
    class TEXT,
    data-id TEXT,
    data-ip TEXT,
    data-mac TEXT,
    data-unauth TEXT,
    id TEXT,
    title TEXT
    );
"""
    return table