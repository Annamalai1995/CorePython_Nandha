# Single try and multi except blocks: over fuel calculation

his = (110,150,200,300,900,450,1500,250,360,850)
try:
    litre = int(input("Tell us liter filled: "))
    index = int(input("Select position  to find milage: "))
    print("Selected distance is:",his[index])
    print(his[index] / litre)
except ValueError as verror:
    print(verror)
    print("Data are should be whole numeric")
    litre = int(input("Tell us liter filled: "))
    index = int(input("Select position inorder to find milage: "))
    print("Selected distance is:", his[index])
    print(his[index] / litre)
except IndexError as ierror:
    print(ierror)
    print("Index should be within",len(his))
    ind = int(input("Select position inorder to find milage: "))
    print("Selected distance is:", his[ind])
    print(his[index] / litre)
except ZeroDivisionError as zerror:
    print(zerror)
    print("Liter should not be ZERO")
    litre = int(input("Tell us liter filled: "))
    print("Selected distance is:", his[index])
    print(his[index] / litre)
except Exception as error:
    print(error)