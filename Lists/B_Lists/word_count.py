def word_count(sentence, target_words):
    count = 0
    for word in sentence.split(" "):
        if word in target_words:
            count += 1
    print(count)
    
word_count("open the window please", ["please", "open", "sorry"])
word_count("drive to the cinema", ["the", "driver"])
word_count("can I have that can", ["can", "I"]) 