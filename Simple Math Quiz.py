#asking the user for their name
username = input("What is your name? ")

#greeting the user and awellcoming them to the quiz
print("Hello " + username + ", Welcome to your Math Quiz!")

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

def user_answer_add():
    user_answer = input("Please type you answer here: ")
    print (user_answer)

def correct_answer_add(): 
    correct_answer = "The correct answer is",  num1 + num2
    print (correct_answer)  
    

def random_question_sub():
    return "What is " + str(num1) + " " + "-" + " " + str(num2) + " ?"
    print (random_question_sub())

def random_question_mult():
    return "What is " + str(num1) + " " + "*" + " " + str(num2) + " ?"
    print (random_question_mult())

def random_question_div():
    return "What is " + str(num1) + " " + "/" + " " + str(num2) + " ?"
    print (random_question_div())


random_question_add()
user_answer_add()
correct_answer_add()
#correct answer may need own def to get userannswer = correcT answer

 

   









