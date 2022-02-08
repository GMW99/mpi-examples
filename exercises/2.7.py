from mpi4py import MPI

comm = (
    MPI.COMM_WORLD
)  # Default communicator in MPI. Groups processes together all are connected.
rank = comm.Get_rank()  # Current process number.
nom_procs = comm.Get_size()  # How many processors there are.

if rank == 0:
    print("Total processors:" + str(nom_procs))

mpi_array = []

size_of_array = 10
# Print to console
print("\n Starting processes %d out of %d" % (rank, nom_procs))
lower_bound = size_of_array * rank+1
upper_bound = size_of_array * (rank+1)


for i in range(lower_bound, upper_bound):
    mpi_array.append(i)
print(mpi_array)
