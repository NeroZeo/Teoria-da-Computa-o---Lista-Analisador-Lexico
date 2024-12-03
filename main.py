import re

TOKEN_EX = [
    ('NUMERO', r'\d+'),
    ('MAIS', r'\+'),
    ('MENUS', r'-'),
    ('VEZES', r'\*'),
    ('DIVISAO', r'/'),
    ('PARENTESE_ESQUERDO', r'\('),
    ('PARENTESE_DIREITO', r'\)'),
    ('ESPAÇO', r'\s+'),
]

token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_EX)
token_re = re.compile(token_regex)

def lexer(code):
    tokens = []
    for match in token_re.finditer(code):
        kind = match.lastgroup
        value = match.group(kind)
        if kind == 'ESPAÇO':
            continue  
        elif kind == 'NUM':
            value = int(value)  
        tokens.append((kind, value))
    return tokens


code = "7 - 6 * (2 + 5) / 9"
tokens = lexer(code)
for token in tokens:
    print(token)
