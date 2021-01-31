try:
    year = int(input("Enter Year: "))
    if(year > 0):
        if((year % 4) == 0) :
            if(year % 100 == 0):
                if(year % 400 == 0):
                    print(year, "is a leap year.")
                else:
                    print(year, "is not a leap year.")
            else:
                print(year, "is a leap year.")
        else:
            print(year, "is not a leap year.")
    else:
        print("Please enter an integer larger than 0 for your year.")
except ValueError:
    print("Not a valid year. Please enter an integer.")
    
    