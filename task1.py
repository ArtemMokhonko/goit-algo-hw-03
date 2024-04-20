from datetime import datetime


def get_days_from_today(date):
    try:
        date_now = datetime.today()
        date = datetime.strptime(date, "%Y-%m-%d")
        days_difference = date_now.toordinal()- date.toordinal()
        return  days_difference
    except ValueError:
        return  "Wrong data format"


res = get_days_from_today("2003-12-21")
print (f"days = {res}")



