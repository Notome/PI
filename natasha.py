#2 задание
def create_grid(size):
    return [[" "] * size for _ in range(size)]

def draw_star(M):
    for i in range(7):
        M[i][3] = "*"
    M[3][:7] = ["*"] * 7

def draw_dot(M):
    M[0][2] = "."
    for i in range(1, 3):
        M[i][1:3] = ["."] * 2
    M[2][:3] = ["."] * 3

def draw_parenthesis(M):
    for i in range(1, 3):
        M[i][6:9] = [")"] * 3
    M[3][8] = ")"
    M[2][6] = " " # Clear cell

def draw_parenthesis_down(M):
    for i in range(6, 9):
        M[i][1] = "("
    for i in range(7, 9):
        M[i][2] = "("
    M[8][1:4] = ["("] * 3

def draw_rectangle(M):
    M[4][4:] = ["0"] * 6
    M[9][4:] = ["0"] * 6
    for i in range(4, 10):
        M[i][4] = "0"
        M[i][9] = "0"

def print_grid(M):
    for row in M:
        print("".join(row))

M = create_grid(10)
draw_star(M)

#3 задание 
def create_grid(size):
    return [[" "] * size for _ in range(size)]

def draw_eyes(M, c):
    M[3][3] = c  
    M[3][6] = c  

def draw_smile(M, c):
    M[6][3: 7] = [c]*4
    M[5][2] = c
    M[5][7] = c
  
M = create_grid(10)
draw_eyes(M, "*")
draw_smile(M, "*")

for row in M:
    print("".join(row))

draw_dot(M)
draw_parenthesis(M)
draw_parenthesis_down(M)
draw_rectangle(M)
print_grid(M)
#5 задание 
def F(*args):
    result = 0
    for x in args:
        result = result + x
    return result

A1, A2, A4, A8, A16, A32, A64 = 1, 2, 4, 8, 16, 32, 64
D = F(A4, A16, A64) 
print(D)
#6 задание 
def F(*args):
    result = 0
    args = sorted(args, reverse=True)
    for num in args:
        if result + num <= 51:
            result += num
        elif result - num >= 0:
            result -= num
    return result

A1, A2, A4, A8, A16, A32, A64 = 1, 2, 4, 8, 16, 32, 64
D = F(A16, A32, A2, A1)
print(D)  
