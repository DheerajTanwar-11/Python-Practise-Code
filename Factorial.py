#Recursive program to find out the factorial of given number.
def factorial(n):
    assert n >= 0 and int(n) == n , "Input number is not correct"
    if n in [0,1]:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(-1))