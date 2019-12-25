import datetime

import pytz

dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
print(dt_utcnow)
dt_mtn = dt_utcnow.astimezone(pytz.timezone("US/Mountain"))
print(dt_mtn)
