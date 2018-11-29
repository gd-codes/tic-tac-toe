#______________________________________________________________________________________________________________________________________________________________________________
#
#                                                                       Tic Tac Toe
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Python 3
# Gautam D -  2018
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import tkinter as tk
import tkinter.messagebox
from tkinter.constants import *
from PIL import Image, ImageTk

from pynput import mouse
from random import sample
from time import sleep


class TicTacToe :
    """ Tic Tac Toe """

    def __init__(self) :
        """1st function called in the main execution flow
           (Initialises the app by creating the GUI)"""
        
        self.root = tk.Tk()
        self.root.iconbitmap('logo.ico')
        self.root.title("Tic Tac Toe")
        self.root.geometry('600x430')
        self.root.minsize(width = 400, height = 400)

        self.container = tk.Frame(self.root) ; self.container.pack()
        self.optpane = tk.Frame(self.container) ; self.optpane.pack(side = LEFT, padx = 10)
        self.gamepane = tk.Frame(self.container) ; self.gamepane.pack(side = RIGHT, padx = 10)

        self.header1 = tk.LabelFrame(self.optpane) ; self.header1.pack(pady = 5)
        self.logoimage = tk.PhotoImage(file = 'icon_brown.png')
        self.header2 = tk.Frame(self.header1) ; self.header2.pack(side = TOP)
        self.logo = tk.Label(self.header2, image = self.logoimage) ; self.logo.pack(side = LEFT, pady = 10, padx = 20)
        self.title = tk.Label(self.header2, text = "Tic\nTac\nToe", font=('Corbel',15,'bold')) ; self.title.pack(side = RIGHT, padx = 20)

        self.settings = tk.Frame(self.header1, pady = 5) ; self.settings.pack(side = BOTTOM)
        self.rules = tk.Button(self.settings, text = "Rules", command = self._showRules, width = 10) ; self.rules.pack(side = LEFT, padx = 5)
        self.about = tk.Button(self.settings, text = "About", command = self._showHelp, width = 10) ; self.about.pack(side = RIGHT, padx = 5)

        self.modechoice = tk.LabelFrame(self.optpane, text = "Choose Game Mode : ", padx = 45) ; self.modechoice.pack(pady = 5)
        self.gamemode = tk.IntVar()
        self.optmode1 = tk.Radiobutton(self.modechoice, text = "Player v/s Player\t   ", variable = self.gamemode, value = 1, command = self.symbolOptions)
        self.optmode2 = tk.Radiobutton(self.modechoice, text = "Player v/s Computer", variable = self.gamemode, value = 2, command = self.symbolOptions)
        self.optmode1.pack(padx = 10) ; self.optmode2.pack(padx = 10)

        print("_" * 50, "\n\n", "Tic Tac Toe".center(50), "\n", "-" * 50)

    def _showRules(self):
        """Called by the Rules button in the window"""
        tk.messagebox.showinfo('Rules of the Game\n\n', "Tic Tac Toe (also called Noughts and Crosses) is a game played by 2, traditionally on a 3x3 grid"+\
                               " drawn on paper. Each of the 2 players chooses a symbol (traditionally a circle and a cross, hence the other name) and ta"+\
                               "ke alternate turns drawing their symbol in one of the free boxes of the grid. The player who first gets 3 of their symbol"+\
                               "s in a line wins - hence, each player must try to 'block' the line being made by the other while trying to make one with "+\
                               "their own symbols. If a player wins, they start the next game; whereas if there is a draw, the other player starts. Enjoy"+\
                               " playing !")
        
    def _showHelp(self):
        """Called by the about button in the window"""
        tk.messagebox.showinfo('How to use this app\n\n', "Tic Tac Toe\n\nGautam D\n30 Apr, 5-6 and 12 May 2018\nWritten in Python 3.4.1 using tkinter GU"+\
                               "I  \n\nThis app has 2 game modes - you must first choose either 'Player versus player' or 'Player versus computer'. Once "+\
                               "selected, six symbols, including the traditiononal circle and cross will be shown - each player must select the one they "+\
                               "would like to play with (The computer will choose its symbol itself). The players are called '1' and '2' in the first mod"+\
                               "e by default. Once the mode and symbols have been chosen, they cannot be changed. The 3x3 game board is then displayed on"+\
                               " the right, along with the players' symbol choices above. The player whose turn it currently is is highlighted in grey. P"+\
                               "layers can then take turns playing their moves by left-clicking on an empty cell (The computer will automatically click o"+\
                               "n the cell of its choice immediately as its turn comes). Once a cell has been filled, it cannot be changed. To get detail"+\
                               "ed info about any move that has been played, right-click on the cell in which it was played. Once any player wins or all "+\
                               "cells have been filled, the game ends and the winning line, if any, is highlighted. Click on the 'New Game' button that a"+\
                               "ppears now to play again (If the mode is 'Player v/s Computer, you get to start each time). Enjoy playing !")
        
    def _loadImages(self):
        """3rd function called in the main execution flow - by self.symbolOptions()
           (Processes the images used as icons in the game)"""
        self.c1 = Image.open('circle.png').resize((50, 50), Image.LANCZOS)
        self.c = ImageTk.PhotoImage(self.c1)

        self.x1 = Image.open('cross.png').resize((50, 50), Image.LANCZOS)
        self.x = ImageTk.PhotoImage(self.x1)

        self.t1 = Image.open('triangle.png').resize((50, 50), Image.LANCZOS)
        self.t = ImageTk.PhotoImage(self.t1)

        self.s1 = Image.open('square.png').resize((50, 50), Image.LANCZOS)
        self.s = ImageTk.PhotoImage(self.s1)

        self.p1 = Image.open('pentagon.png').resize((50, 50), Image.LANCZOS)
        self.p = ImageTk.PhotoImage(self.p1)

        self.h1 = Image.open('hexagon.png').resize((50, 50), Image.LANCZOS)
        self.h = ImageTk.PhotoImage(self.h1)


    def symbolOptions(self):
        """ 2nd function called in the main execution flow - after the user chooses a game-mode
            (Creates the GUI to let player(s) choose their symbols)"""
        
        self.optmode1.config(state = 'disabled')
        self.optmode2.config(state = 'disabled')
        self.modechoice.config(text = "Game Mode")
        print("Game mode : %d" % self.gamemode.get())
        self.symchoice = tk.LabelFrame(self.optpane, text = "Choose a Symbol (Player 1) : ", padx = 35) ; self.symchoice.pack(pady = 5)
        
        if self.gamemode.get() == 2 :
            self.mouse = mouse.Controller()
            self.symchoice.config(text = " Choose a Symbol ")
            self.playernames = {1:'You', 2:'The Computer'}
            
        self._loadImages()
        self.sym1 = tk.Button(self.symchoice, image = self.c, command = lambda : self.selectSymbol(self.sym1))
        self.sym1.grid(column = 0, row = 0, pady = 2, padx = 2)
        self.sym2 = tk.Button(self.symchoice, image = self.x, command = lambda : self.selectSymbol(self.sym2))
        self.sym2.grid(column = 1, row = 0, pady = 2, padx = 2)
        self.sym3 = tk.Button(self.symchoice, image = self.t, command = lambda : self.selectSymbol(self.sym3))
        self.sym3.grid(column = 2, row = 0, pady = 2, padx = 2)
        self.sym4 = tk.Button(self.symchoice, image = self.s, command = lambda : self.selectSymbol(self.sym4))
        self.sym4.grid(column = 0, row = 1, pady = 2, padx = 2)
        self.sym5 = tk.Button(self.symchoice, image = self.p, command = lambda : self.selectSymbol(self.sym5))
        self.sym5.grid(column = 1, row = 1, pady = 2, padx = 2)
        self.sym6 = tk.Button(self.symchoice, image = self.h, command = lambda : self.selectSymbol(self.sym6))
        self.sym6.grid(column = 2, row = 1, pady = 2, padx = 2)
        self.sym_btns = {self.sym1 : self.c,    self.sym2 : self.x,    self.sym3 : self.t,
                         self.sym4 : self.s,    self.sym5 : self.p,    self.sym6 : self.h}
        self.plyr1chosen = False

        self.players = tk.Frame(self.gamepane) ; self.players.pack(pady = 10, padx = 5)
        self.player1 = tk.Label(self.players) ; self.player1.pack(side = LEFT, padx = 10)
        self.player2 = tk.Label(self.players) ; self.player2.pack(side = RIGHT, padx = 10)

    def selectSymbol(self, button):
        """4th function called in the main execution flow - when the player selects a symbol
            (Saves the player's choice of symbol)"""
        
        if self.gamemode.get() == 1 and self.plyr1chosen == False :
            self.shape1 = self.sym_btns[button]
            self.plyr1chosen = True
            button.config(state = 'disabled')
            self.player1.config(text = "  Player 1 : ", image = self.sym_btns[button], compound = RIGHT)
            self.symchoice.config(text = "Choose a Symbol (Player 2) : ")
        elif self.gamemode.get() == 1 and self.plyr1chosen == True :
            self.shape2 = self.sym_btns[button]
            self.player2.config(text = "  Player 2 : ", image = self.sym_btns[button], compound = RIGHT)
            for btn in self.sym_btns.keys() :
                btn.config(state = 'disabled')
            self.symchoice.config(text = "Symbols")
            self.startGame()
        elif self.gamemode.get() == 2 :
            self.shape1 = self.sym_btns[button]
            for btn in self.sym_btns.keys() :
                btn.config(state = 'disabled')
            self.player1.config(text = "  You : ", image = self.sym_btns[button], compound = RIGHT)
            symbuttons = self.sym_btns ; del symbuttons[button]
            auto_sym_choice = sample(symbuttons.keys(), 1)[0]
            self.shape2 = self.sym_btns[auto_sym_choice]
            sleep(0.25)
            self.player2.config(text = "  Computer : ", image = self.shape2, compound = RIGHT)
            for btn in self.sym_btns.keys() :
                btn.config(state = 'disabled')
            self.symchoice.config(text = "Symbols")
            self.startGame()

    def leftClickWidget(self, widget, x=10, y=10):
        """Used by the computer to move the cursor to & click the square of its choice"""
        self.mouse.position = (widget.winfo_rootx() + x, widget.winfo_rooty() + y)
        self.mouse.click(mouse.Button.left, 2)

    def startGame(self, player=1) :
        """5th function called in the main execution flow - by self.selectSymbol()
            (Creates the GUI 3x3 grid in which the game is played)"""
        
        self.board = tk.Frame(self.gamepane) ; self.board.pack(pady = 10)
        self.A1 = tk.Canvas(self.board, name='a1', width=50, height=50, bg='white', borderwidth=2, relief=GROOVE) ; self.A1.grid(column=0, row=0, pady=5, padx=5)
        self.A2 = tk.Canvas(self.board, name='a2', width=50, height=50, bg='white', borderwidth=2, relief=GROOVE) ; self.A2.grid(column=1, row=0, pady=5, padx=5)
        self.A3 = tk.Canvas(self.board, name='a3', width=50, height=50, bg='white', borderwidth=2, relief=GROOVE) ; self.A3.grid(column=2, row=0, pady=5, padx=5)
        self.B1 = tk.Canvas(self.board, name='b1', width=50, height=50, bg='white', borderwidth=2, relief=GROOVE) ; self.B1.grid(column=0, row=1, pady=5, padx=5)
        self.B2 = tk.Canvas(self.board, name='b2', width=50, height=50, bg='white', borderwidth=2, relief=GROOVE) ; self.B2.grid(column=1, row=1, pady=5, padx=5)
        self.B3 = tk.Canvas(self.board, name='b3', width=50, height=50, bg='white', borderwidth=2, relief=GROOVE) ; self.B3.grid(column=2, row=1, pady=5, padx=5)
        self.C1 = tk.Canvas(self.board, name='c1', width=50, height=50, bg='white', borderwidth=2, relief=GROOVE) ; self.C1.grid(column=0, row=2, pady=5, padx=5)
        self.C2 = tk.Canvas(self.board, name='c2', width=50, height=50, bg='white', borderwidth=2, relief=GROOVE) ; self.C2.grid(column=1, row=2, pady=5, padx=5)
        self.C3 = tk.Canvas(self.board, name='c3', width=50, height=50, bg='white', borderwidth=2, relief=GROOVE) ; self.C3.grid(column=2, row=2, pady=5, padx=5)

        # These lists are checked by the computer while it inspects all posible lines of 3 to determine where to make its move
        self.cells = (self.A1, self.A2, self.A3, self.B1, self.B2, self.B3, self.C1, self.C2, self.C3)
        
        self.all_lines = [[self.A1,self.A2,self.A3], [self.B1,self.B2,self.B3], [self.C1,self.C2,self.C3], [self.A1,self.B2,self.C3],
                          [self.A1,self.B1,self.C1], [self.A2,self.B2,self.C2], [self.A3,self.B3,self.C3], [self.A3,self.B2,self.C1]]
        
        self.winning_lines = {self.A1 : ((self.A1,self.A2,self.A3), (self.A1,self.B2,self.C3), (self.A1,self.B1,self.C1)),
                              self.A2 : ((self.A1,self.A2,self.A3), (self.A2,self.B2,self.C2)),
                              self.A3 : ((self.A1,self.A2,self.A3), (self.A3,self.B2,self.C1), (self.A3,self.B3,self.C3)),
                              self.B1 : ((self.B1,self.B2,self.B3), (self.A1,self.B1,self.C1)),
                              self.B2 : ((self.B1,self.B2,self.B3), (self.A2,self.B2,self.C2), (self.A1,self.B2,self.C3), (self.A3,self.B2,self.C1)),
                              self.B3 : ((self.B1,self.B2,self.B3), (self.A3,self.B3,self.C3)),
                              self.C1 : ((self.C1,self.C2,self.C3), (self.A3,self.B2,self.C1), (self.A1,self.B1,self.C1)),
                              self.C2 : ((self.C1,self.C2,self.C3), (self.A2,self.B2,self.C2)),
                              self.C3 : ((self.C1,self.C2,self.C3), (self.A1,self.B2,self.C3), (self.A3,self.B3,self.C3))}
        
        for cell in self.cells :
            cell.bind("<Button-1>", self.writeCell)
        self.timer = tk.Label(self.gamepane, text = "Click on any empty square to play your move", font = ('Calibri', 12, 'italic'))
        self.timer.pack(pady = 10)
        self.moves = 0
        self.current_player = player
        for i in range(2) :
            self.switchPlayer()

    def writeCell(self, event):
        """6th function called in the main execution flow - when a player clicks on a cell
            (Marks the player's symbol in an empty cell when it is clicked and registers the move -
            the player and move number as recorded as tags associated with the canvas image)"""
        self.moves += 1
        event.widget.create_image(28, 28, image=self.current_shape, tags=('Player-%d' % self.current_player, 'Move-%d' % self.moves))
        event.widget.bind("<Button-3>", self.showMoveInfo)
        event.widget.unbind("<Button-1>")
        event.widget.config(bg = '#eeeeee')
        if not self.checkForWin(event.widget):
            self.switchPlayer()
        if self.gamemode.get() == 2 :
            self.updatePriority()

    def switchPlayer(self):
        """8th function called in the main execution flow - by self.writeCell(), if the game hasn't ended 
            (Changes the current player to the other one after each turn)"""
        if self.current_player == 1 :
            self.current_shape = self.shape2 
            self.current_player = 2
            self.player2.config(bg = '#333333', fg = 'white')
            self.player1.config(bg = '#eeeeee', fg = 'black')
        elif self.current_player == 2 :
            self.current_shape = self.shape1
            self.current_player = 1
            self.player1.config(bg = '#333333', fg = 'white')
            self.player2.config(bg = '#eeeeee', fg = 'black')

    def _filledCells(self, row):
        """Checks the lists/tuples in self.startGame() and tells the computer which lines have cells in them filled"""
        n = 0 ; full_boxes = [] ; empty_boxes = []
        for cell in row :
            if len(cell.gettags(ALL)) > 0 :
                n += 1
                full_boxes.append(cell)
            else :
                empty_boxes.append(cell)           
        return (n, full_boxes, empty_boxes)
                

    def updatePriority(self):
        """9th function called in the main execution flow, if self.gamemode is 2, - by self.writeCell()
            (Used by the computer to calculate where it's best to make its move -
            all lists of cells are organised into 6 priority levels based on how they've been filled)"""
        
        self.priorities = { 1:[], 2:[], 3:[], 4:[], 5:[], 6:[] }
        lines = self.all_lines
        for line in lines :
            status = self._filledCells(line)
            if status[0] == 2 :
                if status[1][0].gettags(ALL)[0][-1] == status[1][1].gettags(ALL)[0][-1] == '2' :
                    self.priorities[1].extend(status[2])
                elif status[1][0].gettags(ALL)[0][-1] == status[1][1].gettags(ALL)[0][-1] == '1' :
                    self.priorities[2].extend(status[2])
                else :
                    self.priorities[5].extend(status[2])
            elif status[0] == 1 :
                if status[1][0].gettags(ALL)[0][-1] == '2' :
                    self.priorities[3].extend(status[2])
                else :
                    self.priorities[4].extend(status[2])
            elif status[0] == 0 :
                self.priorities[6].extend(status[2])
        print("Current prediction values :\n", len(self.priorities[1]), len(self.priorities[2]), len(self.priorities[3]),
              len(self.priorities[4]), len(self.priorities[5]), len(self.priorities[6]))
        if self.current_player == 2 :
            self.autoPlayMove()

    def autoPlayMove(self):
        """10th function called in the main execution flow, if self.gamemode is 2, - by self.updatePriority()
            (The computer uses the self.priorities dictionary to make its move)"""
        sleep(0.2)
        if len(self.priorities[1]) > 0 :
            self.leftClickWidget(sample(self.priorities[1], 1)[0])
        elif len(self.priorities[2]) > 0 :
            self.leftClickWidget(sample(self.priorities[2], 1)[0])
        elif len(self.priorities[3]) > 0 :
            self.leftClickWidget(sample(self.priorities[3], 1)[0])
        elif len(self.priorities[4]) > 0 :
            self.leftClickWidget(sample(self.priorities[4], 1)[0])
        elif len(self.priorities[5]) > 0 :
            self.leftClickWidget(sample(self.priorities[5], 1)[0])
        elif len(self.priorities[6]) > 0 :
            self.leftClickWidget(sample(self.priorities[6], 1)[0])           

    def checkForWin(self, cell):
        """7th function called in the main execution flow - by self.writeCell()
            (Checks if all 3 cells in a line are filled by a player, or the whole board is filled and then ends the game)"""
        for line in self.winning_lines[cell] :
            try :
                if (line[0].gettags(ALL))[0] == (line[1].gettags(ALL))[0] == (line[2].gettags(ALL))[0] :
                    self.endGame(line)
                    return True
            except IndexError :
                continue
        if self.moves == 9 :
            self.endGame(None)
            return True                

    def showMoveInfo(self, event):
        """Displays details about the move in a cell when it is right-clicked by the user"""
        if self.gamemode.get() == 1 :
            tk.messagebox.showinfo('Move Info', "Cell : {}\nMove #{}\nPlayed by : Player {}".format(
                str(event.widget)[-2:], event.widget.gettags(ALL)[1][-1], event.widget.gettags(ALL)[0][-1]))
        elif self.gamemode.get() == 2 :
            tk.messagebox.showinfo('Move Info', "Cell : {}\nMove #{}\nPlayed by : {}".format(
                str(event.widget)[-2:], event.widget.gettags(ALL)[1][-1], self.playernames[int(event.widget.gettags(ALL)[0][-1])]))

    def endGame(self, result):
        """11th and last function called in the main execution flow - by self.checkForWin()
            (Completes the game if someone wins or all cells are filled)"""
        self.restart = tk.Button(self.gamepane, text = 'New Game', fg='white', bg='#333333', width = 15, command = self.newGame)
        self.restart.pack(pady = 5)
        
        for cell in self.cells :
            cell.unbind("<Button-1>")
            
        if result == None :
            self.timer.config(text = "Game Over - It's a tie !", font = ('Calibri', 12, 'roman', 'bold'))
            self.winner = None
        else :
            for cell in result :
                cell.config(bg = '#442200')
            if self.gamemode.get() == 1 :
                self.timer.config(text = "Congratulations ! Player {} won the game !".format(self.current_player), font=('Calibri',12,'roman','bold'))
            elif self.gamemode.get() == 2 :
                if self.current_player == 1 :
                    self.timer.config(text = "Congratulations ! You won the game !", font=('Calibri',12,'roman','bold'))
                elif self.current_player == 2 :
                    self.timer.config(text = "The Computer won the game !", font=('Calibri',12,'roman','bold'))
            self.winner = self.current_player

    def newGame(self) :
        """Starts a new game when the New Game button is clicked"""
        self.board.destroy()
        self.timer.destroy()
        self.restart.destroy()
        print('\n')
        if self.gamemode.get() == 1 :
            crnt_plyr = self.current_player
            if (crnt_plyr == 2 and self.winner == None) or self.winner == 1 :
                self.startGame(1)
            if (crnt_plyr == 1 and self.winner == None) or self.winner == 2 :
                self.startGame(2)
        elif self.gamemode.get() == 2 :
            self.startGame(1)


    def __unavailable(self):
        print("This feature is currently unavailable as the app is still being developed")

if __name__ == '__main__' :
    
    print("Loading...")
    game = TicTacToe()
    game.root.mainloop()

#_______________________________________________________________________________________________________________________________________________________________________________
