
from tkinter import *
import random
import time
import datetime

root = Tk()
root.geometry("1300x750+0+0")
root.title("Sales Register")

root.configure(background="black")

f0 = Frame(root, width = 1350, height = 100, bd = 14, relief = "raise")
f0.pack(side = TOP)

f1 = Frame(root, width = 900, height = 650, bd = 8, relief = "raise")
f1.pack(side = LEFT)

f2 = Frame(root, width = 440, height = 650, bd = 8, relief = "raise")
f2.pack(side = RIGHT)




root.mainloop()
