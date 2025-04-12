from source import QuizBrain,Question
from data import data1,logo
question_bank=[]
for data in data1:
    obj=Question(data["question"],data["correct_answer"])
    question_bank.append(obj)

quiz=QuizBrain(question_bank)
print("\n"*20)
print(logo)
while(quiz.still_has_questions()):
    quiz.next_question()
    print("\n")

print(f"Congratulations on completing the quiz with a final score of {quiz.score}/{quiz.question_number} 🎉")

