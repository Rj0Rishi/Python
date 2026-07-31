year = int(input("Enter a year: "))
if (year % 4 == 0):
    if (year % 100 ==0):
        if(year % 400 == 0):
            print(year ,"Is a eap Year")
        else:
            print(year , "Is not a leap Year")
    else:
        print(year , "Is a leap Year")
else:
    print(year ,"Is not a leap Year")
