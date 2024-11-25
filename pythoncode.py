from datetime import datetime

def days_between_dates(date1, date2):
    d1 = datetime.strptime(date1, "%d-%m-%Y")
    d2 = datetime.strptime(date2, "%d-%m-%Y")
    return abs((d2 - d1).days)
date1 = input("Enter the first date : ")
date2 = input("Enter the second date : ")

days = days_between_dates(date1, date2)
print(f"The number of days between {date1} and {date2} is: {days}")