def bleep_vowels(text):
    bleep = "a, e, i, o, u"
    new_str = ""
    for char in text:
        if char.lower() in bleep:
            new_str += "*"
        else:
            new_str += char
    print(new_str)

bleep_vowels("skateboard") #-> 'sk*t*b**rd'
bleep_vowels("slipper") #-> 'sl*pp*r'
bleep_vowels("range") #-> 'r*ng*'
bleep_vowels("brisk morning") #-> 'br*sk m*rn*ng'

def bleep_vowels(text):
    new_str = ""
    for char in text:
        if char in "aeiou":
            new_str = new_str + "*"
        else:
            new_str = new_str + char
    print(new_str)

bleep_vowels("skateboard") #-> 'sk*t*b**rd'
bleep_vowels("slipper") #-> 'sl*pp*r'
bleep_vowels("range") #-> 'r*ng*'
bleep_vowels("brisk morning") #-> 'br*sk m*rn*ng'