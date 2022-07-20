#function to check whether a number is prime or not
def checkIfPrime(numberTocheck):
    for x in range(2, numberTocheck):
        if(numberTocheck % x == 0):
            return False
    return True
       
