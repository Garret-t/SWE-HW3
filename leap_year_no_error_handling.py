### HOW TO RUN ###
#In the file directory, run:
#python leap_year_no_error_handling.py
#or
#python3 leap_year_no_error_handling.py
#depending how you have python setup.
#Then enter in a year > 0 when prompted "Year: ".


user_in = int(input("Year: "))

if user_in % 4 == 0:
    if user_in % 100 == 0:
        if user_in % 400 == 0:
            print(user_in, "is a leap year")
        else:
            print(user_in, "is not a leap year")
    else:
        print(user_in, "is a leap year")
else:
    print(user_in, "is not a leap year")