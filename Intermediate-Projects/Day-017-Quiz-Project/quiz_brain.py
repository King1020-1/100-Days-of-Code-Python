class Question:
    def __init__(self,text,answer):
        self.text = text
        self.answer = answer


class QuizBrain:
    def __init__(self,question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return not self.question_number == len(self.question_list)


    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q{self.question_number}: {current_question.text} (True/False)?: ").title()
        while not user_answer in ["True","False"]:
            print("Invalid Input.")
            user_answer = input(f"Q{self.question_number}: {current_question.text} (True/False)?: ").title()
        self.check_answer(user_answer,current_question.answer)

    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was {correct_answer}")
        print(f"Your score is {self.score}/{self.question_number}")
        print()
