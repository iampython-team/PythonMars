import Levenshtein
#First list
keywords =['gradient','maxima','explore','weight']
#Second list
tokens = ['Let', "'s", 'also', 'see', 'what', 'a', 'macsyma', 'ingredient', 'and', 'explore', 'ingredient', 'mean', 'wait']


for i in range(len(mylist)):
    for token in range(len(tokens)):
        if Levenshtein.distance(mylist[i],tokens[token]) <= 3:
            tokens[token]=mylist[i]
            