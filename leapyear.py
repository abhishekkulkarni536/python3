def leap_year(year):
    if year%100!=0 and year%4==0:
        return "is a leap year"
    elif year%100==0 and year%400==0:
        return "is a leap year"
    else:
        return "is not a leap year"

print(leap_year(int(input("enter year to check :  "))))
    
