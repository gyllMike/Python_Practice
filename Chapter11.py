import math

# 11.1Class (type)

class People:  # start with capital letter of class name

    """Represents a person on earth"""


personal1 = People()

personal1.name = "Mike"
personal1.age = 18
personal1.gender = "Male"
personal1.height = 1.8
personal1.job = "Computer Science"


class Tree():

    """"Represents a type of tree on earth"""


appleTree = Tree()

appleTree.size = 10

class Point:
    """Represents a point in 2-D space."""


print(Point)
blank = Point()
print(blank)

#11.2 Attributes 回归

blank.x = 3.0
blank.y = 4.0

print(blank.y)

x = blank.x #-- this is attributes
print(x)

distance = math.sqrt(blank.x**2 + blank.y**2)
# to calculate the 三角函数
print(distance)

def print_point(p):
     print(p.x, p.y)

print_point(blank) #blank become a object


p1  = Point()
p1.x = 5
p1.y = 1

def distance_between_poit(p1,p2):

    x_distance = (p1.x - blank.x)**2
    y_distance = (p1.y - blank.y)**2
    total_distance = math.sqrt(x_distance + y_distance)
    return total_distance

result = (distance_between_poit(p1,blank))
print(result)

# to calculate the distance between two coordinates

#11.4 Instances as return values

class Rectangle:
    """Represents a rectangel.
    attributes: width, height, corner. """

box = Rectangle()
box.width = 100.0
box.height = 200.0
box.bottomleftcorner = Point()
box.bottomleftcorner.x = 3.0
box.bottomleftcorner.y = 4.0

def find_center(rect):
    p = Point()
    p.x = rect.bottomleftcorner.x + rect.width/2
    p.y = rect.bottomleftcorner.y + rect.height/2
    return p

center = find_center(box)
print_point(center)

#11.5 Objects are mutable

box.width = box.width + 50
box.height = box.height + 100

def grow_rectangle(rect,dwidth,dheight):
    rect.width += dwidth
    rect.height += dheight

    print(box.width,box.height)


grow_rectangle(box,50,100)


class Point:
    """Represents a point in 2-D space."""

class Circle:
    """Represents a circle in 2-D space."""

mycircle = Circle()
mycircle.centerpoint = Point()

mycircle.radius = 75
mycircle.centerpoint.x = 150
mycircle.centerpoint.y = 100

mypoint = Point()
mypoint.x = 100
mypoint.y = 100

def distance_between_points(p1,p2):
    xdistance = p1.x - p2.x
    ydistance = p1.y - p2.y
    distance = math.sqrt(xdistance**2 + ydistance**2)
    print("The distance between the point and the "
          "center point of the circle is ",distance)
    return distance

def point_in_circle(p,c):
    distancetocenter = distance_between_points(p,c.centerpoint)
    print(distancetocenter)
    if distancetocenter <= 75:
        return True
    else:
        return False

print(point_in_circle(mypoint,mycircle))

#======================================================================================================================
#11.6 Classes and Functions 11.7 Pure functions

class Time:
    """Represents the time of day.
    attributes: hour, minute, second"""

def print_time(time):
    print(time.hour, ":", time.minute, ":", time.second)

def add_time(t1, t2):
    sum_time = Time()
    sum_time.hour = t1.hour + t2.hour
    sum_time.minute = t1.minute + t2.minute
    sum_time.second = t1.second + t2.second

    if sum_time.second >= 60:
        sum_time.second -= 60
        sum_time.minute += 1

    if sum_time.minute >= 60:
        sum_time.minute -= 60
        sum_time.hour += 1

    return sum_time

start = Time()
start.hour = 9
start.minute = 45
start.second = 0

duration = Time()
duration.hour = 1
duration.minute = 35
duration.second = 0

result = add_time(start, duration)
print_time(result)


def is_after_add():
    while True:
        time.second += 1

        if time.second >= 60:
            time.second = 0
            time.minute += 1

            if time.minute >= 60:
                time.minute = 0
                time.hour += 1

                if time.hour >= 12:
                    time.hour = 0

        print(f"{time.hour:02}:{time.minute:02}:{time.second:02}")

#is_after_add()

#11.8 Modifiers

def increment(time,seconds):

    while True:
        time.second += seconds
        if time.second >= 60:
            time.second -= 60
            time.minute += 1
        if time.minute >= 60:
            time.minute -= 60
            time.hour += 1

#increment()

#=======================================================================================================================
#11.9 Classes and Methods

class Time1:

    def print_time(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def int_to_time(slef,seconds):
        time = Time1()
        minutes, time.second = divmod(seconds, 60)
        time.hour, time.minute = divmod(minutes, 60)
        return time


e = Time1()
e.print_time(9,45,35)

seconds = e.time_to_int()
print(seconds)

new_time = e.int_to_time(seconds)
print(new_time.hour,new_time.minute,new_time.second)

#11.10 Two other examples

class Time2:

    def print_time(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def int_to_time(self, seconds):
        time = Time2()
        minutes, time.second = divmod(seconds, 60)
        time.hour, time.minute = divmod(minutes, 60)
        return time

    def increment(self, new_seconds):
        seconds = self.time_to_int()
        return_seconds = new_seconds + seconds
        new_time = self.int_to_time(return_seconds)
        return new_time

    def is_after(self, other):
        return self.time_to_int() > other.time_to_int()

e = Time2()
e.print_time(9, 45, 0)

seconds = e.increment(1337)
print(seconds.hour,":", seconds.minute,":",seconds.second)

print(seconds.is_after(e))

#11.11 The init method

class Time3:

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def print_time(self):
        print(self.hour, ":", self.minute, ":", self.second)

    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def int_to_time(self, seconds):
        time = Time3()
        minutes, time.second = divmod(seconds, 60)
        time.hour, time.minute = divmod(minutes, 60)
        return time

    def increment(self, new_seconds):
        seconds = self.time_to_int()
        return_seconds = new_seconds + seconds
        new_time = self.int_to_time(return_seconds)
        return new_time

    def is_after(self, other):
        return self.time_to_int() > other.time_to_int()

time = Time3(9,45)
time.print_time()