#include <stdio.h>

#define N 3

void print_matrix(float a[N][N+1]){
    int row, col;
    for(col=0;col<N+1;col++)printf("-");
    printf("\n");
    for(row=0;row<N;row++){
        for(col=0;col<N+1;col++)printf("%.2f,", a[row][col]);
        printf("\n");}
    for(col=0;col<N+1;col++)printf("-");
    getchar();
}

void reduce_to_1(float a[N][N+1], int row, int s_col, float c){
    int col;
    for(col=s_col;col<N+1;col++)a[row][col] /= c;
}

void reduce_columns(float a[N][N+1], int i){
    int row, col;
    float c;

    for(row=0;row<N;row++){
        if(a[row][i] == 0 || row == i)continue; // Column element already reduced to zero or the diagonal element is being looked at.
        if(a[row][i] != 1)reduce_to_1(a, row, 0, a[row][i]); // If the column value is not 1, it is changed to one.
        for(col=i; col<N+1;col++)a[row][col] -= a[i][col]; // Reduced to zero using the diagonal row.
    }
}

int main(void) {
    int i, j, col;
    float a[N][N+1];

    printf("===%d equations are required===\n", N);
    printf("Enter %d values, seperated by a space or a line break,"
           " corresponding to the coefficients for the variables,\n"
           "and solution to the equation for each row in order. (Coefficients First)\n",N*(N+1));
    for (i = 0; i < N; i++)for (j = 0; j < N+1; j++)scanf("%f", & a[i][j]);

    for (i = 0; i < N; i++){ // Loops through the columns
        for (j = i; j < N; j++){ // Loops through the rows starting from the row with the diagonal element.
        /*Determining the coefficient for row operations*/
        if (a[j][i]!=0){
            if(a[j][i] != 1)reduce_to_1(a, j, i, a[j][i]);
            if(j != i)for(col=i; col<N+1;col++)a[i][col] += a[j][col]; //Add row to diagonal row to make the diagonal value non-zero.
            reduce_columns(a, i);
            break;}
            }
        if(a[i][i] == 0){ // If the diagonal element is not changed to a non-zero element.
            for(j=0;j<i;j++){
                if(a[j][i] != 0){ // If there is a non-zero element above the diagonal, there is no solution.
                    printf("No solution");
                    return 0;}
            }
        }
    }
    printf("The values of the unknown variables in order are\n");
    for (i = 0; i < N; i++)if(a[i][i] == 0)printf("0\n"); else printf("%0.2f\n", a[i][N]/a[i][i]);
    return 0;
}
