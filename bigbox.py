from tkinter import *
from tkinter.scrolledtext import ScrolledText
import time
from datetime import datetime
import os

mainwin = Tk()


Label(mainwin, text="Text Saver:").grid(row=1, column=0)
st = ScrolledText(mainwin, height=5)
st.grid(row=1, column=1)


def myfunc():
    ttext = st.get(1.0, END)

    today = datetime.today()
    datem = str(datetime(today.year, today.month, 1)).split()
    datem = datem[0].split("-")

    if datem[2] == "01":
        parent_dir = "c:/Apps/7618N/"
        path = os.path.join(parent_dir, datem[1])
        os.mkdir(path)

    filepath = "c:/Apps/7618N/" + datem[1] + "/mytext.txt"
    window = open(filepath, "a")
    timer = time.ctime()
    window.write(timer + "(" + ttext + ")\n")

    window.close()
    mainwin.destroy()


Button(mainwin, text="Save and Exit", command=myfunc).grid(
    row=2, column=0, columnspan=3, sticky="EW"
)
mainwin.mainloop()