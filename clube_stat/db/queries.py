

def sample_range_date(cursor, date_start , date_end, club_name):

    """

    :param date_start : datetime.datetime
    :param date_end: datetime.datetime
    """
    req = "SELECT * FROM club WHERE (club = ?) AND (data_time BETWEEN ? AND ?) AND mminute = 0"
    cursor.execute(req, ( club_name, date_start, date_end))
    r1 = cursor.fetchall()
    return r1