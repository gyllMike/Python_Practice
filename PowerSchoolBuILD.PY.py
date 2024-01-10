import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
#=======================================================================================================================
def move_buttom():
    button.place(x=50,y=50)

def hit_me_sign():
    messagebox.showinfo(title="tips", message="you are already in this page")

def hit_me_login():
    messagebox.showinfo(title="tips", message="System is still trying to contribute this page")

def find_pass():
    messagebox.showinfo(title="tips", message="Find your teacher to find your passward")

def if_else():
    entered_username = findentry.get()
    entered_password = findentry1.get()

    user_dict = {}  # Dictionary to store key-value pairs

    fin = open("words.txt")

    fin = open("studentsinfor.txt", "r")
    lines = fin.readlines()

    for i in range(0, len(lines), 2):
        # a loop for go through every even line from zero,
        # because two line are one group with username and password.
        key = lines[i].strip()
        # to gain the username line, strip can delete the space or shift between two strings, so that this key = lines[i] the i only can be username line, the odd line.
        value = lines[i + 1].strip()
        # as same as previous line, to gain the password name, but in this time is begin with key = line[i+1], then i only can be the password line, the even line.
        user_dict[key] = value
        # to let username be a key and password be a value in the dictionary

    print("if you want check members, please look at this line: ",user_dict)
    print("tip: you can add students information in the txt only, the system is just help students check whether they are in the system.")

    if entered_username in user_dict:
        # if enetered_usename which we input in the username entry is in dictionary,
        # then it will check whether your password of your username is correctly and is in the dictionary.
        messagebox.showinfo(title="tips", message="successful,you are already in the system")
    else:
        messagebox.showinfo(title="tips", message="Your user name or Password wrong, please try again")
#=======================================================================================================================
window = tk.Tk()
window.geometry("2000x900")
window.title("PowerSchool Sign in")

window.columnconfigure(0, weight=5)

topframe = ttk.Frame(window)
topframe.grid(column=1, row=0,padx=500, pady=0)
topframe.columnconfigure(0, weight=5)

Zleftframe = ttk.Frame(window)
Zleftframe.grid(column = 0,row = 0)
Zleftframe.columnconfigure(0,weight=2)

bottomframe = ttk.Frame(window)
bottomframe.grid(column = 1,row = 5)
bottomframe.columnconfigure(0,weight=5)

Zrightframe = ttk.Frame(window)
Zrightframe.grid(column = 0,row = 0)
Zrightframe.columnconfigure(0,weight =2)

style1 = ttk.Style()
style1.configure("My.TFrame",background = "blue")

middleframe = ttk.Frame(window)
middleframe.grid(column=1,row = 2,sticky=tk.W, padx=500, pady=1)
middleframe.columnconfigure(5,weight = 3)

style = ttk.Style()
style.configure("My.TFrame", background="white")

smallframe = ttk.Frame(window,style = "My.TFrame")
smallframe.grid(column=1,row=3,sticky=tk.W, padx=500, pady=0)
smallframe.columnconfigure(3,weight = 3)

namiframe = ttk.Frame(window,style = "My.TFrame")
namiframe.grid(column = 1,row = 4,sticky=tk.W, padx=500, pady=0)
namiframe.columnconfigure(3,weight = 3)

weimiframe=ttk.Frame(window)
weimiframe.grid(column = 1,row = 5,sticky = tk.W,padx = 500,pady = 0)
weimiframe.columnconfigure(3,weight = 3)
#=======================================================================================================================
canvas = tk.Canvas(topframe,width=955,height=100)
canvas.grid(column=1, row=0, sticky=tk.W, padx=115, pady=1)
sample_image = tk.PhotoImage(file='pictureofpowerschool.png')
canvas.create_image((105,55),image = sample_image)
#=======================================================================================================================
void = ttk.Label(Zleftframe)
void.grid(column=0, row=2, sticky=tk.W, padx=20, pady=20)

void = ttk.Label(bottomframe)
void.grid(column=0, row=2, sticky=tk.W, padx=20, pady=20)

void = ttk.Label(Zrightframe)
void.grid(column=0, row=2, sticky=tk.W, padx=20, pady=20)
#=======================================================================================================================
lable1 = tk.Label(middleframe,text= "PowerSchool SIS", bg="blue",fg="white",font=("Arial",11),width=50,height=2, anchor = "nw")
lable1.pack()

lable2 = tk.Label(middleframe, text = "Student and Parent Sign In", bg="white",fg="black",font=("Arial",13),width=50,height=3,anchor = "nw")
lable2.pack()

buttom1 = tk.Button(middleframe, text="Sign in", bg = "white",fg = "black", font=("Arial",8), width= 5,height=1,command=move_buttom and hit_me_sign)
buttom1.place(x = 10, y = 79)

buttom2 = tk.Button(middleframe, text="Creat Account", bg = "white",fg = "black", font=("Arial",8), width= 12,height=1,command=move_buttom and hit_me_login)
buttom2.place(x = 50, y = 79)
#=======================================================================================================================
findlabel = ttk.Label(smallframe, text='Select Language')
findlabel.grid(column=0, row=0, sticky=tk.W, padx=1, pady=5)

combo =ttk.Combobox(smallframe,state="readonly",values=["Madring", "English", "Japanese", "Franch"])
combo.grid(column=1, row=0, sticky=tk.W, padx=96, pady=1)

findlabel = ttk.Label(smallframe, text='Username')
findlabel.grid(column=0, row=2, sticky=tk.W, padx=1, pady=5)

findentry = ttk.Entry(smallframe, width=20)
findentry.grid(column=1, row=2, sticky=tk.W, padx=100, pady=5)

findlabel = ttk.Label(smallframe, text='Password')
findlabel.grid(column=0, row=3, sticky=tk.W, padx=1, pady=5)

findentry1 = ttk.Entry(smallframe, width=20,show='*')
findentry1.grid(column=1, row=3, sticky=tk.W, padx=100, pady=5)
#=======================================================================================================================
style = ttk.Style()
style.configure("Blue.TLabel", foreground="blue",font=("Arial", 8))

forgetlabel = ttk.Button(namiframe, text="Forgot Username or Password?", style="Blue.TLabel",command = find_pass)
forgetlabel.grid(column=1, row=3, padx=148, pady=35)

buttom3 = tk.Button(namiframe, text="Sign in", bg = "blue",fg = "white", font=("Arial",8), width= 5,height=1,command=move_buttom and if_else)
buttom3.place(x = 400, y = 55)
#=======================================================================================================================
kk = tk.Label(weimiframe,text="Copyright © 2005-2024 PowerSchool Group LLC and/or its affiliate(s). All rights reserved.",fg="black",font=("Arial",6),width=100,anchor = "nw")
kk.pack()

hh = tk.Label(weimiframe,text="All trademarks are either owned or licensed by PowerSchool Group LLC and/or its affiliates.",fg="black",font=("Arial",6),width=100,anchor = "nw")
hh.pack()

jj = tk.Label(weimiframe,text="Privacy Policy",fg="blue",font=("Arial",6),width=100,anchor = "nw")
jj.pack()
#=======================================================================================================================
window.mainloop()