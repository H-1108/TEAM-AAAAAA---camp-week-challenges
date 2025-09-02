from datetime import date

def solution_station_2(s:str) -> str:
  weekdays = ["月曜日", "火曜日", "水曜日", "木曜日", "金曜日", "土曜日", "日曜日"]
  d = date.fromisoformat(s)
  return weekdays[d.weekday()]
