from spl_ast import Variable, IfStatement, WhileLoop, ForLoop, Function, SPLBoolean, SPLInteger

class SemanticAnalyzer:
    def __init__(self):
        # Initialize the symbol table to store variable names and their data types
        self.symbol_table = {}

    def analyze(self, ast):
        # Clear the symbol table before analyzing a new AST
        self.symbol_table.clear()
        # Start the analysis by visiting the AST
        self.visit(ast)

    def visit(self, node):
        # Dispatch the analysis based on the type of AST node
        if isinstance(node, Variable):
            self.visit_variable(node)
        elif isinstance(node, IfStatement):
            self.visit_if_statement(node)
        elif isinstance(node, WhileLoop):
            self.visit_while_loop(node)
        elif isinstance(node, ForLoop):
            self.visit_for_loop(node)
        elif isinstance(node, Function):
            self.visit_function(node)
        else:
            raise ValueError("Invalid AST node type: {}".format(type(node)))

    def visit_variable(self, variable_node):
        # Check if the variable is already declared in the symbol table
        if variable_node.name in self.symbol_table:
            raise ValueError("Variable '{}' already declared".format(variable_node.name))
        # Add the variable to the symbol table with its data type
        self.symbol_table[variable_node.name] = variable_node.data_type

    def visit_if_statement(self, if_statement_node):
        # Check the expression type of the if statement condition
        self.check_expression_type(if_statement_node.condition, SPLBoolean)

        # Visit the true block of the if statement
        for node in if_statement_node.true_block:
            self.visit(node)

        # Visit the false block of the if statement if it exists
        if if_statement_node.false_block:
            for node in if_statement_node.false_block:
                self.visit(node)

    def visit_while_loop(self, while_loop_node):
        # Check the expression type of the while loop condition
        self.check_expression_type(while_loop_node.condition, SPLBoolean)

        # Visit the loop block of the while loop
        for node in while_loop_node.loop_block:
            self.visit(node)

    def visit_for_loop(self, for_loop_node):
        # Check the data type of the loop variable
        if for_loop_node.variable.data_type != SPLInteger:
            raise ValueError("Loop variable '{}' must be of type SPLInteger".
                             format(for_loop_node.variable.name))

        # Visit the iterable expression of the for loop
        self.visit(for_loop_node.iterable)

        # Visit the loop block of the for loop
        for node in for_loop_node.loop_block:
            self.visit(node)

    def visit_function(self, function_node):
        # Check if the function name clashes with an existing variable or function
        if function_node.name in self.symbol_table:
            raise ValueError("Function name '{}' clashes with existing variable or function".
                             format(function_node.name))

        # Add the function name to the symbol table
        self.symbol_table[function_node.name] = 'function'

        # Visit the body of the function
        for node in function_node.body:
            self.visit(node)

    def check_expression_type(self, expression_node, expected_type):
        pass
        # Placeholder method to check expression types

    def generate_assembly(self, ast):
        # Generate assembly code for the entire AST
        assembly_code = []
        for node in ast:
            assembly_code.extend(self.generate_node_assembly(node))
        return assembly_code

    def generate_node_assembly(self, node):
        # Generate assembly code for a specific AST node
        if isinstance(node, Variable):
            return self.generate_variable_assembly(node)
        elif isinstance(node, IfStatement):
            return self.generate_if_statement_assembly(node)
        elif isinstance(node, WhileLoop):
            return self.generate_while_loop_assembly(node)
        elif isinstance(node, ForLoop):
            return self.generate_for_loop_assembly(node)
        elif isinstance(node, Function):
            return self.generate_function_assembly(node)
        else:
            raise ValueError("Invalid AST node type: {}".format(type(node)))

    def generate_variable_assembly(self, variable_node):
        pass
        # Placeholder method for generating assembly code for variable declarations

    def generate_if_statement_assembly(self, if_statement_node):
        pass
        # Placeholder method for generating assembly code for if statements

    def generate_while_loop_assembly(self, while_loop_node):
        pass
        # Placeholder method for generating assembly code for while loops

    def generate_for_loop_assembly(self, for_loop_node):
        pass
        # Placeholder method for generating assembly code for for loops

    def generate_function_assembly(self, function_node):
        pass
        # Placeholder method for generating assembly code for function definitions
