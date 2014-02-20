from random import shuffle


class NoQuestionAskedException(Exception):
    pass

class QuizShow(object):
    
    
    def __init__(self, questions):
        self.questions = questions
        shuffle(self.questions)
        self.current_question = None
        
    def get_next_question(self):
        if self.questions:
            self.current_question = self.questions.pop(0)
            return self.current_question
    
    def get_answer(self, selected_answer_index):
        if not self.current_question:
            raise NoQuestionAskedException()
        return self.current_question.get_answer(selected_answer_index)
    