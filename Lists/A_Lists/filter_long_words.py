def filter_long_words(words):
    lf = []
    for w in words:
        if len(w) < 5:
            lf.append(w)
    print(lf)

filter_long_words(["kale", "cat", "retro", "axe", "heirloom"]) #-> ['kale', 'cat', 'axe']
filter_long_words(["disrupt", "pour", "trade", "pic"]) #-> ['pour', 'pic']