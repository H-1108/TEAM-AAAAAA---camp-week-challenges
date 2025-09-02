samples = [
  ("2023-04-18", "火曜日"),
  ("2023-07-01", "土曜日"),
  ("2023-07-09", "日曜日"),
  ("2023-03-25", "土曜日"),
  ("2023-07-06", "木曜日"),
  ("2023-11-27", "月曜日"),
  ("2023-11-21", "火曜日"),
  ("2023-11-10", "金曜日"),
  ("2023-05-29", "月曜日"),
  ("2023-04-27", "木曜日"),
]

from datetime import date

def date_to_japanese_weekday(s:str) -> str:
  weekdays = ["月曜日", "火曜日", "水曜日", "木曜日", "金曜日", "土曜日", "日曜日"]
  d = date.fromisoformat(s)
  return weekdays[d.weekday()]

assert all(date_to_japanese_weekday(x) == y for x, y in samples)

inputs = [
  "2024-03-22","2024-05-16","2024-12-18","2024-07-29","2024-12-02","2024-01-13",
  "2024-07-30","2024-05-01","2024-12-21","2024-07-27","2024-10-13",
]

outputs = [date_to_japanese_weekday(s) for s in inputs]
result = dict(zip(inputs, outputs))

if __name__ == "__main__":
    for s, out in zip(inputs, outputs):
        print(s, out)


