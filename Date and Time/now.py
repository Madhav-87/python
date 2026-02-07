import datetime
now=datetime.datetime.now()
print("Date is:",now.day,"-",now.month,"-",now.year)
print(now.strftime("%d/%m/%Y %H:%M:%S"))