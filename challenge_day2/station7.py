consts = {'a': 3, 'b': -1, 'c': 4, 'd': 7, 'e': 0.5}

def solution_station_7(expr: str) -> float:
    expr = expr.replace(" ", "")
    total = 0.0
    for term in expr.split("+"):
        if not term:
            continue
        prod = 1.0
        for v in term.split("*"):
            prod *= consts[v]
        total += prod
    return total
