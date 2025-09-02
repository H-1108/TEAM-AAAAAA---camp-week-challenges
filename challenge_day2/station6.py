samples = [ 
  (0.4, 0.3894),
  (1.1, 0.8912),
  (2.9, 0.2392),
  (1.9, 0.9463),
  (1.6, 0.9996),
  (2, 0.9093),
  (2.5, 0.5985),
  (2.3, 0.7457),
  (0.6, 0.5646),
  (0, 0),
]

import math

def sin_auto(x: float, ndigits: int = 4) -> float:
  rad = math.radians(x) if abs(x) > 2 * math.pi else x
  return round(math.sin(rad), ndigits)

for x, y_expected in samples:
  print(sin_auto(x))

inputs  = [86,16,47,66,27,72,54,31,69,10]
outputs = [sin_auto(v) for v in inputs]
print(outputs)
