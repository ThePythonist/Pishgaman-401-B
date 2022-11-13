# import pytz
# from persiantools.jdatetime import JalaliDate, JalaliDateTime
#
# date = JalaliDateTime(1369, 7, 1, 14, 0, 10, 0, pytz.utc).strftime("%c")
# date = date.split(" ")
#
# print(date[0])

from persiantools.jdatetime import JalaliDate, JalaliDateTime
import pytz
import jdatetime

today = str(jdatetime.datetime.now()).split()
print(today)
year = today[0].split("-")[0]
month = today[0].split("-")[1]
day = today[0].split("-")[2]
hour = today[1].split(":")[0]
minute = today[1].split(":")[1]
second = today[1].split(":")[2]
date = JalaliDateTime(int(year), int(month), int(day), int(hour), int(minute), int(float(second)), 0, pytz.utc).strftime("%c")
date = date.split()
print(date)
