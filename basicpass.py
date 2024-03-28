# Basic Password Generator 
# Checks the strength based on password length

# Imports
import random 

print()
print("Welcome to the Password Generator!\n") 

# function that generates random letters based on the users input
def random_letters():  
    # letters 
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    # User input for how many letters they want to use
    nr_letters= int(input("How many letters would you like in your password? "))  
    l = ''
    for i in range(nr_letters):
        random_char = random.choice(letters) 
        l += random_char 
    return l 


# funtion that generates random symbols from the list of symbols provided 
def random_sym(): 
    # symbols 
    symbols = ['!', '#', '$', '%', '&', '@', '-', '*', '+']  
    
    # User input
    nr_symbols = int(input(f"How many symbols would you like? ")) 
    print()
    s = '' 
    for i in range(nr_symbols): 
        random_symbol = random.choice(symbols) 
        s += random_symbol 
    return s 

# function that generates a list of random numbers based on the users input 
def random_int():   
    
    # numbers 
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 

    # User input 
    nr_numbers = int(input(f"How many numbers would you like? "))  
    n = ''
    for i in range(nr_numbers): 
        random_number = random.choice(numbers) 
        n += random_number   
    return n 

# Combine all the input 

all_input = random_int() + random_letters() + random_sym()

# randomize all of the input now 

# turns the variable all_input into a list, then shuffles it
list = list(all_input) 
random.shuffle(list) 

# converts the shuffled 'list' of characters into a single string, forming the randomized password
password = ''.join(list) 

# Function that determines the length of your password, if it is too short, then it will consider it weak 
def min_length(password): 
    if len(password) >= 15: 
        return f"I like your password, it is strong.\nPassword: {password}" 
    elif len(password) >= 10 and len(password) < 15: 
        return f"Your password is ok, it could use some work\nPassword: {password}\nTry again to make it stronger, choose a higher value for each variable"
    elif len(password) >= 1 and len(password) < 10: 
        return f"Your password is weak and can get cracked easily\nPassword: {password}\nTry again to make it stronger, choose a higher value for each variable" 
    else: 
        return "You have no password you idiot, you will get hacked"  
    
def main():
    print(min_length(password)) 
    print() 

# Call the main function if the script is run directly, ensures that the main() function is only executed if the script is run directly  
# not when it's imported as a module into another script 
# prevents the main functionality of the script from being executed unintentionally when imported elsewhere
if __name__ == "__main__":
    main() 
