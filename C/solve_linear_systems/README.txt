=Solving Linear Systems=

Solves systems of linear equations using Gaussian Elimination.
The number of linear equations handled can be adjusted by changing the value
of the constant value N in the program.

<Method>
Using row operations, the augmented matrix created from the linear equations
inputted by the user is transformed so that the variable side of the matrix
is a diagonal matrix with only 1s on its diagonal. This will lead to the value
of each variable to be on the far right side of the matrix.

<Example operation>
RN represents the Nth row of the matrix. (Ex. R1 is the first row of the matrix.)
[1,-1,1,8]                   [1,-1,1,8]                        [1,-1,1,8]
[2,3,-1,-2] (R2/2, R3/3) ->  [1,1.5,-0.5,-1] (R2-R1, R3-R1) -> [0,2.5,-1.5,-9]
[3,-2,-9,9]                  [1,-0.66,-3,3]                    [0,0.33,-4,-5]

The above process repeats for each column except for the last one that contains the solution.

<Example>
input:
1 -1 1 8 # 2x-y+z = 8
2 3 -1 -2 # 2x+3y-z = -2
3 -2 -9 9 # 3x-2y-9z = 9

output:
4 # x = 4
-3 # y = -3
-1 # z = -1
