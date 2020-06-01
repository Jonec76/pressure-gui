import zmq
import time
from pandas_datareader import data

# create the zmq context and socket and bind the socket to port 1234
socket = zmq.Context(zmq.REP).socket(zmq.PUB)
socket.bind("tcp://*:1234")
print("\nClient has connected \n")

while True:
    socket.send_pyobj(1)
    time.sleep(1)
    print("Server: send signal")
