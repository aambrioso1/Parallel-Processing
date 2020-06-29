"""
A simple prime search program
 
"""

import math
import time

start = time.perf_counter()

def isPrimeTrialDiv(num):
    # Returns True if num is a prime number, otherwise False.
    # Uses the trial division algorithm for testing primality.
    # All numbers less than 2 are not prime:
    if num < 2:
        return False

    # See if num is divisible by any number up to the square root of num:
    i = 2
    lim = int(math.sqrt(num)) + 1
    while i < lim:
        if num % i == 0:
                return False
        i = i + 1

    return True

results = []

n = 16
MAXTOTEST = 2 ** n 

for p in range(0, MAXTOTEST):
	if isPrimeTrialDiv(p) == True:
		results.append(p)

primesfound = len(results)
		
end = time.perf_counter()
totaltime = end - start
		
print('*' * 50)
print(f'Checking the integers from 2 to 2 ** {n} - 1 = {2 ** n - 1} for primes.')
print(f'We found {primesfound} primes')
print(f'The process takes {totaltime} seconds.')
print('*' * 50)
 