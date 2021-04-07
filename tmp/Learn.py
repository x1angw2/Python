from multiprocessing import Process
import time
import random


def produce(i,name):
    p = Process(target=i,args=(name,))

