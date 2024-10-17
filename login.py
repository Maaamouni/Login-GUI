from tkinter import *

login = Tk()
login.title("Login Form")
login.geometry("500x400")
login.resizable(False, False)
login['bg'] = '#333333'

def login_info():
    X = name.get()
    Y = passwd.get()
    print(X)
    print(Y)


lb1 = Label(login, text="Login", font="araial 20", bg="#333333",fg="green")
lb1.place( x = 225, y = 50)

lb2 = Label(login, text="Username", bg="#333333", fg="white",font="georgia 13")
lb2.place( x = 130 , y = 115)

name = StringVar()

user_in = Entry(login, textvariable=name,width=30)
user_in.place( x = 240 , y = 120)

lb3 = Label(login, text="Password", bg="#333333",  fg="white",font="georgia 13")
lb3.place( x = 130 , y = 155)

passwd = StringVar()
pass_in = Entry(login, textvariable=passwd, width=30,show="*")
pass_in.place( x = 240 , y = 160)

login_b = Button(login, text="Login", bg="green", width=10,fg="white", command=login_info)
login_b.place(x = 220, y = 240)

login.mainloop()
