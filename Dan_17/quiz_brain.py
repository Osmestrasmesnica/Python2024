 # TODO: asking the questions
 # TODO: checking if the answer was correct
 # TODO: checking if we're the end of the quiz
 
# TODO: napraviti klasu QuizBrain koja ima atribute question_number 0 i question_list i metodu next_question()

class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

# TODO: Retrive the item at the current question_number from the question_list.
# TODO: Use the input() function to show the user Question text and ask for the user's answer
    def next_question(self):
        current_question = self.question_list[self.question_number]
        question_text = current_question.text
        question_answer = current_question.answer
        self.question_number += 1
        user_answer = input(f"Question {self.question_number}: {question_text} (`True` or `False`)\n")
        self.check_answer(user_answer, question_answer) # --> pozivanje metode unutar metode

# TODO: Create method called still_has_questions(). 
# TODO: Return a boolean depending on the value of question_number. 
# TODO: Use the while loop to show the next question until the end.
    def still_has_question(self, question_list):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False
        
# TODO: check_answer(), score...
# TODO: dodao sam gore score = 0, i sada pravim check_answer() metodu koja proverava da li je unesen odgovor jednak tacnom odgovoru
# TODO: ako jeste onda dodajem na score += 1
    def check_answer(self, user_answer, question_answer):
        if user_answer.lower() == question_answer.lower():
            self.score += 1
            print("Correct!")
        else:
            print("Wrong answer!!")
        print(f"Tacan odgovor je bio: {question_answer}.") # --> sa ovakvom indentacijom dobijamo uvek koji je bio tacan odgboro, a ako ga  uvucemo u else, onda ce se printovati samo ako pogresno odgovorimo na pitanje
        print(f"Vas trenutni skor je {self.score}/{self.question_number}")
        print("\n")