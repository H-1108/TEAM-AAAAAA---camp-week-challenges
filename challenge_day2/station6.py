import math

def solution_station_6(x: float, ndigits: int = 4) -> float:
  rad = math.radians(x) if abs(x) > 2 * math.pi else x
  return round(math.sin(rad), ndigits)
