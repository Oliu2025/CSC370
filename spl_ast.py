class SPLInteger:
    def __init__(self, value):  # Constructor for SPLInteger class, takes a value
        self.value = int(value)  # Convert the value to an integer and store it

    def __repr__(self):  # String representation method
        return str(self.value)  # Return the string representation of the value


class SPLBoolean:
    def __init__(self, value):  # Constructor for SPLBoolean class, takes a value
        if value.lower() == "true":  # If the value is "true" (case insensitive)
            self.value = True  # Set the value to True
        elif value.lower() == "false":  # If the value is "false" (case insensitive)
            self.value = False  # Set the value to False
        else:  # If the value is neither "true" nor "false"
            raise ValueError("Invalid boolean value: {}".format(value))  # Raise a ValueError

    def __repr__(self):  # String representation method
        return str(self.value)  # Return the string representation of the value


class Variable:
    def __init__(self, name, data_type, value):  # Constructor for Variable class, takes a name, data_type, and value
        self.name = name  # Assign the name
        self.data_type = data_type  # Assign the data type
        self.value = value  # Assign the value

class IfStatement:
    def __init__(self, condition, true_block, false_block=None):  # Constructor for
        # IfStatement class, takes a condition, true_block, and optional false_block
        self.condition = condition  # Assign the condition
        self.true_block = true_block  # Assign the true block
        self.false_block = false_block  # Assign the false block (optional)

class WhileLoop:
    def __init__(self, condition, loop_block):  # Constructor for WhileLoop class, takes a condition and loop_block
        self.condition = condition  # Assign the condition
        self.loop_block = loop_block  # Assign the loop block

class ForLoop:
    def __init__(self, variable, iterable, loop_block):  # Constructor for ForLoop
        # class, takes a variable, iterable, and loop_block
        self.variable = variable  # Assign the loop variable
        self.iterable = iterable  # Assign the iterable
        self.loop_block = loop_block  # Assign the loop block

class Function:
    def __init__(self, name, parameters, return_type, body):  # Constructor for Function
        # class, takes a name, parameters, return_type, and body
        self.name = name  # Assign the function name
        self.parameters = parameters  # Assign the function parameters
        self.return_type = return_type  # Assign the return type
        self.body = body  # Assign the function body


class Parser:
    # Initialize the Parser class with a dictionary mapping token types to parsing methods
    def __init__(self):
        self.token_parsers = {
            'def': self.parse_function_definition,  # Mapping 'def' keyword to parse_function_definition method
            'IDENTIFIER': self.parse_variable_declaration  # Mapping 'IDENTIFIER'
            # token to parse_variable_declaration method
        }

    # Method to parse a list of tokens into an abstract syntax tree (AST)
    def parse(self, tokens):
        self.tokens = tokens  # Store the tokens
        self.current_token_index = 0  # Initialize the current token index
        self.ast = []  # Initialize an empty list to store AST nodes

        # Iterate through each token
        while self.current_token_index < len(self.tokens):
            token_type, token_value = self.tokens[self.current_token_index]  # Get the
            # type and value of the current token

            # Check if the token type has a corresponding parsing method
            if token_type in self.token_parsers:
                self.token_parsers[token_type]()  # Call the corresponding parsing method
            else:
                raise SyntaxError("Unexpected token: {}".format(token_value))  # Raise SyntaxError for unexpected tokens

        return self.ast  # Return the generated AST

    # Method to parse variable declarations
    def parse_variable_declaration(self):
        var_name = self.tokens[self.current_token_index][1]  # Get the name of the variable
        self.consume_token('IDENTIFIER')  # Consume the 'IDENTIFIER' token
        self.consume_token('OPERATOR', '=')  # Consume the assignment operator '='
        var_value = self.tokens[self.current_token_index][1]  # Get the value of the variable
        self.consume_token('INTEGER', 'FLOAT', 'BOOLEAN', 'STRING')  # Consume the value token type
        self.ast.append(Variable(var_name, None, var_value))  # Create a Variable node and add it to the AST

    # Method to parse function definitions
    def parse_function_definition(self):
        self.consume_token('KEYWORD', 'def')  # Consume the 'def' keyword
        func_name = self.tokens[self.current_token_index][1]  # Get the name of the function
        self.consume_token('IDENTIFIER')  # Consume the function name
        self.consume_token('PUNCTUATION', '(')  # Consume the opening parenthesis for parameters
        parameters = []  # Initialize an empty list to store function parameters
        while self.tokens[self.current_token_index][0] != 'PUNCTUATION' or self.tokens[self.current_token_index][1] != ')':
            param_name = self.tokens[self.current_token_index][1]  # Get the parameter name
            self.consume_token('IDENTIFIER')  # Consume the parameter name
            parameters.append(param_name)  # Add the parameter name to the list
            # Check for comma to separate multiple parameters
            if self.tokens[self.current_token_index][0] == 'PUNCTUATION' and self.tokens[self.current_token_index][1] == ',':
                self.consume_token('PUNCTUATION', ',')  # Consume the comma
        self.consume_token('PUNCTUATION', ')')  # Consume the closing parenthesis for parameters
        self.consume_token('PUNCTUATION', ':')  # Consume the colon
        # Assuming function body will be parsed separately
        function_node = Function(func_name, parameters, None, [])  # Create a Function node
        self.ast.append(function_node)  # Add the Function node to the AST

    # Method to consume tokens based on expected types
    def consume_token(self, *expected_types):
        token_type, token_value = self.tokens[self.current_token_index]  # Get the type and value of the current token
        # Check if the token type matches any of the expected types
        if token_type in expected_types:
            self.current_token_index += 1  # Move to the next token index
        else:
            raise SyntaxError("Expected token of type {}, but got {}".format(expected_types, token_type))  # Raise
            # SyntaxError for unexpected tokens

