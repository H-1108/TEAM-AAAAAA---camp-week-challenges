def solution_station_1(n: int) -> int:
    """
    It's Fibonacci number,
    Station 1 inputs -> Fibonacci(input)
        input = 4 -> output = 3
        input = 10 -> output = 55
        input = 98 -> output = 135301852344706740000


"""
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


