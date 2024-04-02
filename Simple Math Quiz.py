#asking the user for their name
username = input("What is your name? ")

#greeting the user and awellcoming them to the quiz
print("Hello " + username + ", Welcome to your Math Quiz!")

#setting the score to 0
score = 0

print("To pass this quiz, you must score 8 or more points. Good Luck!")

#defining the random number generator
def random_number (num1, num2):
    import random
    return random.randint(num1, num2)

#defining the num1 and num2 variables
num1 = random_number(10, 20)
num2 = random_number(1, 10)

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

#calling the random question functions
random_question_add()
user_answer_add = int(input("Please type you answer here: "))

random_question_sub()
user_answer_sub = int(input("Please type you answer here: "))

random_question_mult()
user_answer_mult = int(input("Please type you answer here: "))

random_question_div()
user_answer_div = int(input("Please type you answer here: "))

random_question_mult()
user_answer_mult = int(input("Please type you answer here: "))


#Showing the correct answers
while score < 8:
    if user_answer_add == correct_answer_add:
        score += 2
        print ("You are correct!")
    else:
        print ("This is incorrect, the correct answer is: " + str(correct_answer_add) + ".")
    if user_answer_sub == correct_answer_sub:
        score += 2
        print ("You are correct!")
    else:
        print ("This is incorrect, the correct answer is: " + str(correct_answer_sub) + ".")
    if user_answer_mult == correct_answer_mult:
        score += 2
        print ("You are correct!")
    else:
        print ("This is incorrect, the correct answer is: " + str(correct_answer_mult) + ".")
    if user_answer_div == correct_answer_div:
        score += 2
        print ("You are correct!")
    else:
        print ("This is incorrect, the correct answer is: " + str(correct_answer_div) + ".")
    break

print ("Your score is: " + str(score))

if score >= 8:
    print ("Congratulations " + username + ", you have passed the quiz!")   

else:
    print ("Sorry " + username + ", you have failed the quiz. Better luck next time!")  








 

   









