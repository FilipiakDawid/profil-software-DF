from Models.Model import Model


class Location(Model):
    def get_cities(self, quantity):
        self.cur.execute('SELECT count(city),city FROM location group by city order by count(city) desc ' +
                         'LIMIT ' + str(quantity))
        res = self.cur.fetchall()
        self.commit()
        return res
