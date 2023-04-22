import sys
sys.path.append('/home/kali/Desktop/python_project/space_invasion')  
from defenition import *
from models.ships import *

class Enemy(Ship):
    COLOR_MAP = {
        "red" :   (RED_SPACE_SHIP, RED_LASER),
        "green" : (GREEN_SPACE_SHIP, GREEN_LASER),
        "blue" :  (BLUE_SPACE_SHIP, BLUE_LASER)
        }

    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        self.ship_img, self.laser_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)

    def move(self, val):
        self.y += val 
