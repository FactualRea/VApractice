def count_vowels(w):
	vowels = "aeiou"
	return sum(1 for char in w.lower() if char in vowels)


print(count_vowels("hello"))        # 2
print(count_vowels("Programming"))  # 3