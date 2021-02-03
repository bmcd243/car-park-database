import datetime

current = datetime.datetime.now()
day = current.strftime("%w")
year_number = current.strftime("%m")
full_date = datetime.date.today()

print(current)
print(day)
print(year_number)
print(full_date)