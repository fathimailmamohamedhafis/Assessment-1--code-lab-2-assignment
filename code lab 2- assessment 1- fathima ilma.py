from tkinter import*
import tkinter as tk

from random import randint

root = tk. TK()
root.title("MATH QUIZ")
root. geometry("700x700")
##the size of the window in the output
root.resizable(0,0)
#fixes size in output window. 
score=IntVar()
#makes a int variable
labelhead= Label(root, text="Ilma's Quiz", font= ('times new roman', 30))
#adds a header and font
labelhead.grid(row=0, column=0)

homepage= tk.Frame(root)
easypage= tk.Frame(root)
mediumpage=tk.Frame(root)
hardpage=tk.Frame(root)
ending=tk.Frame(root)

