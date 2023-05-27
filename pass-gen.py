import string  # Import the string module to access character sets
import random  # Import the random module for shuffling characters
from csv import writer  # Import the writer class from the csv module


def passgen():
    s1 = string.ascii_lowercase  # Lowercase letters character set
    s2 = string.ascii_uppercase  # Uppercase letters character set
    s3 = string.digits  # Digits character set
    s4 = string.punctuation  # Punctuation marks character set
    
    platform = input("ENTER THE NAME OF THE PLATFORM: \n")  # Prompt the user to enter the platform name
    pass_length = int(input("ENTER THE LENGTH OF THE PASSWORD: \n"))  # Prompt the user to enter the password length
    
    s = []  # Initialize an empty list to store characters for the password
    
    s.extend(list(s1))  # Add lowercase letters to the list
    s.extend(list(s2))  # Add uppercase letters to the list
    s.extend(list(s3))  # Add digits to the list
    s.extend(list(s4))  # Add punctuation marks to the list
    
    random.shuffle(s)  # Shuffle the characters in the list
    
    password = ("".join(s[0:pass_length]))  # Generate the password by joining the first pass_length characters
    
    print(password)  # Print the generated password to the console
    
    passdata = [platform, password]  # Create a list with the platform name and password
    
    with open('pass.csv', 'a') as f:  # Open the CSV file in append mode
        writedata = writer(f)  # Create a writer object
        writedata.writerow(passdata)  # Write the passdata list as a new row in the CSV file


passgen()  # Call the passgen function to generate the password
