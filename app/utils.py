import numpy as np

def globalValidation(lemmas):
    keywords = ['add', 'put', 'insert']
    if not any(keyw in lemmas for keyw in keywords):
        return "please provide a valid operation type (Add, Put, Insert)\n"
    else:
        return None


def subsentenceValidation(lemmas, deps):
    """early version **
    legit subsentence should have one object, currency 
    and one prep - most probably for
    """
    if 'dobj' not in deps and 'conj' not in deps \
        or deps.count('dobj') + deps.count('conj') != 1:
        return "please provide valid object\n"
    elif '$' not in lemmas:
        return "please provide valid currency ($)\n"
    elif deps.count('prep') != 1:
        return "subsentence is not valid\n"
    else:
        return None


def toSublists(aList, keyword):
    indices = [i for i, x in enumerate(aList) if x == keyword] # fetch keyword idxes
    splitted = np.split(np.array(aList), indices) # split on keywords
    resultList = [] 
    for sublist in splitted:
        resultSublist = sublist.tolist()
        resultSublist.pop(0) # remove keyword for each subsentence
        resultList.append(resultSublist)
    return resultList


def initialParse(inText):
    return inText.replace(',', ' and')
    