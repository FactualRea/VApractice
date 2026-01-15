def count_vowels(w):
	vowels = "a,e,i,o,u"
	for i in w:
		if i in vowels:
        
		    w.count(i)

print(count_vowels("hello"))        # 2
print(count_vowels("Programming"))  # 3