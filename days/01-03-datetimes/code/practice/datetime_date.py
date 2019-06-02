#python

from datetime import datetime
from datetime import date



datetime.today()
# datetime.datetime(2019, 2, 22, 12, 30, 20, 826289)

today = datetime.today()

>>> type(today)
# <class 'datetime.datetime'>

todaydate = date.today()
# <class 'builtin_function_or_method'>

type(todaydate)
# <class 'datetime.date'>

todaydate
datetime.date(2019, 2, 22)

todaydate.month
# 2

todaydate.day
# 22

todaydate.year
# 2019

christmas = date(2019, 12, 25)
#christmas
# datetime.date(2019, 12, 25)

christmas - todaydate
# datetime.timedelta(days=306)

(christmas - todaydate).days
# 306

if christmas is not todaydate:
    print ("Sorry there are still " + str((christmas - todaydate).days) + " days until Christmas")
else:
    print("yay it's Christmas")
