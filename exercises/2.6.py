from math import sqrt, ceil
from mpi4py import MPI

comm = MPI.COMM_WORLD

bignum = 2000000111
maxfactor = 45200
####
#### Exercise:
#### - parallelize the loop so that each process
####   tries different candidate numbers
#### - if a process finds a factor, print it to the screen

procno = comm.Get_rank()  # Current process number.
nom_procs = comm.Get_size()  # How many processors there are.

if procno == 0:
    print("Total processors:" + str(nom_procs))

lower_bound = maxfactor*procno+1
upper_bound = maxfactor*(procno+1)

for myfactor in range(lower_bound, upper_bound):
    if bignum%myfactor==0:
        print("Processor %d found factor %d" % (procno, myfactor))
