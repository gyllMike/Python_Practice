#Practice 5.1
def b(z):
     prod = a(z, z)
     print(z, prod)
     return prod

def a(x, y):
     x = x + 1
     return x * y

def c(x, y, z):
     total = x + y + z
     square = b(total)**2
     return square

x = 1
y = x + 1
print(c(x, y+3, x+y))

# What does the program print? Why? Write down the calculation process step by step.
#first, we know x = 1 and y = x+1

#1.c(x, y+3, x+y):
#x is 1.
#y + 3 is 2 + 3, which is 5.
#x + y is 1 + 2, which is 3.
#total is the sum of these values, which is 1 + 5 + 3, resulting in total being 9.
#square = b(total)**2: Calls the function b(total) with total (9) as an argument.
#from this we can know z = 9

#2.b(z):
#z is 9.
#Calls a(9, 9), which returns 9 * 10, resulting in prod being 90.
#Prints z and prod, so it prints 9 90.
#Returns prod, which is 90, to the caller (c function).

#3.square = b(total)**2: square is set to 90**2, which is 8100.

#4.print(c(x, y+3, x+y)): Calls the function c(x, y+3, x+y):
#x is 1.
#y+3 is 5.
#x+y is 3.
#c(1, 5, 3) is called.

#5.c(x, y+3, x+y):
#x is 1.
#y + 3 is 5.
#x + y is 3.
#total is the sum of these values, which is 1 + 5 + 3, resulting in total being 9.
#square = b(total)**2 is called.
#
#b(z) (inside c):

#6.because of z is 9. As same as second step
#Calls a(9, 9), which returns 9 * 10, resulting in prod being 90.
#Prints z and prod, so it prints 9 90.
#Returns prod, which is 81, to the caller (c function).
#
#7.square = b(total)**2 (inside c): square is set to 90**2, which is 8100.
#
#8.so final answer will be 9 90
#                          8100

#Practice 5.2
def Ackermann_Function(m,n):

    if (m == 0):
        return n+1
    elif (m>0 and n == 0):
        return Ackermann_Function(m-1,1)
    elif (m>0 and n>0):
        return Ackermann_Function(m-1,Ackermann_Function(m,n-1))

result = Ackermann_Function(3, 4)
print(result)

#practice 5.3
def first(word):
     return word[0]

def last(word):
     return word[-1]

def middle(word):
     return word[1:-1]

#1.When you call the middle function with a string:

#if the string has two letters, such as "ab," calling middle("ab") will return an empty string, ""
# because it slices the string from the second character (index 1) to the second-to-last character (index -1),
# leaving no characters in between.

#2.Write a function called is_palindrome that takes a string argument and returns True if it is a palindrome and False
# otherwise.
#Remember that you can use the built-in function len to check the length of a string.

def is_palindrome(word):

    if word == word[::-1]:
        # word[::-1] will give the reverse of the string word I find it on python dictionary
        return True
    else:
        return False

print("is_palindrome:noon",is_palindrome("noon"))
print("is_palindrome:booooooob", is_palindrome("boooooquqooooob"))
print("is_palindrome:bpoiuytrewqb", is_palindrome("bpoiuytrewqb"))

#practice 5.4
def is_power(a,b):

    if a == 1:
        return True
    elif a % b == 0 and is_power(a / b, b):
        return True
    else:
        return False

result = is_power(16,2)
print(result)

#practice 5.5
def GCD(a,b):
    if b == 0:
        return a
        #When b is equal to 0, we return a because this is a base case of the greatest common divisor (GCD) calculation
    else:
        r = a % b
        return GCD(b,r)

result1 = GCD(48,18)
print("GCD:",result1)

#Teacher, i wanna try to make the a an d b in GCD be something can input number, How shold I do. I try a lot of times,
#def GCD():
#    a = int(input())
#    b = int(input())
#    GCD() = GCD(a,b)
#It is wrong, but i just want to give value for a and b first, and then put them in GAB()