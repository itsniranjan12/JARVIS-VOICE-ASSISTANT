import random

computer = random.randint(1,100)
a = -1
i = 0
while a != computer:
    a = int(input("Enter your number: "))
    i = i + 1
    if a > computer:
        print("Enter a lower number please")    
    elif a < computer:
        print("Enter a higher number please") 


print(f"You guessed the number in {i} attempts")        
         
