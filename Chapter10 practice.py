#practice 10.1
def most_frequent(input_string):
    letter_frequency = {}

    for i in input_string:
        if i.isalpha(): # to check i is or not a letter. This one is for sentence when has punctuation mark,
            # if just check a singal word, u can delete it.
            i = i.lower() # to make sure evertime the letter is in lower
            letter_frequency[i] = letter_frequency.get(i, 0)
            letter_frequency[i] += 1    #if has key(i) then i + 1 and return key

    sorted_letters = sorted(letter_frequency.items(), key=lambda item: item[1], reverse=True)
    #.item method can shows key and value in dic which letter and frequency and sorted value(frequency) from big to small

    for letter, frequency in sorted_letters:
        print(f"{letter}: {frequency}")

input_text = "I write love write code"
#most_frequent(input_text)  #if you want to run please delete #

#practice 10.2

#10.2 a
def anagram():
    anagram_dict = {}
    fin = open("words.txt")

    for line in fin:
        word = line.strip()

        t = list(word)
        t.sort()
        t = tuple(t)

        if t not in anagram_dict:
            anagram_dict[t] = [word]
        else:
            anagram_dict[t].append(word)

    return anagram_dict

result = anagram()
#print(result)   #if you want to run please delete #

#10.2 b
def anagram1():
    anagram_dict = {}
    fin = open("words.txt")

    for line in fin:
        word = line.strip()
        t = list(word)
        t.sort()
        t = tuple(t)

        if t not in anagram_dict:
            anagram_dict[t] = [word]
        else:
            anagram_dict[t].append(word)

    sorted_tuples = list(anagram_dict.keys())

    sorted_tuples = sorted(sorted_tuples, key=len, reverse=True)
    # this one i learn from dictionary, sorted has two prameter which key and reverse
    #key can output the key for sorting, if key = len, this means I let the value include
    #tuple and become number in len first and sort them.
    #reverse is a boolean which we learned it before. If reverse is False then sorting will begin small to bigger
    #If reverse is True, sorting will begin form big to small

    for sorted_letters_tuple in sorted_tuples:
        anagrams = anagram_dict[sorted_letters_tuple]
        print(f"({', '.join(sorted_letters_tuple)}), ({', '.join(anagrams)})")
        # Join can help me to print more clearly which concatenate a list of strings into a string separated by commas and spaces

#anagram1() #if you want to run please delete #
# in this code, it sort the anagram. Because I know sort key in anagram first,I just want to try.
# So,you can as this code a example. Truly conrrect on is under this code.

def anagram2():
    anagram_dict = {}
    fin = open("words.txt")

    for line in fin:
        word = line.strip()
        t = list(word)
        t.sort()
        t = tuple(t)

        if t not in anagram_dict:
            anagram_dict[t] = [word]
        else:
            anagram_dict[t].append(word)

    sorted_tuples = sorted(anagram_dict.items(), key=lambda item: len(item[1]), reverse = False)
    #This one is different situation when you want to sort the value. Because the words is actually the value not the
    #key in anagram_dic. So anagram_dict.items() which can shows key and values at the same time as a list.
    #Key = lamba which is a function of key function, item:len(item[1]) is means item[1] is the value of the key,
    #len(item[1]) is the length of the value. When we just print the item[1], it will sometimes show a lot of words
    #are put together in list, what we should do is just to let them become number (their length) and then sorted them.

    for sorted_letters_tuple, sorted_anagrams in sorted_tuples: #because I use ".items()", there are key and value in sorted tuples
        print(f"({', '.join(sorted_letters_tuple)}), ({', '.join(sorted_anagrams)})")

#anagram2() #if you want to run please delete #
# in this def, it sort the length of words in each anagram. The reason why I write "reverse = False" is to make the code
#be more clear, if you try "reverse = True" the code just show you part from code because it too long. You can change it
#to True if you want, it denpends on you, but now I just keep False here.

#10.2 c

def anagram3_Bingo():
    anagram_dict = {}
    fin = open("words.txt")

    for line in fin:
        word = line.strip()
        t = list(word)
        t.sort()
        t = tuple(t)

        if t not in anagram_dict:
            anagram_dict[t] = [word]
        else:
            anagram_dict[t].append(word)

    sorted_tuples = sorted(anagram_dict.items(), key=lambda item: len(item[1]), reverse = False)

    for sorted_letters_tuple, sorted_anagrams in sorted_tuples:
        if len(sorted_anagrams) == 8:
            print(f"({', '.join(sorted_letters_tuple)}), ({', '.join(sorted_anagrams)})")

#anagram3_Bingo() #if you want to run please delete #

#practice 10.3
def metathesis_pair():
    anagram_dict = {}
    fin = open("words.txt")

    for line in fin:
        word = line.strip()
        t = list(word)
        t.sort()
        t = tuple(t)

        if t not in anagram_dict:
            anagram_dict[t] = [word]
        else:
            anagram_dict[t].append(word)

    sorted_tuples = list(anagram_dict.keys())

    for sorted_letters_tuple in sorted_tuples:
        anagrams = anagram_dict[sorted_letters_tuple]
        if len(anagrams) > 1: #to print the anagram with more words, these words is the metathesis_pair
            #the code is based on practice2 def anagram2.
            print(f"({', '.join(sorted_letters_tuple)}), ({', '.join(anagrams)})")

#metathesis_pair() #if you want to run please delete #

#practice 10.4

def remove_one_letter(word):
    fin = open("words.txt")

    removed_letters = []
    for i in range(len(word)):
        new_word = word[:i] + word[i + 1:]
        removed_letter = word[i]
        removed_letters.append(removed_letter)


        for line in fin:
            words = line.strip()
            if new_word in words:
                print(new_word)

    return removed_letters

def main():
    anagram_dict = {}
    word = str(input("Please input the word "))
    fin = open("words.txt")

    for line in fin:
        word = line.strip()
        t = list(word)
        t.sort()
        t = tuple(t)

        if t not in anagram_dict:
            anagram_dict[t] = [word]
        else:
            anagram_dict[t].append(word)

        removed_letters_list_child = list(remove_one_letter(word))

        sorted_tuples = list(anagram_dict.keys())

        for sorted_letters_tuple in sorted_tuples:
            for i in removed_letters_list_child:

                anagrams = anagram_dict[sorted_letters_tuple]

                if i == sorted_letters_tuple:
                    print(anagrams)
                else:
                    pass

#main()  #if you want to run please delete #