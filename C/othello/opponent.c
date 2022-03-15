#include "opponent.h"
#include "board.h"
#include "record.h"
#include <stdio.h>

/*Computing computer's move*/
/* Programmed so that the computer chooses the move that flips the most pieces.*/
int computer(int state)
{

    int row, col,flip_max_count = 0,com_row,com_col;

    if(valid_moves_exists(state) == 0)
    {
        printf("No valid moves for the computer. Turn is skipped.\n");
        return 1;
    }

    for (row = 0; row < 8; row++)
    {
        for (col = 0; col < 8; col++)
        {
            validity(row,col,state);
            if (flip_count > flip_max_count)
            {
                flip_max_count = flip_count;
                com_row = row;
                com_col = col;
            }
        }
    }
    validity(com_row,com_col,state);
    place(com_row,com_col,state);
    printf("Computer played %c%d.\n",'a'+com_col,com_row+1);
    flip(state,com_row,com_col);
    save_record(com_row,com_col,state);
    return 0;
}
