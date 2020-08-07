from Models.Users import Users


# procent kobiet i mężczyzn
def male_female_percentage():
    user_model = Users()
    list = user_model.count_male_female()
    sum = list['male'] + list['female']
    if sum !=0:
        male_precent = list['male'] / sum * 100
        print("Male Percent:" + str(male_precent) + "% Female Percent:" + str(100 - male_precent) + " %")
    else:
        print("Empty Database")


