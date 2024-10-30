import random
import re
def multiplication():
    correct_answers = []
    correct_num = 0
    for answer in range(10):
        question_num = 0
        num1 = random.randrange(0,99)
        num2 = random.randrange(0,99)
        user_answer = int(input(str(num1)+"*"+str(num2)+"=? "))
        answer = num1*num2
        if user_answer == answer:
            print("Correct")
            correct_num += 1
        else:
            print("Incorrect")
        correct_answers.append(answer)
    print("You got "+str(correct_num)+" answer(s) correct")
    return  correct_answers
correct_answers = multiplication()
print("The correct answers were: "+ str(correct_answers))