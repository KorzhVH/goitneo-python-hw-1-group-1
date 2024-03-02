from datetime import datetime
from collections import defaultdict


def get_birthdays_per_week(users):
    weekdays_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    now = datetime.today().date()
    people_to_congratulate = defaultdict(list)
    for user in users:
        name = user['name']
        birthday = user['birthday'].date()
        next_birthday = datetime(
            year=now.year,
            month=birthday.month,
            day=birthday.day).date()
        if next_birthday < now:
            next_birthday.replace(year=now.year + 1)
        delta_days = (next_birthday - now).days
        if 7 >= delta_days >= 0:
            weekday = next_birthday.isoweekday()
            if weekday == 6 or weekday == 7:
                weekday = 1
            people_to_congratulate[weekday].append(name)
    for i in range(1, 6):
        if people_to_congratulate.get(i) is not None:
            names = ", ".join(people_to_congratulate[i])
            print(f'{weekdays_list[i - 1]}: {names}')
