import re

# Define token types along with their corresponding regular expressions for pattern matching
TOKEN_TYPES = [
    ('INTEGER', r'\d+'),
    ('FLOAT', r'\d+\.\d+'),
    ('BOOLEAN', r'True|False'),
    ('STRING', r'"(?:\\.|[^"\\])*"'),
    ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*'),
    ('KEYWORD', r'if|else|while|for|def|return'),  # Add more keywords as needed
    ('OPERATOR', r'\+|\-|\*|\/|\=|\==|\!=|\<|\> '),  # Add more operators as needed
    ('PUNCTUATION', r'\(|\)|\{|\}|\[|\]|,|:'),
    ('WHITESPACE', r'\s+'),
    ('COMMENT', r'#[^\n]*')
]

def tokenize(code):
    tokens = []
    code = code.strip()  # Remove leading and trailing whitespace

    # Compile regular expressions outside the loop for efficiency
    compiled_patterns = [(token_type, re.compile(pattern)) for token_type, pattern in TOKEN_TYPES]

    # Continue tokenization until code string is empty
    while code:
        longest_match = None
        # Iterate through each token type and its corresponding pattern
        for token_type, compiled_pattern in compiled_patterns:
            match = compiled_pattern.match(code)
            # Update longest_match if a longer match is found
            if match and (longest_match is None or match.end() > longest_match.end()):
                longest_match = match

        if longest_match:
            value = longest_match.group(0)
            # Add token to the list if it's not whitespace or a comment
            if token_type != 'WHITESPACE' and token_type != 'COMMENT':
                tokens.append((token_type, value))
            # Remove processed token from code string
            code = code[len(value):].strip()
        else:
            # Raise an error if no valid token is found
            raise ValueError("Invalid syntax near: {}".format(code))

    return tokens
