#Student No.:   10352769
#Course:        Programming for Big Data
#Module:        B8IT105
#Assignment:    Continuous Assessment 1

'''Importing all defined scientific functions from calculator.py'''

from calculator import *

#Defining User Interface Menu for user to select which function to they want to user

def show_menu():
   print "##########################"
   print "Enter 1 for Addition"
   print "Enter 2 for Subtraction"
   print "Enter 3 for Multiplication"
   print "Enter 4 for Division"
   print "Enter 5 for Exponentiate"
   print "Enter 6 for Square Root"
   print "Enter 7 for Cube"
   print "Enter 8 for Cube Root"
   print "Enter 9 for Factorial"
   print "Enter 10 for Sine"
   print "Enter 11 for Cosine"
   print "Enter 12 for Tangent" 
   print "Q to quit"
   print "###########################"

#Initiating while loop:   
 
while True:
    show_menu()
    str_input = raw_input("Please input menu choice> ")
    if str_input.upper() == 'Q':
        break
        
#Testing to see if user input is of the correct type:
      
    try:
        choice = int(str_input)
    except:
        print 'Invalid input'
        raw_input("Press 'Enter' to return to the main menu")
        continue
        
#Testing to see if user input is not outside of the menu limits:
        
    if choice < 1 or choice >= 13:
        print 'Invalid input'
        raw_input("Press 'Enter' to return to the main menu")
        continue

#Menu choices 1 to 5 take 2 inputs
         
    elif choice >= 1 and choice <= 5:
        str_input1 = raw_input('Please enter first number for calculation> ')
        str_input2 = raw_input('Please enter second number for calculation> ')

#Testing to see if user input is of the correct type:
        
        try:
            num1 = float(str_input1)
            num2 = float(str_input2)
       
        except:
            print 'Invalid input'
            raw_input("Press 'Enter' to return to the main menu")
            continue

#Menu choices 6 to 11 take 2 inputs
           
    elif choice >= 6 and choice <= 12:
        number1 = raw_input('Please enter number for calculation> ')
        
#Testing to see if user input is of the correct type:

        try:
            number1 = float(number1)
        except:
            print 'Invalid input'
            raw_input("Press 'Enter' to return to the main menu")
            continue 

#Menu choice functions:
            
    if choice == 1:
        print add (num1, num2)
       
    elif choice == 2:
        print subtract (num1, num2)
      
    elif choice == 3:
        print multiply (num1, num2)
       
    elif choice == 4:
        print divide (num1, num2)
       
    elif choice == 5:
        print exponentiate (num1, num2)
       
    elif choice == 6:
        print squareRoot (number1)
       
    elif choice == 7:
        print cube (number1)
       
    elif choice == 8:
        print cubeRoot (number1)
             
    elif choice == 9:
        print factorial (number1)
       
    elif choice == 10:
        print sine (number1)
       
    elif choice == 11:
        print cosine (number1)
        
    elif choice == 12:
        print sine (number1)/cosine (number1)
       
#Prompting the user if they want to quit the program or continue:
       
    if 'Q' == raw_input("Q to quit / Enter to continue> "):
        break

#End of program:
        
print "Thank you"