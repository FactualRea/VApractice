def shorten_long_words(sentence):
    words = sentence.split()
    shortw = []
    
    for w in words:
        if len(w) <= 4:
            new_w = ""
            for char in w:
                if char.lower() not in "aeiou":
                    new_w += char
            shortw.append(new_w)
        else:
            shortw.append(w)
    return " ".join(shortw)

print(shorten_long_words("they are very noble people"))  # 'they are very nbl ppl'
print(shorten_long_words("stick with it"))  # 'stck with it'
print(shorten_long_words("ballerina, you must have seen her"))  # 'bllrna, you must have seen her'