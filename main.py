from datetime import datetime, timedelta
from collections import defaultdict



def get_birthdays_per_week(users):
    birthday_on_week = defaultdict(list) # dictionary with birthdays
    today = datetime.today().date() # today's date without time

    if users:
        for user in users:
            name = user["name"]
            birthday = user["birthday"].date() # convert to type date
            birthday_this_year = birthday.replace(year=today.year) #changing year from birthday on current year

            if birthday_this_year < today: #if birthday passed, change year for next
                birthday_this_year = birthday.replace(year=today.year + 1)

            delta_days = (birthday_this_year - today).days #determine difference between birthday and current day

            if delta_days < 7: #determine if birthdays are in next 7 days, if yes, write day name
                if birthday_this_year.strftime("%A") in ["Saturday", "Sunday"]: #if birthday on Saturday or Sunday, write it as Monday
                    day_name = "Monday"
                else:
                    day_name = birthday_this_year.strftime("%A")
                birthday_on_week[day_name].append(name)

        birthday_on_week = dict(birthday_on_week) #convert to dict format
        for day, employee in birthday_on_week.items(): #return list of birthdays on next 7 days
            if isinstance(employee, list):
                employee = ", ".join(employee)
                print(f"{day}: {employee}")
    else:
        print("The users list is empty")



users_dict = [
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
    {"name": "Steve Wozniak", "birthday": datetime(1998, 1, 30)},
    {"name": "Emma Stone", "birthday": datetime(2002, 7, 8)},
    {"name": "Anna Smith", "birthday": datetime(2005, 10, 12)},
    {"name": "Frida Smith", "birthday": datetime(2006, 10, 13)},
    {"name": "Saturday Smith", "birthday": datetime(2001, 10, 14)},
    {"name": "Sunday Smith", "birthday": datetime(2000, 10, 15)},
    {"name": "Monday Smith", "birthday": datetime(1999, 10, 16)},
    {"name": "Tuesday Miller", "birthday": datetime(2007, 10, 17)},
    {"name": "Wednesday Doe", "birthday": datetime(1989, 10, 18)},
    {"name": "Thursday Kit", "birthday": datetime(1991, 10, 19)},
    {"name": "Thursdaydouble Kittary", "birthday": datetime(1991, 10, 19)},
    {"name": "Nemo Flager", "birthday": datetime(1993, 10, 20)}
    ]
empty_users_dict = []

get_birthdays_per_week(users_dict)
print("")
get_birthdays_per_week(empty_users_dict)



# Result of the get_birthdays_per_week function running on 13.10.2023

# Friday: Frida Smith
# Monday: Saturday Smith, Sunday Smith, Monday Smith
# Tuesday: Tuesday Miller
# Wednesday: Wednesday Doe
# Thursday: Thursday Kit, Thursdaydouble Kittary

# The users list is empty