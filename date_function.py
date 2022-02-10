#DATE
from datetime import date
from datetime import time
from datetime import datetime
today=date.today()
print(today)
print(today.month)
print(today.year)
print(today.day)
#TIME
time=datetime.time(datetime.now())
print(time)
print(time.hour)
print(time.minute)
print(time.second)
#DATETIME
today=datetime.now()
print(today)
print(today.hour)
print(today.minute)
print(today.second)
#weekday returns 0 for monday
wd=date.weekday(today)
days=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
#print("%d" %wd)
print("today is "+days[wd])