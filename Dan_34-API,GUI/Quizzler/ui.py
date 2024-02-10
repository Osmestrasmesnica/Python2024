from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 14, "italic")

class QuizInterface:

    #! dodaje se i quiz_brain: QuizBrain (definisemo da mora da bude QuizBrain object) da bi se iz njega pozivalo next_question()
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain #! --> property koji se poziva na input koji je QuizBrain
        self.window = Tk()
        self.window.title("Quizz by WLQ")
        self.score = 0
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        # Pozadina gde je tekst
        self.canvas = Canvas(width=400, height=300, background="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(200, 150, text="Question text goes here", font=FONT, fill=THEME_COLOR, width=380, justify="center")
        self.canvas.grid(row=1, column=0, columnspan=2, sticky=EW, pady=20)


        # Pravljenje dugmica
        img_true = PhotoImage(file="Dan_34-API,GUI/Quizzler/images/true.png") # --> ovo ne mora u self. da stoji moze i bez toga jer se koristi posle u btn
        self.btn_true = Button(image=img_true, highlightthickness=0, borderwidth=0, background=THEME_COLOR, activebackground=THEME_COLOR, command=self.on_true_clicked)
        self.btn_true.grid(row=2, column=0, padx=20, pady=20)

        img_false = PhotoImage(file="Dan_34-API,GUI/Quizzler/images/false.png") # --> ovo ne mora u self. da stoji moze i bez toga jer se koristi posle u btn
        self.btn_false = Button(image=img_false, highlightthickness=0, borderwidth=0, background=THEME_COLOR, activebackground=THEME_COLOR, command=self.on_false_clicked)
        self.btn_false.grid(row=2, column=1, padx=20, pady=20)

        # Skor
        self.score_label = Label(text=f"Score: {self.score}", fg="white", background=THEME_COLOR, font= ("Arial", 10)) 
        self.score_label.grid(row=0, column=1, sticky=EW, padx=20, pady=20)

        # Pozivanje funkcije
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question() # --> ako ostavis "quiz_brain" samo bez ":QuizBrain" ovo nece biti prepoznato
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text = f"You've reached the end of the quiz\n\nScore: {self.quiz.score}/10")
            # disable btn 
            self.btn_true.config(state="disabled")
            self.btn_false.config(state=DISABLED)

    def on_true_clicked(self):
        is_right = self.quiz.check_answer(user_answer='True')
        self.give_feedback(is_right)

    def on_false_clicked(self):
        is_right = self.quiz.check_answer(user_answer='False')
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)