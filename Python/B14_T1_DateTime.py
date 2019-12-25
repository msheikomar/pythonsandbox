import datetime

d= datetime.date(2018,7,24) # To get date from string
print(d)

tday=datetime.date.today() # to get current date
print(tday)

tday=datetime.date.today() # to get current year
print(tday.year)

tday=datetime.date.today() # to get current Month
print(tday.month)

tday=datetime.date.today() # to get current day
print(tday.day)

#To get day of the week

tday=datetime.date.today() # to get current day
print('weekday')
print(tday.weekday())# Monday 0 sunday 6
print('isoweekday')
print(tday.isoweekday())# Monday 1 sunday 7






