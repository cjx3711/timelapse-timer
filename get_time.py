# Refer to README.md for explainations
import os
import pathlib
import datetime
import time


seconds_threshold = 45
total_seconds = 0

files = [f for f in os.listdir('count') if os.path.isfile(f"count/{f}")]

print(f"Length {len(files)}")

files.sort()
previous_file = None
for f in files:
  if previous_file is None:
    previous_file = f
  else:
    prev_time = time.strptime(previous_file[0:17], '%Y-%m-%d_%H%M%S')
    this_time = time.strptime(f[0:17], '%Y-%m-%d_%H%M%S')
    seconds_between = time.mktime(this_time) - time.mktime(prev_time)
    if (seconds_between <= seconds_threshold):
      total_seconds += seconds_between
    else:
      print(f"Skipped because {seconds_between} > {seconds_threshold}s")
    previous_file = f
    
print(f"Total seconds taken {total_seconds}")
print(f"Total minutes taken {total_seconds / 60}")
print(f"Total hours taken {total_seconds / 60 / 60}")

hours = int(total_seconds / 60 / 60)
minutes = int(total_seconds / 60) % 60
seconds = int(total_seconds) % 60
print(f"Total time taken {hours}:{minutes}:{seconds}")