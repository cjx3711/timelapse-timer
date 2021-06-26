# Timelapse Timer

This is a small utility that will calculate the time taken for a screen recording timelapse by detecting the time between each file and removing any large gaps.

The files should be in a folder called `count` and should be named with the following format: `'2021-05-25_020220_as.jpg'`. This is the output of the automatic screenshoter program on windows.


## Example

Folder structure:
```
get_time.py
count/
  2021-05-25_020220_as.jpg
  2021-05-25_020225_as.jpg
  ...
```

Running:
```
> python3 get_time.py
Length 431
Skipped because 532.0 > 45s
Total seconds taken 761.0
Total minutes taken 12.683333333333334
Total hours taken 0.2113888888888889
Total time taken 0:12:41
```