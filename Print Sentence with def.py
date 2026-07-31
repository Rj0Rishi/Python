def split_and_join(text):
    words = text.split()
    new_text = "-".join(words)
    return new_text
message = input("Enter a sentence : ")
print(split_and_join(message))
