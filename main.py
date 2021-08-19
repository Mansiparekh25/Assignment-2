import random
import tkinter
from tkinter import *
from tkinter import ttk

root = Tk()
myCanvas = Canvas(root)
myCanvas.pack()

X = random.randrange(50, 200)
y=random.randrange(80,100)
class Shape:

    def __init__(self, root= None):
        self.root = root
        self.create()


    def create(self):


             myCanvas.create_rectangle(X, X, X+X, X+X, fill="blue")
             print (X)
             area=Label(root,text="Enter area").place(x=0,y=200)

             a=IntVar()
             a1=ttk.Entry(textvariable=a).place(x=70,y=200)

             Shape.a1=a.get()



             perimiter = Label(root, text="Enter perimiter").place(x=0, y=250)
             b=IntVar()
             ttk.Entry(textvariable=b) .place(x=85, y=250)
             Shape.p1=b.get()
             sbmitbtn = Button(root, text="Submit",command=Shape.click) .place(x=30, y=280)



    def create_Oval():

              myCanvas.create_oval(X,X,y,y,fill="yellow")
              area = Label(root, text="Enter area").place(x=0, y=200)
              Shape.a1 = ttk.Entry(root).place(x=70, y=200)
              perimiter = Label(root, text="Enter perimiter").place(x=0, y=250)
              Shape.p1 = Entry(root).place(x=85, y=250)

              sbmitbtn = Button(root, text="Submit", command=Shape.click1).place(x=30, y=280)
    def Create_Rect():

              myCanvas.create_rectangle(X, y, y,X, fill="RED")
              area = Label(root, text="Enter area").place(x=0, y=200)
              Shape.a1 = ttk.Entry(root).place(x=70, y=200)
              perimiter = Label(root, text="Enter perimiter").place(x=0, y=250)
              Shape.p1 = Entry(root).place(x=85, y=250)

              sbmitbtn = Button(root, text="Submit", command=Shape.click2).place(x=30, y=280)
    def Create_Tri():

               myCanvas.create_line(60, 20, 20, 100, 80, 100, 60, 20, fill="Black")
               area = Label(root, text="Enter area").place(x=0, y=200)
               Shape.a1 = ttk.Entry(root).place(x=70, y=200)
               perimiter = Label(root, text="Enter perimiter").place(x=0, y=250)
               Shape.p1 = Entry(root).place(x=85, y=250)

               sbmitbtn = Button(root, text="Submit", command=Shape.click3).place(x=30, y=280)

    def click3():

        sqaure_area = X * y
        square_Per = 2 * (X + y)

        if sqaure_area == shape.a1 and square_Per == shape.p1:
            Label(root, text="Your ans is correct!").place(x=10, y=300)
        else:
            Label(root, text="Your ans is wrong!").place(x=10, y=300)

    def click2():

        sqaure_area = X*y
        square_Per = 2 * (X+y)

        if sqaure_area == shape.a1 and square_Per == shape.p1:
            Label(root, text="Your ans is correct!").place(x=10, y=300)
        else:
            Label(root, text="Your ans is wrong!").place(x=10, y=300)
            Shape.Create_Tri()
    def click1():

        sqaure_area = 3.14*(X/2)*(X/2)
        square_Per = 2 *3.14*(X/2)

        if sqaure_area==shape.a1 and square_Per==shape.p1:
            Label(root, text="Your ans is correct!").place(x=10, y=300)
        else:
            Label(root, text="Your ans is wrong!").place(x=10, y=300)
            Shape.Create_Rect()
    def click():

        sqaure_area = X + X
        square_Per = 2 * (X + X)

        if sqaure_area==shape.a1 and square_Per==shape.p1:
            Label(root, text="Your ans is correct!").place(x=10, y=300)
        else:
            Label(root, text="Your ans is wrong!").place(x=10, y=300)
            Shape.create_Oval()

if __name__ == "__main__":

    shape = Shape(root)
    root.geometry("330x220+300+300")
    mainloop()



