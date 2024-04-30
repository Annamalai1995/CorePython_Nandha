# #demonstration of LIST
# prop=["Annamalai",5.5,70,'M']
# print(prop)
# #adding the new elements in end if list
# prop.append('Software developer')
# print(len(prop))
# print(prop)
# #adding new elements in list
# prop.insert(4,15.5)
# print(prop)
# #replace the data in respective position
# prop[5]='Team lead'
# print(prop)
# #adding values in list
# monthly=[7000,8000,13000,3000,25000]
# print(min(monthly))
# #sum of the list
# print(sum(monthly))
# #remove and pop the list operation
# monthly.remove(3000)
# print(monthly)
# print(monthly.pop())
# print(monthly.pop(1))
# print(monthly)
# print(monthly.reverse())
# print(monthly)

#Sum of List
sum=[4000,500,555,888,444]
print(sum)
print(sum.pop())
print(sum.pop(3))
print(sum)
sum.reverse()
print(sum)


#List Methods:
li=[1,4,5,6,1,5,8]
a=li.copy()
print('cpy:',a)
count=a.count(5)
print(count)

#List User 
a=input("Enter the name")
list=a.split(",")
print("list names")
for i in list:
    print(i)


#Looping List Values

n=int(input("Enter the lis"))
list1=[]
for i in range(n):
    lival=input("enter the list:")
    list1.append(lival)
    
print("list:",list1)


#Middle List
a=[14,20,50,48,60,80]
print("original list:",a)
val=int(input("Enter the new elemnts:"))
insert=int(input("Enter the position:"))
a.insert(insert,val)
print("Added list:",a)


