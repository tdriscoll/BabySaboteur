from quiz.answer import Answer

class Question(object):

    def __init__(self, question_text, choices):
        self.question_text = question_text
        self.choices = choices
        
    def get_answer(self, selected_answer_index):
        selected_choice = self.choices[selected_answer_index - 1]
#         if choice.is_correct:
#             correct_answer = "#%s" % self.selected_answer_index
#         else:
        for choice_index, choice in enumerate(self.choices):  
            if choice.is_correct:       
                correct_answer = "#%s" % (choice_index+1)
        return Answer(question=self,
                      is_correct=selected_choice.is_correct,
                      description=selected_choice.description, 
                      correct_answer = correct_answer)
    
    @property
    def choice_texts(self):
        return [choice.text for choice in self.choices]
        
        
class Choice(object):
    
    def __init__(self, text, is_correct, description):
        self.text = text 
        self.is_correct = is_correct
        self.description = description
