import zmq
import time
import pandas as pd
from gui import Gui
import random

socket = zmq.Context(zmq.REP).socket(zmq.SUB)
socket.setsockopt_string(zmq.SUBSCRIBE, '')
socket.connect('tcp://127.0.0.1:1234')

g = Gui()

while True:
    # receive python object
    signal = socket.recv_pyobj()# 在收到 server 來的 signal 之前，會卡在此行
    
    datas = random.sample(range(0, 1024), 56) # MODIFY HERE! Replace to serial data.
    
    g.update_matrix(datas)
    # g.save_photo("hi.png") 

    # be nice to the cpu
    time.sleep(.1)