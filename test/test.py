from datetime import datetime
from datetime import date
date_format = "%m/%d/%Y"


def comparedate(start,end,now):
    a = datetime.strptime(start, date_format)
    b = datetime.strptime(now, date_format)
    c = datetime.strptime(end, date_format)
    delta1 = b - a
    delta2 = c - b
    delta3 = a - a
    days=c-a
    print(days)
    fare=int(str(days).split(" ")[0])*50
    print(fare)
    '''if delta1.days >= delta3.days and delta2.days >= delta3.days:
        return True
    else:
        return False
'''
now=date.today().strftime(date_format)
start='9/1/2019'
end='12/1/2019'
comparedate(start,end,now)
'''if comparedate(start,end,now):
    print("IT WORKS")
else:
    print("OOPS...")'''
