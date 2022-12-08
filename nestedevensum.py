#Recursive program to find the sum of even key values of a dictionary.
def nestedevensum(obj,sum=0):
    for key in obj:
        if type(obj[key]) is dict:
            sum += nestedevensum(obj[key])
        elif type(obj[key]) is int and obj[key] % 2 == 0:
            sum += obj[key]
    return sum

obj1 = {
  "outer": 2,
  "obj": {
    "inner": 2,
    "otherObj": {
      "superInner": 2,
      "notANumber": True,
      "alsoNotANumber": "yup"
    }
  }
}

print(nestedevensum(obj1,sum=0))