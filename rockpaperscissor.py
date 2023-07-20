from tkinter import *
import random

master = Tk()
master.title("Rock Paper Scissors")
master.geometry("300x300")

def play_game(ch):
    B1.configure(state=DISABLED)
    B2.configure(state=DISABLED)
    B3.configure(state=DISABLED)
    choices = ["rock", "paper", "scissors"]
    user_choice = ch
    computer_choice = random.choice(choices)

    if(ch == "rock"):
        textString1.set("You choose : Rock ")
    elif (ch == "paper") :
        textString1.set("You choose : paper ")
    else:
        textString1.set("You choose : Scissors ")

    if(computer_choice == "rock"):
        textString2.set("Computer choose : Rock ")
    elif (computer_choice == "paper") :
        textString2.set("Computer choose : paper ")
    else:
        textString2.set("Computer choose : Scissors ")
    
    if user_choice == computer_choice:
        textString3.set("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        textString3.set("Congratulations! You win!")
    else:
        textString3.set("You lose!")
    B4.configure(state=NORMAL)
    B5.configure(state=NORMAL)
def tryagain():
    B1.configure(state=NORMAL)
    B2.configure(state=NORMAL)
    B3.configure(state=NORMAL)
    B4.configure(state=DISABLED)
    B5.configure(state=DISABLED)
def close():
    master.destroy();

label1 = Label(master, text='Welcome to Rock, Paper, Scissors!')
label2 = Label(master, text='Select your choice: ')

label1.place(relx = 0.5, rely = 0.1, anchor = CENTER)
label2.place(x= 60, y = 50 )
B1 = Button(master, text = "Rock", command = lambda :play_game("rock"))
B1.place(x = 70,y = 90)
B2 = Button(master, text = "Paper", command =lambda : play_game("paper"))
B2.place(x = 130,y = 90)
B3 = Button(master, text = "Scissors", command =lambda : play_game("scissors"))
B3.place(x = 190,y = 90)
textString1 = StringVar()
textString2 = StringVar()
label3 = Label(master,textvariable = textString1)
label4 = Label(master,textvariable = textString2)
label3.place(x = 50 , y = 130 )
label4.place(x = 50 , y = 150 )

textString3 = StringVar()
label5 = Label(master,textvariable = textString3)
label5.place(x = 50 , y = 170 )

label6 = Label(master, text = " Wanna try again ? " )
label6.place(x = 50, y = 200 )

B4 = Button(master, text = "Yes", command= tryagain, state=DISABLED)
B4. place(x = 120, y = 230 )

B5 = Button(master, text = "No", command= close,state=DISABLED)
B5. place(x = 200, y = 230 )
mainloop()
