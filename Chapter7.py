fruit = "banana" #0,1,2,3,4......
letter = fruit[1]
print(letter)


print(len(fruit)) # return how many letter

length = len(fruit)
last = fruit[length-1]
print(last)


index = 0
while index < len(fruit):
     letter = fruit[index]
     print(letter)
     index = index + 1


prefixes = str("JKLMNOPQ")
suffix = str("acke")

for letter in prefixes:
     if letter == "O" or "Q":
          print(letter + "U" + suffix)
     else:
          print(letter+suffix)

s= "Monty Python"

print(s[0:5])
print(s[6:2])
#subString
i = 0
s= str("ABCDEFG")

while len(s) > 4:
     print(s[2:4])
     s = s[4:len(s)]

#search:

def find(word, letter,startingindex):

     index = startingindex
     while index < len(word):
         if word[index] == letter:
             return index

         index = index + 1
     return -1

print(find("ABCDEFG","A",0)) #Find the order of word

#UPPER WORD

word = str("banana")
new_word = word.upper()
print(new_word)

index = word.find("a") #word = str("banana")
print(index)

#The in operator


print("a" in "banana")
print("seed" in "banana")


def in_both(word1, word2):    #find same letter in two words

     for letter in word1 and word2:

         word1 = word1[1:len(word1)]
         word2 = word2[1:len(word2)]

         print(word1,word2)
         break


in_both("Python","Java")

for i in range(10):
    i = "hello"
    print(i)




















