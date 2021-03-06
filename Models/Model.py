import os
import sqlite3
from datetime import datetime

from dateutil.relativedelta import relativedelta


class Model:

    def __init__(self):
        if os.path.isfile('profilSoftwareDF.db'):
            con = sqlite3.connect('profilSoftwareDF.db')
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            self.cur = cur
            self.con = con
        else:
            raise sqlite3.OperationalError("Database doesn't exist")

    def commit(self):
        self.con.commit()
        self.cur.close()

    # zadanie liczba dni pozostałych do urodzin danej osoby
    def calculate_days_to_birth(self, date):
        now = datetime.now()
        birth = datetime(now.year, date.month, date.day, date.hour, date.minute, date.second, date.microsecond)
        if now > birth:
            birth = now + relativedelta(years=1)

        return (birth - now).days + 1

    # zadanie oczyść numer telefonu ze znaków specjalnych (powinny zostać same cyfry)
    def clear_cell_phone_number(self, number):
        chars = "()- "
        for c in chars:
            if c in number:
                number = number.replace(c, '')

        return number
