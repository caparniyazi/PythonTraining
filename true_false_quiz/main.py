from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    new_question = Question(q_text=question["text"], q_answer=question["answer"])
    question_bank.append(new_question)

# Init the quiz
quiz = QuizBrain(question_bank)

while quiz.has_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
