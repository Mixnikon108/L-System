# Author: Jorge de la Rosa @mixnikon108
# Date: 4/5/2024
# Description: This program visualizes fractal tree generation. 


import pygame
from utils import LSystemRenderer

# Definición del axioma inicial y las reglas de transformación
axiom = "F"

# Helecho #1
rules = {'F': 'F[-F[-F++F]][+F[--F]]F'}
iterations = 5 
angle = 15 

# # Helecho #2
# rules = {'F': 'F[++F[-F]]F[-FF[F]]'}
# iterations = 5  
# angle = 12 

# # Helecho #3
# rules = {'F': 'F[-FF[+F]]F[+F[+F]]'}
# iterations = 5  
# angle = 20 




# Crear una instancia de la clase LSystemRenderer
l_system = LSystemRenderer(axiom, rules, iterations, angle)

# Calcular el L-system generado
l_system.calculate_points(units=4)

# Inicializar Pygame
pygame.init()

# Definir colores
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)

# Configuración de la pantalla
WINDOW_SIZE = (700, 700)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Fractal Tree")

# Control del loop principal
done = False
clock = pygame.time.Clock()

# Loop principal
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(COLOR_WHITE)

    # Dibujar el fractal del árbol
    for start_point, end_point in l_system.get_points():
        x_start, y_start = start_point
        x_end, y_end = end_point
        pygame.draw.line(screen, COLOR_BLACK,
                         (x_start + WINDOW_SIZE[0]/2, WINDOW_SIZE[1] - y_start),
                         (x_end + WINDOW_SIZE[0]/2, WINDOW_SIZE[1] - y_end), 1)

    pygame.display.flip()

    clock.tick(10)

pygame.quit()