
# Importamos pygame y random
import pygame
import random

# Inicializamos pygame y creamos la ventana
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Flappybird con viento")

# Definimos los colores que vamos a usar
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
yellow = (255, 255, 0)
orange = (255, 165 ,0)

# Creamos una variable para almacenar la velocidad del viento
wind_speed = 0

# Creamos una variable para almacenar la posición del pájaro
bird_x = 100
bird_y = 300

# Creamos una variable para almacenar la velocidad vertical del pájaro
bird_speed_y = 0

# Creamos una lista para almacenar las posiciones de las tuberías
pipes = []

# Creamos una variable para almacenar el ancho y el alto de las tuberías
pipe_width = 50
pipe_height = screen.get_height()

# Creamos una variable para almacenar la puntuación del jugador
score = 0

# Creamos una función para generar nuevas tuberías cada cierto tiempo
def generate_pipes():
    global pipes,score
    
    # Elegimos una altura aleatoria para la abertura entre las tuberías
    gap_y = random.randint(100,500)
    
    # Añadimos una nueva tubería superior a la lista con su posición x e y 
    pipes.append([screen.get_width(), -pipe_height + gap_y -100])
    
    # Añadimos una nueva tubería inferior a la lista con su posición x e y 
    pipes.append([screen.get_width(), gap_y +100])
    
    # Incrementamos la puntuación del jugador en uno 
    score +=1 

# Llamamos a la función para generar las primeras dos tuberías 
generate_pipes()

# Creamos un reloj para controlar el tiempo del juego 
clock=pygame.time.Clock()

# Creamos un bucle principal para el juego 
running=True 
while running: 
    
     # Establecemos el tiempo entre cada fotograma a 60 milisegundos 
     clock.tick(60) 
    
     # Comprobamos los eventos de entrada del usuario (teclado o ratón) 
     for event in pygame.event.get(): 
        
         # Si el usuario cierra la ventana , salimos del bucle y terminamos el juego  
         if event.type == pygame.QUIT:  
             running=False 
        
         # Si el usuario presiona la barra espaciadora , hacemos que el pájaro salte hacia arriba  
         if event.type == pygame.KEYDOWN:  
             if event.key == pygame.K_SPACE:  
                 bird_speed_y=-10 
    
     # Actualizamos la posición del pájaro según su velocidad vertical y el viento  
     bird_y += bird_speed_y + wind_speed 
    
     # Actualizamos la velocidad vertical del pájaro según la gravedad  
     bird_speed_y +=1 
    
     # Comprobamos si el pájaro se sale de los límites de la pantalla y lo corregimos  
     if bird_y <0:  
         bird_y=0 
    
     if bird_y > screen.get_height() -50:  
         bird_y=screen.get_height() -50 
    
     # Actualizamos la posición de las tuberías según su velocidad horizontal  
     for i in range(len(pipes)):  
         pipes[i][0] -=5

# Comprobamos si alguna tubería se sale de los límites de la pantalla y la eliminamos  
     if pipes[0][0] < -pipe_width:  
         pipes.pop(0)  
         pipes.pop(0) 
    
     # Comprobamos si hay que generar nuevas tuberías según la distancia entre ellas  
     if pipes[-1][0] == 400:  
         generate_pipes() 
    
     # Cambiamos aleatoriamente la velocidad del viento cada cierto tiempo  
     if random.randint(1,60) == 1:   
         wind_speed= random.randint(-3,+3) 
    
     print(wind_speed) 
    
     # Dibujamos el fondo en la pantalla con un color blanco 
     screen.fill(white) 
    
     # Dibujamos las tuberías en sus posiciones correspondientes en la pantalla con un color verde 
     for i in range(0,len(pipes),2):   
         pygame.draw.rect(screen,green,(pipes[i][0],pipes[i][1],pipe_width,pipe_height))   
         pygame.draw.rect(screen,green,(pipes[i+1][0],pipes[i+1][1],pipe_width,pipe_height))   
    # Definimos un color para el pájaro
     bird_color = yellow

    # Definimos las coordenadas del centro y el radio del círculo que representa el cuerpo del pájaro
     bird_center = (bird_x + 25 , bird_y + 25)
     bird_radius = 25

    # Dibujamos el círculo que representa el cuerpo del pájaro
     pygame.draw.circle(screen,bird_color,bird_center,bird_radius)

    # Definimos las coordenadas de los tres puntos que forman el triángulo que representa el pico del pájaro
     bird_beak_1 = (bird_x + 50 , bird_y + 25)
     bird_beak_2 = (bird_x + 60 , bird_y + 16)
     bird_beak_3 = (bird_x + 60 , bird_y + 34)

    # Dibujamos el triángulo que representa el pico del pájaro
     pygame.draw.polygon(screen,orange,[bird_beak_1,bird_beak_2,bird_beak_3])

    # Definimos las coordenadas del centro y el radio del círculo que representa el ojo del pájaro
     bird_eye_center = (bird_x + 37 , bird_y +18)
     bird_eye_radius =5

   # Dibujamos el círculo que representa el ojo del pájaro
     pygame.draw.circle(screen,(black),bird_eye_center,bird_eye_radius)

   # Creamos una fuente para dibujar el texto de la puntuación 
     font=pygame.font.SysFont("Arial",32)

   # Creamos un texto con la puntuación y su color 
     text=font.render(str(score),True,(black))

   # Dibujamos el texto en la esquina superior izquierda de la pantalla 
     screen.blit(text,(10,10))

   # Comprobamos si el pájaro colisiona con alguna tubería y terminamos el juego si es así 
     for i in range(0,len(pipes),2):   
       if bird_x +50 > pipes[i][0] and bird_x < pipes[i][0] + pipe_width:   
           if bird_y < pipes[i][1] + pipe_height or bird_y +50 > pipes[i+1][1]:   
               running=False 

   # Actualizamos la pantalla con los nuevos elementos dibujados 
     pygame.display.flip()
