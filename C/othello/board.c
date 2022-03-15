#include "board.h"
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "user_interface.h"
#include <string.h>
#include "opponent.h"

#define EMPTY 0
#define X 1
#define O 2

int player_state, com_state, flip_count;

/*Initial Board*/
void choose_first_player(void)
{
    srand((unsigned)time(NULL));
    player_state = (rand() % 2)+1;
    com_state = 3 - player_state;
}

void initialize(void){
    int i,j;

    choose_first_player();

    if(player_state == O)printf("Player goes first. (Your symbol is O)\n");
    else printf("Computer goes first. (Your symbol is X)\n");

    // Creating board
    for (i = 0 ; i < 8 ; i++)for (j = 0; j < 8; j++)BOARD[i][j] = EMPTY;

    // Setting initial pieces on the board.
    BOARD[3][4] = X;
    BOARD[4][3] = X;
    BOARD[4][4] = O;
    BOARD[3][3] = O;
}

/*Counting Stones Function*/
int stonecount_o,stonecount_x;
void count(void){
    int i,j;

    stonecount_o = 0;
    stonecount_x = 0;
    for (i = 0 ; i < 8 ; i++){
        for (j = 0; j < 8; j++){
            if (BOARD[i][j] == O)stonecount_o += 1;
            else if (BOARD[i][j] == X)stonecount_x += 1;
        }
    }

}


/*Validity Function*/
int opponent_state;
int turn_x[8],turn_y[8], turn_count; // Stores the direction in which to turn?

int vector_validity(int x,int y,int state,int coord_x, int coord_y);

void define_state(int state)
{
    if (state == player_state)opponent_state = com_state; // Checking who's turn it is currently.
    else opponent_state = player_state;
}

void initialize_variables(void){
    int i;
    flip_count = 0;
    turn_count = 0;
    for (i=0;i<8;i++)turn_x[i]=0;
    turn_y[i]=0;
}

int validity(int row,int col,int state){
    define_state(state);
    initialize_variables();

    if (BOARD[row][col] != EMPTY)return 0; // If the square is not empty
    vector_validity(-1,0,state,col,row); // Up
    vector_validity(1,0,state,col,row); // Down
    vector_validity(0,-1,state,col,row); // Left
    vector_validity(0,1,state,col,row); // Right
    vector_validity(-1,-1,state,col,row); // Top Left
    vector_validity(1,-1,state,col,row); // Bottom left
    vector_validity(-1,1,state,col,row); // Top Right
    vector_validity(1,1,state,col,row); // Bottom Right
    return 0;
}

int vector_validity(int v_row,int v_col,int state,int col, int row){
    //Checks if there are any stones that can be flipped by placing at (row, col)
    int i = 1;

    row += v_row;
    col += v_col;
    while (row < 8 && row >= 0 && col < 8 && col >= 0)
    {
        if (BOARD[row][col] == EMPTY)return 0;
        if (BOARD[row][col] == state)
        {
            if (i > 1)
            {
                turn_x[turn_count] = v_col;
                turn_y[turn_count] = v_row;
                turn_count++;
            }
            flip_count += i-1;
            return 0;
        }
        row += v_row;
        col += v_col;
        i++;
    }
    return 0;
}

/*Checks if there are any valid moves for the player*/
int valid_moves_exists(int state){
    int row, col;
    for(row=0;row<8;row++)
    {
        for(col=0;col<8;col++)
        {
            if(BOARD[row][col] == EMPTY)
            {
                validity(row,col,state);
                if(flip_count > 0)return 1;
            }
        }
    }
    return 0;
}

/*Place and Flip function*/
int place(int row, int col, int state)
{
    BOARD[row][col] = state;
    return 0;
}

int flip(int state, int row, int col)
{
    int c_row,c_col,i;
    for (i = 0; i < turn_count; i++) // Goes through each vector where a piece can be flipped
    {
        c_row = row+turn_y[i];
        c_col = col+turn_x[i];
        while(BOARD[c_row][c_col] == opponent_state)
        {
            BOARD[c_row][c_col] = state;
            c_row += turn_y[i];
            c_col += turn_x[i];
        }
    }
    return 0;
}
