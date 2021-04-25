h1 = int(input())
m1 = int(input())
s1 = int(input())

h2 = int(input())
m2 = int(input())
s2 = int(input())

allsec1 = s1 + m1 * 60 + h1 * 60 * 60
allsec2 = s2 + m2 * 60 + h2 * 60 * 60

diffsec = allsec2 - allsec1
print(diffsec)

# d3 = diffsec // (60*60*24)
# h3 = (diffsec // (60*60)) - d3 * 24
# m3 = (diffsec // 60) - (d3 * 24 * 60) - (h3 * 60)
# s3 = diffsec - (d3 * 24 * 60 * 60) - (h3 * 60 * 60) - (m3 * 60)
