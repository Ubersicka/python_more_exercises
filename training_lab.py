import math

w = float(input())
h = float(input())
num = (h - 1) * 100 / 70
row = (w * 100 / 120)
sum = math.floor(num) * math.floor(row) - 3
print(sum)
