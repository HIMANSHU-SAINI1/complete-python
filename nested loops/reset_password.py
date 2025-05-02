password=input("enter password")
confirm_password=input("confirm password")

if password==confirm_password:
    print("password changed")
else:
    if password.casefold()==confirm_password.casefold():
        print("please check cases and try again")
    else:
        print("password do not match")