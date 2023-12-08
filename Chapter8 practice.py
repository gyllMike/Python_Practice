#practice8.1
def nested_sum(list_of_lists):
    total_sum = 0

    for inner_list in list_of_lists:
        total_sum += sum(inner_list)

    return total_sum

t = [[1, 2], [3], [4, 5, 6]]
result = nested_sum(t)
print(result)

#practice8.2
def cumsum(lst):
    cumulative_sum = 0
    result = []

    for num in lst:
        cumulative_sum += num
        result.append(cumulative_sum)

    return result

t = [1, 2, 3]
result = cumsum(t)
print(result)

#practice8.3
def take_middle(list):
    return list[1:-1]

s = [1,2,3,4]
result = take_middle(s)
print(result)

#practice8.4
def chop(list):
    return list[1:-1]

t = [1,2,3,4]
result = chop(t)
print(result)

#practice8.5
def is_sorted(list):
    return list == sorted(list)

r = [1,2,2]
result = is_sorted(r)
print(result)
r1 = ["b","a"]
result1 = is_sorted(r1)
print(result1)

#practice8.6
def is_anagram(list, new_list):

    sorted_list = sorted(list)
    sorted_new_list = sorted(new_list)

    if sorted_list == sorted_new_list:
        return True
    else:
        return False

p = ["abc"]
e = ["abc"]
result = is_anagram(p, e)

print(result)

#pratice8.7
def has_duplicates(ori_list):

    for i in range(len(ori_list)):
        for j in range(i + 1, len(ori_list)):

            if ori_list[i] == ori_list[j]:
                return True
            else:
                return False


s = ["a", "c", "b"]
result = has_duplicates(s)
print(result)

#practice8.8
def append_txt():

    fin = open("words.txt")

    for line in fin:
        word = line.strip()
        word = list(word)
        word.append("abcdefg")
        print(word)

#append_txt    #(if you want to run please delete #)

def add_txt():

    fin = open("words.txt")

    for line in fin:
        word = line.strip()
        word = list(word)
        word = word + ["abcdefg"]
        print(word)

#add_txt  #(if you want to run please delete #)

#In general, the version using the append method is expected to be more efficient. The reason is that the append method
# modifies the list in-place, while the idiom t = t + [x] creates a new list every time it's used. Creating a new list
# involves copying all the elements from the old list to the new one,
# which can be less efficient, especially as the list grows.

#practice8.9
def in_bisect(target, filename="words.txt"):
    with open(filename, 'r') as file:
        word_list = file.read().splitlines()
        #file.read().splitlines() is a sequence of operations that
        # reads the contents of a file, splits it into lines, and creates a list where
        # each element corresponds to a line from the file.

    low = 0
    high = len(word_list) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = word_list[mid]

        if mid_value == target:
            return True
        elif mid_value < target:
            low = mid + 1
        else:
            high = mid - 1

    return False

target_word = input("Enter the word to search: ")

if in_bisect(target_word):
    print(f"{target_word} is in the list.")
else:
    print(f"{target_word} is not in the list.")

#practice8.10
def reverse_pair(word1,word2):

    word_reverse = word1[::-1]

    if word2 == word_reverse:
        print("They are")
    else:
        print("They are not")

a = "was"
b = "saw"
result = reverse_pair(a,b)
print(result)

#practice8.11

def interlock():
    fin = open("words.txt")

    inter_word = []

    for line in fin:
        word = line.strip()

        word_list = list(word)
        print(word_list)

        inter_word.extend(word_list)

        if inter_word == list(word):
            print(inter_word)
        else:
            pass

    fin.close()

interlock()    #(if you want to run please delete #)