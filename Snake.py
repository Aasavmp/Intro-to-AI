# Main code to create the snake game

# Importing the required modules
import pygame
import random

# Defining the game screen
display_width = 800
display_height = 600

# Defining the colors of the game
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)

game_background = white

# Defining the snake size
snake_size = 10
snake_color = green
snake_speed = 10

# Initializing the pygame
pygame.init()

# creating the game screen
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake Game')
pygame.display.update()

# Defining the game clock
clock = pygame.time.Clock()

# Adding 'Game Lost' message
font = pygame.font.SysFont(None, 100)
def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [display_width/2, display_height/2])

# Function to display the full snake
def whole_snake(snake_size, snake_list):
    '''
    function to display the whole snake
    snake_size: Size of the snake
    snake_list: List of the snake body
    '''
    for x in snake_list:
        pygame.draw.rect(gameDisplay, snake_color, [x[0], x[1], snake_size, snake_size])

# Starting the game and Defining the game loop
def Game_Loop():
    # Position of the snake
    snake_x = display_width/2
    snake_y = display_height/2

    # Movement of the snake
    snake_move_x = 0
    snake_move_y = -10

    # Body of snake
    snake_body = []
    snake_length = 1

    # Position of the food
    food_x = round(random.randrange(0, display_width - snake_size)/10.0)*10.0
    food_y = round(random.randrange(0, display_height - snake_size)/10.0)*10.0

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            # Code for snake movement
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake_move_x += -snake_size
                    snake_move_y = 0
                    print("Left")
                elif event.key == pygame.K_RIGHT:
                    snake_move_x += snake_size
                    snake_move_y = 0
                    print("Right")
                elif event.key == pygame.K_UP:
                    snake_move_x = 0
                    snake_move_y += -snake_size
                    print("Up")
                elif event.key == pygame.K_DOWN:
                    snake_move_x = 0
                    snake_move_y += snake_size
                    print("Down")

        # Adding edge walls
        if snake_x >= display_width or snake_x < 0 or snake_y >= display_height or snake_y < 0:
            gameExit = True

        # Make sure snake doesn't stop (move back on itself)
        if snake_move_x != 0 or snake_move_y != 0:
            # Reset movement to snake size if it is greater than snake size
            if abs(snake_move_x) > snake_size:
                snake_move_x = (snake_move_x/abs(snake_move_x))*snake_size

            if abs(snake_move_y) > snake_size:
                snake_move_y = (snake_move_y/abs(snake_move_y))*snake_size

            snake_x += snake_move_x
            snake_y += snake_move_y

            snake_move_x_prev = snake_move_x
            snake_move_y_prev = snake_move_y
        else:
            snake_x += snake_move_x_prev
            snake_y += snake_move_y_prev

            snake_move_x = snake_move_x_prev
            snake_move_y = snake_move_y_prev

        # Adding snake body
        snake_head = []
        snake_head.append(snake_x)
        snake_head.append(snake_y)

        snake_body.append(snake_head)

        # Limiting the snake body length unless food has been eaten
        if len(snake_body) > snake_length:
            del snake_body[0]

        # Adding game over if snake hits itself
        if snake_head in snake_body[:-1]:
            gameExit = True
        
        # Adds the display to the game
        gameDisplay.fill(game_background)

        # Snake display
        whole_snake(snake_size, snake_body)

        # Food display
        pygame.draw.rect(gameDisplay, red, [food_x, food_y, snake_size, snake_size])

        pygame.display.update()

        # Snake eating food
        if snake_x == food_x and snake_y == food_y:
            # New food position
            food_x = round(random.randrange(0, display_width - snake_size)/10.0)*10.0
            food_y = round(random.randrange(0, display_height - snake_size)/10.0)*10.0

            # Increase snake length
            snake_length += 1

        clock.tick(snake_speed)

    message_to_screen("Game Over", red)
    pygame.display.update()
    pygame.time.wait(500)

    pygame.quit()
    quit()

Game_Loop()