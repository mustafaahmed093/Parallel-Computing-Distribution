import numpy
from mpi4py import MPI
from do_something import do_something

comm = MPI.COMM_WORLD
size = comm.size
rank = comm.rank

array_size = 10
recvdata = numpy.zeros(array_size, dtype=numpy.int32)
senddata = (rank + 1) * numpy.arange(array_size, dtype=numpy.int32)

print(f"Process {rank} sending {senddata}")

comm.Reduce(senddata, recvdata, root=0, op=MPI.SUM)

if rank == 0:
    results = []
    do_something(5, results)
    print(f"On task {rank}, after Reduce: data = {recvdata}, computed {len(results)} results")
