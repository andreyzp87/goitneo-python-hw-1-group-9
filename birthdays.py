from collections import defaultdict
from datetime import datetime, timedelta

def get_birthdays_per_week(users: list):
    
    birthdays = defaultdict(list)
    today = datetime.today().date()
    
    # filling birthdays dict
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date().replace(year=today.year)
        
        if birthday < today:
            birthday = birthday.replace(year=today.year+1)
        
        delta_days = (birthday - today).days
        
        if delta_days >= 7:
            continue
        
        weekday = birthday.weekday()
        
        if weekday >= 5:
            weekday = 0
        
        birthdays[weekday].append(name)
    
    # printing results for 7 days starting today
    for i in range(0, 7):
        check_day = today + timedelta(days=i)
        weekday = check_day.weekday()
        
        if weekday not in birthdays:
            continue
        
        result = check_day.strftime('%A: ')+', '.join(birthdays[weekday])
        print(result)


if __name__ == "__main__":
    print('Showing demo results for 7 daily birthdays starting today:')

    users = []

    start_date = datetime.now()

    for i in range(0, 7):
        birthday = start_date + timedelta(days=i)
        weekday = birthday.strftime('%A')
        users.append({ "name": f"{weekday} birthday {i}", "birthday": birthday})

    get_birthdays_per_week(users)