# Write a function named add_time that takes in two required parameters and
# one optional parameter:

# a start time in the 12-hour clock format (ending in AM or PM) a duration
# time that indicates the number of hours and minutes(optional) a starting
# day of the week, case insensitive The function should add the duration time
# to the start time and return the result.

# If the result will be the next day, it should show (next day) after the
# time. If the result will be more than one day later, it should show (n days
# later) after the time, where "n" is the number of days later.

# If the function is given the optional starting day of the week parameter,
# then the output should display the day of the week of the result. The day
# of the week in the output should appear after the time and before the
# number of days later.

# Below are some examples of different cases the function should handle. Pay
# close attention to the spacing and punctuation of the results.

# add_time("3:00 PM", "3:10")
# # Returns: 6:10 PM

# add_time("11:30 AM", "2:32", "Monday")
# # Returns: 2:02 PM, Monday

# add_time("11:43 AM", "00:20")
# # Returns: 12:03 PM

# add_time("10:10 PM", "3:30")
# # Returns: 1:40 AM (next day)

# add_time("11:43 PM", "24:20", "tueSday")
# # Returns: 12:03 AM, Thursday (2 days later)

# add_time("6:30 PM", "205:12")
# # Returns: 7:42 AM (9 days later) Do not import any Python libraries. Assume
#   that the start times are valid times. The minutes in the duration time
#   will be a whole number less than 60, but the hour can be any whole
#   number.
import re
def add_time(start, duration, day_of_week=None):
  weeks = [
      "sunday", "monday", "tuesday", "wednesday", "thursday", "friday",
      "saturday"
  ]
  hour_hand = re.findall(r'([0-9]+):', start + duration)
  minute_hand = re.findall(r':([0-9]+)', start + duration)
  time_of_day = re.findall(r'[A-Z]+$', start)
  total_minute = int(minute_hand[0]) + int(minute_hand[1])
  total_hour = int(hour_hand[0]) + int(hour_hand[1])
  day_later = 0
  if total_minute / 60 > 1.0:
    total_minute = total_minute % 60
    total_hour += 1
  if total_hour % 24 > 1:
    day_later = int(total_hour / 24)
    total_hour %= 24
  if total_hour > 11:
    if time_of_day[0] == "PM":
      day_later += 1
      time_of_day[0] = "AM"
    else:
      time_of_day[0] = "PM"
  if total_hour > 12:
    total_hour = total_hour % 12
  if len(str(total_minute)) == 1:
    total_minute = "0" + str(total_minute)
  if day_of_week == None:
    day_of_week = ""
  else:
    day_of_week = day_of_week.lower()
    weeks_pos = weeks.index(day_of_week)
    weeks_pos = (weeks_pos + day_later) % 7
    day_of_week = ", " + weeks[weeks_pos].capitalize()
  if day_later == 0:
    day_later = ""
  elif day_later == 1:
    day_later = str(" (next day)")
  else:
    day_later = " (" + str(day_later) + " days later)"
  return f"{total_hour}:{total_minute} {time_of_day[0]}{day_of_week}{day_later}"
print(add_time("8:16 PM", "466:02", "tuesday"))