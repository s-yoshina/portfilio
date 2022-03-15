#include <stdio.h>
#include "board.h"
#include "user_interface.h"
#include "opponent.h"
#include "record.h"

#define X 1
#define O 2

int player_turn(int state)
{
    if(valid_moves_exists(state) == 0)
    {
        printf("No moves. Your turn is skipped.\n");
        return 1;
    }
    board();
    input();
    validity(row,col,state);
    while (flip_count == 0)
    {
        printf("That coordinate is invalid\n");
        input();
        validity(row,col,state);
    }
    place(row,col,state);
    flip(state,row,col);
    save_record(row,col,state);
    return 0;
}

int main(void){
    int total_stones, p_skip, com_skip;

    initialize();
    while (total_stones != 64 && (p_skip != 1 && com_skip !=1))
    {
        if(player_state == O)
        {
            p_skip = player_turn(player_state);
            com_skip = computer(com_state);
        }
        else
        {
            com_skip = computer(com_state);
            p_skip = player_turn(player_state);
        }
        count();
        total_stones = stonecount_o+stonecount_x;
    }
    board();
    if (stonecount_o > stonecount_x)printf("\nO wins!");
    else printf("\nX wins!");
    printf(" (O:%d X:%d)\n",stonecount_o, stonecount_x);
    printf("Played moves were saved to save.txt.\n");
    result();
    return 0;
}
