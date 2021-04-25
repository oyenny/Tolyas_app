
# НЕДОПИСАНА
h1 = int(input())
m1 = int(input())
s1 = int(input())

h2 = int(input())
m2 = int(input())
s2 = int(input())

s3 = (s1 + s2) % 60
extraM = (s1 + s2) // 60

m3 = (m1 + m2 + extraM) % 60
extraH = (m1 + m2 + extraM) // 60

h3 = (h1 + h2 + extraH) % 24
extraD = (h1 + h2 + extraH) // 24