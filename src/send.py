# pyserrial is used here
import serial
import pygame
from CONSTS import BAUD_RATE
from random import randrange

WIDTH = 200
HEIGHT = 200

pygame.init()
pygame.joystick.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

joysticks = []  
while joysticks == []:
    joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
joystick = joysticks[0]

print(joystick.get_name())
print(joystick.get_numaxes())

ser = None
while ser == None:
    try:
        ser = serial.Serial('COM4', BAUD_RATE)
    except Exception as e:
        print(f"Error opening serial port: {e}")
        pygame.event.wait(randrange(1000, 4000))


axis = 0 
value = 0
leftx = 0
lefty = 0
rightx = 0
righty = 0
button = 0

running = True
while running:
    
    if ser == None:
        print("Serial port not open")
        try:
            ser = serial.Serial('COM4', BAUD_RATE)
        except Exception as e:
            print(f"Error opening serial port: {e}")
            pygame.event.wait(randrange(1000, 4000))
        
    button = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ser.close()
            pygame.quit()
            running = False
        if event.type == pygame.JOYAXISMOTION:
            axis, value = event.axis, event.value
        if event.type == pygame.JOYBUTTONDOWN:
            button = event.button
    
    screen.fill((0,0,0))
    pygame.draw.circle(screen, (255, 255, 255), (WIDTH//2, HEIGHT//2), min(WIDTH, HEIGHT)//2, width=5)
    scaled_value_x = (value * (WIDTH // 2)) + (WIDTH // 2)
    scaled_value_y = (value * (HEIGHT // 2)) + (HEIGHT // 2)
    
    try:
        if button == 9:
            ser.write(b'3')
            print("Left")
        if button == 10:
            ser.write(b'4')
            print("Right")
        
        if axis == 0:
            if value > 0.5:
                print("Positive")
                ser.write(b'2')
                pygame.time.wait(10)
            if value < -0.5:
                print("Negative")
                ser.write(b'1')
                pygame.time.wait(10)
            leftx = scaled_value_x
        if axis == 1:
            lefty = scaled_value_y
        if axis == 2:
            rightx = scaled_value_x
        if axis == 3:
            righty = scaled_value_y
    except:
        try:
            ser.close()
        except:
            pass
        ser = None
    
    pygame.draw.circle(screen, (255, 0 , 0), (leftx, lefty), min(WIDTH, HEIGHT)/4, width=5)

    pygame.display.flip()

try: 
    ser.close()
    print("Serial port closed")
except Exception as e:
    print(f"Error closing serial port: {e}")