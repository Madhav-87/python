import datetime
#------------------#-------------------#
date=datetime.date.today()
print("Today Date: In Format(Monday-Jan-2026):")
print(date.strftime("%A-%b-%Y"))
#------------------#-------------------#
print("Today Date: In Format(Mon-January-2026):")
print(date.strftime("%a-%B-%Y"))
#------------------#-------------------#
print("Todays date: In Format(07-01-2026):")
print(date.strftime("%d-%m-%Y"))
#------------------#-------------------#
print("Todays date:In Format(07-02-26)")
print(date.strftime("%d-%m-%y"))