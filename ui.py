from tkinter import *
from quiz_brain import QuizBrain
from question_model import Question
from data import Question_Data

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self):
        self.question_bank = Question_Data().question_bank()
        self.quiz_brain = QuizBrain(self.question_bank)

        # Window
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Score Label
        self.score_label = Label(text=f'Score: 0',
                                 fg='white',
                                 bg=THEME_COLOR,
                                 font=('Arial',10,'bold'))
        self.score_label.grid(column=1, row=0)

        # Canvas
        self.canvas = Canvas(width=300, height=300)
        self.question_text = self.canvas.create_text(
                                                    150,
                                                    125,
                                                    width=250,
                                                    text='teste',
                                                    fill=THEME_COLOR,
                                                    font=("Arial",16, "italic")
                                                    )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50, padx=20)

        # Buttons
        green_image = PhotoImage(file='images/true.png')
        self.green_button = Button(image=green_image,
                                   highlightthickness=0,
                                   command=self.right_answer)
        self.green_button.grid(column=1, row=2)
        red_image = PhotoImage(file='images/false.png')
        self.red_button = Button(image=red_image,
                                 highlightthickness=0,
                                 command=self.wrong_answer)
        self.red_button.grid(column=0, row=2)

        # Call First Question
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz_brain.still_has_questions():
            q_text = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.score_label.config(text=f'Score: {self.quiz_brain.score}')
        else:
            self.canvas.itemconfig(self.question_text,
                                   text=f"you've reached the end of the quizz\n Your score is {self.quiz_brain.score}/{self.quiz_brain.question_number}")
            self.green_button.config(state='disabled')
            self.red_button.config(state='disabled')



    def right_answer(self):
        self.give_feedback(self.quiz_brain.check_answer("True"))

    def wrong_answer(self):
        self.give_feedback(self.quiz_brain.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)



