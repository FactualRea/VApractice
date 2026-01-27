def remove_short_words(sentence):
    words = sentence.split(" ")
    result = []
    for i in range(len(words)):
        if len(words[i]) >= 4:
            result.append(words[i])
    print(" ".join(result))


remove_short_words("knock on the door will you") #-> 'knock door will'
remove_short_words("a terrible plan") #-> 'terrible plan'
remove_short_words("run faster that way") #-> 'faster that'