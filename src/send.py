# pyserrial is used here
import serial
import pygame
from CONSTS import BAUD_RATE, PORT
from random import randrange

WIDTH = 400
HEIGHT = 200

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

LEFT_JOYSTICK_CENTER = (WIDTH // 4, HEIGHT // 2)
RIGHT_JOYSTICK_CENTER = (3 * (WIDTH // 4), HEIGHT // 2)

pygame.init()
pygame.joystick.init()
pygame.font.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# ser = None
# while ser == None:
#     try:
#         ser = serial.Serial(PORT, BAUD_RATE)
#     except Exception as e:
#         print(f"Error opening serial port: {e}")
#         pygame.event.wait(randrange(1000, 4000))


running = True

while running:
    
    button = None
    
    # Get the joystick
    try:
        if joystick == None:
            print("No joystick found")
            joystick = pygame.joystick.Joystick(0)
            print(f"Joystick found: {joystick.get_name()}")
            print(f"Number of axes: {joystick.get_numaxes()}")
            print(f"Number of buttons: {joystick.get_numbuttons()}")
    except:
        print("No joystick found")
        joystick = None
    
    # Get the serial port
    try:
        if Ser == None:
            print("No serial port found")
            print(f"Opening serial port: {PORT}")
            Ser = serial.Serial(PORT, BAUD_RATE)
            print(f"Serial port opened: {Ser.name}")
    except Exception as e:
        print(f"Error opening serial port: {e}")
        Ser = None
    
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.JOYBUTTONDOWN:
            button = event.button
    
    if joystick != None:
        
        # joystick down buttons
        l3 = joystick.get_button(7)
        r3 = joystick.get_button(8)
        
        # bumper buttons
        lb = joystick.get_button(9)
        rb = joystick.get_button(10)
        
        # Get the left joystick values
        leftx = joystick.get_axis(0)
        lefty = joystick.get_axis(1)
        
        # Get the right joystick values
        rightx = joystick.get_axis(2)
        righty = joystick.get_axis(3)
        
        # Calculate the screen position of the joysticks
        leftxScreenPos = int(LEFT_JOYSTICK_CENTER[0] + leftx * min(WIDTH, HEIGHT)//2)
        leftyScreenPos = int(LEFT_JOYSTICK_CENTER[1] + lefty * min(WIDTH, HEIGHT)//2)
        leftScreenPos = (leftxScreenPos, leftyScreenPos)
        
        rightxScreenPos = int(RIGHT_JOYSTICK_CENTER[0] + rightx * min(WIDTH, HEIGHT)//2)
        rightyScreenPos = int(RIGHT_JOYSTICK_CENTER[1] + righty * min(WIDTH, HEIGHT)//2)
        rightScreenPos = (rightxScreenPos, rightyScreenPos)
    
    # fill the screen with black
    screen.fill(BLACK)
    
    # Draw the maximum circle of the joystick values
    pygame.draw.circle(screen, WHITE, LEFT_JOYSTICK_CENTER, min(WIDTH, HEIGHT)//2, width=5)
    pygame.draw.circle(screen, WHITE, RIGHT_JOYSTICK_CENTER, min(WIDTH, HEIGHT)//2, width=5)
    
    if joystick != None:
        # draw the joystick positions
        pygame.draw.circle(screen, RED, leftScreenPos, 5, width=5) 
        pygame.draw.circle(screen, RED, rightScreenPos, 5, width=5) 
        if l3:
            pygame.draw.circle(screen, BLACK, leftScreenPos, 2, width=2)
        if r3:
            pygame.draw.circle(screen, BLACK, rightScreenPos, 2, width=2)
    else:
        # Alert the user that no joystick was found
        pygame.draw.circle(screen, RED, LEFT_JOYSTICK_CENTER, 5, width=5)
        pygame.draw.circle(screen, RED, RIGHT_JOYSTICK_CENTER, 5, width=5)
        font = pygame.font.Font(None, 24)
        text = font.render("No joystick found", True, (255, 0, 0))
        text_rect = text.get_rect(center=(WIDTH//2, HEIGHT//2))
        screen.blit(text, text_rect)
    
    # Send the joystick values to the serial
    if joystick != None and Ser != None:
        if leftx < -0.5:
            Ser.write(b'1')
        elif leftx > 0.5:
            Ser.write(b'2')
        if button == 9:
            Ser.write(b'3')
        if button == 10:
            Ser.write(b'4')
        
        pygame.time.wait(10)
    
    pygame.display.flip()