def remove_last_vowel(vowel):
    result = ""
    for i in range(len(vowel)-1, -1, -1):
        if vowel[i] in "aeiou":
            result = vowel[:i] + vowel[i+1:]
            break
    return result

# Write a function `remove_last_vowel` that accepts a string as an argument.
# The function should return the string with its last vowel removed.
# Vowels are the letters: a, e, i, o, u

print(remove_last_vowel("speaker"))# 'speakr'
print(remove_last_vowel("trading"))# 'tradng'
print(remove_last_vowel("thunder"))# 'thundr'
print(remove_last_vowel("myth"))# 'myth'