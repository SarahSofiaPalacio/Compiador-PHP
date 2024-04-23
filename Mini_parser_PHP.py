import ply.yacc as yacc
from Mini_lex_PHP import TokensAll 
import Mini_lex_PHP
import sys

tokens = TokensAll

VERBOSE = 1

def p_program(p):
	'program : header declaration_list'
	pass

def p_header(p):
    'header : OPEN_TAG'
    pass

def p_footer_declaration(p):
    'footer_declaration : CLOSE_TAG'
    pass

def p_declaration_list(p):
	'''declaration_list : declaration 
						| declaration_list declaration'''
	pass

def p_declaration(p):
    '''declaration : COMMENT
                   | COMMENT_HASHTAG
                   | COMMENT_MULTI
                   | header_declaration
				   | var_declaration
				   | constant_declaration
				   | print_declaration
				   | echo_declaration
				   | iteration_stmt
				   | fun_declaration
				   | fun_call
				   | obj_declaration
				   | create_obj_declaration
				   | footer_declaration
                   | empty'''
    pass

def p_data_type(p):
	'''data_type	: NUMBER
					| CADENA'''

def p_header_declaration(p):
    '''header_declaration : include CADENA SEMICOLON'''
    pass

def p_constant_declaration(p):
	'''constant_declaration : const ID EQUAL data_type SEMICOLON'''
	pass

def p_print_declaration(p):
	'''print_declaration : print var_declaration2 SEMICOLON
						| print LPAREN var_declaration2 RPAREN SEMICOLON
						| print LPAREN data_type RPAREN SEMICOLON
						| print data_type SEMICOLON'''
	pass

def p_echo_declaration(p):
	'''echo_declaration : echo var_declaration2 SEMICOLON
						| echo LPAREN var_declaration2 RPAREN SEMICOLON
						| echo LPAREN data_type RPAREN SEMICOLON
						| echo data_type SEMICOLON'''
	pass


def p_var_declaration_1(p):
	'''var_declaration : var_declaration2 SEMICOLON'''
	pass


'''?????????????????????????????????????????????????????????????????????????????????????????'''
def p_var_declaration_2(p):
	'var_declaration : VARIABLE LBRACKET NUMBER RBRACKET SEMICOLON'
	pass

def p_var_declaration_3(p):                     
	'''var_declaration2 :  VARIABLE
                        | VARIABLE COMMA var_declaration2
                        | VARIABLE EQUAL NUMBER COMMA var_declaration2
                        | VARIABLE EQUAL NUMBER
                        | VARIABLE EQUAL VARIABLE COMMA var_declaration2
                        | VARIABLE EQUAL VARIABLE
						| VARIABLE EQUAL expression
                        | COMMA 
                        | data_type COMMA var_declaration2
                        | NUMBER RBRACKET
                        | VARIABLE EQUAL LBRACKET data_type COMMA var_declaration2
                        | CADENA COMMA var_declaration2
                        | CADENA RBRACKET

        '''
	pass

def p_iteration_stmt_1(p):
	'iteration_stmt : while LPAREN expression RPAREN LBLOCK declaration RBLOCK'
	pass

def p_expression_1(p):
	'''expression : additive_expression
					| additive_expression comp_op additive_expression'''
	pass

def p_additive_expression(p):
	'''additive_expression : additive_expression math_op additive_expression
							| NUMBER
							| NUMBER MINUSMINUS
							| NUMBER PLUSPLUS
							| VARIABLE
        '''
	pass

def p_math_op(p):
	'''math_op : PLUS 
				| MINUS
				| TIMES
				| DIVIDE
	'''
	pass

def p_comp_op(p):
	'''comp_op : LESS 
			| LESSEQUAL
			| GREATER
			| GREATEREQUAL
			| DEQUAL
			| DISTINT
			| ISEQUAL
	'''
	pass

def p_fun_declaration(p):
	'fun_declaration : function ID LPAREN params RPAREN LBLOCK declaration RBLOCK'
	pass

def p_fun_call(p):
	'''fun_call : ID LPAREN params RPAREN'''
	pass

def p_obj_declaration(p):
	'obj_declaration : class ID LBLOCK declaration RBLOCK'
	pass

def p_create_obj_declaration(p):
	'create_obj_declaration : new ID LPAREN params RPAREN'
	pass

def p_params(p):
	'''params : param_list
			| var_declaration2
			| empty_function'''
	pass

def p_param_list_1(p):
	'''param_list : param_list COMMA params
				| params'''
	pass

def p_empty_function(p):
	'empty_function :'
	pass


def p_error(p):

	tok = parser.token() 
	print(tok)
	if VERBOSE:
		if p is not None:
			print ("ERROR SINTACTICO EN LA LINEA " + str(p.lexer.lineno) + " NO SE ESPERABA EL Token " + str(p.value))
		else:
			print ("ERROR SINTACTICO EN LA LINEA: " + str(Mini_lex_PHP.lexer.lineno))
		return
	else:
		raise Exception('syntax', 'error')
		
		

parser = yacc.yacc()

if __name__ == '__main__':

	if (len(sys.argv) > 1):
		fin = sys.argv[1]
	else:
		fin = 'Test.php'

	f = open(fin, 'r')
	data = f.read()
	#print(tokens)
	parser.parse(data, tracking=True)
	print("Amiguito, tengo el placer de informar que Tu parser reconocio correctamente todo")
	#input()