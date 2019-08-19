import pygame, random

# Define some colors and other constants
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
GRAY = (25, 25, 25)
WIN_SIZE = 500
# NUM_SQUARES = ??
# WIN_SIZE = NUM_SQUARES * 20 + (NUM_SQUARES + 1) * 5

# 1. Create a set of initial states with simple pattern (Ex. blinker)
cur_states = [0] * 400
cur_states[10] = 1
cur_states[30] = 1
cur_states[50] = 1

generation = 0
is_paused = False

# 1 v.2 Fill cur_states with random states
# cur_states = [0] * 400
# for i in range( 0, len(cur_states)):
#   cur_states[i] = random.randint(0,1)

# 1 v.3 Allow users to choose between several predefined init states


pygame.init()
# Set the width and height of the screen [width, height]
size = (WIN_SIZE, WIN_SIZE)
screen = pygame.display.set_mode(size)

# Add a title
pygame.display.set_caption("Conway's Game of Life")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
    def sum_of_neighbors(grid, cell):
        x = cell[1]
        y = cell[0]
        neighbors_coords = [(y-1,x-1), (y-1, x), (y-1, x+1),(y, x-1),(y, x+1),(y+1, x-1),(y+1, x),(y+1, x+1)]
        neighbors = []

        for coords in neighbors_coords:
            try:
                neighbors.append(grid[coords[0]][coords[1]])
            except IndexError:
                neighbors.append(None)

        neighbor_total = 0
        for i in neighbors:
            if i != None:
                neighbor_total += i


        return neighbor_total
            
    
    # Any live cell with fewer than two live neighbours dies, as if by underpopulation.

    # Any live cell with two or three live neighbours lives on to the next generation.
    # Any live cell with more than three live neighbours dies, as if by overpopulation.
    # Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
    
    # 3. Work on rules that i) look at all neighbors, ii) save new state
    # in next_states[]

    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to gray. Don't put other drawing commands
    # above this, or they will be erased with this command.
    
    screen.fill(GRAY)

    # --- Drawing code should go here
    cur_index = 0
    x = 5

    while x < 500: 
        y = 5
        while y < 500:
            # 2. Draw based on values in cur_states
            state = cur_states[cur_index]
            # 4. Draw based on values in next_states
            if state == 0:
                pygame.draw.rect(screen, BLACK, pygame.Rect(x, y, 20, 20) )
            else:
                pygame.draw.rect(screen, WHITE, pygame.Rect(x, y, 20, 20) )
            cur_index += 1
            y += 25
        x += 25

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 5 frames per second
    clock.tick(5)
    
# Close the window and quit.
pygame.quit()