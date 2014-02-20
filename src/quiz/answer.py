
class Answer(object):

    def __init__(self, question, is_correct, description, correct_answer):
        self.question= question
        self.is_correct = is_correct
        self.description = description
        self.correct_answer = correct_answer
        
    @property
    def question_text(self):
        return self.question.question_text
    
    @property
    def choice_texts(self):
        return self.question.choice_texts