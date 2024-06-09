# Prompt user for current time including time period designation (AM or PM).
current_time = input("What is current time in 12-hour format, including AM or PM?: ")
#
# Split user input into hours, minutes, and time period designation.
time_period = current_time.split()
hour, minute = map(int, time_period[0].split(":"))
#
# Ensure all time_period input is in UPPERCASE for use in conversions below.
am_pm = time_period[1].upper()
#
# Convert time to 24-hour format based on current time and time period input.
if am_pm == "PM" and hour != 12:
    hour += 12
elif am_pm == "AM" and hour == 12:
    hour = 0
#
# Prompt user for number of hours until the alarm goes off.
alarm_hours = int(input("How many hours until your mortal enemy wakes you up? "))

# Calculate the time alarm will go off and use the modulo operator with 24
# to ensure correct format.
#
alarm_hour = (hour + alarm_hours) % 24
alarm_minute = minute  # Minutes remain the same
#
# Format and print the alarm time in military time.
alarm_time = f"{alarm_hour:02d}{alarm_minute:02d}"
print(f"The alarm will go off at {alarm_time} hours so rest up while you can!")
