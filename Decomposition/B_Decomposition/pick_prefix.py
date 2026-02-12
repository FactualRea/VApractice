def pick_prefix(strings, prefix):
    resut = []
    prefix_length = len(prefix)
    for string in strings:
        if string[:prefix_length] == prefix:
            resut.append(string)
    return resut


# Write a function `pick_prefix(strings, prefix)` that accepts:
# - a list of strings
# - a prefix string
#
# The function should return a list of words that begin with the prefix.

print(pick_prefix(['connect','company','concert','cram'],'con'))
# ['connect', 'concert']

print(pick_prefix(['miner','mistake','misspeak','moose','mission'],'mis'))
# ['mistake', 'misspeak', 'mission']
