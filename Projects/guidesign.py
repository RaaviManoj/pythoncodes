import sudoku as Sudo
import sys

# from tkinter import *

a, q = Sudo.all()
print(a, q)


"""
root = Tk()


def showframe1():
    frame2.grid_forget()
    frame1.grid()


def showframe2():
    frame1.grid_forget()
    frame2.grid()


frame1 = Frame(root)
Label(frame1, text="WELCOME").grid(row=1, column=2, padx=50)
Button(
    frame1,
    text="Start Sudoku",
    height=10,
    width=20,
    bg="red",
    fg="green",
    command=showframe2,
).grid(row=2, column=2)

frame2 = Frame(root, width=100, height=100)


def Taker(event):
    print(sys.stderr, "Key-Release event called with args: %s" % event)
    print(sys.stderr, "Entry Widget Content:               %s" % event.widget.get())


def callback(sv):
    print(sv.get())


def display_question():
    question = Sudo.get_question()
    for i in range(9):
        for j in range(9):
            if question[i][j] != ".":
                Label(frame2, text=str(question[i][j]), width=10).grid(row=i, column=j)
            else:
                sv = IntVar()
                sv.trace("w", lambda name, index, mode, sv=sv: callback(sv))
                Entry(frame2, textvariable=sv, width=10).grid(row=i, column=j)


display_question()

frame1.grid(pady=250, padx=500)


root.mainloop()
"""