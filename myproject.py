


import random
from tkinter import Tk,Button,Label
from tkinter import Canvas
root = Tk() 
root.title("stone.paper.sissor") 
root.resizable(False,False)
b = Label(root,text="\nWelcome To My Project \n\n STONE PAPER SISSOR USING GUI(Graphical User Interface)\n\n S.Maguthu Sahith Afri\n\n B.TECH (INFORMATION TECHNOLOGY)\n\n Velammal Insititute OF Technology")
b.pack()
canvas = Canvas(root, width=600, height=600) 
canvas.pack()
root.withdraw()




def score_board(): 
	root2 = Tk() 
	root2.title("stone paper sissor") 
	root2.resizable(False,False)
	canvas2 = Canvas(root2,width=300,height=300) 
	canvas2.pack() 
	
	w = Label(canvas2,text="\nGAME OVER\n\nYOUR SCORE = "
											+ str(list[0]) + "\n\nCOMPUTER SCORE = "
                                                                                                                                              +str(list[1]) + "\n\n"
                                                                                                                                                                                                 +str(list[2]) + "\n\n") 
	w.pack() 
	
	button3 = Button(canvas2, text="PLAY AGAIN", bg="blue", 
						command=lambda:play_again(root2)) 
	button3.pack() 
	
	button4 = Button(canvas2,text="EXIT",bg="red", 
					command=lambda:exit_way(root2)) 
	button4.pack()     
 

def exit_way(root2): 
	root2.destroy() 
	root.destroy() 

def main():
 score=0
 comp_score=0
 

 while True: 

    print("Enter choice \n 1. Rock \n 2. paper \n 3. scissor \n") 

    choice = int(input("User turn: "))

    while choice > 3 or choice < 1: 

        choice = int(input("enter valid input: ")) 

    if choice == 1: 

        choice_name = 'stone' 

    elif choice == 2: 

        choice_name = 'paper' 

    else: 

        choice_name = 'scissor' 

    print("user choice is: " + choice_name) 

    print("\nNow its computer turn.......")

    comp_choice = random.randint(1, 3)

    while comp_choice == choice: 

        comp_choice = random.randint(1, 3) 

    if comp_choice == 1: 

        comp_choice_name = 'stone' 

    elif comp_choice == 2: 

        comp_choice_name = 'paper' 

    else: 

        comp_choice_name = 'scissor' 

          

    print("Computer choice is: " + comp_choice_name)

    print(choice_name + " V/s " + comp_choice_name) 

    if((choice == 1 and comp_choice == 2) or 

      (choice == 2 and comp_choice ==1 )): 

        print("paper wins => ", end = "") 

        result = "paper" 

    elif((choice == 1 and comp_choice == 3) or 

        (choice == 3 and comp_choice == 1)): 

        print("stone wins =>", end = "") 

        result = "Rock" 

    else: 

        print("scissor wins =>", end = "") 

        result = "scissor" 

    if result == choice_name: 

        print("<== User wins ==>")
        score+=1
    

    
    else: 

        print("<== Computer wins ==>")
        comp_score+=1

          

    print("Do you want to play again? (Y/N)") 

    ans = input()

    if(ans == 'n' or ans == 'N'): 

       break

 if(score==comp_score):
     final_winner="MATCH DRAW"
 elif(score>comp_score):
     final_winner="YOU WON"
 else:
     final_winner="YOU LOSE"
 return [score,comp_score,final_winner]


def play_again(root2): 
	root2.destroy()
	a,b,c=main()
	list.append(a)
	list.append(b)
	list.append(c)
	score_board()
	del list[0:3]


 
print("Winning Rules of the Rock paper scissor game as follows: \n" 

                                +"stone vs paper->paper wins \n" 

                                + "stone vs scissor->stone wins \n" 

                                +"paper vs scissor->scissor wins \n")
list=main()
score_board()
del list[0:3]









