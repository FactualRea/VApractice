def make_acronym(str):
    acronym = ""
    list =str.split(" ")
    for w in list:
        acronym += w[0]
    print(acronym)

make_acronym("New York") 
make_acronym("same stuff different day")  
make_acronym("Laugh out loud") 
make_acronym("don't over think stuff") 