from util import get_day_name
data = input().split()
month = int(data[0])
date = int(data[1])
year = int(data[2])
print(get_day_name(month, date, year))