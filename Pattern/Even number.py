row = 5
for i in range(row):
    num = 2**i # i power of 2
    row_number = [] #save numbers in a row
    while num >= 1:
        row_number.append(str(num)) # add number in list
        num = num//2
    
    print(" ".join(row_number))
