# Formulation of the problem

Reversi game or sometimes named Othello is 2 player game with perfect information. We have a square playing area of ​​8 x 8 square tiles. 
The playing area is bounded and the edges of the playing area are not contiguous. We have playing stones of two colors. At the beginning 
of the game, we have two stones of each color placed in the center of the playing area. The player who is on his turn places a stone of his 
color on the board in such a way as to close at least one continuous row of the opponent's stones ending with his own stone. All of your 
opponent's stones in contiguous rows from the place of placement to your stone's place then become the player's stones on the turn. So 
it is possible to close more than one row. This can be done horizontally, vertically and diagonally. If a player cannot place a stone in 
such a way that it takes at least one of the opponent's stones, the opponent plays automatically. The game ends when the entire board is 
filled with stones or if no player can place their stone. The winner of the game is the player with more stones on the board than the opponent.

