def is_palindrome(word):
    if word.lower() == word[::-1].lower():
        return True
    else:
        return False
    
print(is_palindrome("level"))          # True
print(is_palindrome("Race car"))       # True
print(is_palindrome("python"))         # False

