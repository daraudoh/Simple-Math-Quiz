import random

for _ in range(10):  # replace 10 with the number of questions you want
    num1 = random.randint(1, 10)  # replace 1, 10 with the range of numbers you want
    num2 = random.randint(1, 10)

    random_question_add = input("What is " + str(num1) + " " + "+" + " " + str(num2) + " ?")
    random_question_div = input("What is " + str(num1) + " " + "/" + " " + str(num2) + " ?")
    random_question_mult = input("What is " + str(num1) + " " + "*" + " " + str(num2) + " ?")   
    random_question_sub = input("What is " + str(num1) + " " + "-" + " " + str(num2) + " ?")    
    # rest of your code here

#defining the random addition question generator
def random_question_add():
    question = ("What is " + str(num1) + " " + "+" + " " + str(num2) + " ?")
    print (question)

#defining the random subtraction question generator
def random_question_sub():
    question = "What is " + str(num1) + " " + "-" + " " + str(num2) + " ?"
    print (question)

#defining the random multiplication question generator
def random_question_mult():
    question =  "What is " + str(num1) + " " + "*" + " " + str(num2) + " ?"
    print (question)

#defining the random division question generator
def random_question_div():
    question = "What is " + str(num1) + " " + "/" + " " + str(num2) + " ?"
    print (question)

#Adding the correct answer variables
correct_answer_add = num1 + num2   
correct_answer_sub = num1 - num2
correct_answer_mult = num1 * num2
correct_answer_div = num1 / num2

random_question_add()
answer= int(input("Please type you answer here: "))
random_question_sub()
answer= int(input("Please type you answer here: "))
random_question_mult()
answer= int(input("Please type you answer here: "))
random_question_div()
answer= int(input("Please type you answer here: "))

if answer == correct_answer_add:
    print ("You are correct!")
else: 
    print ("This is incorrect, the correct answer is: " + str(correct_answer_add) + ".")
if answer == correct_answer_sub:
    print ("You are correct!")
else:    
    print ("This is incorrect, the correct answer is: " + str(correct_answer_sub) + ".")
if answer == correct_answer_mult:
    print ("You are correct!")
else:    
    print ("This is incorrect, the correct answer is: " + str(correct_answer_mult) + ".")
if answer == correct_answer_div:    
    print ("You are correct!")
else:    
    print ("This is incorrect, the correct answer is: " + str(correct_answer_div) + ".")        
#Showing the correct answers
    
