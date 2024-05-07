a={'Annamalai','Gowthami','Deepika','priya','priya','sathish'}
print(a)
#duplicates
a={'Annamalai','Gowthami','Deepika','priya','priya','sathish'}
print(a)
print(type(a))
print(len(a))
print(a)
#set constructor
s=set(('Annamalai',"Gowthami","Priya"))
print(s)

#Upadteset
#update
ss={'Annamalai','Gowthami','Deepika','priya','sathish'}
#ss1={"ganesh"}
ss.update("Neha")

print(ss)
#Iteratable
a={'Annamalai','Gowthami','Deepika','priya','priya','sathish'}
li=["Venkat"]
a.update(li)
print(a)
#remove Set
a={1,2,3,"sam","pk"}
a.remove("sam")
print(a)
a.discard(2)

print(a)

 
#pop method
s={"sam","pk","sathish","viji" }
s1=s.pop()
print(s1)
print(s)



#Access Set
a={"sam","pk","anu","sathish"}
for i in a:
    print(i)

#check the set is present or not
a={"sam","pk","anu","sathish"}
print("pk" in a)


