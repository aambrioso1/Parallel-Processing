"""
A simple prime search program
 
"""

import math
import time
import plot



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





y_list = []

exp = 20

for n in range(exp):
	MAXTOTEST = 2 ** n
	cumulative_time = []


	trials = 5
	for i in range(trials):
		results = []

		start = time.perf_counter()

		for p in range(0, MAXTOTEST):
			if isPrimeTrialDiv(p) == True:
				results.append(p)

		primesfound = len(results)
				
		end = time.perf_counter()
		totaltime = end - start
		cumulative_time.append(totaltime)
	average_time = sum(cumulative_time) / trials
	y_list.append(average_time)
	print('*' * 50)
	print(f'Checking the integers from 2 to 2 ** {n} - 1 = {2 ** n - 1} for primes.')
	print(f'We found {primesfound} primes')
	print(f'For {trials} trials the process takes an average of {average_time} seconds.')
	print('*' * 50)


x_list = [i for i in range(exp)]
plot.pl(x_list, y_list)
	 