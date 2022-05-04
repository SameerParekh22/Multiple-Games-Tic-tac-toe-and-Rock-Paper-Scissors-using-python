from tkinter import *
from tkinter import messagebox


# tick tock toe functions 
def tick_tack_toe():
    hide_frames()
    b1=Button(tik_tock_frame, text=" ", height=BUTTON_HEIGHT, width=BUTTON_WIDTH,bg= "white", command=lambda:b_click(b1))
    b2=Button(tik_tock_frame, text=" ", height=BUTTON_HEIGHT, width=BUTTON_WIDTH,bg= "white", command=lambda:b_click(b2))
    b3=Button(tik_tock_frame, text=" ", height=BUTTON_HEIGHT, width=BUTTON_WIDTH,bg= "white", command=lambda:b_click(b3))
    b4=Button(tik_tock_frame, text=" ", height=BUTTON_HEIGHT, width=BUTTON_WIDTH,bg= "white", command=lambda:b_click(b4))
    b5=Button(tik_tock_frame, text=" ", height=BUTTON_HEIGHT, width=BUTTON_WIDTH,bg= "white", command=lambda:b_click(b5))
    b6=Button(tik_tock_frame, text=" ", height=BUTTON_HEIGHT, width=BUTTON_WIDTH,bg= "white", command=lambda:b_click(b6))
    b7=Button(tik_tock_frame, text=" ", height=BUTTON_HEIGHT, width=BUTTON_WIDTH,bg= "white", command=lambda:b_click(b7))
    b8=Button(tik_tock_frame, text=" ", height=BUTTON_HEIGHT, width=BUTTON_WIDTH,bg= "white", command=lambda:b_click(b8))
    b9=Button(tik_tock_frame, text=" ", height=BUTTON_HEIGHT, width=BUTTON_WIDTH,bg= "white", command=lambda:b_click(b9))
    
    #arranging the buttons
    b1.grid(row=0,column=0,padx=BX,pady=BY)
    b2.grid(row=0,column=1,padx=BX,pady=BY)
    b3.grid(row=0,column=2,padx=BX,pady=BY)
    b4.grid(row=1,column=0,padx=BX,pady=BY)
    b5.grid(row=1,column=1,padx=BX,pady=BY)
    b6.grid(row=1,column=2,padx=BX,pady=BY)
    b7.grid(row=2,column=0,padx=BX,pady=BY)
    b8.grid(row=2,column=1,padx=BX,pady=BY)
    b9.grid(row=2,column=2,padx=BX,pady=BY)
        

    tik_tock_frame.pack(fill="both",expand=1,padx=FRAME_PADDINGX,pady=FRAME_PADDINGY)
    
    def checkifwon():
        global winner
        winner = False
    
        if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
            b1.config(bg="red")
            b2.config(bg="red")
            b3.config(bg="red")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "Congradulations you have won the game!")
            disable_all_buttons()
    
        elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
            b4.config(bg="red")
            b5.config(bg="red")
            b6.config(bg="red")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "congradulations you have won the game!")
            disable_all_buttons()
    
        elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
            b7.config(bg="red")
            b8.config(bg="red")
            b9.config(bg="red")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "congradulations you have won the game!")
            disable_all_buttons()
    
        elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
            b1.config(bg="red")
            b5.config(bg="red")
            b9.config(bg="red")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "congradulations you have won the game!")
            disable_all_buttons()
        elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
            b3.config(bg="red")
            b5.config(bg="red")
            b7.config(bg="red")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "congradulations you won the game!")
            disable_all_buttons()
        elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
            b1.config(bg="red")
            b4.config(bg="red")
            b7.config(bg="red")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "congradulations you won the game!")
            disable_all_buttons()
        elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
            b2.config(bg="red")
            b5.config(bg="red")
            b8.config(bg="red")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "congradulations you won the game!")
            disable_all_buttons()
        elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
            b3.config(bg="red")
            b6.config(bg="red")
            b9.config(bg="red")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "congradulations you won the game!")
            disable_all_buttons()
        elif b3["text"] == "O" and b6["text"] == "O" and b9 ["text"] == "O":
            b1.config(bg="red")
            b2.config(bg="red")
            b3.config(bg="red")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "congradulations you won the game!")
            disable_all_buttons()
        elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
            b4.config(bg="red")
            b5.config(bg="red")
            b6.config(bg="red")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "congradulations you have won the game!")
            disable_all_buttons()
        elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
            b7.config(bg="red")
            b8.config(bg="red")
            b9.config(bg="red")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "congradulations you have won the game!")
            disable_all_buttons()
        elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
            b1.config(bg="red")
            b5.config(bg="red")
            b9.config(bg="red")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "congradulations you have won the game!")
            disable_all_buttons()
        elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
            b3.config(bg="red")
            b5.config(bg="red")
            b7.config(bg="red")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "congradulations you have won the game!")
            disable_all_buttons()
        elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
            b1.config(bg="red")
            b4.config(bg="red")
            b7.config(bg="red")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "Congradulations you have won the game!")
            disable_all_buttons()
        elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
            b2.config(bg="red")
            b5.config(bg="red")
            b8.config(bg="red")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "congradulations you have won the game!")
            disable_all_buttons()
        elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
            b3.config(bg="red")
            b6.config(bg="red")
            b9.config(bg="red")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "congradulations you have won the game!")
            disable_all_buttons()

        if count == 9 and  winner == False:
            messagebox.showinfo("Tic Tac Toe", "Hey! It's a draw!")
            disable_all_buttons()
    
  
    def b_click(b):
        global clicked,count
    
        if b["text"] == " " and clicked == True:
            b["text"] = "X"
            clicked = False
            count += 1
            checkifwon()
        elif b["text"] == " " and clicked == False:
            b["text"] = "O"
            clicked = True
            count += 1
            checkifwon()
        else:
            messagebox.showerror("Tic Tac Toe", "Hey! That box has already been selected!")
            checkifwon()
        

    def disable_all_buttons():
        b1.config(state=DISABLED)
        b2.config(state=DISABLED)
        b3.config(state=DISABLED)
        b4.config(state=DISABLED)
        b5.config(state=DISABLED)
        b6.config(state=DISABLED)
        b7.config(state=DISABLED)
        b8.config(state=DISABLED)
        b9.config(state=DISABLED)
        
    

##########################################################################################################
# rock paper scissor functions
def rock_paper_scissor():
    hide_frames()
    
    welcomelabel=Label(rock_paper_frame,text="WELCOME TO ROCK PAPER SCISSOR",bg="black",padx=10,pady=10,justify="center",font=(40))
    welcomelabel.configure(foreground="white")
    welcomelabel.pack()
    rock_paper_frame.pack(fill="both",expand=1)
    
    qlabel=Label(rock_paper_frame,text="DARE TO CHALLENGE SYSTEM?",bg="black",padx=10,pady=10,justify="center",font=(38))
    qlabel.configure(foreground="white")
    qlabel.pack()
    rock_paper_frame.pack(fill="both",expand=2)
    
    PlayerLabel=Label(rock_paper_frame,text="PLEASE CHOOSE ONE OF THE BELOW:",justify="center",padx=10,pady=10,bg="black",font=(36))
    PlayerLabel.configure(foreground="white")
    PlayerLabel.pack()
    rock_paper_frame.pack(fill="both",expand=2)
    
    
    #TO GENERATE A RANDOM VALUE FOR COMPUTER.


#TO CREATE THREE BUTTONS.
    import random
    def rockClick():
        optionList=['ROCK','PAPER','SCISSOR']
        import random
        computerOption=random.choice(optionList)
        
       
        if computerOption=='ROCK':
            compLabel.config(text="COMPUTER CHOSE:ROCK")
            show_rock()
            resultLabel.config(text="RESULT=TIE")
        elif computerOption=='PAPER':
            compLabel.config(text="COMPUTER CHOSE:PAPER")
            resultLabel.config(text="RESULT=COMPUTER WINS")
        elif computerOption=='SCISSOR':
            compLabel.config(text="COMPUTER CHOSE:SCISSOR")
            resultLabel.config(foreground="green",text="RESULT=PLAYER WINS")
 

    rockButton=Button(rock_paper_frame,text="ROCK",bg="grey",command=rockClick,height="5",width="10").place(x="280",
                                                    y="200")
    
    def scissorClick():
        optionList=['ROCK','PAPER','SCISSOR']
        import random
        computerOption=random.choice(optionList)
        
    
        
        if computerOption=='ROCK':
            compLabel.config(text="COMPUTER CHOSE:ROCK")
            resultLabel.config(foreground="red",text="RESULT=COMPUTER WINS")
        elif computerOption=='PAPER':
             compLabel.config(foreground="green",text="COMPUTER CHOSE:PAPER")
             resultLabel.config(foreground="green",text="RESULT=PLAYER WINS") 
        elif computerOption=='SCISSOR':
             compLabel.config(text="COMPUTER CHOSE:SCISSOR")
             resultLabel.config(text="RESULT=TIED")

    scissorButton=Button(rock_paper_frame,text="SCISSOR",bg="grey",command=scissorClick,height="5",width="10",justify="center").place(x="360",
                                                                                                                                     y="200")
    
   

    
    def paperClick():
        optionList=['ROCK','PAPER','SCISSOR']
        import random
        computerOption=random.choice(optionList)
       
       
        if computerOption=='ROCK':
            compLabel.config(text="COMPUTER CHOSE:ROCK")
            resultLabel.config(foreground="green",text="RESULT=PLAYER WINS")     
        elif computerOption=='PAPER':
            compLabel.config(text="COMPUTER CHOSE:PAPER")
            resultLabel.config(text="RESULT=TIED") 
        elif computerOption=='SCISSOR':
            compLabel.config(text="COMPUTER CHOSE:SCISSOR")
            resultLabel.config(text="RESULT=COMPUTER WINS")

    paperButton=Button(rock_paper_frame,text="PAPER",bg="grey",command=paperClick,height="5",width="10",justify="center").place(x="440",
                                                    y="200")
    
    #result label
    #result label
    resultLabel=Label(rock_paper_frame,text=" ",bg="grey",padx=10,pady=10)
    resultLabel.pack()
    rock_paper_frame.pack(fill="both",expand=2)
    compLabel=Label(root,text=" ",bg="grey",padx=10,pady=10)
    rock_paper_frame.pack(fill="both",expand=2)
    compLabel.pack()

def show_rock():
    from PIL import ImageTk,Image
    img=ImageTk.PhotoImage(Image.open("rock.png"))
    #img=PhotoImage(file='rock.png')
    lal=Label(rock_paper_frame,image=img)
    lal.pack()
    rock_paper_frame.pack(x=20,y=20)

def hide_frames():
    splash_frame.pack_forget()
    tik_tock_frame.pack_forget()
    rock_paper_frame.pack_forget()
    
def splash_image_frame():
    pass
    # img = PhotoImage(file='nature.png')
    # lbl = Label(splash_frame, image=img)
    # lbl.pack()
    # splash_frame.pack

def top_menu():
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Tick Tack Toe", command=tick_tack_toe)
    filemenu.add_command(label="Rock Paper Scissor", command=rock_paper_scissor)
    menubar.add_cascade(label="Games", menu=filemenu)
    return menubar

def create_main_window(w=800, h=600):
    root.title('Multi Game Program')
    # get screen width and height
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    # calculate position x, y
    x = (ws/2) - (w/2)    
    y = (hs/2) - (h/2)
    # set main windows position
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))

def main():
    create_main_window(800, 600)
    menubar = top_menu()
    root.config(menu=menubar)
    
    splash_image_frame()
    
    root.mainloop()

# main programs starts from here..
# global variables
root = Tk()
splash_frame = Frame(root, bg="white")
tik_tock_frame = Frame(root,bg="black")
rock_paper_frame = Frame(root, bg="black")

#variables for tic tock game
clicked = True
count=0
BUTTON_WIDTH=31
BUTTON_HEIGHT=10
FRAME_PADDINGX=40
FRAME_PADDINGY=40
BX=5
BY=5

#if name == "main":
main()
