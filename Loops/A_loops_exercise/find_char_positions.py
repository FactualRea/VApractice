def find_char_positions(text, char):
    for i in text:
        if i == char:
            print(text.index(i))
            

find_char_positions("banana", "a")