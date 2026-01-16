def wacky_word(str1, str2):
    word = str1[:3:] + str2[::]
    return word

print(wacky_word("very", "kindly"))       # "verly"
print(wacky_word("forever", "sick"))      # "forck"
print(wacky_word("cellar", "door"))       # "celor"
print(wacky_word("bagel", "sweep"))       # "bagep"