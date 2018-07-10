def listSum(inList):
    return sum(inList)
def listDiff(x,y):
    return x-y
def listProduct(x,y):
    return x*y
def listMax(inList):
    return max(inList)

from helperfunctions.py import listSum
print(listSum([1,2]))
from helperfunctions.py import listDiff
print(listDiff([3,4]))
from helperfunctions.py import listProduct
print(listProduct([5,6]))
from helperfunctions.py import listMax
print(listMax([7,8]))