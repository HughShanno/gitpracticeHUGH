#Partner 1: Hugh Shanno
#Partner 2: Daniel Elleman
#################################
#Assignment Name: GitHub Practice - 2/25/20 - 20 points
import random
def getNRandom(n):
    '''takes in an integer and returns a list of n random integers between 1 and 10, inclusive'''
    randlist = []
    for i in range(n):
        randlist.append(random.randint(1,10))
    return randlist

def multiplyRandom(numbers):
    '''takes in a list of n numbers and returns the product of the numbers'''
    product = 1
    for num in numbers:
        product = product*num
    return product

def main():
    print(multiplyRandom(getNRandom(10)))

if __name__ == "__main__":
	main()
