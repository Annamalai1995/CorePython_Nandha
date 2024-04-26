'''

control statement: 
    in oder to understand user requirement also 
    let the user have their execution flow
    
if

syntax:
if
if condition:
    # true branch
    
if else
if condition:
    # true branch
else:
    # false branch

nested if
if condition1:
    #true branch1
    if condition2:
        # true branch2
    else:
        # false branch2
else:
    # false branch1
    
elif ladder
if condition1:
    #true branch1
elif condition2:
    # true branch2
elif condition3:
    # true branch3
.
.
.
.- 
else:
    #false branch

'''

# person=input("Tell us what you are? staff, student or teachers ")

# if person == "student" or person=="staff" or person=='teachers':
#     print("We let you inside the campus")
# else:
#     print("we can't let you inside the campus")

# # themepark
# age=int(input("Tell us age "))
# if age>=18:
#     print("Welcome to wonderLa adventure spot")
#     print("Where you can have thrilling water games")
#     gender=input("tell us gender to find your zone ")
#     if gender == "male" or gender=="MALE":
#         print("your zone number is 42M")
#     else:
#         print("your zone number is 92A,92W")
# else:
#     print("Welcome to wonderLA kids zone at 56Q")


#find vote booth
ward=int(input("Enter the ward number "))
if ward>=31 and ward<=38:
    partNo=int(input("Tell us part number to find vote booth room "))
    if partNo==498:
        print("room no 101 is your voting booth")
    elif partNo==501:
        print("room no 104 is your voting booth")
    elif partNo==911:
        print("room no 102 is your voting booth")
    elif partNo==455:
        print("room no 103 is your voting booth")
    else:
        print("invalid part no")
else:
    print("This isn't your vote zone")