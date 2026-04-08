citizen = input("Are you an INDIAN citizen?(Y/N): ")
if citizen == "Y" or citizen == "y":
    age = int(input("What is your age?: "))
    if age>=18:
        print("Eligible")
    elif age<0:
        print("INVALID INPUT")
    else:
        print("Not Eligible")
else:
    print("Not Eligible to VOTE here...")

# ALL BASIC CONDITIONS

# result = "Positive" if a>b else "Negative"
# result = a if a%2==0 else b
# min_num = "a" if a<b else "b"
# max_num = "a" if a>b else "b"
# status = "adult" if age>18 else "Teen"
