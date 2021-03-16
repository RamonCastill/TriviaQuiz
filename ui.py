from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.score = 0
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.minsize(width=340, height=400)
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Title",
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR
        )

        # Label
        self.score_label = Label(text=f"Score: {self.score}", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        # Buttons
        image_button_true = PhotoImage(file="images/true.png")
        self.button_true = Button(image=image_button_true, highlightthickness=0, command=self.return_true)
        self.button_true.grid(row=2, column=0)
        self.button_true.config(padx=10, pady=10)
        image_button_false = PhotoImage(file="images/false.png")
        self.button_false = Button(image=image_button_false, highlightthickness=0, command=self.return_false)
        self.button_false.grid(row=2, column=1)
        self.button_false.config(padx=20, pady=30)

        self.get_nex_question()

        self.window.mainloop()

    def get_nex_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the  end of the quiz.")
            self.button_true["state"] = "disable"
            self.button_false["state"] = "disable"

    def return_true(self):
        answer = self.quiz.check_answer("True")
        self.check_answer(answer)

    def return_false(self):
        answer = self.quiz.check_answer("False")
        self.check_answer(answer)

    def check_answer(self, answer):

        if answer:
            self.score += 1
            self.canvas.config(bg="green")
            self.score_label.config(text=f"Score: {self.score}")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_nex_question)


