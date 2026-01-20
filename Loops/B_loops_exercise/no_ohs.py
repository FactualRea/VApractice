def no_ohs(text):
    for char in text:
        if char == "o" or char == "O":
            continue
        print(char)

no_ohs("code") 

def no_ohs(str):
    for char in str:
        if char != "o":
            print(char)

no_ohs("Hello World")