def Library():
    books = {"Harry Potter": ["JK Rowling", 3], "Tom Sawyer": ["Mark Twain", 2],
             "The Tale of Two Cities": ["Charles Dickens", 5]}

    starts = input("Welcome to SCP library! What is the book you want to search for?")

    if starts in books:
        author = books[starts][0]
        num_books = books[starts][1]

        print("Author is", author)
        print("There are", num_books, "books in this library avaliable")

        next_step = input("Do you want to borrow a copy?")

        if next_step.lower() == "yes":
            print("You have borrowed", starts)
            books[starts][1] -= 1
            print("Updated Library:", books)
        elif next_step.lower() == "no":
            print("Thank u")

    elif starts not in books:
        index_step = input(starts + " does not exist in our library, would you like to add it?")

        if index_step.lower() == "yes":
            ask_step1 = input("Who is the author of this book?")
            ask_step2 = int(input("How many copies would you like to add?"))
            print("You have successfully added", starts, "to our library")
            books[starts] = [ask_step1, ask_step2]
            print(books)
        elif index_step.lower() == "no":
            print("Thank you")

Library()


def addbook():

    books = ("Harry potter")
    author = ("R,J")
    copies = ("2")


    b = books.split(",")
    a = author.split(",")
    c = copies.split(",")

    aclist = list(zip(a, c))

    aclist = []
    for i in aclist:
        aclist.append(list(i))

    for book, authorandnumber in zip(b, aclist):
        library[book] = authorandnumber

    print(library)

#addbook()





















