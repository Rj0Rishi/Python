s = input("Enter a string:")
rev = ""
for char in s:
    rev = char + rev

if s == rev:
    print("It is Palindrome")
else:
    print("It is not a Palindrome")
