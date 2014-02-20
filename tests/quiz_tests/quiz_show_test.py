import unittest
from quiz.quiz_show import QuizShow, NoQuestionAskedException
from quiz.question import Question, Choice


class QuizShowTest(unittest.TestCase):


    def _create_quiz_show(self, *question_texts):
        return QuizShow([Question(question_text=question_text, 
                                  choices=[Choice("Answer1", False, "Boo"), Choice("Answer2", True, "Yeah"), Choice("Answer3", False, ":(")], 
                                  ) for question_text in question_texts])
    
    def _get_all_question_texts(self, quiz_show):
        results = []
        while True:
            question = quiz_show.get_next_question()
            if not question:
                return results
            results.append(question.question_text)

    def test_when_no_more_questions_return_none(self):
        self.assertEquals(None, QuizShow([]).get_next_question())

    def test_can_get_the_first_question(self):
        quiz_show = self._create_quiz_show("What?")
        question = quiz_show.get_next_question()
        self.assertEquals("What?", question.question_text)
        self.assertEquals(["Answer1", "Answer2", "Answer3"], question.choice_texts)
        
    def test_can_get_two_questions(self):
        quiz_show = self._create_quiz_show("What?", "Who?")
        self.assertEquals(["What?", "Who?"], sorted(self._get_all_question_texts(quiz_show)))
        
    def test_getting_questions_is_in_random_order(self):
        quiz_show1 = self._create_quiz_show(*xrange(1000))
        quiz_show2 = self._create_quiz_show(*xrange(1000))
                                            
        quiz_show1_order = [self._get_all_question_texts(quiz_show1)]
        quiz_show2_order = [self._get_all_question_texts(quiz_show2)]
        self.assertNotEquals(quiz_show1_order, quiz_show2_order)
        
    def test_asking_for_answer_when_there_is_no_question_raises_excepion(self):
        self.assertRaises(NoQuestionAskedException, self._create_quiz_show("Test").get_answer, 2)
        
    def test_can_get_a_correct_answer(self):
        quiz_show = self._create_quiz_show("Test")
        quiz_show.get_next_question()
        answer= quiz_show.get_answer(2)
        self.assertEquals(True, answer.is_correct)
        self.assertEquals("Yeah", answer.description)
        self.assertEquals("Test", answer.question_text)
        self.assertEquals("#2", answer.correct_answer)
        
        
    def test_can_get_a_wrong_answer(self):
        quiz_show = QuizShow([Question(question_text="Where?", 
                                  choices=[Choice("Answer1", True, "Yip"), Choice("Answer2", False, "Yeah"), Choice("Answer3", False, ":(")], 
                                  )])
        quiz_show.get_next_question()
        answer= quiz_show.get_answer(3)
        self.assertEquals(False, answer.is_correct)
        self.assertEquals(":(", answer.description)
        self.assertEquals("#1", answer.correct_answer)
        
        
