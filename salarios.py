import ply.lex as lex
import ply.yacc as yacc

# Tokens
tokens = ['ID', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'NUM']

# expresiones regulares
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_ID = r'[a-zA-Z_][a-zA-Z_0-9]*'
t_ignore = ' \t\n'

variables = {
    "BONO": 200,
    "DEDUCCION": 50
}

def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    print(f"Error léxico en: '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

# gramática para analizar las operaciones
def p_expression_op(p):
    '''expression : expression PLUS term
                  | expression MINUS term'''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_times_divide(p):
    '''term : term TIMES factor
            | term DIVIDE factor'''
    if p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        if p[3] == 0:
            print("Error: división por cero")
            p[0] = 0
        else:
            p[0] = p[1] / p[3]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_num(p):
    'factor : NUM'
    p[0] = p[1]

def p_factor_id(p):
    'factor : ID'
    var_name = p[1]
    if var_name in variables:
        p[0] = variables[var_name]
    else:
        print(f"Error: variable '{var_name}' no definida")
        p[0] = 0

def p_error(p):
    if p:
        print(f"Error sintáctico en '{p.value}'")
    else:
        print("Error sintáctico: entrada incompleta")

parser = yacc.yacc()

def calcular_sueldo(base, expresion):
    """Calcula el sueldo final dada una base y una expresión de bonificaciones y deducciones."""
    resultado = parser.parse(expresion)
    return base + resultado

# función
sueldo_base = 500
bono_deduccion = "BONO + DEDUCCION - 30 * 2"

sueldo_final = calcular_sueldo(sueldo_base, bono_deduccion)
print("Sueldo final:", sueldo_final)
