#!/usr/bin/python

"""TODO(billycao): DO NOT SUBMIT without one-line documentation for analyze_work_history.

TODO(billycao): DO NOT SUBMIT without a detailed description of analyze_work_history.
"""

import datetime
import json

def main():
  json_fp = open("work_history.json")
  json_obj = json.load(json_fp)

  histogram = {
    10: 0,
    9.5: 0,
    9: 0,
    8.5: 0,
    8: 0,
    7.5: 0,
    7: 0,
    6.5: 0,
    6: 0,
    5.5: 0,
    5: 0,
    4.5: 0,
    4: 0,
    3.5: 0,
    3: 0,
    2.5: 0,
    2: 0,
    1.5: 0,
    1: 0,
    0.5: 0,
    0: 0,
  }

  for date_str in json_obj:
    work_day = json_obj[date_str]

    dt = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    date = dt.date()


    try:
      dt_start = datetime.datetime.strptime(work_day["first_seen_at_work"], "%Y-%m-%d %H:%M:%S.%f")
    except ValueError:
      dt_start = datetime.datetime.strptime(work_day["first_seen_at_work"], "%Y-%m-%d %H:%M:%S")

    try:
      dt_finish = datetime.datetime.strptime(work_day["last_seen_at_work"], "%Y-%m-%d %H:%M:%S.%f")
    except ValueError:
      dt_finish = datetime.datetime.strptime(work_day["last_seen_at_work"], "%Y-%m-%d %H:%M:%S")

    timedelta_worked = dt_finish - dt_start

    hours_worked = timedelta_worked.total_seconds() / 3600.0

    for hour in sorted(histogram.keys(), reverse=True):
      if hours_worked > hour:
        histogram[hour] += 1
        break

  for hour in sorted(histogram.keys(), reverse=True):
    print str(hour) + ":\t" + str(histogram[hour])

if __name__ == '__main__':
  main()
