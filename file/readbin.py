from pickle import *
name=open("Annamalai.txt","rb")
# while True:
#     try:
#         school=load(name)
#         print(school)
#     except EOFError as e:
#         break


content=load(name)
print(content)
content1=load(name)
print(content1)
content2=load(name)
print(content2)
# name.close()
