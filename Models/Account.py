from Models.Model import Model


class Account(Model):
    def get_passwords(self, quantity):
        self.cur.execute('SELECT count(password),password FROM account group by password ' +
                         'order by count(password) desc LIMIT ' + str(quantity))
        res = self.cur.fetchall()
        self.commit()
        return res
