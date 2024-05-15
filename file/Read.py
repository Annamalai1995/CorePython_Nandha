
nandha=open("./kumar.doc",'a')
print("File created",nandha.name)
#nandha.write("MY 12 Marks is 551 outof 600")
#print(nandha.read())
print(nandha.writable())
print(nandha.readable())
print(nandha.mode)
nandha.write("My cut of is 192.5")
print("Append successfully")
nandha.close