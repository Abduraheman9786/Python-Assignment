Age=int(input("Enter Your Age: "))

if Age<0 or Age>150:
    print("Invalid Age")
elif Age>=18:
    print("Eligible For Voting")
else:
    print("Not Eligible For Voting")