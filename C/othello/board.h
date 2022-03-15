#ifndef BOARD_H
#define BOARD_H

extern char BOARD[8][8];

extern int player_state,com_state;

/*Initializing the board*/

void initialize(void);

/*Stone count*/

extern int stonecount_o,stonecount_x;

void count(void);

/*Checking validity of coordinate*/

int validity(int row_coord, int col_coord,int state);

extern int flip_count;

/* Checks for any valid moves on the board */

int valid_moves_exists(int state);

/*Placing the piece*/

int place(int coord_x, int coord_y, int state);

int flip(int state, int coord_x, int coord_y);

#endif
