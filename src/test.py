import sys
import pygame

# Initialize
pygame.init()

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 200

# Width and height of the joystick area
JOYSTICK_AREA_SIZE = 200

# Create your screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("PS5 Controller Input")

# Clock to control frame rate
clock = pygame.time.Clock()

# Joystick index
JOYSTICK_INDEX = 0

# Initialize joystick
pygame.joystick.init()
joystick = pygame.joystick.Joystick(JOYSTICK_INDEX)
joystick.init()

# Center position of the left stick
CENTER_POS_LEFT = (100, 100)
# Center position of the right stick
CENTER_POS_RIGHT = (300, 100)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  
            sys.exit(0)       
    
    # Get the state of the joystick's left and right sticks   
    left_stick_x = joystick.get_axis(0)   
    left_stick_y = joystick.get_axis(1)    
    right_stick_x = joystick.get_axis(2)  # Right stick X-axis is axis 2
    right_stick_y = joystick.get_axis(3)  # Right stick Y-axis is axis 3:  
    
    # Normalize the axis values to be between -1 and 1
    normalized_left_x = left_stick_x * 2
    normalized_left_y = left_stick_y * 2
    normalized_right_x = right_stick_x * 2
    normalized_right_y = right_stick_y * 2
    
    # Calculate the position of the circles based on the joystick input
    pos_left_x = CENTER_POS_LEFT[0] + int(normalized_left_x * (JOYSTICK_AREA_SIZE / 4))
    pos_left_y = CENTER_POS_LEFT[1] + int(normalized_left_y * (JOYSTICK_AREA_SIZE / 4)) 
    
    pos_right_x = CENTER_POS_RIGHT[0] + int(normalized_right_x * (JOYSTICK_AREA_SIZE / 4))
    pos_right_y = CENTER_POS_RIGHT[1] + int(normalized_right_y * (JOYSTICK_AREA_SIZE / 4))
    
    # Fill the screen with black
    screen.fill((0, 0, 0))
    
    # Draw white circles around the movement area of each joystick
    pygame.draw.circle(screen, (255, 255, 255), CENTER_POS_LEFT, JOYSTICK_AREA_SIZE / 2)
    pygame.draw.circle(screen, (255, 255, 255), CENTER_POS_RIGHT, JOYSTICK_AREA_SIZE / 2)
    
    # Create a red dot at the center of the left joystick   
    pygame.draw.circle(screen, (255, 0, 0), (int(pos_left_x), int(pos_left_y)), 10)  
    
    # Create a blue dot at the center of the right joystick
    pygame.draw.circle(screen, (0, 0, 255), (int(pos_right_x), 
    int(pos_right_y)), 10)  
    
    # Update display
    pygame.display.update()
    
    # Control frame rate
    clock.tick(60)       