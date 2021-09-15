from tkinter import *
from quiz_brain import QuizBrain
import time
THEME_COLOR = "#375362"

class QuizzlerInterface:

    def __init__(self , quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg= THEME_COLOR , padx=20,pady=20)
        self.canvas = Canvas(bg="white",width= 300,height=250,highlightthickness=0)
        self.canvas.grid(row=1 , column=0 , columnspan = 2,pady=50)
        truth_img = PhotoImage(file="./images/true.png")
        self.check_button = Button(image=truth_img,highlightthickness=0,highlightbackground=THEME_COLOR,command= self.true_button)
        self.check_button.grid(row=2,column=0)
        false_img = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, highlightbackground=THEME_COLOR,command= self.false_button)
        self.false_button.grid(row=2, column=1)
        self.text = self.canvas.create_text(150,125,text="Text",font=("Arial",20,"italic"),fill=THEME_COLOR,width= 280)
        self.score =Label(text=f"Score:{self.quiz.score} ",bg=THEME_COLOR,fg="white")
        self.score.grid(row=0 , column=1)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.config(bg="white")
            self.score.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.text,text=q_text)
        else:
            self.canvas.itemconfig(self.text, text="You reached the End!")
            self.canvas.config(bg="white")
            self.false_button.config(state="disabled")
            self.check_button.config(state="disabled")


    def true_button(self):
        answer = self.quiz.check_answer(True)
        self.change_color(answer)

        # self.get_next_question()


    def false_button(self):
        answer = self.quiz.check_answer(False)
        self.change_color(answer)
        # self.get_next_question()

    def change_color(self,answer):
        if answer == True:
            self.canvas.config(bg="green")
            self.window.after(1000,self.get_next_question)
        else:
            self.canvas.config(bg="red")
            self.window.after(1000, self.get_next_question)
