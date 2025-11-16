userName = input("Create a user name?: ")
if len(userName) > 12:
    print("ur userName is not Valid...!")
elif not userName.isalpha():
    print("userName must not contain numbers or symbols...")
elif not userName.find(" ") == -1:
    print("userName must not contain spaces...")
else:
    print("User registered successfully...!")