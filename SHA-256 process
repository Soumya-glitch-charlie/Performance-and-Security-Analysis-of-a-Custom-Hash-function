# Python program to create a unique hash number using SHA-256 algorithm

# At first, we import the hashlib library module
import hashlib

# then, we create a user input for the hash function
text_input = str(input("Enter the text input: "))

# the first step is to encode the text input
# then apply the hashing algorithms
hashed_output = hashlib.sha256(
    text_input.encode())  # # We took sha256 function from hashlib library and applied to encode the text input the user have given

# then print the hashed_output
print(f'The hash encoded text is : {hashed_output}')

# The hashed object will store at a specific memory location starting with @ which will only show the hashed output of the input text
# Then we have to convert this hashed object into a recognisable Hexadecimal number that we can print
print(f'The final hashed output is : {hashed_output.hexdigest()}')
