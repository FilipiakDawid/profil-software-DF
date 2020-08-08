from Models.Model import Model


class Users(Model):

    def count_male_female(self):
        self.cur.execute(
            """
            SELECT COUNT(gender) as COUNT FROM users
            WHERE gender ='female'
            """)
        female = self.cur.fetchall()

        self.cur.execute(
            """
            SELECT COUNT(gender) as COUNT FROM users
            WHERE gender ='male'
            """)
        male = self.cur.fetchall()
        res = {}
        res['female'] = female[0]['COUNT']
        res['male'] = male[0]['COUNT']
        self.commit()
        return res

    def avg_age(self):
        res = {}
        self.cur.execute('SELECT AVG(age) as AVG FROM users')
        all = self.cur.fetchall()
        res['all'] = all[0]['AVG']
        self.cur.execute("SELECT AVG(age) as AVG FROM users WHERE gender = 'male'")
        male = self.cur.fetchall()
        res['male'] = male[0]['AVG']
        self.cur.execute("SELECT AVG(age) as AVG FROM users WHERE gender = 'female'")
        female = self.cur.fetchall()
        res['female'] = female[0]['AVG']
        self.commit()
        return res

    def get_users_between_birth_date(self, start_date, end_date):
        self.cur.execute('SELECT birth_date , title , first_name , last_name FROM users WHERE birth_date BETWEEN  ? '
                         'AND ? order by birth_date;', (start_date, end_date))
        res = self.cur.fetchall()
        self.commit()

        return res
