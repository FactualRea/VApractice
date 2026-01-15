def case_change(text, make_upper):
    if make_upper:
        return text.upper()
    else:
        return text.lower()

print(case_change("Super", True))      # SUPER
print(case_change("Super", False))     # super
print(case_change("tAmBourine", True)) # TAMBOURINE
print(case_change("tAmBourine", False))# tambourine
