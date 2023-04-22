import sys
sys.path.append('/home/kali/Desktop/python_project/space_invasion')  
from defenition import *
from user.password import *
from database import *
from main import *

def login():
    # Initialize Pygame
    pygame.init()

    FPS = 60 # fram per sconde
    clock = pygame.time.Clock()

    pygame.display.set_caption("Log in")

    # Set up text inputs
    login = ""
    password = ""
    login_input_rect = pygame.Rect(WIDTH/2 - 100 , 250, 200, 30)
    password_input_rect = pygame.Rect(WIDTH/2 - 100 , 350, 200, 30)
    login_input_active = False
    password_input_active = False

    # Set up buttons
    login_button_rect = pygame.Rect(WIDTH/2 - 100 , 455, 200, 30)
    login_button_hover = False
    login_button_click = False

    signup_button_rect = pygame.Rect(WIDTH - 120 , HEIGET -40, 100, 25)
    signup_button_hover = False
    signup_button_click = False

    
    def draw_WIN():

        WIN.blit(TITEL_TEXT_LOGIN, (WIDTH // 2 - TITEL_TEXT_LOGIN.get_width() // 2, 100))
        
        clock.tick(FPS)
        WIN.blit(BG_REGISTER, (0,0))
        # Render login and password input boxes
        pygame.draw.rect(WIN, SKY, login_input_rect, 0 if not login_input_active else 2)
        login_text = FONT_SMALL.render("Log in:", True, BLACK)
        WIN.blit(login_text, (WIDTH/2 - 100 , 220))
        login_input_text = FONT_SMALL.render(login, True, BLACK)
        WIN.blit(login_input_text, (WIDTH/2 - 90, 255))

        pygame.draw.rect(WIN, SKY, password_input_rect, 0 if not password_input_active else 2)
        password_text = FONT_SMALL.render("Password:", True, BLACK)
        WIN.blit(password_text, (WIDTH/2 - 100 , 320))
        password_input_text = FONT_SMALL.render("*" * len(password), True, BLACK)
        WIN.blit(password_input_text, (WIDTH/2 - 90, 355))

        # Render log in button
        login_button_hover = login_button_rect.collidepoint(pygame.mouse.get_pos())
        pygame.draw.rect(WIN, SKY, login_button_rect, 0 if not login_button_hover else 2)
        login_button_text = FONT_LARGE.render("Log in", True, BLACK)
        WIN.blit(login_button_text, (WIDTH/2 - login_button_text.get_width()/2 , 460))

        # render sign up
        signup_button_hover = signup_button_rect.collidepoint(pygame.mouse.get_pos())
        pygame.draw.rect(WIN, SKY, signup_button_rect, 0 if not signup_button_hover else 2)
        signup_button_text = FONT_SMALL.render("Sign up", True, BLACK)
        WIN.blit(signup_button_text, (WIDTH - 105 , HEIGET -35))
    
        # Update display
        pygame.display.update()
#-------------------------------------------------------------------------------------------------------------------------------

  
    #main loop
    run = True
    while run:

        draw_WIN()
        
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if login_input_rect.collidepoint(event.pos):
                    login_input_active = True
                else:
                    login_input_active = False
                    
                if password_input_rect.collidepoint(event.pos):
                    password_input_active = True
                else:
                    password_input_active = False
                if login_button_rect.collidepoint(event.pos):
                    login_button_click = True

                if signup_button_rect.collidepoint(event.pos):
                    signup_button_click = True
            elif event.type == pygame.KEYDOWN:
                if login_input_active:
                    if event.key == pygame.K_BACKSPACE:
                        login = login[:-1]
                    else:
                        login += event.unicode
                if password_input_active:
                    if event.key == pygame.K_BACKSPACE:
                        password = password[:-1]
                    else:
                        password += event.unicode


        # Check if login button is clicked
        if login_button_click:
            try:
                get_user = collection.find({'user_name':login})
                for result in get_user:
                    pwd = result['password']  
                    RECORD = result["record"]
                if fer.decrypt(pwd.encode()).decode() == password:
                    print("login sucsses!")
                    print(f"Player {login}: " , RECORD)               
                    main()
                    update_user = collection.find({"user_name": login})
                    if RECORD < main_player.kill:
                        collection.update_one({"user_name": login}, {"$set":{"level": main_player.level , "record": main_player.kill}})  
                        print(f"New record kill: {main_player.kill}")  
                    run = False  
                        
                else:
                    print("login faild!")

            except Exception:
                print("user not found!")

            run = False
            # Reset login and password
            login_button_click = False
            login = ""
            password = ""
            

        if signup_button_click:
            sign()
            run = False
     
    
            

# --------------------------------------SIGN UP-------------------------------------------- SIGN UP ------------------------------------------------- SIGN UP --------------------------------------------------------------



def sign():

    # Initialize Pygame
    pygame.init()
    FPS = 60 # fram per sconde
    clock = pygame.time.Clock()
    # Set up display
    
    pygame.display.set_caption("Sign Up") 
    
    # Set up text inputs
    user_name = ""
    password = ""
    signup_input_rect = pygame.Rect(WIDTH/2 - 100 , 250, 200, 30)
    password_input_rect = pygame.Rect(WIDTH/2 - 100 , 350, 200, 30)
    signup_input_active = False
    password_input_active = False

    # Set up buttons
    signup_button_rect = pygame.Rect(WIDTH/2 - 60 , 455, 120, 30)
    signup_button_hover = False
    signup_button_click = False

    login_button_rect = pygame.Rect(WIDTH - 120 , HEIGET - 40 , 100, 25)
    login_button_hover = False
    login_button_click = False

    def draw_WIN():
        
        WIN.blit(TITEL_TEXT_SIGNUP, (WIDTH // 2 - TITEL_TEXT_SIGNUP.get_width() // 2, 100))

        # Render signup and password input boxes
        pygame.draw.rect(WIN, WHITE, signup_input_rect, 0 if not signup_input_active else 2)
        signup_text = FONT_SMALL.render("User name:", True, BLACK)
        WIN.blit(signup_text, (WIDTH/2 - 100 , 220))
        signup_input_text = FONT_SMALL.render(user_name, True, BLACK)
        WIN.blit(signup_input_text, (WIDTH/2 - 90, 255))

        pygame.draw.rect(WIN, WHITE, password_input_rect, 0 if not password_input_active else 2)
        password_text = FONT_SMALL.render("Password:", True, BLACK)
        WIN.blit(password_text, (WIDTH/2 - 100 , 320))
        password_input_text = FONT_SMALL.render("*" * len(password), True, BLACK)
        WIN.blit(password_input_text, (WIDTH/2 - 90, 355))

        # Render signup button
        signup_button_hover = signup_button_rect.collidepoint(pygame.mouse.get_pos())
        pygame.draw.rect(WIN, WHITE, signup_button_rect, 0 if not signup_button_hover else 2)
        signup_button_text = FONT_LARGE.render("Sign up", True, BLACK)
        WIN.blit(signup_button_text, (WIDTH/2 - signup_button_text.get_width()/2 , 460))

        # render login button
        login_button_hover = login_button_rect.collidepoint(pygame.mouse.get_pos())
        pygame.draw.rect(WIN, SKY, login_button_rect, 0 if not login_button_hover else 2)
        login_button_text = FONT_SMALL.render("Log in", True, BLACK)
        WIN.blit(login_button_text, (WIDTH - 100 , HEIGET - 35))

    #-------------------------------------------------------------------------------------------------------------------------------
    # Main game loop
    run = True
    while run:

        clock.tick(FPS)
        WIN.blit(BG_REGISTER, (0,0))
        draw_WIN()
        # Update display
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if signup_input_rect.collidepoint(event.pos):
                    signup_input_active = True
                else:
                    signup_input_active = False
                    
                if password_input_rect.collidepoint(event.pos):
                    password_input_active = True
                else:
                    password_input_active = False

                if login_button_rect.collidepoint(event.pos):
                    login_button_click = True

                if signup_button_rect.collidepoint(event.pos):
                    signup_button_click = True

            elif event.type == pygame.KEYDOWN:
                if signup_input_active:
                    if event.key == pygame.K_BACKSPACE:
                        user_name = user_name[:-1]
                    else:
                        user_name += event.unicode
                if password_input_active:
                    if event.key == pygame.K_BACKSPACE:
                        password = password[:-1]
                    else:
                        password += event.unicode

            if signup_button_click:
                if user_name != "" and password != "":
                    user = {'user_name': user_name, "password": fer.encrypt(password.encode()).decode(), 'level': 0 , 'record': 0}
                    collection.insert_one(user)
                    run = False
                else:
                    print("sign up failed. Please try again.")

                user_name = ""
                password = ""
                signup_button_click = False
            
            if login_button_click:
                    login()
                    run = False

