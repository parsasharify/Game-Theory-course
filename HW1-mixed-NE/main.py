import sys

number = int(input())
matrix = []
for i in range(number):
    in_line = input().split()
    line = []
    for digit in in_line:
        line.append(int(digit) - 50)
    matrix.append(line)


def transpose(l1, l2):

    for i in range(len(l1[0])):
        # print(i)
        row = []
        for item in l1:

            row.append(item[i])
        l2.append(row)
    return l2



matrix_hold = [[-1 * element for element in row] for row in matrix]


matrix_T = []

transpose(matrix_hold, matrix_T)
c = []
b = []
bounds = []
A = []
for i in range(number):
    b.append(0)
    c.append(0)
    bounds.append((0, 1))
    A.append(1)

A.append(0)
c.append(-1)
bounds.append((None, None))

for line in matrix:
    line.append(1)

for line_ in matrix_T:
    line_.append(1)


A_eq = [A]
b_eq = [1]

from scipy.optimize import linprog


res = linprog(c=c, A_eq=A_eq, b_eq=b_eq, A_ub=matrix_T, b_ub=b, bounds=bounds, method='simplex')

res1 = list(res.x)
res1.pop()
print(res1)

res = linprog(c=c, A_eq=A_eq, b_eq=b_eq, A_ub=matrix, b_ub=b, bounds=bounds, method='simplex')
res1 = list(res.x)
res1.pop()
print(res1)




