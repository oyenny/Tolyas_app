digit = int(input())
hundreds = digit // 100
# print(hundreds)
tens = (digit // 10) % 10
# print(tens)
units = digit % 10
# print(units)

print(hundreds + tens + units)
