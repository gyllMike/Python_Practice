import math
import random

#practice 6.1
def mysqrt():# sqrt in formula
    x = 0.0
    plus1 = 1.0
    a = 0.0
    y = 0.0
    result = [] #I wanna stroge my value in this function, so I search dictionary find this.

    while True:
        if x < 9.0 and a <9.0:
          a += 1
          x = a - x
          y = round((x + a / x) / 2,2) #Keep two decimal places, but it will let calculation be less accurate
          result.append(y) #to make sure it will not shows the process of during the running program
        else:
            break

    return result #return the result I have storged

def math_squrt():
    number = 0.0
    result = []
    while True:

        if number < 9.0:
            number += 1
            sqrt_result = math.sqrt(number)
            rounded_result = round(sqrt_result, 2)
            result.append(rounded_result)
        else:
            break

    return result

def make_table():
    print("a", "mysqrt(a)", "math.sqrt(a)", "diff")
    print("_", "_________", "_________", "_____")

    mysqrt_values = mysqrt()
    mathsqrt_values = math_squrt()

    for a, q, c in zip(range(1, 10), mysqrt_values, mathsqrt_values):

        # zip(range(x,y)c,d) I search in dictionary, it actually can let two things shows together
        #For example: list = [1,2,3]
        #             list2 = [a,b,c]
        #             result = zip(list1,list2)
        # final result will be: [(1,a) (2,b),(3,c)]

        diff_val = round(q - c , 2)
        print(a,"  ", q, "     ",c, "    ",diff_val)

make_table()

#practice 6.2
def eval_loop():

    result = 0

    while True:
        user_input = input('Enter a Python expression (or "done" to exit): ')

        if user_input == 'done':
            break
        else:
            result = eval(user_input)
            # return the value of the last expression it evaluated.
            print(result)

    return result

# Test the function
last_result = eval_loop()
print("the last result is",last_result)

#practice 6.3

import math

def estimate_pi():
    k = 0
    total = 0
    factor = 2 * math.sqrt(2) / 9801

    while True:
        num = math.factorial(4 * k) * (1103 + 26390 * k)
        #math.factorial in dictionary, it says that it calculates the factorial of a non-negative integer
        den = math.factorial(k) ** 4 * 396 ** (4 * k)
        term = factor * num / den
        total += term

        if abs(term) < 1e-15:
        # absolute value
            break

        k += 1

    return 1 / total

# Test the function and compare with math.pi
pi_estimate = estimate_pi()
print("Estimated Pi:", pi_estimate)
print("Actual Pi   :", math.pi)

#practice6.4

def is_divisiable():

    number1 = 5
    number2 = 7

    x = int(input("input the begin number"))
    y = int(input("inout the last number"))

    for find in range(x,y):
        if find % 5 == 0 and find % 7 ==0:
            print("The final answer would be",find)
        else:
            pass

is_divisiable()

#practice 6.5
def guess_number():

    guessnumber = int(input("please input your guess number between 1-100:"))

    if guessnumber > 100:
        print("your number ought to be between 1-100")
        guess_number()

    number = random.randint(1,100)

    while True:

        if guessnumber > number:
            print("so hight,the actual number is lower than yours")
        elif guessnumber < number:
            print("so low,the actual number is higher than your")
        elif guessnumber == number:
            print("FINAL NUMBER IS",number,"YOU WIN, WELL DONE!!!")
            break

        guessnumber = int(input("Please input your guess number: "))

guess_number()