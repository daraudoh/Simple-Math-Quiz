#asking the user for their name
username = input("What is your name? ")

#greeting the user and welcoming them to the quiz
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
    global score
    num1 = random_number(10, 20)
    num2 = random_number(1, 10)
    question = ("What is " + str(num1) + " " + "+" + " " + str(num2) + " ?")
    print (question)
    correct_answer_add = num1 + num2
    user_answer_add = int(input("Please type you answer here: "))
    if correct_answer_add == user_answer_add:
        score += 1
        print ("You are correct!")
    else:    
        print ("This is incorrect, the correct answer is: " + str(correct_answer_add) + ".")


#defining the random subtraction question generator
def random_question_sub():
    global score
    num1 = random_number(10, 20)
    num2 = random_number(1, 10)
    question = "What is " + str(num1) + " " + "-" + " " + str(num2) + " ?"
    print (question)
    correct_answer_sub = num1 - num2 
    user_answer_sub = int(input("Please type you answer here: "))
    if user_answer_sub == correct_answer_sub:
        score += 1
        print ("You are correct!")
    else:
        print ("This is incorrect, the correct answer is: " + str(correct_answer_sub) + ".")
    

#defining the random multiplication question generator
def random_question_mult():
    global score
    num1 = random_number(10, 20)
    num2 = random_number(1, 10)
    question =  "What is " + str(num1) + " " + "*" + " " + str(num2) + " ?"
    print (question)
    correct_answer_mult = num1 * num2
    user_answer_mult = int(input("Please type you answer here: "))
    if user_answer_mult == correct_answer_mult:
        score += 1
        print ("You are correct!")
    else:
        print ("This is incorrect, the correct answer is: " + str(correct_answer_mult) + ".")
    

#defining the random division question generator
def random_question_div():
    global score
    num1 = random_number(10, 20)
    num2 = random_number(1, 10)
    question = "What is " + str(num1) + " " + "/" + " " + str(num2) + " ?"
    print (question)
    correct_answer_div = float (num1 / num2)
    user_answer_div = float (input("Please type you answer here: "))
    if user_answer_div == correct_answer_div:
        score += 1
        print ("You are correct!")
    else:
        print ("This is incorrect, the correct answer is: " + str(correct_answer_div) + ".")


#calling the random question functions to total 10 question
print ()   #creating a space between the questions for better readability      
random_question_mult()  #1
print () 

random_question_add()   #2
print ()

random_question_sub()   #3
print ()

random_question_mult()  #4
print ()

random_question_sub()   #5
print ()

random_question_div()   #6    
print ()

random_question_mult()  #7
print ()

random_question_add()   #8
print ()

random_question_sub()   #9        
print ()

random_question_div()   #10
print ()

#showing the user their score
print ("Your score is: " + str(score))

#determining if the user has passed or failed the quiz
if score >= 8:
    print ("Congratulations " + username + ", you have passed the quiz!")   

else:
    print ("Sorry " + username + ", you have failed the quiz. Better luck next time!")  








 

   









