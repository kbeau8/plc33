import re

# Define regular expressions for each token type
TOKEN_REGEXES = [
    (r'\+', 'ADD_OP'),
    (r'-', 'SUB_OP'),
    (r'\*', 'MUL_OP'),
    (r'/', 'DIV_OP'),
    (r'%', 'MOD_OP'),
    (r'\(', 'LEFT_PAREN'),
    (r'\)', 'RIGHT_PAREN'),
    (r'=', 'ASSIGN_OP'),
    (r'==', 'EQUALS_OP'),
    (r'<', 'LESS_THAN_OP'),
    (r'<=', 'LESS_THAN_OR_EQUAL_TO_OP'),
    (r'>', 'GREATER_THAN_OP'),
    (r'>=', 'GREATER_THAN_OR_EQUAL_TO_OP'),
    (r'&&', 'LOGICAL_AND_OP'),
    (r'\|\|', 'LOGICAL_OR_OP'),
    (r'[a-zA-Z_][a-zA-Z0-9_]*', 'IDENTIFIER'),
    (r'\d+\.\d+', 'FLOAT_LITERAL'),
    (r'\d+', 'INT_LITERAL'),
]

class Token:
    def __init__(self, token_type, value=None):
        self.type = token_type
        self.value = value

    def __repr__(self):
        return f'Token({self.type}, {self.value})'

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0

    def skip_whitespace(self):
        while self.pos < len(self.text) and self.text[self.pos].isspace():
            self.pos += 1

    def match_token(self):
        for regex, token_type in TOKEN_REGEXES:
            match = re.match(regex, self.text[self.pos:])
            if match:
                value = match.group(0)
                token = Token(token_type, value)
                self.pos += len(value)
                return token

        # If no match found, raise an exception
        raise ValueError(f'Invalid syntax at position {self.pos}')

    def get_next_token(self):
        self.skip_whitespace()

        if self.pos >= len(self.text):
            return Token('EOF')

        return self.match_token()

