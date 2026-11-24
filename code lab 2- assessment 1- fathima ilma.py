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
            

            ui = "quiz"[level]
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
            answer = a+b
            display = f"{a} + {b}= ?"
            #what the display will be
        elif operation == "-":
            a = randint (low, high)
            a = randint (low, high)
            if b> a:
                a,b = b, a 
            #makes sure the answer isnt negative
                
            answer = a - b
            display = f"{a} - {b}= ?"

        elif operation =="*":
            if level=="Easy":
             a,b = randint ( 10, 50), randint (10, 50)
            elif level == "Medium":
             
             a, b = randint= (50, 100), randint (50, 100)
            else:
             a,b = randint (100, 500), randint (100,500)
             answer = a*bdisplay = f"{a} * {b}= ?"
        else: #division
           if level== "Easy" : 
              divisor = randint (10, 50) # picking the divisor and quotient first causee itll multiply to get the exact divident
              quotient = randint (10, 50)
           elif level == "Medium":
              divisor = randint (50, 100)
              quotient = randint (50, 100)
           else :
              divisor = randint (100, 500)
              quotient = randint (100, 500)
           divident = divisor * quotient 
           a, b = divident, divisor
           answer = quotient 
           #puts large number first and smaller number 2nd
           display = f"{divident} / {divisor}"

        return a, b , operation, answer, display 

    def numbers ():
       #check if users input matches correctanswer and update the score.
       global score, currentanswer, answered, num1, num2, correctanswer
       ui = "quiz"[current_level]

       if answered or currentanswer:
          ui["result_label"].config(text = "already answered", fg= "red")
          #stops user from trying to answer again
          return
       try: 
          youranswer = int (ui["entry"].get().strip())
       except ValueError:
          ui["result_label"].config(text=":please enter a number", fg="red")
          return 
       #makes an integer out of the text that was inputed- shows thatt its an error if the text isnt a number

       answered = True
       currentanswer= True

       ui["enter"].config(state="disabled")


       #makes questions that r already answered disabled
      
 

    
        




           



          

    


root.mainloop()




