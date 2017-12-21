
def map_table():
    table = """\
    CREATE TABLE IF NOT EXISTS club_tab
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
    login TEXT,
    level TEXT,
    discount TEXT,
    subscription TEXT,
    time_start TIMESTAMP
    );
"""
    return table

def stat_table():
    table = """\
    CREATE TABLE club
    (
    dt DATA,
    data_time TIMESTAMP,
    mhour HOUR,
    mminute MINUTE,
    club TEXT,
    load INTEGER,
    taken INTEGER,
    free INTEGER,
    guest INTEGER,
    resident INTEGER,
    admin INTEGER,
    workers INTEGER,
    school INTEGER,
    visitor INTEGER
    );
"""
    return table