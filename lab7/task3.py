import random

GRID_SIZE = 5

def create_grid():
    return [['~'] * GRID_SIZE for _ in range(GRID_SIZE)]

def place_ship(grid):
    r, c = random.randint(0, 4), random.randint(0, 4)
    grid[r][c] = 'S'
    return (r, c)

def print_grid(grid, reveal=False):
    print("  " + " ".join(map(str, range(GRID_SIZE))))
    for i, row in enumerate(grid):
        print(i, " ".join(cell if reveal or cell != 'S' else '~' for cell in row))

def battleship_game():
    player_grid = create_grid()
    ai_grid = create_grid()
    player_ship = place_ship(player_grid)
    ai_ship = place_ship(ai_grid)
    hits = {'player': False, 'ai': False}

    while not all(hits.values()):
        print("\nYour Turn:")
        print_grid(ai_grid)
        try:
            r, c = map(int, input("Enter attack coordinates (row col): ").split())
            if ai_grid[r][c] == 'S':
                ai_grid[r][c] = 'X'
                hits['player'] = True
                print("Hit!")
            else:
                ai_grid[r][c] = 'O'
                print("Miss.")
        except:
            print("Invalid input.")
            continue

        if hits['player']: break

        print("\nAI's Turn:")
        while True:
            r, c = random.randint(0, 4), random.randint(0, 4)
            if player_grid[r][c] in ['~', 'S']:
                if player_grid[r][c] == 'S':
                    print(f"AI attacks: {r},{c} → Hit!")
                    hits['ai'] = True
                else:
                    print(f"AI attacks: {r},{c} → Miss")
                break

    print("\nGame Over!")
    if hits['player']:
        print("You Win!")
    else:
        print("AI Wins!")
    print("Player Grid:")
    print_grid(player_grid, reveal=True)
    print("AI Grid:")
    print_grid(ai_grid, reveal=True)

battleship_game() 
