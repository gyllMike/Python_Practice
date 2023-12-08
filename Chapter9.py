#9.1 A dictionary is a mapping
#Dictionary
eng2CN = dict()
eng2CN = {"one":"一",
          "two":"二","three":"三"}
print(eng2CN)

#"one" is a key after : "一“ is value
#"key" is a index in a list, but shows the words not int

print(len(eng2CN))

print("one" in eng2CN) #only works for key
print("zero" in eng2CN) # if not in dictionary of eng2CN, False

vales = eng2CN.values() #only works for value
print("一" in vales)
print("四" in vales) #if not in dictionary of eng2CN, Flase

#9.2 Dictionary as a collection of counters
def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1

    return d

t = "abcd"
result = histogram(t)
print(result)

#get
h = histogram("a")
print(h)

print(h.get("a",0))

print(h.get("b",0))

#9.3 looping and dictionaries

def print_hist(h):
    for c in h:
        print(c,h[c])

h = histogram("parrot")
print_hist(h)
# recording how many time does a letter appear in one word

def reverse_lookup(d,v):
    for k in d:
        if d[k] == v:
            return k

key = reverse_lookup(h,2)
print(key)

# searching which word has appeared twice in one word

#9.5 Dictionary and lists

def invert_dict(d):
    inverse = dict()
    #creating a dictionary first

    for key in d: #此时，d 便是inverse 中的键
        #这是一个循环，遍历字典“d“中的每一个键
        val = d[key]

        #这一行获取字典 d 中与当前键 key 关联的值，并将其赋给变量 val。

        if val not in inverse:
            # 检测 val 是否成为了inverse中的键，因为上一步是将val转换成inverse中的键
            inverse[val] = [key]
            # 如果val真的不在inverse中， 那么就在inverse中建一个新的值 val然后将 val 设为inverse 中的key

        else:
            inverse[val].append(key)
            #如果val已经在inverse中， 那么将当前的 key 添加到与 val 相关的现有列表中
            #这就是为什么我们可以看到两组分类的数据，因为上一个不在inverse中就创建了一个新的值，而此次已有的便在原先的去append
            #又因为我们将inverse的val 变成了key 此处进行了reverse 反转，所以在结果里我们可以看到数字是提前的
            #结果：{1 : [ ,  ,  ,  ,  ,], 2 : [ ,  ,  ,  ,  ,]
                #  key      value        key        value


    return inverse

print(invert_dict(h))

# distiguishing the two group of letters in one words which appeard once and twice

#9.6 Global variables

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("model", "Bronco")

print(x)
print(car)

x = car.setdefault("color", "white")

print(x)
print(car)

# setdefault can add a key and value in dictionary


def setdefault(d):

    inverse = dict()
    for key in d:
        inverse.setdefault(d[key],[]).append(key)
        print(inverse)
    return inverse


print(setdefault(h))

been_called = False

def example():
    global been_called
    been_called = True

example()


print(been_called)














