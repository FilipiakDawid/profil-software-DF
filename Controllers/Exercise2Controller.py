from Models.Users import Users
from Models.Location import Location
from Models.Account import Account
from datetime import datetime


# procent kobiet i mężczyzn
def male_female_percentage():
    user_model = Users()
    list = user_model.count_male_female()
    sum = list['male'] + list['female']
    if sum != 0:
        male_precent = list['male'] / sum * 100
        print("Male Percent:" + str(male_precent) + "% Female Percent:" + str(100 - male_precent) + " %")
    else:
        print("Empty Database")


# średnia wieku
def male_female_avg_age():
    user_model = Users()
    list = user_model.avg_age()
    for key, value in list.items():
        print("AVG age for: " + key + " -> " + str(round(value)))


# N najbardziej popularnych miast
def most_popular_cities(quantity):
    location_modal = Location()
    list = location_modal.get_cities(quantity)
    count = 1
    for item in list:
        print(str(count) + ". " + item['city'] + " = " + str(item['count(city)']))
        count += 1


# N najpopularniejszych haseł w formacie
def most_popular_pass(quantity):
    account_modal = Account()
    list = account_modal.get_passwords(quantity)
    count = 1
    for item in list:
        print(str(count) + ". " + item['password'] + " = " + str(item['count(password)']))
        count += 1


# wszystkich użytkowników którzy urodzili się w zakresie dat podanym jako parametr
def users_between_birth_date(start_date, end_date):
    format = "%Y-%m-%d"

    try:

        date_start_object = datetime.strptime(start_date, format)
        date_end_object = datetime.strptime(end_date, format)
        user_model = Users()
        list = user_model.get_users_between_birth_date(date_start_object, date_end_object)
        count = 1
        print("From " + start_date + " to " + end_date)
        for item in list:
            print(str(count) + ". " + item['title'] + " " + item['first_name'] + " " + item['last_name']
                  + ": " + item['birth_date'].split(" ")[0])
            count += 1

    except ValueError:
        print("This is the incorrect date string format. It should be YYYY-MM-DD")



