def funny_phrase(sentence):
    list = sentence.split(" ")
    ans_list = []
    for i in range(len(list)):
        if 3 % 2 == 0:
            ans_list.append(list[i])
        else:
            double_word = double_word(list[i])
            ans_list.append(double_word)

def double_vowel(word):
    result = ""
    for i in word:
        if i in "aeiou":
            result += i * 2# result = result + i + i
        else:
            result += i
    return result