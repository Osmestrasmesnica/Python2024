from question_model import Question
from data import question_data, nature_and_science
from quiz_brain import QuizBrain

question_bank = []

for pitanje in nature_and_science:
    question_text = pitanje["question"]
    question_answer = pitanje["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
# print(question_bank[0].text)
# print(question_bank[0].answer)

quiz = QuizBrain(question_bank)

while quiz.still_has_question(question_bank):
    quiz.next_question()
    
print("Kraj kviza. Hvala sto ste proverili znanje sa nama.")
print(f"Vas skor je: {quiz.score}/{quiz.question_number}")