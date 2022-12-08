#Recursive program to capitalize the elements of list.
def capitalizeWords(arr):
    result = []
    if len(arr) == 0:
        return result
    result.append(arr[0].upper())
    return result + capitalizeWords(arr[1:])

words = ['My','name','is','dheeraj','tanwar']
print(capitalizeWords(words))