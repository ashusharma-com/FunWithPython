import datetime

udate = input("Enter Birth date (1994-8-5): ")
d0 = datetime.datetime.today().date()
print("current date: ", d0)
d1 = datetime.datetime.strptime(udate, "%Y-%m-%d").date()
print("birth date:", d1)
delta = d0 - d1
print("total days :", delta.days)
month = delta.days / 30
year = month / 12
print("age is :", int(year))

