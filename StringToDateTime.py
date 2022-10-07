from datetime import datetime

my_date_string = 'Mar 11 2011 13:51:34'

datetime_object = datetime.strptime(my_date_string, '%b %d %Y  %H:%M:%S')

print(datetime_object)