# a={"name":"sam","age":25,"name1":"samm"}
# print(a)
# print(a["age"])

# a={"name":"kumar","name1":"nandha","age":20}
# print(a)
# print(len(a))
# print(type(a))

# # #Adding Dict
# a={"name":"priya","age":27,"Hobbies":"chatting","frds":["Annamalai","priya","Gowthami"]}
# print(a)
# a["college"]="KCE"
# print(a)
# a.update({"Degree":"BE"})
# print(a)


# bio={"Name":"Annamalai","Age":25,"Native":"salem"}
# print(bio)
# #clearMEthod
# bio.clear()
# print(bio)
# print(bio)
# #copyMEthod
# bio={"Name":"Annamalai","Age":25,"Native":"salem"}
# a=bio.copy()
# print(a)
# #get method
# a=bio.get("Native")
# print(a)
# a=bio.get("car","Altroz")
# print(bio)
# print(a)
# print(a)
# #items method
# a=bio.items()
# print(a)
# #key methid
# a=bio.keys()
# print(a)
# a=bio.keys()
# bio["hobby"]="chatting"
# print(a)
# #pop
# bio.pop("Age")
# print(bio)
# a=bio.pop("Name")
# print(a)
#popitems
# bio={"Name":"Annamalai","Age":25,"Native":"salem"}
# print(bio)
# bio.popitem()
# print(bio)
# #set default
# a=bio.setdefault("frnds","pp")
# print(a)
# #update
# bio.update({"car":"altroz"})
# print(bio)
# #values
# a=bio.values()
# print(a)
# a=bio.values()
# bio["CRH"]="pk"
# print(a)


# #Loop Dict
# a={"name":"pp","age":25,"Hobbies":"chatting","frds":["sam","pk","rajesh"]}
# #print(a)
# #key names
# for i in a:
#     print(i)
# #values
# for i in a:
#     print(a[i])
# #using values 
# for i in a.values():
#     print(i)
# #using keys 
# for i in a.keys():
#     print(i)
# #using items
# for i,j in a.items():
#     print(i,j)


#REMOVE 
a={"name":"pp","age":25,"Hobbies":"chatting","frds":["sam","pk","rajesh"]}
print(a)
a.pop("name")
print(a)
#del
del a["age"]
print(a)
#clear
a={"name":"pp","age":25,"Hobbies":"chatting","frds":["sam","pk","rajesh"]}
print(a)
a.clear()
print(a)


#GETTING DICT
a={"name":"pp","age":25,"Hobbies":"chatting","frds":["sam","pk","rajesh"]}
print(a)
b=a.items()
print(b)
#add dict
a["car"]="IGNIS"
print(b)
#check dict
if "name" in a:
    print("yes,do you have chatting with frnds ")

#COPY DICT

a={"name":"pp","age":25,"Hobbies":"chatting","frds":["sam","pk","rajesh"]}
print(a)
b=a.copy()
print(b)
#using bulit fuction
b=dict(a)
print(b)


for i in range(0,10):
    print(i)


#change Dict
a={"name":"pp","age":25,"Hobbies":"chatting","frds":["sam","pk","rajesh"]}
print(a)
a["age"]=29
print(a)
#update dict
a.update({"name":"raja"})
print(a)