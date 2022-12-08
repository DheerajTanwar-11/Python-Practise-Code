#Recursive program to find the sum of positive integers.
def sum(n):
    assert n >= 0 and int(n) == n,"The Input Number Is Incorrect!"
    if n == 0:
        return 0
    else:
        return n + sum(n-1)
print(sum(100))