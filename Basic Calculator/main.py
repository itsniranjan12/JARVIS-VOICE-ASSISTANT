
# Basic CLI Calculator
# Supports addition, subtraction, multiplication, and division for user-defined number of inputs


# Welcome message
print("Welcome to our calculator")

# Ask user how many numbers they want to operate on
n = int(input("Enter your number: "))


# Display operation menu
print("Select your Operation: ")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")


# Take operation input from user
choice = int(input("Enter Your Operation: "))


# Define addition function
def Add():
    sum = 0
    pos = 0
    while pos < n:
        choice_n = int(input("Enter your number: "))
        sum = sum + choice_n
        pos = pos + 1
    print(f"Your answer is {sum}")



# Define subtraction function
# Subtracts all positive numbers, adds all negative numbers (non-standard behavior, possibly intentional)
def Subtract():
    answer = 0
    pos = 0
    while pos < n:
        choice_n = int(input("Enter your number: "))
        if pos == 0:
            if choice_n < 0:
                print("Enter a positive number: ")
                choice_n = int(input('Enter your number: '))
                answer = answer - choice_n
                pos = pos + 1
            
        else:
            answer = answer - choice_n
            pos = pos + 1
    print(f"Your answer is {answer}")


# Define multiplication function
def Multiply():
    ans = 1
    pos = 0
    while pos < n:
        choice_n = int(input("Enter your number: "))
        ans = ans * choice_n
        pos = pos + 1
    print(f"Your answer is {ans}")

# Define division function
# Divides the first number by the next numbers sequentially
def Divide():
    pos = 0
    b = 1  # Dummy initial divisor
    while pos<n:
        if pos == 0:
            choice_n = int(input("Enter your number: "))
            answer = choice_n / b
            pos = pos + 1
        else:
            choice_n = int(input("Enter your number: "))
            answer = answer / choice_n
            pos = pos + 1
    print(f"Your answer is {answer}")            



# Main execution block            
if __name__ == "__main__":
    # Run the chosen operation based on user input
    while (choice == 1) or (choice == 2) or (choice == 3) or (choice == 4):
        if (choice == 1):
         Add()
         break
        elif (choice == 2):
         Subtract()
         break
        elif (choice == 3):
         Multiply()
         break
        elif (choice == 4):
         Divide()
         break
        else:
         print("Invalid Operation")


# Exit message         
print("Thanks For Using")        


        

    

     




