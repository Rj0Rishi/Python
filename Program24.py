with open("String.txt","r",encoding="UTF-8") as point1:
    content=point1.read()
    with open("New.txt","a",encoding="UTF-8")as point2:
        point2.write(content)
print("Content of 'String.txt' have been added to 'New.txt'.")        
