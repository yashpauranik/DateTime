from datetime import datetime
now = datetime.today()

year = now.strftime("%Y")
print("year",year)

month  = now.strftime("%m")
print("month",month)

day = now.strftime("%d")
print("day",day)

time = now.strftime("%H:%M:%S")
print("time", time)

