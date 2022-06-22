import time
import calendar

ticks = time.time()

print("Number of ticks since January 1, 1970 12:00AM: ", + ticks)

# Print time in struct_time format
localtime = time.localtime(time.time())
print("Local current time :", localtime)

# Print formatted time
formatted_time = time.asctime(time.localtime(time.time()))
print("Current time is: ", formatted_time)

