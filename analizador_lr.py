# analizador_lr.py

import ply.yacc as yacc
from analizadores.analizador_lexico import tokens

# Reglas de gramática para LALR
def p_expression_op(p):
    '''expression : expression PLUS term
                  | expression TIMES term'''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_factor(p):
    'term : NUM'
    p[0] = int(p[1])

def p_error(p):
    print("Error sintáctico")

parser = yacc.yacc()

def analizar(texto):
    return parser.parse(texto)

#ejemplo de uso para que corra
from analizadores.analizador_lr import analizar

texto = "4 + 3 * 2"
resultado = analizar(texto)
print("Resultado:", resultado)
