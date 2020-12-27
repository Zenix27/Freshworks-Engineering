import threading 
import time
from threading import*

para={} 


def create(key,value,runtime=0):
    if key in para:
        print("ERROR: key already present") 
    else:
        if(key.isalpha()):
            if len(para)<(1024*1020*1024) and value<=(16*1024*1024): 
                if runtime==0:
                    z=[value,runtime]
                else:
                    z=[value,time.time()+runtime]
                if len(key)<=32: 
                    para[key]=z
            else:
                print("ERROR: The memory limit has exceeded ")
        else:
            print("ERROR: keyname INVALID, it should contain alphabets only, no special characters or numerics allowed")


            
def read(key):
    if key not in para:
        print("ERROR: Enter a valid key, the given key does not exist in DB") 
    else:
        x=para[key]
        if x[1]!=0:
            if time.time()<x[1]: 
                arr=str(key)+":"+str(x[0]) 
                return arr
            else:
                print("ERROR: time_to_live of the",key,"has terminated") 
        else:
            arr=str(key)+":"+str(x[0])
            return arr



def delete(key):
    if key not in para:
        print("ERROR: Enter a valid key, the given key does not exist in DB") 
    else:
        x=para[key]
        if x[1]!=0:
            if time.time()<x[1]: 
                del para[key]
                print("Key has been deleted")
            else:
                print("ERROR: time_to_live of the",key,"has terminated") 
        else:
            del para[key]
            print("Key has been deleted")



def modify(key,value):
    x=para[key]
    if x[1]!=0:
        if time.time()<x[1]:
            if key not in para:
                print("ERROR: Enter a valid key, the given key does not exist in DB") 
            else:
                z=[]
                z.append(value)
                z.append(x[1])
                para[key]=z
        else:
            print("ERROR: time_to_live of the",key,"has terminated") 
    else:
        if key not in para:
            print("ERROR: Enter a valid key, the given key does not exist in DB") 
        else:
            z=[]
            z.append(value)
            z.append(x[1])
            para[key]=z
