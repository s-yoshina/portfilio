#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "board.h"
#include "user_interface.h"

/*External Variables*/

char BOARD[8][8];
int col, row;

/*Displaying the Board*/

void board(void)
{
    int i,j;

    /*Board Design*/
    static char *piece[]={"   |", " X |", " O |"};
    printf("   a   b   c   d   e   f   g   h\n");
    printf(" +---+---+---+---+---+---+---+---+\n");

    /*Creating the Board*/
    for (i = 0 ; i < 8 ; i++)
    {
        printf("%d|", i+1);
        for (j=0 ; j < 8 ; j++)printf("%s",piece[BOARD[i][j]]);
        printf("\n");
        printf("-+---+---+---+---+---+---+---+---+\n");
    }

}

/*Reading input from user*/

void input(void)
{
    int coord_length;
    char col_label = 'a',row_label = '0',coord[10];

    printf("Enter the coordinate of your move: ");
    scanf("%s", coord);

    coord_length = strlen(coord);

    col = coord[0] - col_label;
    row = coord[1] - row_label - 1;

    /*Invalid coordinate case*/
    while (coord_length > 2 || col > 8 || col < 0 || row > 8 || row < 0)
    {
        printf("Please enter an coordinate: ");
        scanf("%s", coord);

        coord_length = strlen(coord);
        col = coord[0] - col_label;
        row = coord[1] - row_label - 1;
    }
}


