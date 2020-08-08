import sqlite3
try:
    # create database
    con = sqlite3.connect('profilSoftwareDF.db')
    con.row_factory = sqlite3.Row

    cur = con.cursor()

    cur.executescript("""
        DROP TABLE IF EXISTS account;
        CREATE TABLE IF NOT EXISTS account (
            id INTEGER PRIMARY KEY ASC,
            uuid varchar(250) NOT NULL,
            username varchar(250) NOT NULL,
            password varchar(250) NOT NULL,
            create_time DATETIME NOT NULL,
            age INTEGER NOT NULL
        )""")

    cur.executescript("""
        DROP TABLE IF EXISTS location;
        CREATE TABLE IF NOT EXISTS location (
            id INTEGER PRIMARY KEY ASC,
            city varchar(250) NOT NULL,
            state varchar(250) NOT NULL,
            country varchar(250) NOT NULL,
            postcode varchar(50) NOT NULL,
            street_number INTEGER NOT NULL,
            street_name varchar(250) NOT NULL,
            coordinates_latitude varchar(50) NOT NULL,
            coordinates_longitude varchar(50) NOT NULL,
            timezone_offset varchar(25) NOT NULL,
            timezone_description varchar(250) NOT NULL
        )""")

    cur.executescript("""
        DROP TABLE IF EXISTS users;
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY ASC,
            title varchar(50) NOT NULL,
            first_name varchar(250) NOT NULL,
            last_name varchar(250) NOT NULL,
            gender TEXT ,
            email varchar(50) NOT NULL,
            birth_date DATETIME NOT NULL,
            days_to_birth_date INTEGER NOT NULL,
            age INTEGER NOT NULL,
            phone varchar(15),
            cellphone varchar(15),
            id_name varchar(15),
            id_value varchar(250),
            nat varchar(15),
            account_id INTEGER,
            location_id INTEGER,
            FOREIGN KEY(account_id) REFERENCES account(id),
            FOREIGN KEY(location_id) REFERENCES location(id),
            CHECK (gender = 'male' or (gender = 'female'))
        )""")

    cur.close()
    print("Database created successfully")
except BaseException:
    print("Error which Database created")
