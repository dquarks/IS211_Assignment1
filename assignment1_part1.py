
def listDivide(numbers, divide=2):
    t = [i % divide for i in numbers]
    v = [x for x in t if x == 0]

def testListDivide():
    listDivide([1,2,3,4,5])
    listDivide([2,4,6,8,10])
    listDivide([30,54,63,98,100], divide=10)
    listDivide([])
    listDivide([1,2,3,4,5], 1)

class ListDivideException(Exception):
    pass

try:
    testListDivide()
except:
    print("Error")
