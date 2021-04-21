### HOW TO RUN ###
#In the file directory, run:
#python leap_year_error_handling.py
#or
#python3 leap_year_error_handling.py
#depending how you have python setup.
#Then enter in a year > 0 when prompted "Year: ".

while True:
    try:
        user_in = input("Year: ")
        user_in = int(user_in)
        if user_in <= 0:
            raise Exception
        break
    except ValueError:
        print("Enter in an integer greater than 0!")
    except Exception:
        print("Enter a year greater than 0!")


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