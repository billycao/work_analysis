#!/usr/bin/python

"""TODO(billycao): DO NOT SUBMIT without one-line documentation for analyze.

TODO(billycao): DO NOT SUBMIT without a detailed description of analyze.
"""

import datetime
import json

def is_at_work(location):
  lat = location["latitudeE7"]
  lng = location["longitudeE7"]

  # Approximately MTV main campus
  if (lat > 374123420 and lat < 374299680 and
      lng > -1220905630 and lng < -1220672180):
    return True


def main():
  json_fp = open("location_history.json")
  json_obj = json.load(json_fp)
  locations = json_obj["locations"]

  work_history = {}
  for location in locations:
    dt = datetime.datetime.fromtimestamp(float(location['timestampMs'])/1000)

    dayofweek = dt.weekday()
    # Forget < 2017, bro.
    if dt.year < 2017:
      continue
    # Analysis is only valid Mon - Wed and Fri, as I work from home Thurs
    if not ((dayofweek >= 0 and dayofweek <= 2) or dayofweek == 4):
      continue

    date_str = str(dt.date())
    dt_str = str(dt)
    if is_at_work(location):
      if not (date_str in work_history):
        work_history[date_str] = {}

      if not ("first_seen_at_work" in work_history[date_str]):
        work_history[date_str]["first_seen_at_work"] = dt
      elif (dt < work_history[date_str]["first_seen_at_work"]):
        work_history[date_str]["first_seen_at_work"] = dt

      if not ("last_seen_at_work" in work_history[date_str]):
        work_history[date_str]["last_seen_at_work"] = dt
      elif (dt > work_history[date_str]["last_seen_at_work"]):
        work_history[date_str]["last_seen_at_work"] = dt

  for date in work_history:
    work_history[date]["first_seen_at_work"] = str(work_history[date]["first_seen_at_work"])
    work_history[date]["last_seen_at_work"] = str(work_history[date]["last_seen_at_work"])

  # Save our work
  work_history_json = json.dumps(work_history)
  output_fp = open("work_history.json", "w")
  output_fp.write(work_history_json)

if __name__ == '__main__':
  main()
