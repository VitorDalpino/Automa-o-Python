import pyautogui as pg

distance = 200
while distance> 0:
    pg.drag(distance, 0, duration=0.5) # move para a direita
    distance -= 5
    pg.drag(0, distance, duration=0.5) # move para baixo
    pg.drag(-distance, 0, duration=0.5) # move para esquerda
    distance -=5
    pg.drag(0, -distance, duration=0.5) # move para cima
    
