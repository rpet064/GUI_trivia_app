from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 15, "italic")
FONT1 = ("Arial", 20, "italic")

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        # window setup
        self.window = Tk()
        self.window.title("Rob's Quiz")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        # canvas setup
        self.canvas = Canvas(width=400, height=250, bg="white")
        self.question_text = self.canvas.create_text(200, 125, text="Some Question Text", font=FONT1, fill=THEME_COLOR, width=380)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        # score label
        self.score_label = Label(text="Score:0", bg=THEME_COLOR, fg="white", font=FONT)
        self.score_label.grid(row=0, column=1)
        self.button()
        self.get_new_question()
        self.window.mainloop()


    def button(self):
        # button setup
        self.correct = PhotoImage(file="C:/Users/robertp/OneDrive - Papatoetoe Intermediate/Desktop/Python Files/flash-card-project-start/images/right.png")
        self.true_button = Button(image=self.correct, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0, padx=20, pady=20)
        self.wrong = PhotoImage(file="C:/Users/robertp/OneDrive - Papatoetoe Intermediate/Desktop/Python Files/flash-card-project-start/images/wrong.png")
        self.false_button = Button(image=self.wrong, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1, padx=20, pady=20)

    def get_new_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f'''Congratulations! You finished the quiz
                                                            Your final score is {self.quiz.score}/10'''
                                   )
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")


    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right == True:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_new_question)

