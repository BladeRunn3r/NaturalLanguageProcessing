import numpy as np

def globalValidation(lemmas):
    if 'add' not in lemmas:
        return "please provide a valid operation type (eg Add)\n"
    else: 
        return None


def subsentenceValidation(lemmas, deps): # early version
    if 'dobj' not in deps and 'conj' not in deps and 'pobj' not in deps:
        return "please provide valid object"
    elif '$' not in lemmas:
        return "please provide valid currency ($)\n"
    elif 'nummod' not in deps or 'prep' not in deps:
        return "subsentence is not valid"
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