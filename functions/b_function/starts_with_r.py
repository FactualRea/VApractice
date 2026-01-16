def starts_with_r(line):
    l = line.lower()
    if l[0] == 'r':
        return True
    else:
        return False
    
print(starts_with_r("roger that"))        # True
print(starts_with_r("Row, row, row your boat"))  # True
print(starts_with_r("slip"))              # False
print(starts_with_r("Taxicab"))           # False