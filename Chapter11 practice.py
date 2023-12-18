import math
import datetime

#practice 11.1
class Point:
    """Represents a point in 2-D space."""

    def __init__(self, x,y):
        self.x = x
        self.y = y

class Rectangle:
    """Represents a point in 2-D space."""

    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.x4 = x4
        self.y4 = y4

class ExtralCircla:
    """Represents a point in 2-D space."""

    def __init__(self, radius, center_point_x, center_point_y):
        self.radius = radius
        self.center_point_x = center_point_x
        self.center_point_y = center_point_y

class Circle:
    """Represents a circle in 2-D space."""

    def __init__(self, radius=75, center_point_x=150, center_point_y=100):
        self.radius = radius
        self.center_point_x = center_point_x
        self.center_point_y = center_point_y

    def distance_between_points(self, p1, p2):
        x_distance = p1.x - p2.x
        y_distance = p1.y - p2.y
        distance = math.sqrt(x_distance ** 2 + y_distance ** 2)
        return distance

    def point_in_circle(self, x, y):
        distance_to_center = math.sqrt((self.center_point_x - x) ** 2 + (self.center_point_y - y) ** 2)

        if distance_to_center <= self.radius:
            print("This point is inside the circle.")
        else:
            print("This point is outside the circle.")

    def rect_in_circle(self, q):
        distances = [
            self.distance_between_points(Point(q.x1, q.y1), Point(self.center_point_x, self.center_point_y)),
            self.distance_between_points(Point(q.x2, q.y2), Point(self.center_point_x, self.center_point_y)),
            self.distance_between_points(Point(q.x3, q.y3), Point(self.center_point_x, self.center_point_y)),
            self.distance_between_points(Point(q.x4, q.y4), Point(self.center_point_x, self.center_point_y)),
        ]

        if any(distance > self.radius for distance in distances):

            # i check this on web, any() can write as this way to check any of number of distances in distance is bigger
            # than radius of circle or smaller than radius of circle. can use for loop in any()method, but i need to
            #creat a list of distances first and then I can check each item of distance number in ditances.

            print("The rectangle is outside the circle.")
        else:
            print("The rectangle is inside the circle.")

    def rect_circle_overlap(self,p,q):

        distance_between_centers = math.sqrt((self.center_point_x - p.center_point_x) ** 2 + (self.center_point_y - p.center_point_y) ** 2)

        distances = [
            self.distance_between_points(Point(q.x1, q.y1), Point(self.center_point_x, self.center_point_y)),
            self.distance_between_points(Point(q.x2, q.y2), Point(self.center_point_x, self.center_point_y)),
            self.distance_between_points(Point(q.x3, q.y3), Point(self.center_point_x, self.center_point_y)),
            self.distance_between_points(Point(q.x4, q.y4), Point(self.center_point_x, self.center_point_y)),
        ]

        if distance_between_centers <= self.radius and any(distance < self.radius for distance in distances):
            print("This cirlce and retangle is inside the circle.")
        else:
            print("This cirlce and rerangle is outside the circle.")
#=======================================================================================================================
#a
circle1 = Circle()
circle1.point_in_circle(150,100)

#b
rectangle = Rectangle(130, 120, 130, 110, 150, 120, 150, 110)
circle2 = Circle()
circle2.rect_in_circle(rectangle)

#c
rectangle = Rectangle(130, 120, 130, 110, 150, 120, 150, 110)
circle = ExtralCircla(75,150,100)
circle3 = Circle()
circle3.rect_circle_overlap(circle,rectangle)
#=======================================================================================================================

#practice 11.2
class Distance:

    def __init__(self,o):
        self.o = o

class Time:

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

    def Calculate_Velocity(self,new_seconds):
        seconds = self.time_to_int()
        return_seconds = new_seconds - seconds
        e = Distance(1500) # U can change distance if you want, this one is just a example
        v = e.o / return_seconds
        return v

initial_time1 = Time(9, 45, 15)
final_time1 = Time(9, 50, 30)
velocity1 = initial_time1.Calculate_Velocity(final_time1.time_to_int())
print("Velocity 1:", velocity1)

initial_time2 = Time(9, 45, 15)
final_time2 = Time(9, 57, 18)
velocity2 = initial_time2.Calculate_Velocity(final_time2.time_to_int())
print("Velocity 2:", velocity2)

#practice 11.3

#a
current_date = datetime.datetime.now()
print(current_date)

#b
class Date:

    def __init__(self, year=0, month=0, day=0):
        self.year = year
        self.month = month
        self.day = day

    def print_date(self):
        print(self.year, ":", self.month, ":", self.day)

    def date_to_int(self):
        months = self.year * 12 + self.month
        days = months * 30 + self.day
        return days

    def int_to_date(self):
        date = Date()
        months, date.day = divmod(days,30)
        date.year,date.month = divmod(months,12)
        return date

    def rest_of_day(self,new_date):
        days = self.date_to_int()
        return_days = new_date - days
        return return_days

    def double_day(self,a,b):
        age1 = m
        age2 = n

e = Date(2023, 12, 18)
f = Date(2024, 4, 12)
rest_days = e.rest_of_day(f.date_to_int())

print("Remaining days:", rest_days)

#c
from datetime import datetime, timedelta

def calculate_double_day(birthday1, birthday2):
    birthdate1 = datetime.strptime(birthday1, "%Y-%m-%d")
    birthdate2 = datetime.strptime(birthday2, "%Y-%m-%d")

    age1 = (datetime.now() - birthdate1).days
    age2 = (datetime.now() - birthdate2).days

    double_day = abs(age1 - age2)
    double_day_date = datetime.now() - timedelta(days=double_day)

    return double_day_date.strftime("%Y-%m-%d")

birthday_person1 = "2006-04-12"
birthday_person2 = "2001-11-11"

double_day = calculate_double_day(birthday_person1, birthday_person2)
print(f"The Double Day is: {double_day}")

# I learn from https://docs.python.org/3/library/datetime.html


