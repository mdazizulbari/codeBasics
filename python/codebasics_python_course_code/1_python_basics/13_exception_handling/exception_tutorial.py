# Get two numbers from user as strings
x = input("Enter number 1: ")
y = input("Enter number 2: ")

# Try block - contains code that might raise exceptions
try:
    z = int(x) / int(y)  # Convert strings to integers and divide
                          # Can raise: ValueError (invalid int), ZeroDivisionError (y=0)
    
    a = 'baby yoda' + 56  # Attempting to add string + integer
                          # ALWAYS raises TypeError (can't concatenate str and int)

# Except block 1 - catches division by zero errors
except ZeroDivisionError as ze:
    print("Exception occured: ", ze)  # Print error details
    z = 0  # Set default value when division fails

# Except block 2 - catches type mismatch errors
except TypeError as te:
    print("Exception occured: ", te)  # Print error details
    z = 0  # Set default value

# Except block 3 - catches ALL other exceptions (catch-all)
except Exception as e:
    print("Generic exception occured: ", e)  # Print any other error
    z = 0  # Set default value

# This always runs - whether exception occurred or not
print("division is: ", z)

# Second try-except block - file operations
try:
    file = open("example.txt", "r")  # Try to open file in read mode
                                     # Raises FileNotFoundError if file doesn't exist
    content = file.read()  # Read entire file content
    print(content)  # Print file content

# Catch specific error - file not found
except FileNotFoundError:
    print("Error: The file was not found.")  # Inform user file is missing

# Finally block - ALWAYS executes, even if exception occurs
# Used for cleanup operations (closing files, releasing resources)
finally:
    file.close()  # Close the file (BUG: crashes if file was never opened)
    print("File closed.")