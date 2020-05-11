from MultipleChoiceQuizClass import questions

qstn = [
    "What colour are apples?\n(A) Red/Green\n(B)Yellow\n(C)Blue\n",
    "What colour are bananas?\n(A)Orange\n(B)Red\n(C)Yellow\n",
    "What colour are strawberries?\n(A)Black\n(B)Red Pinkish\n(C)Yellow\n"
]

questions = [
    questions(qstn[0],"A"),
    questions(qstn[1],"C"),
    questions(qstn[2],"B")
]

def MCQ(questions):
    score = 0
    for question in questions:
        ans = input(question.q)
        if ans==question.ans:
            score +=1
        print(score)

MCQ(questions)