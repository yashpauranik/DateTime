from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta
class main:
    def AddMonths():
        print("Add Months")
        date_1 = date.today()
        print("Todays date" ,date_1)

        result = date_1 + relativedelta(months=+2)
        print("added months")
        return (result)
    print(AddMonths())

    def AddDays() :
        print("Add Days")
        print("Current time: ", datetime.now())
        print("Added days" ,datetime.now() + timedelta(days=-6))
    AddDays()

    def AddYears():
        print("Add Years")
        date_1 = date.today()
        print("Todays date" ,date_1)
        result = date_1 + relativedelta(years=+2)
        print("Added Years" ,result)
    AddYears()

    def StringToDateTime():
        print("String to Date Time")
        my_date_string = 'Mar 11 2011 13:51:34'
        datetime_object = datetime.strptime(my_date_string, '%b %d %Y  %H:%M:%S')
        print(datetime_object)
    StringToDateTime()

    def DateTimeToString():
        print("DateTime To String ")
        now = datetime.today()
        year = now.strftime("%Y")
        print("year",year)

        month  = now.strftime("%m")
        print("month",month)

        day = now.strftime("%d")
        print("day",day)

        time = now.strftime("%H:%M:%S")
        print("time", time)
    DateTimeToString()