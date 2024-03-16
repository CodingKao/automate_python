### Day 22: Working with Dates

## Write a script that prints the current date and time using the `datetime` module.

import datetime

def print_current_date_time():
    current_date_time = datetime.datetime.now()
    print("Current date and time: ", current_date_time)

    previous_date_time = current_date_time - datetime.timedelta(days=1)
    print("Previous date adn time:", previous_date_time)

# Print Output
print_current_date_time()