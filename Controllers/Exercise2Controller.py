import argparse
import re
from datetime import datetime

from Models.Account import Account
from Models.Location import Location
from Models.Users import Users

parser = argparse.ArgumentParser(description='Exercise 2 Controller')
parser.add_argument('--malefemaleprecent', help="Return percentage of women and men", action='store_true')


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

parser.add_argument('--avgage', help="Return average of women or men", type=str, choices=['all', 'male', 'female'])


def male_female_avg_age(choice):
    user_model = Users()
    list = user_model.avg_age(choice)
    for key, value in list.items():
        print("AVG age for: " + key + " -> " + str(round(value)))


# N najbardziej popularnych miast

parser.add_argument('--popularcities', help="Return most popular cities", type=int)


def most_popular_cities(quantity):
    location_modal = Location()
    list = location_modal.get_cities(quantity)
    count = 1
    for item in list:
        print(str(count) + ". " + item['city'] + " = " + str(item['count(city)']))
        count += 1


# N najpopularniejszych haseł w formacie

parser.add_argument('--popularpassword', help="Return most popular password (s)", type=int)


def most_popular_pass(quantity):
    account_modal = Account()
    list = account_modal.get_passwords(quantity)
    count = 1
    for item in list:
        print(str(count) + ". " + item['password'] + " = " + str(item['count(password)']))
        count += 1


# wszystkich użytkowników którzy urodzili się w zakresie dat podanym jako parametr

parser.add_argument('--birthdate', help="Return users born in the date range", nargs=2, type=str)

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


# najbezpieczniejsze hasło
def calculate_pass_strength(password) -> int:
    points = 0

    if any(x.isupper() for x in password):
        points += 2

    if any(x.islower() for x in password):
        points += 1

    if any(x.isdigit() for x in password):
        points += 1

    if len(password) >= 8:
        points += 5

    if re.findall('[^A-Za-z0-9]', password):
        points += 3

    return points


parser.add_argument('--safestpass', help="Return the safest password", action='store_true')


def safest_users_passwords():
    account_modal = Account()
    list = account_modal.get_all_passwords()
    max_points = -1
    password_list = []

    for item in list:
        tmp_points = calculate_pass_strength(item['password'])

        if tmp_points > max_points:
            password_list.clear()
            max_points = tmp_points
            password_list.append(item['password'])
        elif tmp_points == max_points:
            password_list.append(item['password'])

    print("The safest password (s) (strength " + str(max_points) + ") is:")
    print(str(password_list))


args = parser.parse_args()
# argparse
if args.malefemaleprecent:
    male_female_percentage()
elif args.avgage:
    male_female_avg_age(args.avgage)
elif args.popularcities:
    most_popular_cities(args.popularcities)
elif args.popularpassword:
    most_popular_pass(args.popularpassword)
elif args.birthdate:
    users_between_birth_date(args.birthdate[0], args.birthdate[1])
elif args.safestpass:
    safest_users_passwords()
else:
    print(parser.print_help())
