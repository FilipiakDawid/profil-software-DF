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
