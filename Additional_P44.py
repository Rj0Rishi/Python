class student:
    def __init__(self , name,roll_no):
        self.name = name
        self.roll_no = roll_no
        self.age = None
        self.marks = None

    def setmarks(self ,marks):
        self.marks = marks
    def setage(self ,age):
            self.age = age
    def display(self):
        print("name :",self.name)
        print("roll no :",self.roll_no)
        print("age :",self.age)
        print("marks :",self.marks)

s1 = student("Rishi",500)
s1.setage(20)
s1.setmarks(460)
s1.display()
