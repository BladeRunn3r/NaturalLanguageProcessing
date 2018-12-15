def parseText():
    nlp = spacy.load('en')
    inText = input("please provide sentence to parse\n")
    tokens = nlp(inText)
    lemmas = []
    deps = []
    for token in tokens:
        lemmas.append(token.lemma_)
        deps.append(token.dep_)
    lemmas = ['$' if lemma in ['dollar', 'usd'] else lemma for lemma in lemmas] # map text to symbol
    validation = checkInput(lemmas)
    if validation:
        print(validation)
        parseText()
    else:
        zippedPairs = zip(lemmas, deps) # parsed lemmas and syntactic dependency
        print(list(zippedPairs)) # TODO add final logic stub


def checkInput(lemmas):
    if '$' not in lemmas:
        return "please provide valid currency"
        # TODO better logic for many items in same sentence 
    elif 'add' not in lemmas:
        return "please provide a valid operation type (eg Add)"
    else: 
        # TODO ask specifically for item/price if still here
        return None 

import spacy
parseText()