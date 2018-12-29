def parseText(nlp):
    inText = input("please provide sentence to parse\n")
    tokens = nlp(inText)
    lemmas = []
    deps = []
    for token in tokens:
        lemmas.append(token.lemma_)
        deps.append(token.dep_)
    lemmas = ['$' if lemma in ['dollar', 'usd'] else lemma for lemma in lemmas] # map text to symbol
    validation = utils.globalValidation(lemmas)
    if validation:
        print(validation)
        parseText(nlp)
    else:
        lemmas = utils.toSublists(lemmas, 'and') # split to subsentences by 'and'
        deps = utils.toSublists(deps, 'cc')
        zippedPairs = zip(lemmas, deps) # parsed lemmas and syntactic dependency
        getResult(zippedPairs, nlp)


def getResult(zippedPairs, nlp):
    correctCounter = 0
    errorCounter = 0
    validationMessage = ''
    for sbsntc in zippedPairs:
        # print(sbsntc[0], sbsntc[1])
        validation = utils.subsentenceValidation(sbsntc[0], sbsntc[1])
        if validation:
            validationMessage += validation
            errorCounter += 1
        else:
            getResultForSubsentence(sbsntc)
            correctCounter += 1
    showGlobalResult(correctCounter, errorCounter, validationMessage, nlp)


def showGlobalResult(correctCounter, errorCounter, msg, nlp):
    print('\n')
    if correctCounter > 0:
        print(str(correctCounter) + " subsentences parsed correctly")
    if errorCounter > 0:
        print(str(errorCounter) + " subsentences with errors:")
        print(msg)
        parseText(nlp)
    if correctCounter == 0:
        pass # TODO escape sequence here

    inText = input("do you want to add another item? (y/n)\n")
    parseText(nlp) if inText.lower() == 'y' else None


def getResultForSubsentence(sbsntc): # early
    lemmas = sbsntc[0]
    # print(lemmas)
    deps = sbsntc[1]
    # print(deps)
    prepIdx = deps.index('prep')
    price = getPrice(lemmas, prepIdx)
    objIdx = deps.index('dobj') if 'dobj' in deps \
        else deps.index('conj')
    obj = lemmas[objIdx]
    amount = getAmount(lemmas, deps, objIdx)
    print("\nobject: " + obj, "price: " + price, "amount: " + amount)
    # print("-----------------------")


def getPrice(lemmas, prepIdx):
    """get price by prep position""" 
    price = lemmas[prepIdx + 1] + lemmas[prepIdx + 2] # price + currency
    price = '$' + price[:-1] if price[-1:] == '$' else price
    return price


def getAmount(lemmas, deps, objIdx):
    """get amount by obj position"""
    amount = lemmas[objIdx - 1] if deps[objIdx - 1] == 'nummod' \
        else lemmas[objIdx + 1]
    return amount


def init():
    return spacy.load('en') # load only once


import spacy
import utils
nlp = init()
parseText(nlp)