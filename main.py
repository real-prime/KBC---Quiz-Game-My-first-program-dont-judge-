import os
import time
import sys

def clear_screen():
    """Clears the terminal screen."""
    # Works for Windows and Linux/Mac
    os.system('cls' if os.name == 'nt' else 'clear')
def cooldown():
    time.sleep(1)
def question():
    print("""
░██████╗░██╗░░░██╗███████╗░██████╗████████╗██╗░█████╗░███╗░░██╗██╗
██╔═══██╗██║░░░██║██╔════╝██╔════╝╚══██╔══╝██║██╔══██╗████╗░██║╚═╝
██║██╗██║██║░░░██║█████╗░░╚█████╗░░░░██║░░░██║██║░░██║██╔██╗██║░░░
╚██████╔╝██║░░░██║██╔══╝░░░╚═══██╗░░░██║░░░██║██║░░██║██║╚████║░░░
░╚═██╔═╝░╚██████╔╝███████╗██████╔╝░░░██║░░░██║╚█████╔╝██║░╚███║██╗
░░░╚═╝░░░░╚═════╝░╚══════╝╚═════╝░░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝╚═╝\n""")
    
def bal():
    print("                                                                                              BALANCE: ", amount)
print("""
██╗░░██╗██████╗░░█████╗░
██║░██╔╝██╔══██╗██╔══██╗
█████═╝░██████╦╝██║░░╚═╝
██╔═██╗░██╔══██╗██║░░██╗
██║░╚██╗██████╦╝╚█████╔╝
╚═╝░░╚═╝╚═════╝░░╚════╝░""")
print("""
Welcome to **KBC – Kaun Banega Crorepati (Quiz Game)**

📝 Instructions:
1. You will be asked 5 questions with different prize money (game money).
2. Each question has 4 options (a,b, c, d) – only one is correct.
3. Type the option letter (a/b/c/d) to lock your answer.
4. Answer carefully! Wrong answers may end the game.
5. Good luck and play honestly!

Let's begin... (Press 'ENTER' key to continue)
""")
input1 = (input(""))
if(input1 == ""):
    clear_screen()
print("""
██████╗░███████╗████████╗░█████╗░██╗██╗░░░░░░██████╗
██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██║██║░░░░░██╔════╝
██║░░██║█████╗░░░░░██║░░░███████║██║██║░░░░░╚█████╗░
██║░░██║██╔══╝░░░░░██║░░░██╔══██║██║██║░░░░░░╚═══██╗
██████╔╝███████╗░░░██║░░░██║░░██║██║███████╗██████╔╝
╚═════╝░╚══════╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝╚══════╝╚═════╝░""")
print("----------------------------------------------")
name = (input("ENTER YOUR NAME: "))
age = (input("ENTER YOUR AGE(IN NUMBERS): "))
expmoney = int(input("ENTER AMOUNT YOU EXPECT YOU CAN WIN(MAX:31,000,000): "))
print("----------------------------------------------")
if(expmoney>31000000):
    print("THE AMOUNT IS MORE THAN THE LIMIT! ENTER LESSER AMOUNT")
    cooldown()
    sys.exit()
clear_screen()
amount = int(0)

# QUESTION 1

print("""
░██████╗░██╗░░░██╗███████╗░██████╗████████╗██╗░█████╗░███╗░░██╗██╗
██╔═══██╗██║░░░██║██╔════╝██╔════╝╚══██╔══╝██║██╔══██╗████╗░██║╚═╝
██║██╗██║██║░░░██║█████╗░░╚█████╗░░░░██║░░░██║██║░░██║██╔██╗██║░░░
╚██████╔╝██║░░░██║██╔══╝░░░╚═══██╗░░░██║░░░██║██║░░██║██║╚████║░░░
░╚═██╔═╝░╚██████╔╝███████╗██████╔╝░░░██║░░░██║╚█████╔╝██║░╚███║██╗
░░░╚═╝░░░░╚═════╝░╚══════╝╚═════╝░░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝╚═╝\n""")
print("                                                                                         BALANCE: $",amount)
print("Q1. What is the capital of India?")                                       
print("a) Mumbai                b) New Delhi")
print("c) Kolkata               d) Chennai\n")
answer1 = (input("Enter your answer: "))
if(answer1 == "b"):
    print("Your answer is correct! You won 1,000,000$")
    amount += 1000000
    cooldown()
    clear_screen()
elif(answer1 == "a", "c", "d"):
    print("Your answer is wrong! You won nothing :(")
    cooldown()
    clear_screen()
else:
    print("Your option is not valid! You won nothing:(")
    cooldown()
    clear_screen()

# QUESTION 2 

question()
print("                                                                                         BALANCE: $",amount)
print("""Q2. Who is known as the “Father of the Nation” in India?
a) Subhas Chandra Bose             b) Jawaharlal Nehru
c) Mahatma Gandhi                  d) Bhagat \n""")
answer2 = (input("Enter your answer: "))
if(answer2 == "c"):
    print("Your answer is correct! You won 2,000,000$")
    amount += 2000000
    cooldown()
    clear_screen()
elif(answer2 == "a","b","d"):
    print("Your answer is wrong! You won nothing :(")
    cooldown()
    clear_screen()
else:
    print("Your option is not valid! You won nothing:(")
    cooldown()
    clear_screen()

#  QUESTION 3

question()
print("                                                                                         BALANCE: $",amount)
print("""Q3. What is the national currency of India?
a) Dollar                              b) Pound
c) Rupee                               c) Yen\n""")
answer3 = (input("Enter your answer: "))
if(answer3 == "c"):
    print("Your answer is correct! You won 4,000,000$")
    amount += 4000000
    cooldown()
    clear_screen()
elif(answer3 == "a","b","d"):
    print("Your answer is wrong! You won nothing :(")
    cooldown()
    clear_screen()
else:
    print("Your option is not valid! You won nothing:(")
    cooldown()
    clear_screen()

# QUESTION 4

question()
print("                                                                                         BALANCE: $",amount)
print("""Q4. Who was the first Prime Minister of India?
a) Mahatma Gandhi                       b) Jawaharlal Nehru
c) Dr. B.R. Ambedkar                    d) Sardar Vallabhbhai Patel\n""")
answer4 = (input("Enter your answer: "))
if(answer4 == "b"):
    print("Your answer is correct! You won 8,000,000$")
    amount += 8000000
    cooldown()
    clear_screen()
elif(answer4 == "a","c","d"):
    print("Your answer is wrong! You won nothing :(")
    cooldown()
    clear_screen()
else:
    print("Your option is not valid! You won nothing:(")
    cooldown()
    clear_screen()

# QUESTION 5

question()
print("                                                                                         BALANCE: $",amount)
print("""Q5. Which is the national animal of India?
a) Lion                                    b) Tiger
c) Elephant                                d) Peacock""")
answer5 = (input("Enter your answer: "))
if(answer5 == "b"):
    print("Your answer is correct! You won 16,000,000$")
    amount += 16000000
    cooldown()
    clear_screen()
elif(answer5 == "a","c","d"):
    print("Your answer is wrong! You won nothing :(")
    cooldown()
    clear_screen()
else:
    print("Your option is not valid! You won nothing:(")
    cooldown()
    clear_screen()

# ending page

print("""
███████╗███╗░░██╗██████╗░██╗███╗░░██╗░██████╗░░░░░░░
██╔════╝████╗░██║██╔══██╗██║████╗░██║██╔════╝░░░░░░░
█████╗░░██╔██╗██║██║░░██║██║██╔██╗██║██║░░██╗░░░░░░░
██╔══╝░░██║╚████║██║░░██║██║██║╚████║██║░░╚██╗░░░░░░
███████╗██║░╚███║██████╔╝██║██║░╚███║╚██████╔╝██╗██╗
╚══════╝╚═╝░░╚══╝╚═════╝░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝╚═╝\n""")
print(f"""🎉 Thanks {name} for playing KBC Quiz Game! 🎉

We hope you enjoyed testing your knowledge.
Keep learning and come back to play again soon. 😊

Goodbye and have a great day!\n""")
if(amount>expmoney):
    print("Congratulations 🎉 you won more money then expect from yourself 😊\n")
elif(amount==expmoney):
    print("Good game! you won the same money you expect from yourself 😊\n")
else:
    print("""Sadly! you have not the money you expect from yourself
          but no problem play again and get your goal 😊\n""")
print("TOTAL MONEY YOU WON: ",amount)
print("")
print("A̲ P̲R̲O̲G̲R̲A̲M̲ B̲Y̲ S̲H̲O̲U̲R̲Y̲A̲\n\n")


print("PRESS 'ENTER' TO EXIT THE PROGRAM.")
exitinput = (input(""))
if(exitinput==""):
    sys.exit()
else:
    print("INPUT IS INVALID! PLEASE PRESS 'ENTER' KEY WITH KEEPING THE BLANK")
