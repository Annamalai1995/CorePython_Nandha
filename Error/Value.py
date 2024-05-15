try:
    annual = int(input("Tell us Annual salary: "))
    print(annual / 12*10)
except ValueError as verror:
    print('went inside except block')
    print(verror)
    annual = float(input("Tell us Annual salary: "))
    print((annual / 12)*10)
finally:
    print("Calculation done")