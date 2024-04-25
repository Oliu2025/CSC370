import unittest
from lexer import tokenize
from spl_ast import Parser
from semantic import SemanticAnalyzer


class TestSPLSyntax(unittest.TestCase):
    def test_valid_code_1(self):
        code = """
        def main():
            age = 25
            name = "John"
            if age >= 18:
                print(name + " is an adult")
            else:
                print(name + " is a minor")
            i = 0
            while i < 5:
                print("Iteration:", i)
                i += 1
            for j in range(3):
                print("For loop iteration:", j)
            def add(a, b):
                return a + b
            result = add(3, 5)
            print("Result of add function:", result)

        main()
        """

        print("Test Case:")
        print(code)  # Print the test case
        # Tokenize the code
        tokens = tokenize(code)
        # Parse the code and construct AST
        parser = Parser()
        ast = parser.parse(tokens)  # Pass tokens, not code
        # Perform semantic analysis
        analyzer = SemanticAnalyzer()
        for node in ast:  # Iterate over each node in the AST
            analyzer.visit(node)  # Call visit method for each node

    def test_valid_code_2(self):
        code = """
        x = 10
        y = 20
        if x < y:
            print("x is less than y")
        else:
            print("x is greater than or equal to y")
        """

        print("Test Case:")
        print(code)  # Print the test case
        # Tokenize the code
        tokens = tokenize(code)
        # Parse the code and construct AST
        parser = Parser()
        ast = parser.parse(tokens)  # Pass tokens, not code
        # Perform semantic analysis
        analyzer = SemanticAnalyzer()
        for node in ast:  # Iterate over each node in the AST
            analyzer.visit(node)  # Call visit method for each node

    def test_invalid_code_1(self):
        code = """
        x = 10
        y = "Hello"
        z = x + y
        """

        print("Test Case:")
        print(code)  # Print the test case
        # Tokenize the code
        tokens = tokenize(code)
        # Parse the code and construct AST
        parser = Parser()
        with self.assertRaises(ValueError):
            ast = parser.parse(tokens)  # Pass tokens, not code

    def test_invalid_code_2(self):
        code = """
        def func(a, b):
            return a + b + c
        func(5, 10)
        """

        print("Test Case:")
        print(code)  # Print the test case
        # Tokenize the code
        tokens = tokenize(code)
        # Parse the code and construct AST
        parser = Parser()
        with self.assertRaises(ValueError):
            ast = parser.parse(tokens)  # Pass tokens, not code


if __name__ == '__main__':
    unittest.main()
