#gramática simple como S -> 'a' S 'b' | 'a' 'b'.
# analizador_descendente.py

def parse_s(input_string):
    if input_string == "":
        return False
    elif input_string[0] == 'a' and input_string[-1] == 'b':
        if len(input_string) == 2:
            return True
        else:
            return parse_s(input_string[1:-1])
    else:
        return False
