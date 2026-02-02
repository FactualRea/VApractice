def remove_vowels(s):
    vowels = "aeiou"
    no_vowel_words = ""
    for char in s:
        if char.lower() not in vowels:
            no_vowel_words += char
    return no_vowel_words

print(remove_vowels("jello"))  # 'jll'
print(remove_vowels("sensitivity"))  # 'snstvty'
print(remove_vowels("cellar door"))  # 'cllr dr'