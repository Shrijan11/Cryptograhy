from math import gcd
m = int(input("Enter the number m: "))

list = []

for i in range(0,m):
  list.append(i)

phi_m = 0

for i in list:
  gcd(i,m)
  if gcd(i,m) == 1:
    phi_m = phi_m + 1

print(f"Phi({m}) = {phi_m}")