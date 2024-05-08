# def greet():
#     ans=input("Tell us ur desired city: ")
#     if ans == 'Chennai': print("Too dangerous to live to now")
#     elif ans == 'Salem': print("Safe to go out")
#     elif ans == 'Villupuram': print("Don't ever think to go")
#     else: print("Stay where you are")
# greet()

def prompt(qual,ref):
    if qual == 'ug' and ref == 'HR':
        print("you are in uk team")
    elif qual == 'diploma' and ref == 'TestLead':
        print("Test Associate")
    elif qual == 'diploma' and ref == 'TestLead':
        print("Test Associate")
    else:print("you are hired")
prompt('engg','Project Manager')
prompt('ug','HR')
prompt(ref='TestLead',qual='diploma')


