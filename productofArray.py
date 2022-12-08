#Recursive program to find the product of elements of array.
def productofArray(arr):
    if len(arr) == 0:
        return 1
    else:
        return arr[0] * productofArray(arr[1:])

print(productofArray([1,2,3,4]))
print(productofArray([1,5,3,8,6,5,3,8,9,7]))