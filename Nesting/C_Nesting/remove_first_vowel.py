def remove_first_vowel(s):
    vowels = "aeiou"
    for i in range(len(s)):
        if s[i].lower() in vowels:
            first = s[:i] 
            second = s[i+1:]
            return first + second

def remove_first_vowel(s):
    vowels = "aeiou"
    for i in range(len(s)):
        if s[i].lower() in vowels:
            return s[:i] + s[i+1:]

print(remove_first_vowel("volcano"))  # 'vlcano'
print(remove_first_vowel("celery"))  # 'clery'
print(remove_first_vowel("juice"))  # 'jice'
