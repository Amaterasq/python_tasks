import datetime

# first_date = list(map(int, input().split()))
# dif = int(input())

first_date = [2016, 4, 20]
dif = 14

end_date = (
    datetime.date(*first_date) + datetime.timedelta(days=dif)
).strftime('%Y %#m %#d')  # Вывод без ведущих нулей

print(end_date)
