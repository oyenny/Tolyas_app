SecondsCount = int(input())

MinutesCount = SecondsCount // 60
HoursCount = MinutesCount // 60
DaysCount = HoursCount // 24

MinutesStrBig = '10' + str((MinutesCount - HoursCount * 60))
# print(MinutesStrBig)
m1 = str((int(MinutesStrBig) // 10) % 10)
# print('m1',m1)
m2 = str(int(MinutesStrBig) % 10)
# print('m2',m2)
MinutesStr = m1 + m2


SecondsStrBig = '10' + str(SecondsCount - MinutesCount * 60)
# print(SecondsStrBig)
s1 = str((int(SecondsStrBig) // 10) % 10)
# print('s1',s1)
s2 = str(int(SecondsStrBig) % 10)
# print('s2',s2)
SecondsStr = s1 + s2


# print()
print(HoursCount - DaysCount * 24, ':', MinutesStr, ':', SecondsStr, sep='')
