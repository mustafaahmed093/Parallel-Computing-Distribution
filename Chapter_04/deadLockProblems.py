from mpi4py import MPI
from do_something import do_something

comm = MPI.COMM_WORLD
rank = comm.rank

print("My rank is", rank)

if rank == 1:
    data_send = "a"
    destination_process = 5
    source_process = 5

    data_received = comm.recv(source=source_process)
    comm.send(data_send, dest=destination_process)

    results = []
    do_something(5, results)

    print(f"Process {rank}: sent {data_send} to {destination_process}, received {data_received}, computed {len(results)} results")

elif rank == 5:
    data_send = "b"
    destination_process = 1
    source_process = 1

    comm.send(data_send, dest=destination_process)
    data_received = comm.recv(source=source_process)

    results = []
    do_something(5, results)

    print(f"Process {rank}: sent {data_send} to {destination_process}, received {data_received}, computed {len(results)} results")
