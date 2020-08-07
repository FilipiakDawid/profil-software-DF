from Models.Users import Users
from Models.Location import Location


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


