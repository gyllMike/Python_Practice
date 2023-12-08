#practice9.1

def word_dictionary():
    check_word = input("What word do you want to search for?")

    fin = open("words.txt")

    word_dict = {}

    for line in fin:
        word = line.strip()
        word_dict[word] = None

    print(check_word in word_dict)

#word_dictionary()

#practice9.2

def find_min_key():
    number = {"Five": 5, "Two": 2, "Nine": 9}
    values = list(number.values())

    if not values:
        return None

    min_value = min(values)

    for key, value in number.items():
        if value == min_value:
            return key


result = find_min_key()
print(result)

#practice 9.3

def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1

    return d

h = histogram("parrot")

def setdefault(d):

    inverse = dict()
    for key in d:
        inverse.setdefault(d[key],[]).append(key)

    return inverse


print(setdefault(h))

#practice 9.4

def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

def has_duplicates(d):
    for key in d:
        if d[key] > 1:
            return True
    return False

input_word = str(input("Input the word you want to play with duplicates: "))
h = histogram(input_word)

result = has_duplicates(h)
print(result)


#practice 9.5

def rotate_word():

    rotated_amount = int(input("input amound: "))
    rotated_result = ""

    fin = open("words.txt")


    for line in fin:
        word = line.strip()

        for letter in word:
            if letter.isupper():
                rotated_letter = chr((ord(letter) - ord('A') + rotated_amount) % 26 + ord('A'))
                # the rotation is done modulo 26 to ensure that the result stays within the bounds of the alphabet.
                rotated_result += rotated_letter
            elif letter.islower():
                rotated_letter = chr((ord(letter) - ord('a') + rotated_amount) % 26 + ord('a'))
                rotated_result += rotated_letter
            else:
                rotated_result += letter  # If the character is not a letter, keep it unchanged


        if rotated_result in word:
            return True
        return False


#rotate_word()

#practice 9.6

def main():
    balance = 0
    amount = 0

    while True:
        operation = input(
            "What would you like to do?\n"
            " d) deposit  "
            " w) withdraw  "
            " b) balance  "
            " q) quit\n"
            "> "
        )
        if operation in "dD":
            amount = float(input("Enter the deposit amount: "))

            balance += amount
            print(f"Successful deposit: +${amount:,.2f}")
            print(f"Your balance now is: +${balance:,.2f}")

        if operation in "wW":

            if amount > 0:
                amount1 = float(input("Enter the withdraw amount: "))
                balance -= amount1
                print(f"Successful withdraw: -${amount1:,.2f}")
            else:
                print("Not enough funds for this transaction")

            print(balance)

        elif operation in "bB":
            print(balance)
        elif operation in "qQ":
            print("Goodbye")
            break

main()