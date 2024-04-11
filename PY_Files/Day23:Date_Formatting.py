### Day 23: Date Formatting

## Modify the script to print the current date and time in a specific format.

import datetime

def current_date_time():
    current_date_time = datetime.datetime.now()
    print("Current date and time: ", current_date_time)

    formatted_date_time = current_date_time.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time: ", formatted_date_time)

# Print Output
current_date_time()
