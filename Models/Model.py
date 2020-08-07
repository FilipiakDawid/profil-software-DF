import sqlite3
from datetime import datetime
from dateutil.relativedelta import relativedelta


class Model:

    def __init__(self):
        con = sqlite3.connect('../profilSoftwareDF.db')
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        self.cur = cur
        self.con = con

    def commit(self):
        self.con.commit()
        self.cur.close()

    def calculate_days_to_birth(self, date):
        now = datetime.now()
        birth = datetime(now.year, date.month, date.day, date.hour, date.minute, date.second, date.microsecond)
        if now > birth:
            birth = now + relativedelta(years=1)

        return (birth - now).days + 1

    def clear_cell_phone_number(self, number):
        chars = "()- "
        for c in chars:
            if c in number:
                number = number.replace(c, '')

        return number
