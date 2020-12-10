#!/usr/bin/env python
from pyparsing import *
from enum import Enum
import sys
import re

class UsualFct(Enum):
    cos = 1
    sin = 2
    tan = 3
    abs = 4
    sqrt = 5
    exp = 6
    log = 7
    power = 8
    cbrt = 9
    arccos = 10
    arcsin = 11
    arctan = 12

# Function : ANALYSEUR SYNTAXIQUE
def VerifToken(tokenArray):
    tokenString = ''.join(str(v) for v in tokenArray).replace("]", '').replace("[", '') #List to string and remove '[' and ']'
    tokenArray = re.compile("'([^']*?)'").split(tokenString)  #Match simple quote element
    tokenString = ""
    for element in tokenArray:
        element = re.sub(r'(\W|\w),(\w)', r'\1_\2', element)  #Fix `power(x,y)` function issue, replacing ',' to '_' in array element
        tokenString += element  #Convert to string 

    tokenString = tokenString.replace(",", '').replace(" ", '').replace("'", '')  #removing withespace and quote
    tokenString = tokenString.replace("_", ',')  #replacing '_' to simple ','

    # Match all funtion string, with a length from 3 to 6
    tokenFct = re.findall(r'\b[a-zA-Z]{3,6}',tokenString)

    # Check if given function(s) are supported
    for fct in tokenFct:
        if fct not in UsualFct._member_names_:
            # DEBUG
            #print("Mauvaise saisie: ")
            #print(fct)
            return False

        else:
            # Prefix function name with "np" to use numpy math function (function_name => np.function_name)
            tokenString = tokenString.replace(fct, "np."+fct)      

    return tokenString


# Function : ANALYSEUR LEXICAL
def LexicalAnalysis(myExpr):
    myExpr = myExpr.replace(" ", "") #remove withespaces
    expr = Forward()
    integer = Word(nums).setParseAction(lambda t:int(t[0]))  #  -> "W:(0-9)"   Convert num string to int 
    variable = Word(alphas)    ##     -> "W:(A-Za-z)"
    #double = Word(nums + ".").setParseAction(lambda t:float(t[0]))   #  -> "W:(0-9)"   Convert num string to float 
    
    argFunc = Group(Optional(delimitedList(expr, delim=',', combine=True)))
    funccall = Group(variable + "(" + argFunc + ")")

    #array_func = Group(funccall + "[" + Group(delimitedList(expr, "][")) + "]")  #match array element after function : fct()[0]
    #array_var = Group(variable + "[" + Group(delimitedList(expr, "][")) + "]")  #match array : array['a','b']

    operand = integer | funccall | variable    # (pick the first left-to-right match)

    expr << infixNotation( operand,
     [
        ('-', 1, opAssoc.RIGHT),
        (oneOf('* /'), 2, opAssoc.LEFT),  #Repetition of one or more of the given expression
        (oneOf('+ -'), 2, opAssoc.LEFT),
    ])

    result = expr.parseString(myExpr)

   # DEBUG
   # expr.runTests('''
   # -2--11
   # 5+3*6
   # (5+3)*6
   # 6*(5+3)
   # cos(x+1) + 20
   # power(cos(x+1)*x, 4)
   # power(x,5)
   # ''')

    return(result)

# DEBUG

VerifToken(LexicalAnalysis('power(cos(x+1),4)'))
#VerifToken(LexicalAnalysis('power(x,4)'))
