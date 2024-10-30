# analizador_ascendente.py

import ply.yacc as yacc
from analizadores.analizador_lexico import tokens

# Reglas de gramática para shift-reduce
def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_times(p):
    'term : term TIMES factor'
    p[0] = p[1] * p[3]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_num(p):
    'factor : NUM'
    p[0] = int(p[1])

def p_error(p):
    print("Error sintáctico")

parser = yacc.yacc()

def analizar(texto):
    return parser.parse(texto)
