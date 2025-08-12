# Bracket-balancer
A simple Python program to check if a string of brackets is balanced. The program ensures that the user inputs only brackets ((), {}, []) and rejects empty or invalid inputs until a valid one is entered.

Features:
a)Validates user input to ensure only brackets are entered.
b)Rejects empty input with an error message.
c)Uses stack-based logic to check if brackets are balanced.
d)Loops until a valid bracket string is provided.

How It Works:
1)Input Validation:
a)If the input is empty, the program asks again.
b)If the input contains any character other than brackets, it prompts the user to re-enter.
2)Balanced Bracket Check:
a)Uses a stack to store opening brackets.
b)For every closing bracket, checks if it matches the top of the stack.
c)If all brackets match and the stack is empty at the end, the input is balanced.

Technologies Used:
a)Python 3 (No external libraries required)
