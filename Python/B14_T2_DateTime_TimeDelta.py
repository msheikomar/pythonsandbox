import datetime

tday=datetime.date.today() # to get current date
tdelta=datetime.timedelta(days=7)
print(tday+tdelta)

print(tday-tdelta)

# date2 = date1 + timedelta
# timedelta = date1+date2
print('--------------------')
bday=datetime.date(1993,9,13)
till_bday=bday-tday
print(till_bday)
print(till_bday.days)# only days
print(till_bday.total_seconds()) # To get seconds