# tic-tac-toe
Contains a Python 3 - based functional Tic Tac Toe game

The program uses tkinter for GUI, along with PIL (see https://pypi.org/project/Pillow/) to load images required, and pynput (see https://pypi.org/project/pynput/) to control the mouse cursor when the computer plays its move; and the standard modules random and time.
The 2 non-standard modules PIL and pynput are included in this repository for convenince.

2 game modes are available - player v/s player and player v/s computer. In the former, 2 players can alternately take turns clicking on squares and play. In the latter, the algorithm for the computer as a player organises all the cells available to play a move into 6 priority levels, moves the cursor to the best one and clicks it. 

There are 6 icons from which players can choose symbols - these images are included in the repository.

Detailed instructions on how to play are included in the game window.
