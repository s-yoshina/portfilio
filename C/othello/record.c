#include "board.h"
#include "record.h"
#include <stdio.h>



/*
 * A function to save game record
 */

int save_record(int row, int col,int state)
{
    FILE *fp;
    char state_record;
    static int count = 0;

    if (state == player_state)state_record = 'O';
    else state_record = 'X';

    if (count == 0)
    {
        fp = fopen("save.txt", "w+");
        count += 1;
    }
    else fp = fopen("save.txt", "a");

    fprintf(fp,"%c: %c%d\n",state_record,'a'+col,row+1);
    fclose(fp);
    return 0;
}

/* A function to load and display game record */
void result(void)
{
    FILE *fp;
    char code,ch;

    fp = fopen("save.txt", "r");

    printf("Do you want to show the game record? [y/n]\n");
    scanf("%c", &code);

    while (getchar() != '\n');
    switch (code)
    {
        case 'y':
        {
            while ((ch = fgetc(fp)) != EOF)printf("%c",ch);
        }
        default: break;
    }
    getchar();
}
