from mpi4py import MPI
from do_something import do_something

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

data = (rank + 1) ** 2
data = comm.gather(data, root=0)

results = []
do_something(5, results)

if rank == 0:
    print(f"Rank {rank}: gathered data = {data}, computed {len(results)} results")
    for i in range(1, size):
        print(f" Process {rank} received {data[i]} from process {i}")
