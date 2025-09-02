import sympy as sp

def solution_station_7(input_expr):
    values = {
        'a': 3,
        'b': -1,
        'c': 4,
        'd': 7,
        'e': 0.5
    }
    
  
    symbols = {sp.symbols(key): value for key, value in values.items()}
    
    try:
        expr = sp.sympify(input_expr)
        result = expr.subs(symbols)
        return float(result) 
    except Exception as e:
        return f"false: {e}"


if __name__ == "__main__":
    test_expressions = [
        "b*d+e",
        "b*c*e",
        "b+c+e*a"
    ]
    
    for expr in test_expressions:
        result = solution_station_7(expr)
        print(f"{expr} = {result}")



