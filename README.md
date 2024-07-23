# Formulation of the problem

Reversi game or sometimes named Othello is 2 player game with perfect information. We have a square playing area of ​​8 x 8 square tiles. 
The playing area is bounded and the edges of the playing area are not contiguous. We have playing stones of two colors. At the beginning 
of the game, we have two stones of each color placed in the center of the playing area. The player who is on his turn places a stone of his 
color on the board in such a way as to close at least one continuous row of the opponent's stones ending with his own stone. All of your 
opponent's stones in contiguous rows from the place of placement to your stone's place then become the player's stones on the turn. So 
it is possible to close more than one row. This can be done horizontally, vertically and diagonally. If a player cannot place a stone in 
such a way that it takes at least one of the opponent's stones, the opponent plays automatically. The game ends when the entire board is 
filled with stones or if no player can place their stone. The winner of the game is the player with more stones on the board than the opponent.

<img width="150" alt="reversi" src="https://github.com/user-attachments/assets/4528fb01-a92b-4bc4-83ea-dc8573ebd06f">

# Solution of the problem

The player is deciding every round which move to make according to values of the tiles. I assigned a value to every tile of the playing area 
which is constructed as 2D array:<br />
                          &emsp;&emsp;&emsp;  [[8, 2, 6, 4, 4, 6, 2, 8], <br />
                          &emsp;&emsp;&emsp;  [2, 0, 4, 4, 4, 4, 0, 2],<br />
                          &emsp;&emsp;&emsp;  [6, 4, 6, 6, 6, 6, 4, 6],<br />
                          &emsp;&emsp;&emsp;  [4, 4, 6, 6, 6, 6, 4, 4],<br />
                          &emsp;&emsp;&emsp;  [4, 4, 6, 6, 6, 6, 4, 4],<br />
                          &emsp;&emsp;&emsp;  [6, 4, 6, 6, 6, 6, 4, 6],<br />
                          &emsp;&emsp;&emsp;  [2, 0, 4, 4, 4, 4, 0, 2],<br />
                          &emsp;&emsp;&emsp;  [8, 2, 6, 4, 4, 6, 2, 8]]<br />
It is especially advantageous to occupy the corners, because the stone in the corner cannot be turned in any way (there is no way to close it between the opponent's stones).
