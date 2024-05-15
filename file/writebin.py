from pickle import *
name=open("Annamalai.txt","wb")
school=[101,"Nandhakumar","Swamy","Salem"]

college={"Name":"Nandhakumar","College":"kumaraguru","Rollno":501}

Frnds=("Naveen","Mohan")

dump(school,name)
dump(college,name)
dump(Frnds,name)
name.close()
