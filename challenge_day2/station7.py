import sympy as sp
import numpy as np
import pandas as pd

def solution_station_7(input_expr):
   
    # Define symbolic variables
    a, b, c, d, e = sp.symbols('a b c d e')
    
    # Create equations from the provided data
    equations = [
        c + e + a + d - 14.5,    # c+e+a+d = 14.5
        c * d + b - 27,           # c*d+b = 27
        c + a + d * b,            # c+a+d*b = 0
        e * a * c - 6,            # e*a*c = 6
        b + c * a * e - 5,        # b+c*a*e = 5
        e * b + d - 6.5,          # e*b+d = 6.5
        a * d + e + b - 20.5,     # a*d+e+b = 20.5
        a + d + b + c - 13,       # a+d+b+c = 13
        e + d + a + b - 9.5,      # e+d+a+b = 9.5
        e + b + 0.5,              # e+b = -0.5
        e * b * d * a + 10.5,     # e*b*d*a = -10.5
        a * b + 3,                # a*b = -3
        d + c - 11,               # d+c = 11
        e * a * d - 10.5,         # e*a*d = 10.5
        e * b + a + d - 9.5       # e*b+a+d = 9.5
    ]
    
    # Solve the system of equations
    solutions = sp.solve(equations, (a, b, c, d, e), dict=True)
    
    if not solutions:
        raise ValueError("No solution found for the given equations")
    
    # Extract the solution
    solution = solutions[0]
    a_val = solution[a]
    b_val = solution[b]
    c_val = solution[c]
    d_val = solution[d]
    e_val = solution[e]
    
    # Create a dictionary of variable values for substitution
    var_dict = {
        'a': a_val,
        'b': b_val,
        'c': c_val,
        'd': d_val,
        'e': e_val
    }
    
    # Evaluate the input expression
    try:
        # Parse the expression
        expr = sp.sympify(input_expr)
        # Substitute the values
        result = expr.subs(var_dict)
        return float(result)  # Convert to float for consistent output
    except Exception as ex:
        raise ValueError(f"Error evaluating expression: {ex}")

# Example usage and testing
if __name__ == "__main__":
    # Test with the provided examples
    test_expressions = [
        "b*d+e",
        "b*c*e",
        "b+c+e*a"
    ]
    
    print("Testing the solution function:")
    for expr in test_expressions:
        result = solution_station_7(expr)
        print(f"{expr} = {result}")
    
    # Interactive mode
    print("\nInteractive mode (type 'quit' to exit):")
    while True:
        user_input = input("Enter expression: ").strip()
        if user_input.lower() == 'quit':
            break
        try:
            result = solution_station_7(user_input)
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}")



