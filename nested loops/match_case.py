day=int(input("enter day number"))
match day:
    case 0:
        print("monday")
    case 1:
        print("tuesday")
    case 2:
        print("wednesday")
    case 3:
        print("thursday")
    case 4:
        print("friday")
    case 5:
        print("saturday")
    case 6:
        print("sunday")
    case _:
        print("invalid day number")