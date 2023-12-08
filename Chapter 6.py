#calcu skill
x = 0
x = x-1
x -= 1

#loop

def printtimes():
    x = 10
    while x > 0:
        print("hellow")

        x -= 1  # x = x-1

printtimes()

def printimes():
    for i in range(10):
        print("hellow")

printimes()

def countdown(n):
     while n > 0:
         print("Blastoff")
         n -= 1

countdown(10)

def sequence(n):
     while n != 1:
         print(n)
         if n % 2 == 0: # n is even
             n = n / 2
         else: # n is odd
             n = n*3 + 1

sequence(10)

def printnumber():

    r = int(input())
    while r < 4:
        print(r)
        r += 1
    print("time is up")

printnumber()

def is_square():
    a = float(input("Enter a number: "))  # Use float instead of int for decimal values
    x = a  # Initialize x with the input value

    while True:
        y = (x + a / x) / 2

        if abs(y - x) < 0.0001:  # Check if the difference is very small (close enough)
            break
        else:
            x = y  # Update x with the new approximation

    return x  # Return the square root approximation

result = is_square()
print("The square root is approximately",result)

import math

def mysqrt(x):
    guess = x / 2.0
    epsilon = 1e-16

    while True:
        y = (guess + x / guess) / 2.0
        if abs(y - guess) < epsilon:
            break
        guess = y

    return y

def test_square_root():
    print("a\tmysqrt(a)\tdiff")
    print("-\t--------\t----")

    for a in range(1, 10):
        mysqrt_a = mysqrt(float(a))
        math_sqrt_a = math.sqrt(float(a))
        diff = abs(mysqrt_a - math_sqrt_a)

        print(f"{a}\t{mysqrt_a:.11f}\t{diff:.11f}")

test_square_root()


