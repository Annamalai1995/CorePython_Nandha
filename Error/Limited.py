# no of limited chances

from array import *
arr=array('i',[128,45,85,98,101,102,65,45,66,77,58])

def extract(index,limit=1):
    try:
        print(arr[index])
    except IndexError as ierror:
        print(ierror)
        limit+=1
        if limit<=2:
            extract(int(input("Tell us index: ")),limit)
        else:
            return
        #print(arr[int(input("Tell us index: "))])


extract(int(input("Tell us index: ")))