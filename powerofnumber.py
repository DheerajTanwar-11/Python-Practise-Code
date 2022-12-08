#Recursive program to apply power function.
def power(base,expo):
    assert expo >= 0 and int(expo) == expo, 'The exponent number is incorrect!'
    if expo == 0:
        return 1
    else:
        return base * power(base,expo-1)

print(power(3,3))