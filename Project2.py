def print_Longword():

    fin = open("words.txt")

    for line in fin:
        word = line.strip()
        if len(word.replace(" ", "")) > 20:
            print(word)

#print_Longword()

def has_no_e():

    fin = open("words.txt")

    for line in fin:
        word = line.strip()

        if "e" not in word:
            print(word)
    fin = open("words.txt")

#has_no_e()

def uses_all():
    put_letters = input("Input the letters you want to search: ")
    fin = open("words.txt")

    for line in fin:
        word = line.strip()
        contains_all = True

        for letter in put_letters:
            if letter not in word:
                contains_all = False
                break

        if contains_all:
            print(word)

    fin.close()

#uses_all()

def is_abecedarian():
    fin = open("words.txt")

    for line in fin:
        word = line.strip()
        is_abecedarian_word = True

        for letter in range(len(word) - 1):
            if ord(word[letter]) > ord(word[letter + 1]):
                is_abecedarian_word = False
                break

        if is_abecedarian_word:
            print(word)

    fin.close()

#is_abecedarian()