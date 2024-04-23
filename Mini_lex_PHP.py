import ply.lex as lex
import sys

# lista de tokens
reserved = {
    # Reserverd words
    'ABSTRACT': 'abstract',
    'AND': 'and',
    'ARRAY': 'array',
    'AS': 'as',
    'BREAK': 'break',
    'CALLABLE': 'callable',
    'CASE': 'case',
    'CATCH': 'catch',
    'CLASS': 'class',
    'CLONE': 'clone',
	'OBJECTOPERATOR' : 'objectoperator',
    'READONLY': 'readonly',
    'CONST': 'const',
    'CONTINUE': 'continue',
    'DECLARE': 'declare',
    'DEFAULT': 'default',
    'DIE': 'die',
    'DO': 'do',
    'ECHO': 'echo',
    'ELSE': 'else',
    'ELSEIF': 'elseif',
    'EMPTY': 'empty',
    'ENDCLARE': 'endclare',
    'ENDFOR': 'endfor',
    'ENDFOREACH': 'endforeach',
    'ENDIF': 'endif',
    'ENDSWITCH': 'endswitch',
    'ENDWHILE': 'endwhile',
    'EVAL': 'eval',
    'EXIT': 'exit',
    'EXTENDS': 'extends',
    'FINAL': 'final',
    'FINALLY': 'finally',
    'FOR': 'for',
    'FOREACH': 'foreach',
    'FUNCTION': 'function',
    'GLOBAL': 'global',
    'GOTO': 'goto',
    'IF': 'if',
    'IMPLEMENTS': 'implements',
    'INCLUDE': 'include',
    'INCLUDE_ONCE': 'include_once',
    'INSTANCEOF': 'instanceof',
    'INSTEADOF': 'insteadof',
    'INTERFACE': 'interface',
    'ISSET': 'isset',
    'LIST': 'list',
    'MATCH': 'match',
    'NAMESPACE': 'namespace',
    'NEW': 'new',
    'OR': 'or',
	"ABS": "abs",
    "CEIL": "ceil",
    "FLOOR": "floor",
    "ROUND": "round",
    "RAND": "rand",
    "MAX": "max",
    "MIN": "min",
    "SIN": "sin",
    "COS": "cos",
    "SQRT": "sqrt",
	"POW": "pow",
    "EXP": "exp",
    "LOG": "log",
    "LOG10": "log10",
    "DEG2RAD": "deg2rad",
    "RAD2DEG": "rad2deg",
    'PRINT': 'print',
    'PRIVATE': 'private',
    'PROTECTED': 'protected',
    'PUBLIC': 'public',
    'REQUIRE': 'require',
    'REQUIRE_ONCE': 'require_once',
    'RETURN': 'return',
    'STATIC': 'static',
    'SWITCH': 'switch',
    'THROW': 'throw',
    'TRAIT': 'trait',
    'TRY': 'try',
    'UNSET': 'unset',
    'USE': 'use',
    'VAR': 'var',
    'WHILE': 'while',
    'XOR': 'xor',
    'PHP': 'php'
}

tokens = [
    #SYMBOLS
	'OPEN_TAG',
    'CLOSE_TAG',
    'ASSIGN',
	'MULEQUAL',
    'MOD',
    'PLUS',
	'BACKSLASH',
    'PLUSPLUS',
    'PLUSEQUAL',
    'MINUS',
    'MINUSMINUS',
    'MINUSEQUAL',
	'COMMENT',
	'COMMENT_MULTI',
    'TIMES',
    'DIVIDE',
	'DIVEQUAL',
    'XOREQUAL',
    'POW',
    'LESS',
    'LESSEQUAL',
    'GREATER',
    'GREATEREQUAL',
    'EQUAL',
    'DEQUAL',
    'DISTINT',
    'ISEQUAL',
	'ISIDENTICAL',
    'ISNOTIDENTICAL',
    'BOOL_OR',
    'BOOL_AND',
    'ANDEQUAL',
    'SEMICOLON',
	'SL',
    'SLEQUAL',
    'SR',
    'SREQUAL',
    'NOT',
    'COMMA',
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'RBRACKET',
    'LBLOCK',
    'RBLOCK',
    'COLON',
    'AMPERSANT',
    'HASHTAG',
    'DOT',
    'QUESTIONMARK',
    'COMILLASIMPLE',
    'COMILLASDOBLES',
    'COMMENT_HASHTAG',
	'INVALID_NUMBER_SEQUENCE',
	'INVALID_VARIABLE',
    'VARIABLE',  
    'NUMBER',
    'CADENA',
    'ID'
	
]

TokensAll = tokens + list(reserved.values())
tokens = tokens + list(reserved.values())
print(TokensAll)

t_MOD = r'%'
t_PLUS   = r'\+'
t_MINUS  = r'-'
t_TIMES  = r'\*'
t_DIVIDE = r'/'
t_EQUAL  = r'='
t_DISTINT = r'!'
t_LESS   = r'<'
t_GREATER = r'>'
t_SEMICOLON = ';'
t_COMMA  = r','
t_LPAREN = r'\('
t_RPAREN  = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBLOCK   = r'{'
t_RBLOCK   = r'}'
t_COLON   = r':'
t_AMPERSANT = r'\&'
t_HASHTAG = r'\#'
t_DOT = r'\.'
t_COMILLASIMPLE = r'\''
t_COMILLASDOBLES = r'\"'
t_QUESTIONMARK = r'\?'
t_NOT = r'~'

def t_OPEN_TAG(t): 
    r'<\?php'
    return t

def t_CLOSE_TAG(t): 
    r'\?>'
    return t

def t_INVALID_NUMBER_SEQUENCE(t):
    r'\d+[a-zA-Z_]+'
    print(f"Error léxico: secuencia numérica inválida '{t.value}' {t.lineno} {t.lexpos}")
    t.lexer.skip(1)  
	
def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t

def t_INVALID_VARIABLE(t):
    r'\$\d+'
    print(f"Error léxico: Variable inválida '{t.value}' {t.lineno} {t.lexpos}")
    t.lexer.skip(len(t.value)) 
	
def t_VARIABLE(t):
    r'\$[a-zA-Z_](\w)*'
    return t

def t_COMMENT(t):
    r'\/\/.*'
    return t

def t_COMMENT_HASHTAG(t):
    r'\#.*'
    return t

# Expresión regular para comentarios de varias líneas
def t_COMMENT_MULTI(t):
    r'\/\*(.|\n)*?\*\/'
    t.lexer.lineno += t.value.count('\n')  # Actualizar el contador de líneas
    return t

def t_ID(t):
    r'[a-zA-Z_](\w)*' #[a-zA-Z_0-9]
    t.type = reserved.get(t.value.upper(), 'ID')  # Verifica si la palabra está en el diccionario 'reserved'
    return t

# Definir la regla para la cadena (cadena entre comillas dobles o simples)
def t_CADENA(t):
    r'(\"[^\"]*\"|\'[^\']*\')'
    return t

def t_LESSEQUAL(t):
	r'<='
	return t

def t_GREATEREQUAL(t):
	r'>='
	return t

def t_ASSIGN(t):
    r'=>'
    return t

def t_DEQUAL(t):
	r'!='
	return t

def t_ISEQUAL(t):
	r'=='
	return t
    
def t_MINUSMINUS(t):
	r'--'
	return t

def t_ANDEQUAL(t): 
    r'\&=' 
    return t

def t_ISIDENTICAL(t):
	r'==='
	return t

def t_ISNOTIDENTICAL(t):
	r'!=='
	return t

def t_BOOL_AND(t): 
    r'\&\&' 
    return t

def t_BOOL_OR(t): 
    r'\|\|' 
    return t

def t_PLUSEQUAL(t):
	r'\+='
	return t

def t_MINUSEQUAL(t):
	r'-='
	return t

def t_MULEQUAL(t):
	r'\*='
	return t

def t_DIVEQUAL(t):
	r'/='
	return t

def t_POW(t):
	r'\*\*'
	return t

def t_BACKSLASH(t):
    r'\\'
    return t

def t_XOREQUAL(t): 
    r'\^=' 
    return t

def t_SL(t):
	r'<<'
	return t

def t_SLEQUAL(t):
	r'<<='
	return t

def t_SR(t):
	r'>>='
	return t

def t_SREQUAL(t):
	r'>>='
	return t

def t_PLUSPLUS(t):
	r'\+\+'
	return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
 

def t_space(t):
    r'\s+'
    t.lexer.lineno += len(t.value)
    
t_ignore = ' \t'
"""
def t_comments(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')
	


def t_comments_C99(t):
    r'//(.)*?\n'
    t.lexer.lineno += 1 """

def t_error(t):
    print ("Lexical error: " + str(t.value[0]))
    t.lexer.skip(1)
    
def test(data, lexer):
	lexer.input(data)
	while True:
		tok = lexer.token()
		if not tok:
			break
		print (tok)

lexer = lex.lex()
 
if __name__ == '__main__':
	if (len(sys.argv) > 1):
		fin = sys.argv[1]
	else:
		fin = 'Test.php'
	f = open(fin, 'r')
	data = f.read()
	print (data)
	lexer.input(data)
	test(data, lexer)
	#input()