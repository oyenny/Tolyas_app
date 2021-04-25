h = int(input())
a = int(input())
b = int(input())

dspeed = a - b
# print('dspeed', dspeed)

newh = h + a
c = a + dspeed - 1 // dspeed
print(c)

prevdnewh = (newh - a) // dspeed

print(prevdnewh - c + 1)





