from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry (root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3,padx=10,pady=20)

def button_click(number):
   #e.delete(0,END)
   current = e.get()
   e.delete(0, END)
   e.insert(0,str(current) + str(number))
def button_clear():
   e.delete(0, END)
def button_add():
   first_number = e.get()
   global f_num
   global math
   math = "addition"
   f_num = int(first_number)
   e.delete(0, END)

def button_equal():
   second_number = e.get()
   e.delete(0, END)

   if math == "addition":
      e.insert(0, f_num+int(second_number))
   if math == "subtraction":
      e.insert(0, f_num - int(second_number))
   if math == "multiplication":
      e.insert(0, f_num * int(second_number))
   if math == "division":
      e.insert(0, f_num // int(second_number))


def button_sub():
   first_number = e.get()
   global f_num
   global math
   math = "subtraction"
   f_num = int(first_number)
   e.delete(0, END)

def button_multiply():
   first_number = e.get()
   global f_num
   global math
   math = "multiplication"
   f_num = int(first_number)
   e.delete(0, END)

def button_divide():
   first_number = e.get()
   global f_num
   global math
   math = "division"
   f_num = int(first_number)
   e.delete(0, END)





b1 = Button(root, text="1",padx=40, pady=20, command=lambda :button_click(1))
b2 = Button(root, text="2",padx=40, pady=20, command=lambda : button_click(2))
b3 = Button(root, text="3",padx=40, pady=20, command=lambda : button_click(3))
b4 = Button(root, text="4",padx=40, pady=20, command=lambda : button_click(4))
b5 = Button(root, text="5",padx=40, pady=20, command=lambda : button_click(5))
b6 = Button(root, text="6",padx=40, pady=20, command=lambda : button_click(6))
b7 = Button(root, text="7",padx=40, pady=20, command=lambda : button_click(7))
b8 = Button(root, text="8",padx=40, pady=20, command=lambda : button_click(8))
b9 = Button(root, text="9",padx=40, pady=20, command=lambda : button_click(9))
b0 = Button(root, text="0",padx=40, pady=20, command=lambda : button_click(0))
bclear = Button(root, text="C",padx=39, pady=20, command= button_clear )
bequal = Button(root, text="=",padx=41, pady=20, command= button_equal)
badd = Button(root, text="+",padx=39, pady=20, command= button_add)
bsub = Button(root, text="-",padx=41, pady=20, command= button_sub)
bmultiply = Button(root, text="x",padx=40, pady=20, command= button_multiply)
bdivide = Button(root, text="/",padx=41, pady=20, command= button_divide)



b1.grid(row=3, column = 0)
b2.grid(row=3, column = 1)
b3.grid(row=3, column = 2)
badd.grid(row=3,column=3)
b4.grid(row=2, column = 0)
b5.grid(row=2, column = 1)
b6.grid(row=2, column = 2)
bsub.grid(row=2,column=3)
b7.grid(row=1, column = 0)
b8.grid(row=1, column = 1)
b9.grid(row=1, column = 2)
bmultiply.grid(row=1,column=3)
b0.grid(row=4, column =1)
bclear.grid(row=4,column=0)
bdivide.grid(row=4,column=2)
bequal.grid(row=4,column=3)



root.mainloop()