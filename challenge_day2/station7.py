import sympy as sp

a, b, c, d, e = sp.symbols('a b c d e')

equations = [
    c + e + a + d - 14.5,   
    c * d + b - 27,        
    c + a + d * b,          
    e * a * c - 6,           
    b + c * a * e - 5,       
    e * b + d - 6.5,         
    a * d + e + b - 20.5,   
    a + d + b + c - 13,     
    e + d + a + b - 9.5,     
    e + b + 0.5,            
    e * b * d * a + 10.5,   
    a * b + 3,               
    d + c - 11,              
    e * a * d - 10.5,        
    e * b + a + d - 9.5     
]

solution = sp.solve(equations, (a, b, c, d, e), dict=True)
if solution:
    a_val = solution[0][a]
    b_val = solution[0][b]
    c_val = solution[0][c]
    d_val = solution[0][d]
    e_val = solution[0][e]
    print(f"Solved values: a = {a_val}, b = {b_val}, c = {c_val}, d = {d_val}, e = {e_val}")
else:
    print("No solution found")
    exit()

values = {a: a_val, b: b_val, c: c_val, d: d_val, e: e_val}
for i, eq in enumerate(equations):
    result = sp.simplify(eq.subs(values))
    if result != 0:
        print(f"Equation {i+1} may not hold: {result}")


input_expressions = [
    b*d+e,
    b*c*e,
    b+c+e*a
]

outputs = []
for expr in input_expressions:
    output_val = expr.subs(values)
    outputs.append(output_val)


print("\nOutput for input expressions:")
for expr, output in zip(input_expressions, outputs):
    print(f"{expr} = {output}")
