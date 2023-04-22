import pygame
import os

pygame.font.init()

 
WIDTH, HEIGET = 1200, 750
WIN = pygame.display.set_mode((WIDTH, HEIGET))
pygame.display.set_caption("Space invasion")

# Images
RED_SPACE_SHIP = pygame.image.load(os.path.join("images", "ship_red.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("images", "ship_green.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("images", "ship_blue.png"))

# Player ship
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("images", "ship_yellow.png"))

# Lasers
RED_LASER = pygame.image.load(os.path.join("images", "laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join("images", "laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join("images", "laser_blue.png"))
YELLOW_LASER = pygame.image.load(os.path.join("images", "laser_yellow.png"))

# Bacground
BG = pygame.transform.scale(pygame.image.load(os.path.join("images", "Background.png")), (WIDTH,HEIGET))
BG_REGISTER = pygame.transform.scale(pygame.image.load(os.path.join("images", "BG_register.png")), (WIDTH,HEIGET))

# Set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SKY = (190, 200, 205)

# Set up fonts
FONT_LARGE = pygame.font.SysFont(None, 30)
FONT_SMALL = pygame.font.SysFont(None, 25)
TITEL_FONT = pygame.font.Font(None, 40)
TITEL_FONT_R = pygame.font.Font(None, 60)

TITEL_COLOR = (236, 240, 241)

# titel text pages
TITEL_TEXT_SIGNUP = TITEL_FONT.render("Sign up", True, TITEL_COLOR)
TITEL_TEXT_LOGIN = TITEL_FONT.render("Log in", True, TITEL_COLOR)
TITEL_TEXT_REGISTER = TITEL_FONT_R.render("Space invasion :)", True, TITEL_COLOR)

