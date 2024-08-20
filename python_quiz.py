# quiz game implementing use of dictionary loops
questions = [
    {
        "prompt": "What is the correct syntax to ouput  'Hello World' in python ? ",
        "options": ['A. print("Hello World")  ', "B. p('Hello World')", "C. echo('Hello World')", "D. echo'Hello world'"],
        "answer": "A"
    },
    {
        "prompt": "How do you insert COMMENTS in Python code?",
        "options": ["A. #This is a comment", "B. //this is a comment", "C. /*This is a comment*/", "D. *This is a comment"],
        "answer": "A"
    },

]


def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Type your answer A,B,C or D: \n").upper()
        if answer == question["answer"]:
            print("correct! 10 points awarded! \n")
            score += 10
        else:
            print("wrong answer!")
    correct = {score/10}
    print(f"final score {score} you got correct {
          correct} answers out of {len(questions)} questions")


run_quiz(questions)
