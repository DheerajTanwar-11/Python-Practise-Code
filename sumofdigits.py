#Recursive program to find the sum of digits of number.
def sumofdigits(n):
    assert n >= 0 and int(n) == n, "The input number is not correct!"
    if n == 0:
        return 0
    else:
        return int(n%10) + sumofdigits((int(n/10)))

print(sumofdigits(547))