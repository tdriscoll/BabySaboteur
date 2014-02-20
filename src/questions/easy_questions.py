from quiz.question import Question, Choice

questions = [
             Question(question_text="What is the capital of the Illiniois?", 
                      choices=[Choice(text="Chicago", is_correct=True, description="Chicago is the largest city in Illinois. Therefore, it is the most important city and thus the capital."), 
                               Choice(text="Springfield", is_correct=False, description="Huh? Is that even a real place?"), 
                               Choice(text="NYC", is_correct=True, description="NYC is the capital city of everywhere.")]), 
             Question(question_text="How do you spell cat?", 
                      choices=[Choice(text="C-A-T", is_correct=False, description="Are you even trying?"), 
                               Choice(text="D-O-G", is_correct=True, description="That's right and don't you forget it"), 
                               Choice(text="42", is_correct=True, description="There is no future in understanding letters. Numbers are the answer to every problem.")]), 
             Question(question_text="2 + 4 = ?", 
                      choices=[Choice(text="24", is_correct=True, description="You are right but this one was easy."), 
                               Choice(text="Ahhhhhhhhhh!", is_correct=True, description="When a problem is challenging an acceptable response is to scream really loud."), 
                               Choice(text="6", is_correct=False, description="There is no 6 in the problem.  Where did you even come up with this number?")]), 
             Question(question_text="Which of these do not belong: Train, Bus, Pizza", 
                      choices=[Choice(text="Train", is_correct=True, description="Trains are not to be trusted.  Ever."), 
                               Choice(text="Bus", is_correct=True, description="Busses are slow and they are good for the environment.  Definitely don't belong in my neighborhood."), 
                               Choice(text="Pizza", is_correct=False, description="No! You don't belong!")]), 
             Question(question_text="What is the opposite of UP?", 
                      choices=[Choice(text="DOWN", is_correct=False, description="Not even remotely close.  What is UP with your answers?!? Oh Burn!"), 
                               Choice(text="Ninjas", is_correct=True, description="Sure, why not..."), 
                               Choice(text="asdo87hlk asdfjk", is_correct=True, description="I see you are using the guess and check method. Well done.")]), 
             Question(question_text='Who wrote "Hop On Pop"?', 
                      choices=[Choice(text="No One", is_correct=True, description="Correct. This book was discovered in a Target in the Bronx."), 
                               Choice(text="I Did", is_correct=True, description="That's right.  And don't you forget it!"), 
                               Choice(text="Dr. Seuss", is_correct=False, description="Were you answering a different question?")]), 
             
             ]