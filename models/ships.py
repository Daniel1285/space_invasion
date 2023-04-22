import sys
sys.path.append('/home/kali/Desktop/python_project/space_invasion')  

from defenition import *
from models.laser import *
pygame.font.init()

class Ship:
    COOLDOWN = 30
    def __init__(self, x, y, health=100):
            self.x = x
            self.y = y
            self.health = health
            self.ship_img = None
            self.laser_img = None
            self.lasers =[]
            self.cool_down_counter = 0

    def draw(self, window):
          window.blit(self.ship_img, (self.x, self.y))
          for laser in self.lasers:
                laser.draw(window)

    def get_width(self):
          return self.ship_img.get_width()
          
    def get_height(self):
          return self.ship_img.get_height()
          
    def shoot(self):
          if self.cool_down_counter == 0:
                laser = Laser(self.x - 15 , self.y, self.laser_img)
                self.lasers.append(laser)
                self.cool_down_counter = 1

    def cooldown(self):
          if self.cool_down_counter >= self.COOLDOWN:
                 self.cool_down_counter = 0
          elif self.cool_down_counter > 0:
                self.cool_down_counter += 1

    def move_lasers(self, val, obj):
          self.cooldown()
          for laser in self.lasers:
                laser.move(val)
                if  laser.off_screen(HEIGET):
                      self.lasers.remove(laser)
                elif laser.collision(obj):
                      obj.health -= 10
                      self.lasers.remove(laser)
                  
                      

          
    