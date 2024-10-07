import datetime
user_BD = str(input())
year , month , day = list(map(int, user_BD.split('/')))
if month > 12 or day > 31:
    print('WRONG')
else:
    today = datetime.date.today()
    age = today.year - year - ((today.month, today.day) < (month, day))
    print(age)

