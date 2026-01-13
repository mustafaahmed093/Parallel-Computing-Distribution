from mpi4py import MPI
import numpy
from do_something import do_something

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

senddata = (rank + 1) * numpy.arange(size, dtype=int)
recvdata = numpy.empty(size, dtype=int)
comm.Alltoall(senddata, recvdata)

# Use the imported function
results = []
do_something(5, results)

print(f"Process {rank}: sent {senddata}, received {recvdata}, computed {len(results)} items")
