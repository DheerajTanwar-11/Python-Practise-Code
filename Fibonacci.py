#Recursive program to find out the nth element of fibonacci series.
def fibonacci(n):
    assert n>= 0 and int(n) == n,"Input Number Is Not Correct!"
    if n in [0,1]:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(6))