import time

def minutes_to_seconds(min):
  return min * 60

def minutes_from_now(minutes=0):
  # Returns the timestamp `minutes` after the current time.
  return time.time() + minutes_to_seconds(minutes)
