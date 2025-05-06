import datetime

# yr = int(input("ENTER THE YEAR : "))
# mth = int(input("ENTER THE MONTH : "))
# dy = int(input("ENTER THE DAY : "))

def get_day(year, month, day):
    return datetime.datetime(year=year, month=month, day=day).year

curr_date = datetime.datetime.now().year
bday = get_day(2001,2,8)

print("you are now this old : ", curr_date-bday)