def happy(n1):
    number = 0
    while n1 != 1 and number != 10:
        sum = 0
        while n1 > 0:
            sum += (n1%10)**2
            n1 = int(n1/10)
        n1 = sum
        number += 1
    return n1 == 1


n = 19
print(happy(n))



