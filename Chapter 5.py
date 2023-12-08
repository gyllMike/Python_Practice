import math
# return values

def area(radius):
   a = math.pi * radius**2
   return a

print(area(2))

def distance(x1,x2,y1,y2):
   print(math.sqrt(math.pow(x2-x1,2)+math.pow(y2-y1,2)))

distance(3,4,5,6)

# To calculate the area of trapezoid function
def Trapezoid_function(x1,y1,x2,y2,x3,y3,x4,y4):
   top = 0
   top = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
   bottom = math.sqrt(math.pow(x4-x3,2)+math.pow(y4-y3,2))
   height = y3-y1
   sum = top +buttom
   answer = sum * h

Trapezoid_function(3,6,6,6,1,1,8,1)

# To calculate the area of cricle
def circle_function(x1,y1,x2,y2):
   a = x2-x1
   b = y2-y1
   C = a**2 + b**2
   d = math.sqrt(C)
   r = d
   circle_function = marh.pi*r**2

circle_function(2,3,4,5)

def is_divisible(x, y):
    if x % y == 0:
        return True
    else:
        return False

x = int(input())
y = int(input())

if is_divisible(x, y) == True:
    print("Yes,", x, "is divisible by", y)
else:
    print("No,", x, "is not divisible by", y)

#Practice inclass

def sum_digits():

    number = int(input("first number"))
    divided = 10

    remainder = number % divided
    answer = number // divided

    if number < 1000:
         tence = answer // 10
         ones = answer % 10
         sum = tence + ones + remainder
    else:
        hundreds = answer // 100
        tence = (answer // 10) % 10
        ones = answer % 10
        sum = hundreds + tence + ones + remainder

    print(sum)

sum_digits()

# improve
def sumdigits(a):
    digit_sum = 0

    while a > 0:
        last_digit = a % 10
        digit_sum += last_digit

        a //= 10
    return digit_sum

print(sumdigits(12345))



def printtimes():
    x  = 10
    while x > 0:
        print("hellow")

        x -= 1 # x = x-1

printtimes()