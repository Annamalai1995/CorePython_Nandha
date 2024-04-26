#relational >,<,>=,<=
#personal Loan
score=int(input("enter the cibil score"))
print("To get loan 1Lakh",(score>=650))
Assert=int(input("Tell us Assert details"))
print("To get Businness Loan 10Lakh:",(score>=800 and Assert>8))
print("To get home loan 50Laksh:",(Assert>=9 or score>=950))


