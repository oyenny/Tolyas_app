SecondsCount = int(input())

MinutesCount = SecondsCount // 60
HoursCount = MinutesCount // 60
DaysCount = HoursCount // 24

MinutesStrBig = '10' + str((MinutesCount - HoursCount * 60))
MinutesStr = int(MinutesStrBig) % (10 ** 2)

print(HoursCount, ':', MinutesStr, ':', SecondsCount - MinutesCount * 60, sep='')
