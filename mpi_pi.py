"""
This program is based on a program from Gary Sims Gary's explains GitHub account:
https://github.com/garyexplains/examples/blob/master/primality_cluster_test2.py.
It demonstrates parallel processing and MPI by using MPI's gather and scatter commands
to share a list of consecutive integer and search the list for primes.

I added code to time the process and to list the primes at the end of the program>
I am interested in seeing how much the parallel structure speeds up the code. 

This program will test using MPI compute primes using parallel processing on a single processor:
	Intel(R) Core(TM) i7-1065G7 CPU @ 1.30GHz, 1498 Mhz, 4 Core(s), 8 Logical Processor(s)

(1)  The program computes prime numbers.
(2)  Executes the program with several different nodes.
(3)  Records time on a text files stored on the working directory.
 
"""

from mpi4py import MPI
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


mylist = []
totalnodes_list = []
totaltime_list = []
numstested = 0



n = 16
MAXTOTEST = 2 ** n 

primesfound = 0
primei = 0

comm=MPI.COMM_WORLD
rank = comm.rank
totalnodes = comm.size

BATCHSZ = MAXTOTEST // totalnodes

if rank==0:
	print('The total number of nodes is ' + str(totalnodes))

while numstested < MAXTOTEST:
	if rank==0:
		mylist = []
		for i in range(0,totalnodes):
			innerlist = []
			innerlist.append(primei * BATCHSZ)
			innerlist.append(((primei+1) * BATCHSZ)-1)
			mylist.append(innerlist)
			# print(f'innerlist = {innerlist}')
			primei = primei + 1
	
	# print(f'mylist = {mylist}')
	
	me = comm.scatter(mylist, root=0)
	numstested = numstested + (totalnodes * BATCHSZ)
	results = []
	
	# print(f'me[0], me[1] = {me[0]}, {me[1]}')
	
	for p in range(me[0], me[1]+1):
		if isPrimeTrialDiv(p) == True:
			results.append(p)

	# print(f'My rank is {rank} and I am processing {me[0]} to {me[1]}')


	mylist = comm.gather(results)
	
	if rank==0:
		for inn in mylist:
			primesfound = primesfound + len(inn)
		print(f'Primes found so far: {primesfound}')
		# print(f'My rank is {rank} and mylist is {mylist} with length {len(mylist)}')
		end = time.perf_counter()
		totaltime = end - start
		
		with open('mpi_pi_out.txt','a') as f:
			if totalnodes == 1:
				f.write(f'Checking the integers from 2 to 2 ** {n} = {2 ** n} for primes\n')
			f.write(f'Using {totalnodes} node it takes {totaltime} seconds\n')
			if totalnodes == 128:
				f.write('\n')


		print('*' * 50)
		print(f'With {totalnodes} nodes the process takes {totaltime} seconds.')
		print('*' * 50)
