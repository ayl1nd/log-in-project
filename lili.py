from tkinter import *
from tkinter import messagebox

win =Tk()
win.geometry('650x300')
win.title('login page')
win.config(bg= 'white')

def sing_in():
    messagebox.showinfo(title = 'fact',massege=('login aylin'))

left_frame = Frame(win, bg='white' , highlightthickness=1, highlightbackground='black', padx= 20 , pady=20)
left_frame.grid(column=0 , row=0 , pady='50' , padx='50')

right_frame= Frame(win)
right_frame.grid(column=1 , row=0 , pady='50' , padx='50')

lbl_username= Label(left_frame, text= 'username', bg='white')
lbl_username.grid(column=0, row=0, pady=10)

ent_username= Entry(left_frame)
ent_username.grid(column= 1 , row=0, padx=20)

lbl_password=Label(left_frame, text='password' , bg='white')
lbl_password.grid(column=0, row=1, pady=10)

ent_password=Entry(left_frame)
ent_password.grid(column=1, row=1, pady=20)

selected_value= IntVar()

Radiobutton(left_frame, text="male" , variable= selected_value, value= 1).grid(column=0 , row=2) 
Radiobutton(left_frame, text="female" , variable= selected_value , value= 2).grid(column=1 , row=2)

selected_value.set(0)

btn_sign= Button(left_frame , text="sign in", bg="blue" , fg="white" , width= 25, command=sing_in)
btn_sign.grid(column=0 , columnspan=2 , row=3 , pady=5 , padx= 10)

win.mainloop()
