#Recursive progarm to flatten the given list.
def flatten(arr):
    result = []
    for i in arr:
        if type(i) == list:
            result.extend(flatten(i))
        else:
            result.append(i)
    return result

print(flatten([[1], [2], [3]]))
print(flatten([[[[1], [[[2]]], [[[[[[[3]]]]]]]]]]))