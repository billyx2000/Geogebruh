# FROM https://www.bornageek.com/general/development/2013/05/10/lexical-analysis-using-python.html
# Might need to edit to suit our need

#!/usr/bin/env python from pyparsing import Word, Regex, Literal, OneOrMore, ParseException
import sys
import re

def main(argv):
	form = argv[0]

	# Do something with this data. 	if form is not None:
		try:
			operator = Regex(r'(?<!--[\+\-\^\*/%])[\+\-]|[\^\*/%!]')<br /-->
			function = Regex(r'[a-zA-Z_][a-zA-Z0-9_]*(?=([ \t]+)?\()')
			variable = Regex(r'[+-]?[a-zA-Z_][a-zA-Z0-9_]*(?!([ \t]+)?\()')
			number = Regex(r'[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?')
			lbrace = Word('(')
			rbrace = Word(')')
			assign = Literal(':=')
			linebreak = Word('\n')
			skip = Word(' \t')

			lexOnly = operator | function | variable | number | lbrace \
				| rbrace | assign | linebreak | skip
			lexAllOnly = OneOrMore(lexOnly)

			print lexAllOnly.parseString(form)
		except ParseException, err:
			print err.line
			print " "*(err.column-1) + "^"
			print err
	else:
		print 'Invalid parameters.\n'
		sys.exit(1)

if __name__ == "__main__":
	main(sys.argv[1:])
