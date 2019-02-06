class Collector:

 add = 0
count = 0
sum = 0
sum_squares = 0
average = 0
variance = 0
standard_deviation= 0

myList = input("Enter a series of integers")
print(myList)
type(myList)

def __init__(self, add, count, sum, sum_squares, average, variance, standard_deviation):
    self.add = add
    self.count = len(myList)
    self.sum = sum
    self.sum_squares = sum_squares
    self.average = sum/count
    self.variance = variance
    self.standard_deviation = standard_deviation



print(

#Add
    print("What index would you like to add the number to?")
    index =[int(z) for z in input().split()]
    print("What number would you like to add?")
    value = [int(y) for y in input().split()]
    myList.insert(index, value)
    print("Updated List:",myList)