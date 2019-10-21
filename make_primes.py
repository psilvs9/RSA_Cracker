import random
from math import sqrt

def getRandomPrime(min, max):
    arr = []

    while(min < max):
        if(isPrime(min)):
            arr.append(min)
        min += 1

    x = random.randint(0 , len(arr))

    return arr[x]
        
    
def isPrime(i):
    index = 2
    
    while(isPrime and index < sqrt(i) + 1): 
        if(i % index == 0):
            return False
        index += 1
        
    return True

