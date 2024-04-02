num1 = 5
num2 = 10

def random_question_add():
    question = ("What is " + str(num1) + " " + "+" + " " + str(num2) + " ?")
    print (question)

random_question_add()
user_answer = int (input("Please type you answer here: "))
print (user_answer)


correct_answer = num1 + num2
print ("The correct answer is", correct_answer)


if user_answer == correct_answer:
    print ("you are correct")

else:
    print ("incorrect")
    
