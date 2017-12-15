
def table():
    table = """\
    CREATE TABLE club_tab
    (
    dt DATA,
    data_time TIMESTAMP,
    mhour HOUR,
    mminute MINUTE,
    club TEXT,
    ncomp TEXT,
    class TEXT,
    data_id TEXT,
    data_ip TEXT,
    data_mac TEXT,
    data_unauth TEXT,
    id TEXT,
    title TEXT
    );
"""
    return table