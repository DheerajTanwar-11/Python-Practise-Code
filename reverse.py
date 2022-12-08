#Recursive Program to Reverse the String.
def reverse(string):
    if len(string) <= 1:
        return string
    else:
        return string[len(string) - 1] + reverse(string[0:len(string)-1])

print(reverse('python'))
print(reverse('java'))