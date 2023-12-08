#practice 7.1

def find_word():
    word = str(input("input ur word:"))
    new_letter = str(input("input letter in your word:"))
    count = 0


    for letter in word:

        if letter == new_letter:
            count += 1


    print(count)

find_word()

#practice 7.2

def find1_word():
    word = "worry"
    new_letter = "r"
    count = 0

    for letter in word:

        if letter == new_letter:
            count += 1
        else:
            continue

    print(count)


find1_word()

#practice 7.3

def is_palindrome(word):

    if word == word[::-1]:
        return True
    else:
        return False

#practice 7.4

def any_lowercase1(s):
     for c in s:
         if c.islower():
             return True
         else:
             return False
#The any_lowercase1 function takes a string s as a parameter and iterates through each character c in the string.
# Within each iteration, it checks if the character c is lowercase using the condition c.islower().

#However, there's a significant issue in this function. The return statements are inside the loop,
# and they are executed during the first iteration.
# This means that the function will return True if the first character of the string is lowercase and False otherwise.
# The loop doesn't have a chance to check the rest of the characters in the string.

#In other words, this function checks only the case of the first character in the string and returns True if it's lowercase;
# otherwise, it returns False. This behavior is not what you would expect for a function designed to check if any character in the string is lowercase.

def any_lowercase2(s):
     for c in s:
         if 'c'.islower():
             return 'True'
         else:
             return 'False'
#The any_lowercase2 function takes a string s as a parameter and iterates through each character c in the string.
# Within each iteration, it checks if the string 'c' (literal letter "c") is lowercase using the condition 'c'.islower().
# However, this condition always evaluates to True because the character 'c' is lowercase.
#Since the condition is always True, the function immediately returns the string 'True' within the first iteration of the loop.
# This means that the function will return 'True' regardless of the actual contents of the string s.
# The loop doesn't consider the actual characters in the string;
# it only checks if the literal letter 'c' is lowercase, which is not the intended behavior.

def any_lowercase3(s):
     for c in s:
         flag = c.islower()
     return flag
#the function any_lowercase3 checks if the last character in the string is a lowercase letter and returns True if it is,
# and False otherwise.

def any_lowercase4(s):
     flag = False
     for c in s:
         flag = flag or c.islower()
     return flag
#The any_lowercase4 function takes a string s as a parameter and initializes a boolean variable flag to False.
# It then iterates through each character c in the string s. During each iteration, it updates the flag by performing a
# logical OR (flag or c.islower()). The c.islower() checks if the current character is a lowercase letter.
#The purpose of the function is to determine whether there is at least one lowercase letter in the given string.
# If any of the characters in the string is a lowercase letter, the flag becomes True. The final result (flag) indicates
# whether the string contains at least one lowercase letter.


def any_lowercase5(s):
     for c in s:
         if not c.islower():
             return False
     return True
#The any_lowercase5 function takes a string s as a parameter and iterates through each character c in the string.
# Within each iteration, it checks if the character is not a lowercase letter using the condition not c.islower().
# If it finds any character that is not a lowercase letter, the function immediately returns False,
# indicating that there is at least one non-lowercase letter in the string.
#If the function iterates through the entire string without finding any non-lowercase letters, it returns True,
# indicating that all characters in the string are lowercase letters.


#practice 7.5

def rotate_word():

    rotated_word = str(input("input word"))
    rotated_result = ""

    for letter in rotated_word:

        if letter.isupper():
            rotated_letter = chr(ord(letter)+32+1)
            # I find a regular rule is that when one specifec letter is upper, ord(letter)+32 will be it's lower.
            #To give an example of letter"W", it is at 87, 87+32 = 119, "w" is at 119.
            rotated_result += rotated_letter

        elif letter.islower():
            rotated_letter = chr(ord(letter) + 1)
            rotated_result += rotated_letter


    print(rotated_result)


#rotate_word()

def rotate_word():
    rotated_word = str(input("Input word: "))
    rotated_amount = int(input("input amound: "))
    rotated_result = ""

    fin = open("words.txt")


    for letter in rotated_word:
        if letter.isupper():
            rotated_letter = chr((ord(letter) - ord('A') + rotated_amount) % 26 + ord('A'))
            rotated_result += rotated_letter
        elif letter.islower():
            rotated_letter = chr((ord(letter) - ord('a') + rotated_amount) % 26 + ord('a'))
            rotated_result += rotated_letter
        else:
            rotated_result += letter  # If the character is not a letter, keep it unchanged
    print(rotated_result)

rotate_word()