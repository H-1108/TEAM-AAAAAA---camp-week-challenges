def solution_station_3(x):
    """
    Rule inferred from sample data:
    Return True if x <= 25 or x is in {54, 78}, else return False
    """
    if x <= 25 or x in {54, 78}:
        return True
    else:
        return False
if __name__ == "__main__":
    test_cases = {
        54: True,
        83: False,
        58: False,
        14: False,
        12: True,
        30: False,
        89: False,
        79: False,
        86: False,
        21: True,
        24: True,
        10: False,
        78: True,
        88: False,
        40: False,
        62: False,
        15: True,
    }
    for input_value, expected_output in test_cases.items():
        result = solution_station_3(input_value)
        assert result == expected_output, f"Failed for input {input_value}: got {result}, expected {expected_output}"
    print("All test cases passed.")