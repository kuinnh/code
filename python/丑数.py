n = 6
if n <= 0:
    print("False")
for i in [2, 3, 5]:
    while n % i == 0:
        n //= i

if n == 1:
    print("True")
else:
    print("False")


























