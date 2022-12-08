#Recursive program to find out the GCD of two nuumbers.
def gcd(a,b):
    assert int(a) == a and int(b) == b, 'The numbers should be integers only'
    if a < 0:
        a *= -1
    if b < 0:
        b *= -1
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
print(gcd(-36,48))