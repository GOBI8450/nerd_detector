import pygame
import math
import serial
import random
from pygame import mixer

arduino_port = 'COM4'
arduino = serial.Serial(port=arduino_port, baudrate=9600, timeout=.2)
distance = 50

# Creating the screen
pygame.init()
width, height = 1920 - 100, 1080 - 100
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Nerd Detector 2000')

mixer.init()
mixer.music.load('boom_sound.mp3')

background = pygame.Surface((width, height))
background.fill((0, 0, 0))
imp = pygame.image.load("nerd_green.png").convert_alpha()
imp = pygame.transform.scale(imp, (imp.get_width() // 2.5, imp.get_height() // 2.5))

started_nerding = 0
row_lock = 1
opacity_nerd = 10
angle_end_row1 = 360
angle_start_row1 = 270
angle_end_row2 = 269
angle_start_row2 = 180
angle_end_row3 = 179
angle_start_row3 = 90
angle_end_row4 = 89
angle_start_row4 = 0
posY_positive = 155
posX_positive = 570
angle_different = angle_end_row1 - angle_start_row1
angle_different_real = 255 / angle_different
decressing_flag = False
r1 = random.randint(-100, 1000)
r2 = random.randint(-300, 300)

circle_center = (width // 2, height // 2)
circle_radius = 400
pygame.draw.circle(background, (41, 73, 25), circle_center, circle_radius)

line_length = circle_radius
line_angle = 0

pygame.display.flip()

flag = True
clock = pygame.time.Clock()
while flag:
    if arduino.in_waiting > 0:
        distance = int(arduino.readline().decode().strip())
        print("Distance:", distance, "cm")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False

    # Clear the screen
    screen.blit(background, (0, 0))

    # Rotate the line
    line_end = (circle_center[0] + int(line_length * math.cos(math.radians(line_angle))),
                circle_center[1] + int(line_length * math.sin(math.radians(line_angle))))
    line_angle_fixed = int(line_angle)
    # Draw the rotated line
    pygame.draw.line(screen, (190, 225, 88), circle_center, line_end, width=15)

    # Draw expanding circles for sonar effect
    for i in range(5):
        decrece_radius = circle_radius - i * 120
        pygame.draw.circle(screen, (190, 225, 88), circle_center, decrece_radius, width=5)

    if distance <= 40 and started_nerding == 0:
        if line_angle_fixed == angle_start_row1:
            started_nerding = 1
            mixer.music.play()
        elif line_angle_fixed == angle_start_row2:
            started_nerding = 2
            mixer.music.play()
        elif line_angle_fixed == angle_start_row3:
            started_nerding = 3
            mixer.music.play()
        elif line_angle_fixed == angle_start_row4:
            started_nerding = 4
            mixer.music.play()
    print("nerd situation",started_nerding)
    print("line_angle", line_angle)

    if started_nerding == 1:
        if opacity_nerd <= (angle_different * angle_different_real) / 2 and not decressing_flag:
            opacity_nerd += 2
        else:
            decressing_flag = True
            opacity_nerd -= 4
        imp.set_alpha(opacity_nerd)
        screen.blit(imp, (posX_positive + 270, posY_positive))
    elif started_nerding == 2:
        if opacity_nerd <= (angle_different * angle_different_real) / 2 and not decressing_flag:
            opacity_nerd += 2
        else:
            decressing_flag = True
            opacity_nerd -= 4
        imp.set_alpha(opacity_nerd)
        screen.blit(imp, (posX_positive, posY_positive))
    elif started_nerding == 3:
        if opacity_nerd <= (angle_different * angle_different_real) / 2 and not decressing_flag:
            opacity_nerd += 2
        else:
            decressing_flag = True
            opacity_nerd -= 4
        imp.set_alpha(opacity_nerd)
        screen.blit(imp, (posX_positive, posY_positive+300))
    elif started_nerding == 4:
        if opacity_nerd <= (angle_different * angle_different_real) / 2 and not decressing_flag:
            opacity_nerd += 2
        else:
            decressing_flag = True
            opacity_nerd -= 4
        imp.set_alpha(opacity_nerd)
        screen.blit(imp, (posX_positive + 270, posY_positive+300))

    # Update the display
    pygame.display.update()

    # Increment the angle for the next frame
    if line_angle >= 360:
        line_angle = 0
        opacity_nerd = 0
        decressing_flag = False
        r1 = random.randint(-500, 1000)
        r2 = random.randint(0, 500)
        row = 1
        row_lock = 1
        started_nerding = 0
    else:
        # line_angle += 1.1
        line_angle += 1.1
    clock.tick(60)

pygame.quit()
# arduino.close()  # Close the serial connection
