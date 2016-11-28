#Student No.:   10352769
#Course:        Programming for Big Data
#Module:        B8IT105
#Assignment:    Continuous Assessment 1


'''Below are 11 defined functions used for our Scientific Calculator Program'''

#Defining addition function:

def add (first, second):        
    return first + second

#Defining subtraction function:
    
def subtract (first, second):   
    return first - second

#Defining multiplication function:

def multiply (first, second):   
    return first * second

#Defining Division function:  
 
def divide (first, second):     
    return first / second

#Defining Exponential function:

def exponentiate (first, second):   
    return first ** second

#Defining Square Root function:

def squareRoot(first):          
    return first ** (0.5)

#Defining Cube function:

def cube(first):                
    return first ** 3
    
#Defining Cube Root function:

def cubeRoot(first):             
    return first ** (1.0 / 3)

#Defining Factorial function: 

def factorial(n):               
    if n == 1:
        return 1
    else:
        res = n * factorial(n - 1)
        return res
    
#Defining Sine function:
 
def sine(n):
    x = n * 0.017455329
    sin = x - (x**3)/factorial(3) + (x**5)/factorial(5) - (x**7)/factorial(7) + (x**9)/factorial(9) - (x**11)/factorial(11) + (x**13)/factorial(13) - (x**15)/factorial(15) + (x**17)/factorial(17) - (x**19)/factorial(19) 
    return sin

#Defining Cosine function:
   
def cosine(n):
    x = n * 0.017455329
    cos = 1 - (x**2)/factorial(2) + (x**4)/factorial(4) - (x**6)/factorial(6) + (x**8)/factorial(8) - (x**10)/factorial(10) + (x**12)/factorial(12) - (x**14)/factorial(14) + (x**16)/factorial(16) - (x**18)/factorial(18) 
    return cos

