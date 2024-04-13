### Day 31: Error Handling: 

### Learn about Python's exception handling mechanism and how to use try-except blocks effectively.

try:
    # Code that may raise an exception
    # For example:
    result = 10 / 0
    # If an exception occurs, the execution jumps to the except block
except ZeroDivisionError:
    # Handle the specific exception
    print("Error: Division by zero!")
except Exception as e:
    # Handle other exceptions
    print("An error occurred:", e)
else:
    # Optional block that runs if no exceptions occurred
    print("No errors occurred.")
finally:
    # Optional block that always runs, regardless of whether an exception occurred
    print("This block always executes.")


