# quiz game implementing use of dictionary loops
questions = [
    {
        "prompt": "What is the correct syntax to ouput  'Hello World' in python ? ",
        "options": ['A. print("Hello World")  ', "B. p('Hello World')", "C. echo('Hello World')", "D. echo'Hello world'"],
        "answer": "A"
    },
    {
        "prompt": "How do you insert COMMENTS in Python code?",
        "options": ["A. //this is a comment  ", "B. #This is a comment", "C. /*This is a comment*/", "D. *This is a comment"],
        "answer": "B"
    },
    {
        "prompt": "Which one is NOT a legal variable name??",
        "options": ["A. my-var", "B. _myvar", "C. my_var", "D. Myvar"],
        "answer": "A"
    },
    {
        "prompt": "How do you create a variable with the numeric value 5?",
        "options": ["A. x = int(5)", "B. X=5", "C. both answers are correct", "D. all answers are wrong"],
        "answer": "C"
    },
    {
        "prompt": "What is the file extension for Python files",
        "options": ["A. .pyt", "B. .pt", "C. .py", "D. .pyth"],
        "answer": "C"
    },
    {
        "prompt": "What is the correct syntax to output the type of a variable or object in Python?",
        "options": ["A. print(typeof x)", "B. print(typeof(x)) ", "C. print(type(x)) ", "D. print(typeOf(X)) "],
        "answer": "C"
    },
    {
        "prompt": "What is the correct way to create a function in Python?",
        "options": ["A. create myFunction():", "B. def myFunction():", "C. function myfunction():", "D. all answers are correct"],
        "answer": "B"
    },
    {
        "prompt": """In Python, 'Hello', is the same as "Hello" """,
        "options": ["A. true", "B. false"],
        "answer": "A"
    },
    {
        "prompt": "What is a correct syntax to return the first character in a string?",
        "options": ["""A. x= "Hello".sub(0,1) """, """B. x=sub("Hello", 0,1) """, """C. x="Hello"[0] """],
        "answer": "C"
    },
    {
        "prompt": "Which method can be used to remove any whitespace from both the beginning and the end of a string?",
        "options": ["A. trim() ", "B. strip() ", "C. len()", "D. ptrim()"],
        "answer": "B"
    },
    {
        "prompt": "Which method can be used to return a string in upper case letters?",
        "options": ["A. upperCase() ", "B. upper() ", "C. toUpperCase()", "D. uppercase()"],
        "answer": "B"
    },
    {
        "prompt": "Which method can be used to replace parts of a string?",
        "options": ["A. replaceString() ", "B. switch() ", "C. replace()", "D. repl()"],
        "answer": "C"
    },
    {
        "prompt": "Which operator is used to multiply numbers??",
        "options": ["A. X ", "B. % ", "C. #", "D. *"],
        "answer": "D"
    },
    {
        "prompt": "Which operator is used to multiply numbers??",
        "options": ["A. X ", "B. % ", "C. #", "D. *"],
        "answer": "D"
    },
    {
        "prompt": "Which operator can be used to compare two values??",
        "options": ["A. <> ", "B.  == ", "C. =", "D. ><"],
        "answer": "B"
    },
    {
        "prompt": "Which of these collections defines a LIST?",
        "options": ["""A. {"name":"apple", "color:"green"} """, """B. ["apple", "banana", "cherry"]   """, """C. ("apple", "banana" , "cherry")""", """D. {"apple","banana", "cherry"}"""],
        "answer": "B"
    },
    {
        "prompt": "Which of these collections defines a TUPPLE?",
        "options": ["""A. {"name":"apple", "color:"green"} """, """B. ["apple", "banana", "cherry"]   """, """C. ("apple", "banana" , "cherry")""", """D. {"apple","banana", "cherry"}"""],
        "answer": "C"
    },
    {
        "prompt": "Which of these collections defines a SET?",
        "options": ["""A. {"name":"apple", "color:"green"} """, """B. ["apple", "banana", "cherry"]   """, """C. ("apple", "banana" , "cherry")""", """D. {"apple","banana", "cherry"}"""],
        "answer": "D"
    },
    {
        "prompt": "Which of these collections defines a DICTIONARY?",
        "options": ["""A. {"name":"apple", "color:"green"} """, """B. ["apple", "banana", "cherry"]   """, """C. ("apple", "banana" , "cherry")""", """D. {"apple","banana", "cherry"}"""],
        "answer": "A"
    },
    {
        "prompt": "Which collection is ordered, changeable, and allows duplicate members?",
        "options": ["A. LIST ", "B. SET", "C. DICTIONARY", "D. TUPLE"],
        "answer": "A"
    },
    {
        "prompt": "Which collection DOES NOT allow duplicate members?",
        "options": ["A. LIST ", "B. SET",  "C. TUPLE"],
        "answer": "B"
    },
    {
        "prompt": "How do you start writing an if statement in Python?",
        "options": ["A. if x > y then : ", "B. if x > y:",  "C. if(x>y)"],
        "answer": "B"
    },
    {
        "prompt": "How do you start writing a while loop in Python?",
        "options": ["A. while x > y { ", "B. while(x > y)",  "C. while x > y:", "D.  x > y While{"],
        "answer": "C"
    },
    {
        "prompt": "How do you start writing a for loop in Python?",
        "options": ["A. for x > y : ", "B. for x in y:",  "C. for each x in y:"],
        "answer": "B"
    },
    {
        "prompt": "Which statement is used to stop a loop?",
        "options": ["A.  exit", "B. stop",  "C. return",  "D. break"],
        "answer": "D"
    },






]
print(type(questions))


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
    correct = round(score/10)
    print(f"final score {score} you got correct {
          correct} answers out of {len(questions)} questions")


run_quiz(questions)
