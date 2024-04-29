import ply.yacc as yacc
# Importar el conjunto de palabras reservadas y simbolos reconocidos por el lexer
from Mini_lex_PHP import tokens, lexer
import sys

VERBOSE = 1

#nivel de prioridad de los operadores aritmeticos
precedence = (
    ('left', 'BOOL_OR', 'or'),
    ('left', 'BOOL_AND', 'and'),
    ('left', 'EQUAL'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)

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
				   | if_statement
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

def p_var_declaration_2(p):
	'var_declaration : VARIABLE LBRACKET NUMBER RBRACKET SEMICOLON'
	pass
#original pero genera conflicto reduce/reduce con Number y Variable con la gramatica additive_expression
""" def p_var_declaration_3(p):                     
	'''var_declaration2 : VARIABLE
                        | VARIABLE COMMA var_declaration2
                        | VARIABLE EQUAL NUMBER COMMA var_declaration2
                        | VARIABLE EQUAL NUMBER
                        | VARIABLE EQUAL VARIABLE COMMA var_declaration2
                        | VARIABLE EQUAL VARIABLE
                        | VARIABLE EQUAL CADENA
						| VARIABLE EQUAL expression
                        | COMMA 
                        | data_type COMMA var_declaration2
                        | NUMBER RBRACKET
                        | VARIABLE EQUAL LBRACKET data_type COMMA var_declaration2
                        | CADENA COMMA var_declaration2
                        | CADENA RBRACKET

        '''
	pass """
 
#modificado para evitar conflicto reduce/reduce 
def p_var_declaration_2(p):
    '''var_declaration2 : VARIABLE assignment_tail'''

def p_assignment_tail(p):
    '''assignment_tail : EQUAL expression
                       | EQUAL NUMBER COMMA var_declaration2
                       | EQUAL VARIABLE COMMA var_declaration2
                       | EQUAL CADENA
                       | COMMA var_declaration2
                       | EQUAL LBRACKET expression COMMA var_declaration2
                       | EQUAL LBRACKET data_type COMMA var_declaration2
                       | RBRACKET'''
    pass
#...............................................

def p_iteration_stmt_1(p):
	'iteration_stmt : while LPAREN expression RPAREN LBLOCK declaration RBLOCK'
	pass


def p_expression_1(p):
	'''expression : additive_expression
 					| additive_expression logical_op additive_expression
					| additive_expression comp_op additive_expression
     				| additive_expression comp_op additive_expression logical_op additive_expression comp_op additive_expression'''
	pass
# Conflicto reduce/reduce con la gramatica original
""" def p_additive_expression(p):
	'''additive_expression : additive_expression math_op additive_expression
							| NUMBER
							| NUMBER MINUSMINUS
							| NUMBER PLUSPLUS
							| VARIABLE
        '''
	pass """
# modificado para evitar conflicto reduce/reduce
def p_additive_expression(p):
    '''additive_expression : term
                           | term math_op term'''
    pass

def p_term(p):
    '''term : factor
            | factor increment_decrement_op
            | increment_decrement_op factor'''

def p_factor(p):
    '''factor : NUMBER
              | VARIABLE
              | LPAREN expression RPAREN'''
    pass

def p_increment_decrement_op(p):
    '''increment_decrement_op : PLUSPLUS
                              | MINUSMINUS'''
    pass
#...............................................
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

def p_logical_op(p):
    '''logical_op : BOOL_OR
                    | BOOL_AND
                    | NOT
                    | or
                    | and '''
    pass

def p_if_statement(p):
    '''if_statement : if LPAREN expression RPAREN LBLOCK declaration_list RBLOCK else_part'''

def p_else_part(p):
    '''else_part : elseif LPAREN expression RPAREN LBLOCK declaration_list RBLOCK else_part
                 | else LBLOCK declaration_list RBLOCK
                 | endif
                 | empty'''
                 
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

""" def p_params(p):
	'''params : param_list
			| var_declaration2
			| empty_function'''
	pass

def p_param_list_1(p):
	'''param_list : param_list COMMA params
				| params'''
	pass """
#modificado para evitar conflicto reduce/reduce 
def p_params(p):
    '''params : single_param
              | params COMMA single_param'''

def p_single_param(p):
    '''single_param : var_declaration2
                    | empty_function'''
    pass
#...............................................
def p_empty_function(p):
	'empty_function :'
	pass

def p_error(p):
	# Manejo de errores sintacticos (la libreria invoca este metodo de forma automatica)
	# 'p' contiene el token que causo el error
	if VERBOSE:
		if p is not None:
			print ("ERROR SINTACTICO EN LA LINEA " + str(p.lexer.lineno) + " NO SE ESPERABA EL Token " + str(p.value) + ": " + str(p))
		else:
			print ("ERROR SINTACTICO EN LA LINEA: " + str(lexer.lineno))
		return
	else:
		raise Exception('syntax', 'error')
		
# Contruir el parser (con ayuda de la libreria ply)		
parser = yacc.yacc()

if __name__ == '__main__':
	if (len(sys.argv) > 1):
		# Si recibe un parametro, se toma como el nombre del archivo a leer
		php_code = sys.argv[1]
	else:
		# Si no recibe un parametro, se toma el archivo Test.php como el nombre del archivo a leer
		php_code = 'Test3.php'
	try:
		# Leer el archivo
		file = open(php_code, 'r')
	except:
		# Si el archivo no se encuentra en el directorio, terminar el programa
		print("El archivo no se encuentra en el directorio")
		sys.exit()
	# Guardar el contenido del archivo en la variable data
	data = file.read()
	# Enviar el código fuente al parser para que lo analice
	parser.parse(data, tracking=True)
	print("Amiguito, tengo el placer de informar que Tu parser reconocio correctamente todo")
 
	#input() <--- Evaluar eliminación (funcion definida en otra libreria)