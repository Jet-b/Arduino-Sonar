# pyserrial is used here
import serial
from random import randrange
from time import sleep
import pygame
from CONSTS import BAUD_RATE

# while True:
#     try:
#         ser = serial.Serial('COM4', 9600)
#     except Exception as e:
#         print(f"Error opening serial port: {e}")
#         sleep(randrange(1,4))

#     try:
#         while True:
#             line = ser.readline().decode('utf-8').strip()
#             print(line)
#     except Exception as e:
#         print(f"Error reading serial port: {e}")

#     except KeyboardInterrupt:
#         ser.close()
#         print("Serial port closed")
#         print("Exiting...")
#         break

pygame.init()
pygame.font.init()

WIDTH = 200
HEIGHT = 800

ser = None
while ser == None:
    try:
        ser = serial.Serial('COM4', BAUD_RATE)
    except Exception as e:
        print(f"Error opening serial port: {e}")
        pygame.event.wait(randrange(1000, 4000))

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Serial Data")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    try:
        dist = ser.readline().decode('utf-8').strip()
        dist = int(dist) if dist.isnumeric() else -1
    except Exception as e:
        print(f"Error reading serial port: {e}")
        ser = None
        dist = -1
    
    if ser == None:
        screen.fill((0,0,0))
        font = pygame.font.Font(None, 24)
        text = font.render("Error reading serial port", True, (255, 0, 0))
        text_rect = text.get_rect(center=(WIDTH//2, HEIGHT//2))
        screen.blit(text, text_rect)
        try:
            ser = serial.Serial('COM4', BAUD_RATE)
        except Exception as e:
            print(f"Error opening serial port: {e}")
            pygame.event.wait(randrange(1000, 4000))
    
    if dist <= 400 and dist >= 0:
        screen.fill((0,0,0))
        rec = pygame.Rect((0, HEIGHT - dist*2, WIDTH, dist*2))
        pygame.draw.rect(screen, (0, 255, 0), rec, width=0)
    
    pygame.display.flip()

if ser != None: 
    ser.close()
    print("Serial port closed")
pygame.quit()