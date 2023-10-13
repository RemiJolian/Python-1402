def day_calculator(d):         # d = input('enter date yyyy-mm-dd')
    # This library needed:
    from datetime import date
    from datetime import datetime

    # Convert the birthdate string to a date object
    d = datetime.strptime(d, '%Y-%m-%d') #d = date.fromisoformat(d)

    days_m = 0

    # Calculate the days in month
    for i in range (1, d.month):
        if d.month == 1 :
            break
        if i in [1, 3, 5, 7, 8, 10, 12]:
            days_m += 31
        elif i in [4, 6, 9, 11]:
            days_m += 30
        else:
            days_m += 28

    total_days = d.year * 365 + d.year//4 + days_m + d.day 

    date_born = date(1999, 1, 14)
    total_days_born = date_born.year * 365 + date_born.year // 4 + 14   

    # Calculate number of days old
    dif_days = total_days - total_days_born
    if dif_days > 0:
        return dif_days
    else:
        return 'Not yet born'
day_calculator('1999-02-14')

#  OR this clear code:
from datetime import datetime

def day_calculator(date):
    # تاریخ تولد سجاد
    birthday = datetime(1999, 1, 14)

    # تاریخ مورد نظر
    target_date = datetime.strptime(date, '%Y-%m-%d')

    # محاسبه تفاوت بین دو تاریخ
    days_lived = (target_date - birthday).days

    if days_lived < 0:
        return "Not yet born"
    else:
        return days_lived

