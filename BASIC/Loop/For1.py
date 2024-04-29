'''
Looping statements:
    repeataion to ignore rewrite same statement multiple times
    series, patterns, real time process
    
    attributes:
        loop control var/obj
            start       initialization
            end         condition
            step up     iteration
    types:
        while
        for>> for in range
           >> for in
'''

# for bike in "Nandhakumar":
#     print(bike)

# alpha={5300,"Nandhakumar",6.0,600}
# for n in alpha:
#     print(n)

tup=("Nadha",4500.2,"kumar","Wipro",True)
# for q in tup:print(q)
# pos=0
# while pos<len(tup):
#     print(tup[pos])
#     pos+=1

# pos=2
# while pos<len(tup):
#     print(tup[pos])
#     pos+=1

# pos=0
# while pos<len(tup)-2:
#     print(tup[pos])
#     pos+=1

# for index in range(len(tup)):
#     print(tup[index])

# for index in range(len(tup)-2):
#     print(tup[index])

# for index in range(2,len(tup)-1):
#     print(tup[index])

# for index in range(len(tup)-1,-1,-1):
#     print(tup[index])

# for var in range(start,condition,iter):
    # loop ends before condition step
    # default iteration is +1
    # default initialization is 0
# for hai in range(1,101,+1):
#     print(hai)

# for hai in range(1,101):
#     print(hai)

# for hai in range(1,101,+2):
#     print(hai)

# for hai in range(100,2,-1):
#     print(hai)

# for hai in range(101):
#     print(hai)

# fibonacci series: 0 1 1 2 3 5 8 13 21 34 55 
# end=int(input("tell us how many digits you want in the series "))#10
# num1,num2=0,1
# if end>=2:
#     print(num1)
#     print(num2)
#     for steps in range(3,end+1):
#         sum=num1+num2
#         print(sum)
#         num1=num2
#         num2=sum
# else:
#     print("fibonacci wouldn't come")


# sale
stock=5
for stock in range(5,0,-1):
    amt=int(input("enter the amount to purchase "))
    if amt>=10000:
        print("stock quantity one has purchased")
        stock-=1
    else:
        print("insufficient amount to purchase")
