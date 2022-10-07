from datetime import date , datetime
from dateutil.relativedelta import relativedelta
date_1 = date.today()
print(date_1)

result = date_1 + relativedelta(years=+2)
print(result)