#interactive PC Quiz by DC
#module import

import time
import webbrowser

#main questions and if-else statements
intro = (input("Hello ! Do you want to play the quiz? The PC quiz? Only for enthusiasts! \n"))
score = 0
if "Yes" or "Sure" or "Alright" or "Why not?" or "Of Course" or "yes" in intro:
    print('''Alright, let's move further.
         ''') 
    
    time.sleep (4)
    
    question_1 = (input("What is the full form of CPU? \n"))
    if "Central Proccessing Unit" or "Central proccessing unit" or "central proccessing unit" in question_1:
        print("Wow ! Correct answer! Kindly wait for 5 secs.")
        score = score+1
    else:
        print("Oops, incorrect answer! Kindly wait for 5 secs.")

    time.sleep (5)
    
    question_2 = (input("What is the full form of GPU? \n"))
    if "Graphical Processing Unit" or "Graphical processing unit" or "graphical processing unit" in question_2:
        print("Wow ! Correct answer! Kindly wait for 5 secs.")
        score = score+1
    else:
        print("Oops, incorrect answer! Kindly wait for 5 secs.")    

    time.sleep (5)

    question_1 = (input("What is the full form of RAM? \n"))
    if "Random Access Memory" or "Random access memory" or "random access memory" in question_1:
        print("Wow ! Correct answer! \n")
        score = score+1
    else:
        print("Oops, incorrect answer!")   
    
else:
    print("Alright, as you wish.")
    quit()

time.sleep (2)

#loading section
print("Calculating your score...")

time.sleep (3)

#result section
print ("\n You have scored", score, "marks in our quiz.")
if score > 1:
    print ("\n CONGRATULATIONS ! You have passed our quiz!")
else:
    opinion = str(input("\n You have scored very less in our quiz. Do you want us to open a web page for you to learn the basics and prepare best for the next time? \n"))
    if "Yes" or "Sure" or "Alright" or "Why not?" or "Of Course" or "yes" in opinion:
        webbrowser.open("htutorialspoint.com/basics_of_computers/index.htm")
    else:
        print("No problem. Have a great day.")

#-end-