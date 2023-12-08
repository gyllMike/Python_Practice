#10.1 tuples are immutable

t = "a","b","c","d","e"
print(t)

#{ Curly Brackets
#[ Square Brackets
#( Round Brackets

t2 = ("a",)
print(t2)
print(type(t2))

t3 = tuple("lupins")
print(t3)

t4 = ("a","b","c","d","e")
print(t4[0])
print(t4[1:3])
t4 = ("A",) + t[1:5]
print(t4)

print((0,1,2) < (0,3,4))
print((0,1,2000000) < (0,3,4))
#第一个与第一个比较，如果相同则第二个与第二个进行比较
#如果第一个与第一个比较，前者比后者大，如果前者<后者 那么False

fruit_tuple = ("apple","banana","pear")
for i in fruit_tuple:
    print(i)
#printing out ordinary string, instead of tuple

fruit_list = list(fruit_tuple)

fruit_list[1] = "pineapple"
fruit_tuple = tuple(fruit_list)
print(fruit_tuple)
#Replacing onething to tuple

fruit_list = fruit_tuple[::-1]
fruit_tuple = tuple(fruit_list)
print(fruit_tuple)
#Reversing whole tuple list

fruit_list = list(fruit_tuple)
del fruit_list[0]
fruit_tuple = tuple(fruit_list)
print(fruit_tuple)
#Removing one item in tuple

#10.2 Tuple assighment

a = 5
b = 10
temp = a
a = b
b = temp
print(a)
print(b)

addr = "monty@python.org"
uname, domain = addr.split("@")

print(uname)
print(domain)

#10.3 Tuples as return values

q = divmod(7,3)
print(q)

#(2,1)
#2 is quotient(商); 1 is remainder(余)

q1 = divmod(100,3)
print(q1)
#result is a tuple, not int

tuple1 = (1,2,3,4,5,6,7,8,9)

def mian_max(t):
    return min(t), max(t)

print(mian_max(tuple1))
#to print biggist and lowest number in one tuple

def calcugrade():

    tuple2 = (8.7, 9.2, 7.5, 9.1, 10)

    a = min(tuple2)
    b = max(tuple2)

    tuple2_list = list(tuple2)
    tuple2_list.remove(a)
    tuple2_list.remove(b)

    tuple2 = tuple(tuple2_list)

    average = sum(tuple2) / len(tuple2)

    print(average)

calcugrade()

#10.4 Variable_length argument tuples

def printall(*args):
    print(args)

printall(1,2.0,"3")

print(max(1,2,3))
quist = (1,2,3)
print(sum(quist))

def dosum(a):
    return sum(a)

wind = (1,2,3,4,5,6)

print(dosum(wind))

#10.5 Lists and tuples

s = "abc"
t = [0,1,2]
for pair in zip(s,t): #zip method
    print(pair)
#represent a tuple

print(list(zip("Anna","Elk")))

td = [("a", 0), ("b", 1), ("c", 2)]

for letter, number in td:
    print(number, letter, end='\n')

def has_match(t1,t2):
    for x,y in zip(t1,t2):
        if x == y:
            return True
    return False

tuple1 = ("a","b","c")
tuple2 = ("b","y","z")

print(has_match(tuple1,tuple2))


for index, element in enumerate("abc"):
    print(index,element)


index = 0
for s in "abc":
    print(index,s)
    index += 1

#They are same to each other, but use enmurate will be easier for writing

#12.6 Ditionaries and tuples

d = {"a":0, "b":1, "c":2}
t = d.items()  #not list not dictionary not tuple but we have connection to tuple
print(t)

for key,value in d.items():
    print(key,value)

#change tuple to dictionary

t = [("a", 0), ("c",2), ("b", 1)]
d = dict(t)
print(d)

contacts = {("Smith", "John"): "111", ("Doe", "John"): "222", ("Luo", "Guanzhong"): "333"}


def find_contact():
    search = str(input("Please put the name you want to search: "))

    for key in contacts:
        key_list = list(key)

        if search in key_list:
            phone = contacts[key]
            print("Phone number:", phone)
            break
    else:
        print("Contact not found")

find_contact()










