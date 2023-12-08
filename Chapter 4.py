import random
import time

#4.1
text = input("please input something")
print(text)

def right_Justify(text):
    spaces = 70 - len(text)
    print(" "*spaces,text)

right_Justify(text)

#4.2
#random method
x = random.randint(1,100)
print(x)

#input two numbers and give answer
number = input("please input your number")
number1  = input("please input your number1")

number = int(number)
number1 = int(number1)

if (number > number1):
    print(number,"is bigger than", number1)
else:
    print(number,"is smaller than", number1)

#Recursion

def countdown(n):
    if n <= 0:
        print("Tyler")
    else:
        print(n)
        countdown(n-1)

countdown(4)

#Practice 4.1
def changetime (hour,  min ,sec, addinsec):
    addmin = int(addinsec / 60)
    addsec = addinsec % 60
    sec = int((sec + addinsec) % 60)

    temp = int( (sec + addsec)/60 )
    min = min + temp +addmin
    temp = int(min / 60 )
    min = int (min % 60)

    hour = hour + temp
    if hour >= 24 :
         hour = hour % 24

    print(hour, ":", min,":",sec)

changetime(0,0,0,time.time())

#practice 4.2

def check_Fermat():
    a = int(input("a"))
    b = int(input("b"))
    c = int(input("c"))
    n = int(input("n"))
    AN = a ** n
    BN = b ** n
    CN = c ** n
    if (AN + BN == CN and n>2):
        print("erro, Fermat is incorrect")
    else:
        print("Fermat is correct")

check_Fermat()

#practice 4.3
def check_triangle():
    x = int(input("the first side"))
    y = int(input("the second side"))
    z = int(input("the third side"))

    if (x + y > z and x + z > y and y + z > x ):
        print("Yes, it is an triangel")
    else:
        print("No, they can not make a triangel")

check_triangle()

#practice 4.4

def recurse(n, s):
    if n == 0:
       print(s)
    else:
        recurse(n-1, n+s)

recurse(3, 0)

#What is the output of the following program?
#recurse(3, 0) is called initially, and n is 3, and s is 0.
#In the first recursive call, recurse(2, 3) is called because n-1 is 2, and n+s is 3.
#In the second recursive call, recurse(1, 5) is called because n-1 is 1, and n+s is 5.
#In the third recursive call, recurse(0, 6) is called because n-1 is 0, and n+s is 6.
#When n becomes 0, the base case is reached, and the value of s (which is 6) is printed.

#What would happen if you called this function like this: recurse(-1, 0)?
# result will be: erro, that because if n = -1, Now, if you were to call recurse(-1, 0),
# you would encounter a problem. The function is not designed to handle negative values of n,
# and there is no base case for this situation. It would result in infinite recursion, leading to a "RecursionError:

#practice 4.5
def Sigma_fuction():
    start = int(input("The first term of number"))
    end   = int(input("The last term of number"))
    totalsum = 0
    totalsum = int(totalsum)

    for i in range(start, end + 1):
        term = i
        if (start > 0 or start == 0):
            totalsum += term #Equivalent to x = x + term
            print("Sum", totalsum)
        else:
            Sigma_fuction()
            #if start term of number is negative, rewrite input (Recuse Fuction)

Sigma_fuction()

#practice 4.6
def DvideTen_function():
    number = int(input("The number you want to calculate"))
    count = 0 # At least zero digit

    if (number >= 10):
       while number >= 10:
           number = number // 10 # make sure number is int
           count += 1 # We add 1 to this value for each time we divide it by 10.
           print("This number is", count,"digits")
    else:
        DvideTen_function() # if number < 10, using Recuse Fucntion

DvideTen_function()