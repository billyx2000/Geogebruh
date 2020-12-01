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

# Function : EVALUATEUR
def VerifToken(tokenArray):

    # DEBUG
    #print(tokenArray)

    tokenArray = tokenArray.asList()
    #tokenString = ''.join(str(v) for v in tokenArray).replace('[', '(').replace(']', ')') #List to string and replace '[' to '('
    tokenString = ''.join(str(v) for v in tokenArray).replace('[', '').replace(']', '') #List to string and replace '[' to '('

    # DEBUG
    #print(tokenString)
    
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

    # Clean up the token string
    tokenString = tokenString.replace(",", '')
    tokenString = tokenString.replace(" ", '')
    tokenString = tokenString.replace("'", '')
    tokenString = re.sub(r'(.*\(x)(\d\))', r'\1,\2', tokenString)

    return tokenString

# Function : ANALYSEUR LEXICAL
def LexicalAnalysis(myExpr):
    expr = Forward()
    double = Word(nums + ".").setParseAction(lambda t:float(t[0]))
    integer = Word(nums).setParseAction(lambda t:int(t[0]))
    variable = Word(alphas)
    string = dblQuotedString
    funccall = Group(variable + "(" + Group(Optional(delimitedList(expr))) + ")")
    array_func = Group(funccall + "[" + Group(delimitedList(expr, "][")) + "]")
    array_var = Group(variable + "[" + Group(delimitedList(expr, "][")) + "]")

    operand = integer | string | array_func | funccall | array_var | variable

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
#print(VerifToken(LexicalAnalysis('2*sin(t)')))
#print(VerifToken(LexicalAnalysis('power(x,5)')))

