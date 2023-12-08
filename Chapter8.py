#8.1 A list is a sequence:

cheeses = ["Cheddar", "Edam", "Gouda"]

numbers = [42, 123]
empty = []

print(cheeses, numbers, empty)
#["Cheddar”, “Edam”, “Gouda”] [42, 123] []

#8.2 Lists are mutable:
print(cheeses[0]) # 0 is the first word of cheeses, "Cheddar"
print(cheeses[1]) # out put shold be "Edam"

numbers[1] = 5
# aim to change the second int of numbers 123 to change into 5
print(numbers)
#result will be [42,5]

print("Edam" in cheeses) #True
print("Brie" in cheeses) #False

#8.3 Traversing a list
for cheese in cheeses: #to print evey word in vertical line
    print(cheese)

for i in range(len(numbers)): # let the every int in numbers *2 in the loop
    numbers[i] *= 2

print(numbers)

for x in []:
    print("This never happens")


#practice:
List1 = [1,2,3,4,5,6]
List1.reverse() # to let the [1,2,3,4,5] become in [5,4,3,2,1]
print(List1)

#8.4 List operations and slices:

List2 = [1,2,3,4,5,6,7]
print(List2[::-1])

#8.5 List methods

t = ["a","b","c"]
t.append("d")
print(t)
# append

t1 = ["a","b","c"]
t2 = ["d","e"]
t1.extend(t2)
print(t1)
# extend

t4 = [3,8,6,1,2]
t4.sort()
print(t4)

t5 = [3,8,6,1,2]
t5.sort(reverse = True)
print(t4)


list1 = ["Hello","take"]
list2 = ["Dear", "Sir"]

print(list1[0],list2[0],list1[0],list2[1],list1[1],list2[0],list1[1],list2[1])

def make_sentece():
    List1 = ["Hello","take"]
    List2 = ["Dear", "Sir"]

    newlist = []

    for l in List1:
        for i in List2:
            temp = l + "" + i
            newlist.append(temp)

        print(newlist)

make_sentece()

list3 = [2,3,1,7,5]
list3.sort(reverse = True)
print(list3)



#8.6 Some more common functions for lists

t = [1,2,3]
print(sum(t))


#8.7 Deleting elements

t = ["a","b","c"]
x = t.pop(1)
#if chose 1, it dosen't print 1 (b)
#if chose 2, it dosen't print 2 (c)
print(t)
print(x)

t1 = ["a","b","c"]
del t1[1]   #delet "b"
#t1.remove("a")  #delet "a"
print(t1)

t2 = ["a", "b", "c", "d", "e", "f"]
del t2[2:4]
print(t2)

#8.8 Lists and strings

s = "spam"
t3 = list(s)
print(t3)
#result:["s","p","a","m"]

s = "Pining for the fjords"
t4 = s.split()
print(t4)
#result: ["pining","for","the","fjors"]

s = "spam-spam-spam"
delimiter = "-"
t5 = s.split(delimiter)
print(t5)
#result: spam-spam-spam

t6 = ["pining","for","the","fjords"]
delimiter = " "
s = delimiter.join(t6)
print(s)

#result: pining for the fjors

def reverse_list(li):
    reverselist = []
    for i in range(len(li)):
        reverselist.append(li(len(li)-i-1))
        return reverselist

def is_reverse(s1,s2):

    l1 = list(s1)
    l2 = list(s2)

    if l1 == l2[::-1]:
        return True
    else:
        return False

print(is_reverse("spam","maps"))


def make_sentece():
    List1 = ["Hello","take"]
    List2 = ["Dear", "Sir"]

    newlist = []

    for l in List1:
        for i in List2:
            temp = l + "" + i
            newlist.append(temp)

        print(newlist)

make_sentece()


#8.9 Modifying a list and creating a new list

def delet_head(t):
    del t[0]