#Recursive program to capitalize the first letter of each element of list.
def capitalizeFirst(arr):
    result = []
    if len(arr) == 0:
        return result
    result.append(arr[0][0].upper() + arr[0][1:])
    return result + capitalizeFirst(arr[1:])

words = ['my','name','is','dheeraj','tanwar']
print(capitalizeFirst(words))