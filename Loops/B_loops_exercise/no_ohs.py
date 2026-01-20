def no_ohs(text):
    for char in text:
        if char == "o":
            continue
        print(char)

no_ohs("code") 

def no_ohs(str):
    for char in str:
        if char != "0":
            print(char)

no_ohs("Hello World")