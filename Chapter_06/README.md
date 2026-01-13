PDC_Coursework – Chapter 6 Experiments

This contains examples and experiments using Pyro4 (Python Remote Objects), Celery (distributed task queue), and Socket programming in Python. The following sections summarize the outputs and observations from running different scripts in the project.

1. Pyro4 – First Example (Simple Server-Client)

Files:

pyro_server.py

pyro_client.py

Steps & Observations:

Start Name Server:

python -m Pyro4.naming


Output:

NS running on localhost:9090 (127.0.0.1)
Warning: HMAC key not set. Anyone can connect to this server!
URI = PYRO:Pyro.NameServer@localhost:9090


Name server started successfully on port 9090.

HMAC key warning indicates unsecured access (acceptable for local testing).

Start Pyro Server:

python pyro_server.py


Output:

Ready. Object uri = PYRO:obj_3908a1f7ca7546238bfb6ad879e148f0@localhost:59945


Server registered with the Pyro name server.

Ready to accept client connections.

Client Execution:

python pyro_client.py


Client prompts for a name and receives a welcome message from the server.

Conclusion:
The Pyro4 first example works successfully when the name server and Pyro server are running. The object URI allows the client to locate the server and execute remote methods.

2. Pyro4 – Second Example (Chain of Servers)

Files:

server_chain_1.py

server_chain_2.py

server_chain_3.py

client_chain.py

Observed Outputs (unordered):

server_chain_1.py:

server_1 started 
1 forwarding the message to the object 2
Back at 1; the chain is closed!


server_chain_2.py:

server_2 started 
2 forwarding the message to the object 3


server_chain_3.py:

server_3 started 
3 forwarding the message to the object 1


client_chain.py:

Result=['passed on from 1', 'passed on from 2', 'passed on from 3', 'complete at 1']


Analysis:

Servers forward messages in a cyclic chain: 1 → 2 → 3 → 1.

The client receives the messages in order of traversal and confirms that the chain completes.

Demonstrates chained remote method calls using Pyro4 proxies.

Conclusion:
The chain server example works as expected. Messages propagate through the servers, and the client receives the cumulative result.

3. Celery Tasks (Add Task Example)

Files:

addTask.py

addTask_main.py

Expected Workflow:

Start a Celery worker:

celery -A addTask worker --loglevel=info


Expected Worker Output:

[INFO/MainProcess] Connected to amqp://guest@localhost//
[INFO/MainProcess] mingle: searching for neighbors
[INFO/MainProcess] mingle: all alone
[INFO/MainProcess] celery@hostname ready.


Execute task from Python:

add.delay(5,5)


Expected Task Output on Worker:

[INFO/MainProcess] Received task: addTask.add[<task-id>]
[INFO/MainProcess] Task addTask.add[<task-id>] succeeded in 0.001s: 10


Conclusion:
The Celery add task executes successfully and returns the expected result of 10 for add(5,5).

4. Socket Programming Example

Files:

server2.py

client2.py

client.py

Socket Client (client.py):

import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()
port = 9999

# connection to hostname on the port
s.connect((host, port))

# receive no more than 1024 bytes
tm = s.recv(1024)
s.close()

print("Time connection server: %s" % tm.decode('ascii'))


Observed Behavior:

Server initially failed to open mytext.txt:

FileNotFoundError: [Errno 2] No such file or directory: 'mytext.txt'


Client (client2.py) executed successfully once the file was present:

file opened
receiving data...
Successfully get the file
connection closed


Simple time client (client.py) successfully received the server time:

Time connection server: Wed Dec 24 03:19:37 2025


Conclusion:

Socket examples work once the source file exists.

The client.py demonstrates a simple TCP connection retrieving server data (here, the server time).

File transfer works correctly in client2.py when the file exists in the server directory.

5. Summary & Key Observations
Example	Status	Notes
Pyro4 – First Example	✅ Works	Client-server communication successful using Pyro4 name server.
Pyro4 – Chain Example	✅ Works	Servers forward messages in a loop; client receives full chain results.
Celery Add Task	✅ Works	add(5,5) executed successfully; worker output shows result 10.
Socket File Transfer	⚠ Initially ❌, then ✅	Works once the source file exists; otherwise FileNotFoundError.
Socket Time Client	✅ Works	Simple client-server TCP communication; client receives server time.