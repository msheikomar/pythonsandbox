import datetime

dt = datetime.datetime  (2018,11,3,7,18,45,100000)
print(dt.date())
print(dt.time())
print(dt.year)

# Days
dt = datetime.datetime(2018,11,3,7,18,45,100000)
tdelta = datetime.timedelta(days=7)
print(dt+tdelta)

#Hours
dt = datetime.datetime(2018,11,3,7,18,45,100000)
tdelta = datetime.timedelta(hours=7)
print(dt+tdelta)