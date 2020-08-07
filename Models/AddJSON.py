from Models.Model import Model
from datetime import datetime


class AddJSON(Model):
    table_name = "account"

    def add_to_base_json(self, file):
        for row in file['results']:
            self.cur.execute('INSERT INTO ' + self.table_name + ' VALUES(NULL, ?,?,?,?,?);',
                             (row['login']['uuid'], row['login']['username'], row['login']['password'],
                              datetime.strptime(row['registered']['date'], '%Y-%m-%dT%H:%M:%S.%fZ'),
                              int(row['registered']['age'])))

            last_account_id = self.cur.lastrowid

            self.cur.execute('INSERT INTO location VALUES(NULL, ?,?,?,?,?,?,?,?,?,?);',
                             (row['location']['city'], row['location']['state'], row['location']['country'],
                              row['location']['postcode'], row['location']['street']['number'],
                              row['location']['street']['name'], row['location']['coordinates']['latitude'],
                              row['location']['coordinates']['longitude'], row['location']['timezone']['offset'],
                              row['location']['timezone']['description']
                              ))
            last_location_id = self.cur.lastrowid

            self.cur.execute('INSERT INTO users VALUES(NULL, ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);',
                             (row['name']['title'], row['name']['first'], row['name']['last'], row['gender'],
                              row['email'], datetime.strptime(row['dob']['date'], '%Y-%m-%dT%H:%M:%S.%fZ'),
                              self.calculate_days_to_birth(datetime.strptime(row['dob']['date'], '%Y-%m-%dT%H:%M:%S.%fZ')),
                              row['dob']['age'],
                              self.clear_cell_phone_number(row['phone']), self.clear_cell_phone_number(row['cell']),
                              row['id']['name'], row['id']['value'], row['nat'], last_account_id, last_location_id))

        self.commit()
