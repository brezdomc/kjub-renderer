import pygame
import os
import math
from matrix import matrix_multiplication
from getkey import getkey, keys

os.environ["SDL_VIDEO_CENTERED"]='1'
black, white, blue  = (10, 10, 10), (230, 230, 230), (230, 0, 0)
width, height = 520, 520

pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
fps = 60
angle = 0
cube_position = [width//2, height//2]
scale = 500
speed = 0.02
points = [n for n in range(8)]


# Sredina od kjuba na sredi

points[0] = [[-1], [-1], [1]]
points[1] = [[1], [-1], [1]]
points[2] = [[1], [1], [1]]
points[3] = [[-1], [1], [1]]
points[4] = [[-1], [-1], [-1]]
points[5] = [[1], [-1], [-1]]
points[6] = [[1], [1], [-1]]
points[7] = [[-1], [1], [-1]]

# Kornr na sredini
# points[0] = [[0], [0], [2]]
# points[1] = [[2], [0], [2]]
# points[2] = [[2], [2], [2]]
# points[3] = [[0], [2], [2]]
# points[4] = [[0], [0], [0]]
# points[5] = [[2], [0], [0]]
# points[6] = [[2], [2], [0]]
# points[7] = [[0], [2], [0]]




def connect_point(i, j, k):
    a = k[i]
    b = k[j]
    pygame.draw.line(screen, white, (a[0], a[1]), (b[0], b[1]), 2)

run = True
while run:
    clock.tick(fps)
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False




#Rotaciski matrix

    index = 0
    projected_points = [j for j in range(len(points))]

    rotation_x = [[1, 0, 0],
                  [0, math.cos(angle), -math.sin(angle)],
                  [0, math.sin(angle), math.cos(angle)]]

    rotation_y = [[math.cos(angle), 0, -math.sin(angle)],
                  [0, 1, 0],
                  [math.sin(angle), 0, math.cos(angle)]]


    rotation_z = [[math.cos(angle), -math.sin(angle), 0],
                   [math.sin(angle), math.cos(angle), 0],
                   [0, 0 ,1]]

    for point in points:
        rotated_2d = matrix_multiplication(rotation_y, point)
        # rotated_2d = matrix_multiplication(rotation_y, rotated_2d)
        # rotated_2d = matrix_multiplication(rotation_z, rotated_2d)


        distance = 5
        z = 1/(distance - rotated_2d[2][0])
        projection_matrix = [[z, 0, 0],
                            [0, z, 0]]
        projected_2d = matrix_multiplication(projection_matrix, rotated_2d)
        x = int(projected_2d[0][0] * scale) + cube_position[0]
        y = int(projected_2d[1][0] * scale) + cube_position[1]
        projected_points[index] = [x, y]
        index += 1

    for m in range(4):
        connect_point(m, (m+1)%4, projected_points)
        connect_point(m+4, (m+1)%4 + 4, projected_points)
        connect_point(m, m+4, projected_points)

    angle += speed
    pygame.display.update()

pygame.quit()
