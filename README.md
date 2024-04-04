# Simple-Math-Quiz

## Objective
To create a simple math quiz for elementary school students that:
 1. Asks the student for their name.
 2. Displays a personalized message on the student's screen that welcomes the 
    student to the math quiz.
 3. Presents the student with 10 random math questions based on addition, 
    subtraction, multiplication and division.
 4. Checks the student's answer with the correct answer.
 5. Lets the student know if their answer was correct or incorrect.
 6. Displays the correct answer if the answer was incorrect.
 7. Keeps track of the student's score by adding 1 point to every correct 
    answer.
 8. Lets the student know their score at the end of the quiz.
 9. Lets the student know if they based or failed the quiz.     

Project Steps
1.	Used the input function to get the student’s name inside the username variable.
2.	Printed the welcome message on the screen using the print function and let the student know how many points are needed to pass the test.
3.	Set the score variable to 0.
4.	Printed the number of points needed to pass the quiz using the print function.
5.	Created a user-defined function named random_number to generate a random number for variables num1 and num2.
6.	Assigned the num1 variable to generate a random number between 10 and 20 and the num2 variable to generate a random number between 1 and 10.
7.	Created 4 user-defined question function that:
    a.	Enables our score variable to be modified inside the function by using the global keyword.
b.	Generate a random number for our num1 and num2 variables. 
c.	Creates a question variable that prints an addition, subtraction, multiplication, and division question using the num1 and num2 variables set within our function.

d.	Converting the num1 and num2 variables to strings to concatenate the other strings within the question.

e.	Prints the question.

f.	Sets the correct answer variable to equate to the random num 1 and num2 variables based on the math operation used.

g.	Used the input function to get the students answer, converted the user answer to an integer and set it within the user answer variable.

h.	Used the if else statements to print ‘correct’ or ‘incorrect’ along with the correct answer if incorrect by comparing the user’s answer to the correct answer variables.

i.	Increases the score by 1 if the answer is correct.

8.	Called the user- defined question function 10 times for a total of 10 questions.
9.	Showed the student their score using the print function and the score variable.
10.	Used the if else statements and the print function to let the student know if they passed or failed the test based on the number of points accumulated.
