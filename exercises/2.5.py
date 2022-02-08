# Write a program where only the process with number zero reports on how many processes there are in total.

from mpi4py import MPI

comm = (
    MPI.COMM_WORLD
)  # Default communicator in MPI. Groups processes together all are connected.
proc_nom = comm.Get_rank()  # Current process number.
nom_procs = comm.Get_size()  # How many processors there are.

if proc_nom == 0:
    print("Total processors:" + str(nom_procs))
