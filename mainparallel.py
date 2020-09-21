import pandas as pd
from threading import Thread
from queue import Queue
import os

def runXsec(index, row):
    print("\n \n \n ************Starting Job*****************\n \n \n")
    if row['ranXSec'] == 0:
        print("calculating xsections for: n1={}, n2={}, n3={}, j0= {}".format(row['n1'], row['n2'], row['n3'], row['j0']))

        os.system('./xSection/calcXSection.sh {} {} {} {}'.format(row['n1'], row['n2'], row['n3'], row['j0']))

        data.at[index,'ranXSec'] = 1

        data.to_csv('input.csv',index=False)

    else:
        print("already calculated xsections for: n1={}, n2={}, n3={}, j0= {}".format(row['n1'], row['n2'], row['n3'], row['j0']))

    return None

data = pd.read_csv('input.csv')

#Define jobs
que =Queue()
def worker():
    while True:
        index, row = que.get()
        runXsec(index, row)
        que.task_done()
N_cores=10
for i in range(N_cores):
    thread=Thread(target=worker)
    #thread.deamon= True
    thread.start()
    
for index, row in data.iterrows():
    #runXsec(index, row)
    que.put((index, row))
que.join()
