from quiz.quiz_show import QuizShow

class Presenter(object):

    def __init__(self, view, questions):
        self.quiz_show = QuizShow(questions)
        self.view = view
        
    def initialize(self):
        self.bind_events()
        self.load_from_model()
        
    def bind_events(self):
        self.view.select_answer = self.select_answer
        self.view.next = self.next
    
    def select_answer(self, key_index):
        answer = self.quiz_show.get_answer(key_index)
        self.view.display_answer(answer.question_text, 
                                 answer.choice_texts, 
                                 answer.correct_answer,
                                 answer.description, 
                                 selected_index=key_index, 
                                 correct=answer.is_correct)
        
    def load_from_model(self):
        self.next()
        self.view.show()
        
    def next(self):
        question = self.quiz_show.get_next_question()
        if not question:
            self.view.quit()
            return
        self.view.display_question(question.question_text, question.choice_texts)
