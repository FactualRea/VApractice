def lengthiest_word(sentence):
    length = 0
    ans_word = ""
    ls_words = sentence.split(" ")
    for word in ls_words:
        if len(word) >= length:
            length = len(word)
            ans_word = word
    print(ans_word)
    
lengthiest_word("I am pretty hungry")
lengthiest_word("we should think outside of the box") 
lengthiest_word("down the rabbit hole") 
lengthiest_word("simmer down") 