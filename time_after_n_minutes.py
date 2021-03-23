munutes = int(input())

alltodayminutes = (munutes % 1440)
todayhours = alltodayminutes // 60
todayminutes = alltodayminutes % 60

print(todayhours, todayminutes, end='')
