import datetime
DT = datetime.datetime.now()

dic2={'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}

def age(z,y,x):                      #z,y,x is the input day,month and year respectivly
    y=dic2[y]                        #To get month in numeric value
    if y<DT.month:
        years=DT.year-x
        if DT.day<z:
            days=(30-z)+DT.day
            months=DT.month-y-1
        else:
            days=DT.day-z
            months=DT.month-y
    elif y>DT.month:
        years=DT.year-x-1
        if DT.day>z:
            months=(12-y)+(DT.month)
            days=DT.day-z
        elif DT.day<z:
            months=(12-y)+(DT.month-1)
            days=((30-z)+DT.day)
        else:
            months=(12-y)+(DT.month)
            days=0
    else:
        years=DT.year-x
        if DT.day>=z:
            days=DT.day-z
            months=DT.month-y
        else:
            years=year-1
            days=30-(z-DT.day)
            months=11
    return days,months,years
