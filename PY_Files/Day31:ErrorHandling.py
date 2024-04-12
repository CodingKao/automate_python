### Day 31: Error Handling: 

### Learn about Python's exception handling mechanism and how to use try-except blocks effectively.

try:
    # Code that may riase an exception
    # Example
    result = 10/0
    # If exception occurs, the execution jumps to the except block
except ZeroDivisionError:
    # Handle the specific exception
    print("Error: Division by zero!")

