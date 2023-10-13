from datetime import datetime, timedelta
from collections import defaultdict



def get_birthdays_per_week(users):
    birthday_on_week = defaultdict(list)
    today = datetime.today().date()

    if users:
        for user in users:
            name = user["name"]
            birthday = user["birthday"].date()
            birthday_this_year = birthday.replace(year=today.year)

            if birthday_this_year < today:          #if birthday passed, change year for next
                birthday_this_year = birthday.replace(year=today.year + 1)

            delta_days = (birthday_this_year - today).days

            if delta_days < 7:          #if birthdays are in next 7 days, write day name
                if birthday_this_year.strftime("%A") in ["Saturday", "Sunday"]:         #if birthday on Weekend, write it as Monday
                    day_name = "Monday"
                else:
                    day_name = birthday_this_year.strftime("%A")
                birthday_on_week[day_name].append(name)

        birthday_on_week = dict(birthday_on_week)
        for day, employee in birthday_on_week.items():          #return list of birthdays on next 7 days
            if isinstance(employee, list):
                employee = ", ".join(employee)
                print(f"{day}: {employee}")
    else:
        print("The users list is empty")
