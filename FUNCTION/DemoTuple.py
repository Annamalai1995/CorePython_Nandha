s=('sam',"Nadhakumar",4,8,8,5)
print(s)
print(type(s))
#range of tuple

a=('Annamalai','Gowthami','Deepika','priya','sathish')
print(a[0:4])
print(a[:2])
print(a[2:])

a1=10
b=10.5
c='Anu'
print(type(a1))
print(type(b))
print(type(c))



#Tuple method
a=(1,2,3,4,5,6,1,8,3,4,1,510,1)
b=a.count(1)
print(b)
#index
s=(1,2,3,4,5,6,7)
d=s.index(2)
print(d)


#append method
a=('Annamalai','Gowthami','Deepika','priya','sathish')
b=list(a)
b.append("Neha")
a=tuple(b)
print(a)
#adding tuple in tuple
a=('Annamalai','Gowthami','Deepika','priya','sathish')
b=("Neha",)
a += b
print(a)



a=('Annamalai','Gowthami','Deepika','priya','sathish')
if 'Gowthami' in a:
    print("Preety ")
else:
    print("NOt valid")

#del keyword
# a=("sam","sathish","anu","pk","raja")
# del a
# print(a)

#Join 
a=('Annamalai','Gowthami','Deepika','priya','sathish')
a=a*3
print(a) 


a=('Annamalai','Gowthami','Deepika','priya','sathish')
b=(1,2,3)
c=a + b
print(c)



a=('Annamalai','Gowthami','Deepika','priya','sathish')
for i in a:
    print(i)
#range methods
a=(1,2,3,"sam","pk")
for i in range(len(a)):
    print(a[i])
#while Loop
'''
a=("sam","raja",1,2,3)
i=0
while i<len(a):
    print(a[i])
    i=i+1'''



#remove
a=('Annamalai','Gowthami','Deepika','priya','sathish')
b=list(a)
b.remove("sathish")
a=tuple(b)
print(a)