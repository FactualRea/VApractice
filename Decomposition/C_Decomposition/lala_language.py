def lala_language(sentence):
    ns = sentence.split()
    for i in ns:
        if len(i) > 3:
            for j in i:
                if j in 'aeiou':
                    i = i.replace(j, j + 'l' + j)
            sentence = sentence.replace(i, i)
    return sentence
# Write a function `lala_language` that accepts a sentence string as an argument.
# The function should return a new sentence where words longer than 3 characters
# are modified.
#
# Modified words should have each vowel followed by 'l' and the same vowel again.
# See the examples below.

print(lala_language('this is pretty strange'))
# 'thilis is preletty stralangele'

print(lala_language('can you speak our language'))
# 'can you spelealak our lalangulualagele'
