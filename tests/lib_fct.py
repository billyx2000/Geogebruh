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
    power = 8 # Error because "power(x, 2)" parsed as "power(x2.0)"
    cbrt = 9
    arccos = 10
    arcsin = 11
    arctan = 12

def VerifToken(tokenArray):
    # DEBUG
    #print(tokenArray)

    tokenArray = tokenArray.asList()
    #tokenString = ''.join(str(v) for v in tokenArray).replace('[', '(').replace(']', ')') #List to string and replace '[' to '('
    tokenString = ''.join(str(v) for v in tokenArray).replace('[', '').replace(']', '') #List to string and replace '[' to '('

    # DEBUG
    #print(tokenString)
    
    tokenFct = re.findall(r'\b[a-zA-Z]{3,6}',tokenString) # Match all funtion string, with a length from 3 to 6
    
    for fct in tokenFct:
        if fct not in UsualFct._member_names_:
	    # DEBUG
            print("Mauvaise saisie: ")
            print(fct)
            return False
        else:
             tokenString = tokenString.replace(fct, "np."+fct)  #remplace fct par np.fct pour appel numpy
                
    tokenString = tokenString.replace(",", '')
    tokenString = tokenString.replace(" ", '')
    tokenString = tokenString.replace("'", '')

    return tokenString

def LexicalAnalysis(myExpr):
    expr = Forward()
    double = Word(nums + ".").setParseAction(lambda t:float(t[0]))
    integer = Word(nums).setParseAction(lambda t:int(t[0]))
    variable = Word(alphas)
    string = dblQuotedString
    funccall = Group(variable + "(" + Group(Optional(delimitedList(expr))) + ")")
    array_func = Group(funccall + "[" + Group(delimitedList(expr, "][")) + "]")
    array_var = Group(variable + "[" + Group(delimitedList(expr, "][")) + "]")

    operand = double | string | array_func | funccall | array_var | variable

    expop = Literal('^')
    signop = oneOf('+ -')
    multop = oneOf('* /')
    plusop = oneOf('+ -')

    expr << operatorPrecedence( operand,
    [("^", 2, opAssoc.RIGHT),
    (signop, 1, opAssoc.RIGHT),
    (multop, 2, opAssoc.LEFT),
    (plusop, 2, opAssoc.LEFT),]
    )

    result = expr.parseString(myExpr)
    return(result)

# DEBUG
#rep = LexicalAnalysis('2*sin(t)')
#VerifToken(rep)

