"""
Given n as input, print the sum of 3^1 + 3^2+....+3^n
Input-> n=3
Output -> 39 (because 39 = 3+9+27)
"""

n = 3
b = 3
total = 0
for i in range(1,n+1):
  total = total + b**i
print(total)
