class Question:
    def __init__(self,text,answer):
        self.text=text
        self.answer=answer

class QuizBrain:
    def __init__(self,list):
        self.question_number=0
        self.question_list=list
        self.score=0
        
    def check_answer(self,response,answer):
        if(response.lower()==answer.lower()):
            self.score+=1
            print(f"You got that correct, which means the score is {self.score}/{self.question_number}")
        else:
            print("Wrong answer.")
            print(f"The correct answer was {answer},which means the score is {self.score}/{self.question_number}")
    
    def next_question(self):
        current_question=self.question_list[self.question_number]
        self.question_number+=1
        response=input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(response,current_question.answer)
    
    def still_has_questions(self):
        length=len(self.question_list)
        if(self.question_number<length):
            return True
        else:
            return False
        
 