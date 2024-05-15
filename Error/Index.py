#index error: list,tuple,array, str


lst=[7,'Annamalai',45,10,8,15,20]

tup=(34,56,108,10,'Priya')

from array import *
arr=array('f',[1.2,5.6,8.9,12.4])

s="@Saran"


#print(lst[0],tup[3],arr[2],s[4])

try:
    index = int(input("Tell us index  "))
    print(lst[index], tup[index], arr[index], s[index])
except IndexError as ierror:
    print(ierror)
    print("index within ",len(s))
    index = int(input("Tell us index : "))
    print(lst[index], tup[index], arr[index], s[index])
finally:
    print(" satisfied")