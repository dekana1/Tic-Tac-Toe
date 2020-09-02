row0 = [" ", " ", " "]
row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
grid = [row0, row1, row2]
game_state = "run"


def print_board():
    print("-" * 9)
    print("| " + grid[0][0] + " " + grid[0][1] + " " + grid[0][2] + " |")
    print("| " + grid[1][0] + " " + grid[1][1] + " " + grid[1][2] + " |")
    print("| " + grid[2][0] + " " + grid[2][1] + " " + grid[2][2] + " |")
    print("-" * 9)


def check_state():
    global game_state
    if grid[0][0] == grid[0][1] == grid[0][2] and grid[0][0] != " ":
        game_state = "won"
        print(grid[0][0], "wins")
    elif grid[1][0] == grid[1][1] == grid[1][2] and grid[1][0] != " ":
        game_state = "won"
        print(grid[1][0], "wins")
    elif grid[2][0] == grid[2][1] == grid[2][2] and grid[2][0] != " ":
        game_state = "won"
        print(grid[2][0], "wins")
    # 3 vertical wins
    elif grid[0][0] == grid[1][0] == grid[2][0] and grid[0][0] != " ":
        game_state = "won"
        print(grid[0][0], "wins")
    elif grid[0][1] == grid[1][1] == grid[2][1] and grid[0][1] != " ":
        game_state = "won"
        print(grid[0][1], "wins")
    elif grid[0][2] == grid[1][2] == grid[2][2] and grid[0][2] != " ":
        game_state = "won"
        print(grid[0][2], "wins")

    # 2 diagonal wins
    elif grid[2][0] == grid[1][1] == grid[0][2] and grid[2][0] != " ":
        game_state = "won"
        print(grid[2][0], "wins")
    elif grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] != " ":
        game_state = "won"
        print(grid[0][0], "wins")
    elif len([x for row in grid for x in row if x == " "]) == 0:
        game_state = "draw"
        print("Draw")


count = 0
print_board()
while game_state == "run":
    x, y = input("Enter the coordinates:").split()
    player = "X" if count % 2 == 0 else "O"
    if x.isdigit() and y.isdigit():
        x = int(x)
        y = int(y)
    else:
        print("You should enter numbers!")
        continue
    if x >= 4 or y >= 4:
        print("Coordinates should be from 1 to 3!")
        continue
    elif y == 3:
        if grid[0][x - 1] == " ":
            grid[0][x - 1] = player
            print_board()
            count += 1
            check_state()
            continue
        else:
            print("This cell is occupied! Choose another one!")
            continue
    elif y == 2:
        if grid[1][x - 1] == " ":
            grid[1][x - 1] = player
            print_board()
            count += 1
            check_state()
            continue
        else:
            print("This cell is occupied! Choose another one!")
            continue
    elif y == 1:
        if grid[2][x - 1] == " ":
            grid[2][x - 1] = player
            print_board()
            count += 1
            check_state()
            continue
        else:
            print("This cell is occupied! Choose another one!")
            continue
