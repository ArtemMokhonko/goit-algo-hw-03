from datetime import datetime, timedelta

def get_upcoming_birthdays(users: list):
    today = datetime.today().date()
    upcoming_birthdays = []
    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        
        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today:  # якщо минув
            birthday_this_year = birthday.replace(year=today.year + 1) 
        
        delta = birthday_this_year - today
        
        if 0 <= delta.days <= 7:
            if birthday_this_year.weekday() > 4:  
                
                days_till_monday = 7 - birthday_this_year.weekday()
                congratulation_date = birthday_this_year + timedelta(days=days_till_monday)
            else:
                congratulation_date = birthday_this_year
            
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })
    return upcoming_birthdays


users = [
    {"name": "John Doe", "birthday": "1985.04.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
