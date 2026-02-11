def double_vowel(word):
    result = ""
    for i in word:
        if i in "aeiou":
            result += i * 2# result = result + i + i
        else:
            result += i
    return result

print(double_vowel("runner"))
# 'ruunneer'

print(double_vowel("stoplight"))
# 'stoopliight'

print(double_vowel("gardener"))
# 'gaardeeneer'

