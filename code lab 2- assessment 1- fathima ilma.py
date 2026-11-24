from tkinter import*
import tkinter as tk

from random import choice, randint

from mathquiz import next_question

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

PAGES= {
    "Home":homepage,
    "Easy":easypage,
    "Medium":mediumpage,
    "Ending":ending,
}
for page in PAGES.value():
    page.grid(row = 0, column= 0)

    num1= 0
    num2=0
    score=0
    maxques=10
    questionstart=0
    correctanswer=0
    currentanswer= False
    answered=False
    current_level="easy"


    def showpage(level)
        global num1, num2, score, questionstart, correctanswer, currentanswer
        currentlevel= level
        score=0
        questionstart=0
        answered=False
        currentanswer=False

        if level in ("Easy", "Medium", "Hard"):
            class quiz:
                ...

            ui = quiz[level]
            #checking a dictionary of the certain level.
            ui["score_label"].config(text="score: 0" fg: "black")
            #resets score
            ui["result_label"].config(text="", fg= "purple")
            #clears feedback 
            ui["entry"].config(state="normal")
            #unlocks text box
            next_question()

        PAGES[level].tkraise()

    def generate(level):

        operation= choice (["+", "-", "*", "/"])

        if level=="Easy":
            low, high = 10, 50
        elif level == "Medium":
            low, high == 50, 100
        else:
            low, high = 100, 500
            #numbers beterrn 10, 50 for easy and 50, 100 for medium and 100, 500 for hard

        if operation == "+":
            a = randint (low, high)
            b = randint (low, high)
            #randomizes numbers between the low and high numbers
            answered = a+b
            display = f"{a} + {b}= ?"
            #what the display will be
          

    def add_ numbers







