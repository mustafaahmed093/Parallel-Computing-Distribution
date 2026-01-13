from mpi4py import MPI
from do_something import do_something

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    variable_to_share = 100
else:
    variable_to_share = None

variable_to_share = comm.bcast(variable_to_share, root=0)

# Use imported function
results = []
do_something(variable_to_share // 10, results)

print(f"Process {rank}: variable shared = {variable_to_share}, computed {len(results)} results")
