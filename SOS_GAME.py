from tkinter import *
root = Tk()
from itertools import chain


#declaring of variables
root.configure(bg='black')
player_1_score = [0]
player_2_score = [0]
round = 0
P1 = Label(root,padx=265, pady=33,text="current player is Player 1", bg='grey15', fg='purple')
P1.grid(row = 5, column = 0, columnspan=8)
P1_counter = Label(root, text="P1's score is: 0", padx=99, pady=33,fg='green',bg='grey20',borderwidth=0)
P2_counter = Label(root, text="P2's score is: 0", padx=99, pady=33,fg='green',bg='grey20',borderwidth=0)
counter = 0


def check_S(row, col):   #checks whether there's a win condition around the pressed S

    global player_1_score, player_2_score, round
    player_score = player_1_score if round%2==0 else player_2_score

    if col + 2 <= 3 and grid[row] [col+1] == 'O' and grid[row] [col+2] == 'S': #checks if the column on its right and the one after that are O S and the rest under this line
        player_score[0] += 1                                                   # are doing the same with slight adjustment
    if col - 2 >= 0 and grid[row] [col-1] == 'O' and grid[row] [col-2] == 'S':
        player_score[0] += 1
    if row + 2 <= 3 and grid[row+1] [col] == 'O' and grid[row+2] [col] == 'S':
        player_score[0] += 1
    if row - 2 >= 0 and grid[row-1] [col] == 'O' and grid[row-2] [col] == 'S':
        player_score[0] += 1
    if col + 2 <= 3 and row + 2 <= 3 and grid[row+1] [col+1] == 'O' and grid[row+2] [col+2] == 'S':
        player_score[0] += 1
    if col - 2 >= 0 and row - 2 >= 0 and grid[row-1] [col-1] == 'O' and grid[row-2] [col-2] == 'S':
        player_score[0] += 1
    if col + 2 <= 3 and row - 2 >= 0 and grid[row-1] [col+1] == 'O' and grid[row-2] [col+2] == 'S':
        player_score[0] += 1
    if col - 2 >= 0 and row + 2 <= 3 and grid[row+1] [col-1] == 'O' and grid[row+2] [col-2] == 'S':
        player_score[0] += 1
    
    


def check_O(row, col):  #checks whether there's a win condition around the pressed O
    
    global player_1_score, player_2_score, round
#    player = 'player_1' if round%2 == 0 else 'player_2'
    player_score = player_1_score if round%2==0 else player_2_score
    
    if col-1 >= 0 and col+1 <= 3 and grid[row] [col-1] == 'S' and grid[row] [col+1] == 'S':
        player_score[0] += 1
    if row-1 >= 0 and row+1 <= 3 and grid[row-1] [col] == 'S' and grid[row+1] [col] == 'S':
        player_score[0] += 1
    if row-1 >= 0 and col >= 0 and row+1 <=3 and col+1 <= 3 and grid[row-1] [col+1] == 'S' and grid[row+1] [col-1] == 'S':
        player_score[0] += 1
    if row-1 >= 0 and col >= 0 and row+1 <=3 and col+1 <=3 and grid[row+1] [col-1] == 'S' and grid[row-1] [col+1] == 'S':
        player_score[0] += 1



def player_separation(row, col, O_or_S):    #separates player one from player two by using a round counter, it also tells the code whether to check for S or to check for O
    global round, player_1_score, player_2_score, counter
    round += 1
    if O_or_S == 'S':
        check_S(row, col)
    elif O_or_S == 'O':
        check_O(row, col)
    player_visual()
    counter += 1
    if counter == 16:
        game_end()





def S_big(): #declares 16 big labels with S written on them
    for a in range(0,16):
        globals()[f"S_big_{a}"] = Label(root, text="S", padx=56, pady=33,fg='magenta',bg='black',borderwidth=0)
S_big()



def O_big(): #declares 16 big labels with O written on them
    for a in range(0,16):
        globals()[f"O_big_{a}"] = Label(root, text="O", padx=56, pady=33,fg='magenta',bg='black',borderwidth=0)
O_big()

def O_press(c):         #functionality when O is pressed, calls player_Separation() and removes the button pressed and the button adjacent to it and places a big O instead
    if c == 0:
        player_separation(0, 0, 'O')
        grid[0][0] = 'O'
        S_button_0.grid_forget()
        O_button_0.grid_forget()
        O_big_0.grid(row=0, column=0, columnspan=2)
    elif c == 1:
        player_separation(1, 0, 'O')
        grid[1][0] = 'O'
        S_button_1.grid_forget()
        O_button_1.grid_forget()
        O_big_1.grid(row=1, column=0, columnspan=2)
    elif c == 2:
        player_separation(2, 0, 'O')
        grid[2][0] = 'O'
        S_button_2.grid_forget()
        O_button_2.grid_forget()
        O_big_2.grid(row=2, column=0, columnspan=2)
    elif c == 3:
        player_separation(3, 0, 'O')
        grid[3][0] = 'O'
        S_button_3.grid_forget()
        O_button_3.grid_forget()
        O_big_3.grid(row=3, column=0, columnspan=2)
    elif c == 4:
        player_separation(0, 1, 'O')
        grid[0][1] = 'O'
        S_button_4.grid_forget()
        O_button_4.grid_forget()
        O_big_4.grid(row=0, column=2, columnspan=2)
    elif c == 5:
        player_separation(1, 1, 'O')
        grid[1][1] = 'O'
        S_button_5.grid_forget()
        O_button_5.grid_forget()
        O_big_5.grid(row=1, column=2, columnspan=2)
    elif c == 6:
        player_separation(2, 1, 'O')
        grid[2][1] = 'O'
        S_button_6.grid_forget()
        O_button_6.grid_forget()
        O_big_6.grid(row=2, column=2, columnspan=2)
    elif c == 7:
        player_separation(3, 1, 'O')
        grid[3][1] = 'O'
        S_button_7.grid_forget()
        O_button_7.grid_forget()
        O_big_7.grid(row=3, column=2, columnspan=2)
    elif c == 8:
        player_separation(0, 2, 'O')
        grid[0][2] = 'O'
        S_button_8.grid_forget()
        O_button_8.grid_forget()
        O_big_8.grid(row=0, column=4, columnspan=2)
    elif c == 9:
        player_separation(1, 2, 'O')
        grid[1][2] = 'O'
        S_button_9.grid_forget()
        O_button_9.grid_forget()
        O_big_9.grid(row=1, column=4, columnspan=2)
    elif c == 10:
        player_separation(2, 2, 'O')
        grid[2][2] = 'O'
        S_button_10.grid_forget()
        O_button_10.grid_forget()
        O_big_10.grid(row=2, column=4, columnspan=2)
    elif c == 11:
        player_separation(3, 2, 'O')
        grid[3][2] = 'O'
        S_button_11.grid_forget()
        O_button_11.grid_forget()
        O_big_11.grid(row=3, column=4, columnspan=2)
    elif c == 12:
        player_separation(0, 3, 'O')
        grid[0][3] = 'O'
        S_button_12.grid_forget()
        O_button_12.grid_forget()
        O_big_12.grid(row=0, column=6, columnspan=2)
    elif c == 13:
        player_separation(1, 3, 'O')
        grid[1][3] = 'O'
        S_button_13.grid_forget()
        O_button_13.grid_forget()
        O_big_13.grid(row=1, column=6, columnspan=2)
    elif c == 14:
        player_separation(2, 3, 'O')
        grid[2][3] = 'O'
        S_button_14.grid_forget()
        O_button_14.grid_forget()
        O_big_14.grid(row=2, column=6, columnspan=2)
    elif c == 15:
        player_separation(3, 3, 'O')
        grid[3][3] = 'O'
        S_button_15.grid_forget()
        O_button_15.grid_forget()
        O_big_15.grid(row=3, column=6, columnspan=2)

def S():                #functionality when S is pressed, calls player_Separation() and removes the button pressed and the button adjacent to it and places a big S instead
    globals()[f"S_button_0"] = Button(root, text="S", padx=28, pady=33, command=lambda: S_press(0), fg='green',
                                      bg='black', borderwidth=0)
    globals()[f"S_button_1"] = Button(root, text="S", padx=28, pady=33, command=lambda: S_press(1), fg='green',
                                      bg='black', borderwidth=0)
    globals()[f"S_button_2"] = Button(root, text="S", padx=28, pady=33, command=lambda: S_press(2), fg='green',
                                      bg='black', borderwidth=0)
    globals()[f"S_button_3"] = Button(root, text="S", padx=28, pady=33, command=lambda: S_press(3), fg='green',
                                      bg='black', borderwidth=0)
    globals()[f"S_button_4"] = Button(root, text="S", padx=28, pady=33, command=lambda: S_press(4), fg='green',
                                      bg='black', borderwidth=0)
    globals()[f"S_button_5"] = Button(root, text="S", padx=28, pady=33, command=lambda: S_press(5), fg='green',
                                      bg='black', borderwidth=0)
    globals()[f"S_button_6"] = Button(root, text="S", padx=28, pady=33, command=lambda: S_press(6), fg='green',
                                      bg='black', borderwidth=0)
    globals()[f"S_button_7"] = Button(root, text="S", padx=28, pady=33, command=lambda: S_press(7), fg='green',
                                      bg='black', borderwidth=0)
    globals()[f"S_button_8"] = Button(root, text="S", padx=28, pady=33, command=lambda: S_press(8), fg='green',
                                      bg='black', borderwidth=0)
    globals()[f"S_button_9"] = Button(root, text="S", padx=28, pady=33, command=lambda: S_press(9), fg='green',
                                      bg='black', borderwidth=0)
    globals()[f"S_button_10"] = Button(root, text="S", padx=28, pady=33, command=lambda: S_press(10), fg='green',
                                       bg='black', borderwidth=0)
    globals()[f"S_button_11"] = Button(root, text="S", padx=28, pady=33, command=lambda: S_press(11), fg='green',
                                       bg='black', borderwidth=0)
    globals()[f"S_button_12"] = Button(root, text="S", padx=28, pady=33, command=lambda: S_press(12), fg='green',
                                       bg='black', borderwidth=0)
    globals()[f"S_button_13"] = Button(root, text="S", padx=28, pady=33, command=lambda: S_press(13), fg='green',
                                       bg='black', borderwidth=0)
    globals()[f"S_button_14"] = Button(root, text="S", padx=28, pady=33, command=lambda: S_press(14), fg='green',
                                       bg='black', borderwidth=0)
    globals()[f"S_button_15"] = Button(root, text="S", padx=28, pady=33, command=lambda: S_press(15), fg='green',
                                       bg='black', borderwidth=0)
S()



def O():    #defines the O buttons
    globals()[f"O_button_0"] = Button(root, text="O", padx=28, pady=33, command=lambda: O_press(0),fg='green',bg='black',borderwidth=0)
    globals()[f"O_button_1"] = Button(root, text="O", padx=28, pady=33, command=lambda: O_press(1),fg='green',bg='black',borderwidth=0)
    globals()[f"O_button_2"] = Button(root, text="O", padx=28, pady=33, command=lambda: O_press(2),fg='green',bg='black',borderwidth=0)
    globals()[f"O_button_3"] = Button(root, text="O", padx=28, pady=33, command=lambda: O_press(3),fg='green',bg='black',borderwidth=0)
    globals()[f"O_button_4"] = Button(root, text="O", padx=28, pady=33, command=lambda: O_press(4),fg='green',bg='black',borderwidth=0)
    globals()[f"O_button_5"] = Button(root, text="O", padx=28, pady=33, command=lambda: O_press(5),fg='green',bg='black',borderwidth=0)
    globals()[f"O_button_6"] = Button(root, text="O", padx=28, pady=33, command=lambda: O_press(6),fg='green',bg='black',borderwidth=0)
    globals()[f"O_button_7"] = Button(root, text="O", padx=28, pady=33, command=lambda: O_press(7),fg='green',bg='black',borderwidth=0)
    globals()[f"O_button_8"] = Button(root, text="O", padx=28, pady=33, command=lambda: O_press(8),fg='green',bg='black',borderwidth=0)
    globals()[f"O_button_9"] = Button(root, text="O", padx=28, pady=33, command=lambda: O_press(9),fg='green',bg='black',borderwidth=0)
    globals()[f"O_button_10"] = Button(root, text="O", padx=28, pady=33, command=lambda: O_press(10),fg='green',bg='black',borderwidth=0)
    globals()[f"O_button_11"] = Button(root, text="O", padx=28, pady=33, command=lambda: O_press(11),fg='green',bg='black',borderwidth=0)
    globals()[f"O_button_12"] = Button(root, text="O", padx=28, pady=33, command=lambda: O_press(12),fg='green',bg='black',borderwidth=0)
    globals()[f"O_button_13"] = Button(root, text="O", padx=28, pady=33, command=lambda: O_press(13),fg='green',bg='black',borderwidth=0)
    globals()[f"O_button_14"] = Button(root, text="O", padx=28, pady=33, command=lambda: O_press(14),fg='green',bg='black',borderwidth=0)
    globals()[f"O_button_15"] = Button(root, text="O", padx=28, pady=33, command=lambda: O_press(15),fg='green',bg='black',borderwidth=0)
O()


def O_Visual():     #places the buttons declared earlier on the screen
    for c in range(0,4):
        globals()[f"O_button_{c}"].grid(row=c, column=1)
    for c in range(0,4):
        globals()[f"O_button_{c+4}"].grid(row=c, column=3)
    for c in range(0,4):
        globals()[f"O_button_{c+8}"].grid(row=c, column=5)
    for c in range(0,4):
        globals()[f"O_button_{c+12}"].grid(row=c, column=7)
O_Visual()

def S_Visual():     #places the buttons declared earlier on the screen
    for c in range(0, 4):
        globals()[f"S_button_{c}"].grid(row=c, column=0)
    for c in range(0, 4):
        globals()[f"S_button_{c+4}"].grid(row=c, column=2)
    for c in range(0, 4):
        globals()[f"S_button_{c+8}"].grid(row=c, column=4)
    for c in range(0, 4):
        globals()[f"S_button_{c+12}"].grid(row=c, column=6)
S_Visual()



def build_matrix(rows, cols):   #builds a 2D matrix
    matrix = []

    for r in range(0, rows):
        matrix.append([0 for c in range(0, cols)])

    return matrix



grid = build_matrix(4, 4)



def S_press(c):     #functionality of the button S
    if c == 0:
        player_separation(0, 0, 'S')
        grid[0][0] = 'S'
        S_button_0.grid_forget()
        O_button_0.grid_forget()
        S_big_0.grid(row=0, column=0, columnspan=2)
    elif c == 1:
        player_separation(1, 0, 'S')
        grid[1][0] = 'S'
        S_button_1.grid_forget()
        O_button_1.grid_forget()
        S_big_1.grid(row=1, column=0, columnspan=2)
    elif c == 2:
        player_separation(2, 0, 'S')
        grid[2][0] = 'S'
        S_button_2.grid_forget()
        O_button_2.grid_forget()
        S_big_2.grid(row=2, column=0, columnspan=2)
    elif c == 3:
        player_separation(3, 0, 'S')
        grid[3][0] = 'S'
        S_button_3.grid_forget()
        O_button_3.grid_forget()
        S_big_3.grid(row=3, column=0, columnspan=2)
    elif c == 4:
        player_separation(0, 1, 'S')
        grid[0][1] = 'S'
        S_button_4.grid_forget()
        O_button_4.grid_forget()
        S_big_4.grid(row=0, column=2, columnspan=2)
    elif c == 5:
        player_separation(1, 1, 'S')
        grid[1][1] = 'S'
        S_button_5.grid_forget()
        O_button_5.grid_forget()
        S_big_5.grid(row=1, column=2, columnspan=2)
    elif c == 6:
        player_separation(2, 1, 'S')
        grid[2][1] = 'S'
        S_button_6.grid_forget()
        O_button_6.grid_forget()
        S_big_6.grid(row=2, column=2, columnspan=2)
    elif c == 7:
        player_separation(3, 1, 'S')
        grid[3][1] = 'S'
        S_button_7.grid_forget()
        O_button_7.grid_forget()
        S_big_7.grid(row=3, column=2, columnspan=2)
    elif c == 8:
        player_separation(0, 2, 'S')
        grid[0][2] = 'S'
        S_button_8.grid_forget()
        O_button_8.grid_forget()
        S_big_8.grid(row=0, column=4, columnspan=2)
    elif c == 9:
        player_separation(1, 2, 'S')
        grid[1][2] = 'S'
        S_button_9.grid_forget()
        O_button_9.grid_forget()
        S_big_9.grid(row=1, column=4, columnspan=2)
    elif c == 10:
        player_separation(2, 2, 'S')
        grid[2][2] = 'S'
        S_button_10.grid_forget()
        O_button_10.grid_forget()
        S_big_10.grid(row=2, column=4, columnspan=2)
    elif c == 11:
        player_separation(3, 2, 'S')
        grid[3][2] = 'S'
        S_button_11.grid_forget()
        O_button_11.grid_forget()
        S_big_11.grid(row=3, column=4, columnspan=2)
    elif c == 12:
        player_separation(0, 3, 'S')
        grid[0][3] = 'S'
        S_button_12.grid_forget()
        O_button_12.grid_forget()
        S_big_12.grid(row=0, column=6, columnspan=2)
    elif c == 13:
        player_separation(1, 3, 'S')
        grid[1][3] = 'S'
        S_button_13.grid_forget()
        O_button_13.grid_forget()
        S_big_13.grid(row=1, column=6, columnspan=2)
    elif c == 14:
        player_separation(2, 3, 'S')
        grid[2][3] = 'S'
        S_button_14.grid_forget()
        O_button_14.grid_forget()
        S_big_14.grid(row=2, column=6, columnspan=2)
    elif c == 15:
        player_separation(3, 3, 'S')
        grid[3][3] = 'S'
        S_button_15.grid_forget()
        O_button_15.grid_forget()
        S_big_15.grid(row=3, column=6, columnspan=2)





def counter_visual():   #places the player scores on the screen
    P1_counter.grid(column=0, row=4, columnspan=4)
    P2_counter.grid(column=4, row=4, columnspan=4)
counter_visual()



def  player_visual():    #tells the user which player is playing
    current_player = 'current player is Player 1' if round%2 == 0 else 'current player is player 2'
    P1.configure(text=current_player)
    P1_counter.configure(text=player_1_score[0])
    P2_counter.configure(text=player_2_score[0])
player_visual()



def game_end_check():   #checks if the game has ended
    if 0 not in chain (*grid):
        game_end()



def all_children (window) :     #places all the widgets in a list
    _list = window.winfo_children()

    for item in _list :
        if item.winfo_children() :
            _list.extend(item.winfo_children())

    return _list



def game_end():     #game_end functionality, checks if the game has ended and reacts accordingly
    global player_1_score, player_2_score
    widget_list = all_children(root)
    for item in widget_list:
        item.grid_forget()
    if player_1_score > player_2_score:  
        player_won = "Player 1 wins!"
    elif player_1_score < player_2_score:
        player_won = "player 2 wins!"
    else:
        player_won = "TIE!"

    win_message = Label(root, text = player_won)
    win_message.pack()



root.mainloop()