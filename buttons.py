from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="Look! I clicked a Button!!")
    myLabel.pack()



myButton = Button(root, text="Click me", padx=50, pady = 50, command= myClick,fg= "blue", bg="red")
mybutton2 = Button(root, text="Click", state=DISABLED)
mybutton2.pack()
myButton.pack()

root.mainloop()
