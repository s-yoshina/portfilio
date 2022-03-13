#include <stdio.h>
#include <math.h>

#define N 100000000

double riemann_zeta_2(void){
    double i = 1, sum = 0;
    while(i <= N){
        sum += 1/(i*i);
        i++;
    }
    return sum;
}

int main(void){
    double final, sum;
    // pi is obtained by multiplying the summation by 6 and taking the square root of the product.
    sum = riemann_zeta_2();
    final = sqrt(6*sum);
    printf("%.8f\n", final);
    return 0;
}
