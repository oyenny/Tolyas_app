A = int(input())
B = int(input())
N = int(input())

CostInKop = (A * 100) + B
CostAllPurchise = CostInKop * N

print(CostAllPurchise // 100, CostAllPurchise % 100)
