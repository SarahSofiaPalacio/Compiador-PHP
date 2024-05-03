import ply.yacc as yacc
# Importar el conjunto de palabras reservadas y simbolos reconocidos por el lexer
from Mini_lex_PHP import tokens, lexer
import sys
#import warnings
#warnings.filterwarnings("ignore")

VERBOSE = 1

#nivel de prioridad de los operadores 
precedence = (
    ('left', 'or', 'BOOL_OR'),
    ('left', 'and', 'BOOL_AND'),
    ('nonassoc', 'EQUAL', 'DEQUAL', 'ISEQUAL', 'DISTINT', 'LESS', 'LESSEQUAL', 'GREATER', 'GREATEREQUAL'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'UMINUS'),
    ('right', 'NOT'),  
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
                   | namespace_declaration
				   | var_declaration
				   | constant_declaration
				   | print_declaration
				   | echo_declaration
				   | iteration_stmt
				   | if_statement
				   | fun_declaration
				   | fun_call
				   | return_statement
				   | class_declaration
                   | class_extension
				   | create_obj_declaration
      			   | interface_declaration
                   | trait_declaration
                   | use_declaration
                   | continue_declaration
                   | label_declaration
                   | goto_declaration
                   | declare_statement
                   | match_declaration
				   | footer_declaration
				   | for_loop
				   | foreach_loop
				   | switch_statement
                   | try_statement
                   | throw_statement
				   | exit_statement
				   | empty'''
    pass

     

def p_header_declaration(p):
    '''header_declaration : include CADENA SEMICOLON
      					   | include_once CADENA SEMICOLON
						   | require CADENA SEMICOLON
                           | require_once CADENA SEMICOLON'''
    pass

def p_namespace_declaration(p):
    '''namespace_declaration : namespace ID SEMICOLON'''
    pass

def p_constant_declaration(p):
	'''constant_declaration : const ID EQUAL CADENA SEMICOLON
 							| const ID EQUAL NUMBER SEMICOLON'''
	pass

def p_print_declaration(p):
	'''print_declaration : print var_declaration2 SEMICOLON
						| print LPAREN var_declaration2 RPAREN SEMICOLON
						| print LPAREN NUMBER RPAREN SEMICOLON
						| print LPAREN CADENA RPAREN SEMICOLON
						| print NUMBER SEMICOLON
      					| print CADENA SEMICOLON'''
	pass

def p_echo_declaration(p):
	'''echo_declaration : echo var_declaration2 SEMICOLON
						| echo LPAREN var_declaration2 RPAREN SEMICOLON
						| echo LPAREN NUMBER RPAREN SEMICOLON
						| echo LPAREN CADENA RPAREN SEMICOLON
						| echo NUMBER SEMICOLON
                        | echo ceil_expression SEMICOLON
      					| echo CADENA SEMICOLON'''
	pass

def p_var_declaration_1(p):
	'''var_declaration : var_declaration2 SEMICOLON
      					| global var_declaration2 SEMICOLON
                        | visibility var_declaration2 SEMICOLON
                        | visibility readonly var_declaration2 SEMICOLON'''
	pass

def p_var_declaration_2(p):
	'''var_declaration : VARIABLE LBRACKET NUMBER RBRACKET SEMICOLON
      					| global VARIABLE LBRACKET NUMBER RBRACKET SEMICOLON'''
	pass

#Eliminacion de conflictos con reglas que incluyen COMMA, debido a ya estar en params
#Tambien eliminacion de algunas reglas que no existen en php como :VARIABLE EQUAL NUMBER COMMA var_declaration2
	#$a = 2, $b; por ejemplo da error sintactico en el ","

def p_var_declaration_3(p):                     
	'''var_declaration2 : VARIABLE
						| VARIABLE expression
                        | VARIABLE EQUAL NUMBER
                        | VARIABLE EQUAL VARIABLE
                        | VARIABLE EQUAL CADENA
						| VARIABLE EQUAL Built_In_Declaration
						| VARIABLE EQUAL expression
						| VARIABLE assignation VARIABLE 
						| VARIABLE assignation NUMBER
                        | VARIABLE EQUAL ceil_expression 
                        | VARIABLE EQUAL clone_declaration
						| Built_In_Declaration
						| Concatenar_Cadenas_declaration
						| VARIABLE EQUAL ID LPAREN params RPAREN
						| VARIABLE QUESTIONMARK var_declaration2 COLON var_declaration2
						| VARIABLE OBJ_OPERATOR ID EQUAL expression
						| VARIABLE OBJ_OPERATOR ID LPAREN params RPAREN
						| VARIABLE EQUAL create_obj_declaration
        '''
	pass
 
#modificado para evitar conflicto reduce/reduce
#Añadido conexion con assignment_tail 
def p_var_declaration_2(p):
    '''var_declaration2 : VARIABLE EQUAL assignment_tail'''


#Eliminacion de conflictos con reglas que incluyen COMMA, debido a ya estar en params

def p_assignment_tail(p):
    '''assignment_tail : COMMA var_declaration2
					   | LBRACKET params RBRACKET
					   | LBLOCK params RBLOCK
					   | VARIABLE LBRACKET expression COMMA params
					   | VARIABLE LBRACKET params RBRACKET
					   | VARIABLE LBLOCK params RBLOCK
					   '''
    pass


#...............................................

def p_iteration_stmt_1(p):
	'''iteration_stmt : while LPAREN expression RPAREN LBLOCK declaration_list RBLOCK
 						| while LPAREN expression RPAREN COLON declaration_list endwhile SEMICOLON'''
	pass

def p_iteration_stmt_2(p):
	'''iteration_stmt : do LBLOCK declaration_list RBLOCK while LPAREN expression RPAREN SEMICOLON
						| do COLON declaration_list endwhile SEMICOLON'''
	pass

def p_expression_1(p):
	'''expression : additive_expression
				
 					| additive_expression logical_op additive_expression
					| additive_expression comp_op additive_expression
     				| additive_expression comp_op additive_expression logical_op additive_expression comp_op additive_expression
					| additive_expression bits_op additive_expression
                    | VARIABLE instanceof ID
					
'''
	pass

# modificado para evitar conflicto reduce/reduce
def p_additive_expression(p):
    '''additive_expression : term
                           | term math_op term'''
    pass

def p_expression_uminus(p):  	#UMINUS sirve cuando se tienen operaciones como 2 * -2;
    '''term : MINUS term %prec UMINUS'''#????


def p_term(p):
    '''term : factor
            | factor increment_decrement_op
            | increment_decrement_op factor'''

def p_factor(p):
    '''factor : NUMBER
              | VARIABLE
              | bool_type
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
				| MULEQUAL
				| PLUSEQUAL
				| MINUSEQUAL
				| MOD
	'''
	pass

def p_comp_op(p):
	'''comp_op : LESS 
			| LESSEQUAL
			| GREATER
			| GREATEREQUAL
			| DEQUAL
			| DISTINT
			| DIVEQUAL
			| ISEQUAL
			| ISIDENTICAL
			| ISNOTIDENTICAL
	'''
	pass

def p_logical_op(p):
    '''logical_op : BOOL_OR
                    | BOOL_AND
                    | NOT
                    | or
                    | and 
                    | xor'''
    pass

def p_if_statement(p):
    '''if_statement : if LPAREN expression RPAREN LBLOCK declaration_list RBLOCK else_part'''

def p_else_part(p):
    '''else_part : elseif LPAREN expression RPAREN LBLOCK declaration_list RBLOCK else_part
                 | else LBLOCK declaration_list RBLOCK
                 | endif
                 | empty_function'''
                 
def p_fun_declaration(p):
	'''fun_declaration : function ID LPAREN params RPAREN LBLOCK declaration_list RBLOCK
       					| function ID LPAREN params RPAREN LBLOCK declaration_list return_statement RBLOCK
                        | visibility function ID LPAREN params RPAREN LBLOCK declaration_list RBLOCK
                        | visibility function ID LPAREN params RPAREN LBLOCK declaration_list return_statement RBLOCK
                        | visibility static function ID LPAREN params RPAREN LBLOCK declaration_list RBLOCK 
                        | visibility static function ID LPAREN params RPAREN LBLOCK declaration_list return_statement RBLOCK'''
	pass

def p_fun_call(p):
	'''fun_call : ID LPAREN params RPAREN'''
	pass

def p_return_statement(p):
    '''return_statement : return expression SEMICOLON
					   | return params SEMICOLON
                       | return SEMICOLON
                       | return ID LPAREN expression RPAREN SEMICOLON'''
    pass


def p_class_declaration(p):
    '''class_declaration : class ID LBLOCK class_body RBLOCK
    					| final class ID LBLOCK class_body RBLOCK
                        | class ID implements ID LBLOCK class_body RBLOCK
    					| final class ID implements ID LBLOCK class_body RBLOCK'''
    pass

def p_class_extension(p):
    '''class_extension : class ID extends ID LBLOCK RBLOCK 
						| class ID extends Exception LBLOCK RBLOCK
						| class ID extends ErrorException LBLOCK RBLOCK
						| class ID extends Error LBLOCK RBLOCK
						| class ID extends ParseError LBLOCK RBLOCK
						| class ID extends TypeError LBLOCK RBLOCK'''
    pass 

def p_create_obj_declaration(p):
	'create_obj_declaration : new ID LPAREN params RPAREN'
	pass

def p_class_body(p):
    '''class_body : class_body_element
                  | class_body class_body_element
                  | empty_function'''
    pass

def p_class_body_element(p):
    '''class_body_element : visibility var_declaration2 SEMICOLON
                          | visibility fun_declaration
                          | declaration'''
    pass

def p_interface_declaration(p):
    '''interface_declaration : interface ID LBLOCK interface_body RBLOCK'''
    pass

def p_interface_body(p):
    '''interface_body : interface_method_declaration
                      | interface_body interface_method_declaration
                      | empty_function'''
    pass

def p_interface_method_declaration(p):
    '''interface_method_declaration : visibility function ID LPAREN params RPAREN SEMICOLON'''
    pass

def p_trait_declaration(p):
    '''trait_declaration : trait ID LBLOCK trait_body RBLOCK'''
    pass

def p_trait_body(p):
    '''trait_body : trait_element
                  | trait_body trait_element
                  | empty_function'''
    pass

def p_trait_element(p):
    '''trait_element : visibility var_declaration SEMICOLON
                     | visibility fun_declaration'''
    pass

def p_use_declaration(p):
    '''use_declaration : use ID SEMICOLON
      					| use id_list LBLOCK use_body RBLOCK'''
    pass

def p_use_body(p):
    '''use_body : use_body use_statement
      			| use_statement
                | empty_function'''
    pass

def p_use_statement(p):
    '''use_statement : ID COLON COLON ID insteadof ID SEMICOLON'''
    pass

def p_id_list(p):
    '''id_list : id_list COMMA id_declaration
      					| id_declaration'''
    pass

def p_id_declaration(p):
    '''id_declaration : ID'''
    pass

def p_match_declaration(p):
    '''match_declaration : VARIABLE EQUAL match LPAREN single_param RPAREN LBLOCK match_body RBLOCK SEMICOLON'''
    pass

def p_match_body(p):
    '''match_body : match_body match_statement COMMA
      			| match_statement COMMA 
                | empty_function'''
    pass

def p_match_statement(p):
    '''match_statement : single_param ASSIGN single_param
    					| expression ASSIGN single_param'''
    pass

def p_visibility(p):
    '''visibility : private
                  | protected
                  | public
                  | var'''
    pass

def p_continue_declaration(p):
    '''continue_declaration : continue SEMICOLON'''
    pass

def p_label_declaration(p):
    '''label_declaration : ID COLON'''
    pass

def p_goto_declaration(p):
    '''goto_declaration : goto ID SEMICOLON'''
    pass

def p_callable_declaration(p):
    '''callable_declaration : callable VARIABLE'''
    pass

#modificado para evitar conflicto reduce/reduce 
def p_params(p):
    '''params : single_param
              | params COMMA single_param'''

def p_single_param(p):
    '''single_param : var_declaration2
					| NUMBER
					| CADENA
                    | bool_type
                    | callable_declaration
                    | empty_function
					'''
    pass

def p_bool_type(p):
    '''bool_type : true
				| false'''
    pass
#...............................................
def p_for_loop(p):
    '''for_loop : for LPAREN for_init for_expr for_update RPAREN LBLOCK declaration_list RBLOCK
    			| for LPAREN for_init for_expr for_update RPAREN COLON declaration_list endfor SEMICOLON'''
    pass

def p_for_init(p):
    'for_init : var_declaration2 SEMICOLON'
    pass

def p_for_expr(p):
    'for_expr : expression SEMICOLON'
    pass

def p_for_update(p):
    'for_update : expression'
    pass

def p_exit_statement(p):
    'exit_statement : exit LPAREN expression RPAREN SEMICOLON'
    pass

def p_foreach_loop(p):
    '''foreach_loop : foreach LPAREN expression as expression RPAREN LBLOCK declaration_list RBLOCK
    				| foreach LPAREN expression as expression RPAREN COLON declaration_list endforeach SEMICOLON'''
    pass

def p_switch_statement(p):
    '''switch_statement : switch LPAREN expression RPAREN LBLOCK case_blocks default_block RBLOCK
    					| switch LPAREN expression RPAREN COLON case_blocks default_block endswitch SEMICOLON'''
    pass

def p_case_blocks(p):
    '''case_blocks : case_blocks case_block
                   | case_block
                   | empty_function'''
    pass

def p_case_block(p):
    '''case_block : case expression COLON statement_list
                  | case expression COLON statement_list break SEMICOLON'''
    pass

def p_default_block(p):
    '''default_block : default COLON statement_list
					 | default COLON statement_list break SEMICOLON
                     | empty_function'''
    pass


def p_try_statement(p):
    'try_statement : try LBLOCK statement_list RBLOCK catch_blocks'
    pass

def p_catch_blocks(p):
    '''catch_blocks : catch_blocks catch_block
                   | catch_block
                   | catch_blocks finally_block
                   | finally_block'''
    pass

def p_catch_block(p):
    '''catch_block : catch LPAREN list_exception RPAREN LBLOCK statement_list RBLOCK'''
    pass

def p_list_exception(p):
	'''list_exception : list_exception PIPE exception_statement
						| exception_statement'''
	pass

def p_exception_statement(p):
	'''exception_statement : Exception VARIABLE
                       | ID VARIABLE'''
	pass

def p_throw_statement(p):
      '''throw_statement : throw create_obj_declaration SEMICOLON
        				| throw new Exception LPAREN params RPAREN SEMICOLON'''
      pass

def p_finally_block(p):
    '''finally_block : finally LBLOCK statement_list RBLOCK'''
    pass


def p_statement_list(p):
    '''statement_list : declaration
                      | statement_list declaration
                      | empty_function'''
    pass

def p_Built_In_Declaration(p):
    '''Built_In_Declaration : array LPAREN params RPAREN
							| pow LPAREN params RPAREN
							| POW LPAREN params RPAREN
							| abs LPAREN params RPAREN
							| cos LPAREN params RPAREN
							| deg2rad LPAREN params RPAREN
							| rad2deg LPAREN params RPAREN
							| die LPAREN params RPAREN
							| exp LPAREN params RPAREN
							| floor LPAREN params RPAREN
							| isset LPAREN params RPAREN
							| list LPAREN params RPAREN
							| log LPAREN params RPAREN
							| log10 LPAREN params RPAREN
							| max LPAREN params RPAREN
							| min LPAREN params RPAREN
							| rand LPAREN params RPAREN
							| round LPAREN params RPAREN
							| sin LPAREN params RPAREN
							| sqrt LPAREN params RPAREN
							| unset LPAREN params RPAREN
                            | eval LPAREN params RPAREN
							'''
    pass

def p_Concatenar_Cadenas_declaration(p):
	'''Concatenar_Cadenas_declaration : VARIABLE DOT VARIABLE
										| CADENA DOT CADENA
										| CADENA DOT VARIABLE
										| VARIABLE DOT CADENA'''
	pass

#.................................................................................................

def p_bits_op(p):
	'''bits_op : AMPERSANT
				| SR
                | SL
                
				'''
pass
def p_assignation(p):
	'''assignation : ASSIGN
 					| SREQUAL
                	| SLEQUAL
            		| XOREQUAL	
                	| ANDEQUAL
      				'''
pass

def p_ceil_expression(p):
    '''ceil_expression : ceil LPAREN expression RPAREN'''
    pass


def p_clone_declaration(p):
     '''clone_declaration : clone expression'''
     pass
    

	 
def p_declare_statement(p):
    '''declare_statement : declare LPAREN ID EQUAL expression RPAREN SEMICOLON'''
    pass


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
