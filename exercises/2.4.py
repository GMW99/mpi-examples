from mpi4py import MPI

comm = (
    MPI.COMM_WORLD
)  # Default communicator in MPI. Groups processes together all are connected.
proc_nom = comm.Get_rank()  # Current process number.
nom_procs = comm.Get_size()  # How many processors there are.

# Print to console
print("\n Starting processes %d out of %d" % (proc_nom, nom_procs))

# Write to a file
f = open("hello.txt", "a")
f.write("Starting processes %d out of %d \r\n" % (proc_nom, nom_procs))
f.close()

# Only Process 0 report how many processes into total
