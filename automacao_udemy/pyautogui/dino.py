from PIL import ImageGrab
import pyautogui as pg

def isCollision(data):
    for i in range(760, 835):
        for j in range(290, 330):
            id data[i,j] < 100: # type: ignore
            pg.keyDown("up")
            print("pulando")
            return
    return

if __name__ == "__main__":
    while True:
        image = ImageGrab().convert('L')
        data = image.load
        isCollision(data)

