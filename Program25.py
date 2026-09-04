with open("String.txt","r",encoding="UTf-8")as point:
    line=point.readlines()
    for i in range(0,len(line),2):
        print(line[i].strip())
