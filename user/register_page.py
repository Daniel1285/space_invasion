import sys
sys.path.append('/home/kali/Desktop/python_project/space_invasion')
from user.login_and_signup_page import *
from defenition import *


def first_page():
    pygame.init()
    FPS = 60  # frame per second
    clock = pygame.time.Clock()

    # Set up WIN dimensions
    pygame.display.set_caption("Log in / Sign up")

    # Set up colors
    bg_color = (44, 62, 80)
    button_color = (41, 128, 185)
    button_hover_color = (52, 152, 219)
    text_color = (255, 255, 255)

    # Set up fonts
    button_font = pygame.font.Font(None, 36)

    # Set up buttons
    signup_button = pygame.Rect(WIDTH // 2 - 100, HEIGET // 2 + 50, 200, 50)
    login_button = pygame.Rect(WIDTH // 2 - 100, HEIGET // 2 + 150, 200, 50)

    # main loop
    run = True
    while run:
        clock.tick(FPS)
        WIN.blit(BG, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        WIN.blit(TITEL_TEXT_REGISTER, (
            WIDTH // 2 - TITEL_TEXT_REGISTER.get_width() // 2,
            HEIGET // 2 - TITEL_TEXT_REGISTER.get_height() // 2 - 100))
        # Draw the signup button
        pygame.draw.rect(WIN, button_color, signup_button)
        signup_text = button_font.render("Sign up", True, text_color)
        WIN.blit(signup_text, (WIDTH // 2 - signup_text.get_width() // 2,
                               HEIGET // 2 + 50 + signup_button.height // 2 - signup_text.get_height() // 2))

        # Draw the login button
        pygame.draw.rect(WIN, button_color, login_button)
        login_text = button_font.render("Log in", True, text_color)
        WIN.blit(login_text, (WIDTH // 2 - login_text.get_width() // 2,
                              HEIGET // 2 + 150 + login_button.height // 2 - login_text.get_height() // 2))

        # Check for button hover
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if signup_button.collidepoint(mouse_x, mouse_y):
            pygame.draw.rect(WIN, text_color, signup_button, width=2, border_radius=5)
        if login_button.collidepoint(mouse_x, mouse_y):
            pygame.draw.rect(WIN, text_color, login_button, width=2, border_radius=5)

        # Check for button click
        click = pygame.mouse.get_pressed()
        if click[0] == 1:
            if signup_button.collidepoint(mouse_x, mouse_y):
                sign()

            # Add your code for signup button functionality here
            elif login_button.collidepoint(mouse_x, mouse_y):
                login()

        pygame.display.flip()


first_page()
