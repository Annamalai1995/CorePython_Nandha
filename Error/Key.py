#KeyError


names={"name":['Annamalai','swetha','Gowthami','priya'],
           "skills":['Html','Springboot','python','Django'],
           "poc":[4,3,6,2],
           "annum":[4.5,10.5,6.5,8.5,12.5],
           "org":'CTS'}

print(names['name'][2])

try:
    details = input("Tell us what you want: ")
    print(names[details])
except KeyError as kerror:
    print(kerror)
    print("Column/ credential",details,"not found")
    details = input("Tell us what you want: ")
    print(names[details])
finally:
    print("Verify")