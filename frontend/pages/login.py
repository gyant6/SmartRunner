from assets.components import *
from page import *


class LoginPage(Page):
    def __init__(self, screen):
        super().__init__(screen)
        self.name = "login"
        self.data = {
            "current_page": self.name,
            "username": "",
            "password": "",
            "exit": False
        }

    # set all component variables on input screen
    def set_components(self, screen):
        # background
        bg_img = pygame.image.load('assets/img/sky.png')
        background = Background("background", screen, bg_img)
        self.components["background"] = background

        # start button
        #from top left
        # start_button_rel_x = 1 / 10
        # start_button_rel_y = 1 / 2
        # start_button_rel_width = 1 / 3
        # start_button_rel_height = 1 / 5
        # start_button_img = pygame.image.load('assets/img/start_btn.png')
        # start_button = ImageButton("start_button", screen, start_button_rel_x, start_button_rel_y, start_button_rel_width,
        #                       start_button_rel_height, start_button_img)
        # self.components["start_button"] = start_button

        # picture display - sun to be replaced with a game introduction image
        home_image_rel_x = 1 / 10
        home_image_rel_y = 1 / 2
        home_image_rel_width = 1 / 3
        home_image_rel_height = 1 / 5
        home_image_img = pygame.image.load('assets/img/sun.png')
        home_image_box = ImageDisplay("home_image_box", screen, home_image_rel_x, home_image_rel_y,
                                       home_image_rel_width, home_image_rel_height,home_image_img)
        self.components["home_image_box"] = home_image_box

        #new user creates account
        sign_in_button_rel_x = 7 / 10
        sign_in_button_rel_y = 3 / 4
        sign_in_button_rel_width = 1 / 8
        sign_in_button_rel_height = 1 / 8
        sign_in_button_img = pygame.image.load('assets/img/start_btn.png')
        sign_in_button = ImageButton("sign_in_button", screen, sign_in_button_rel_x, sign_in_button_rel_y,
                                   sign_in_button_rel_width,
                                   sign_in_button_rel_height, sign_in_button_img)
        self.components["sign_in_button"] = sign_in_button

        #user signs in
        create_acc_button_rel_x = 41 / 80
        create_acc_button_rel_y = 3 / 4
        create_acc_button_rel_width = 1 / 8
        create_acc_button_rel_height = 1 / 8
        create_acc_button_img = pygame.image.load('assets/img/start_btn.png')
        create_acc_button = ImageButton("create_acc_button", screen, create_acc_button_rel_x, create_acc_button_rel_y,
                                        create_acc_button_rel_width,
                                        create_acc_button_rel_height, create_acc_button_img)
        self.components["create_acc_button"] = create_acc_button

        # username text input box
        username_input_rel_x = 1 / 2
        username_input_rel_y = 1 / 2
        username_input_rel_width = 1 / 3
        username_input_rel_height = 1 / 16
        username_input_box = TextInput("username_input_box", screen, username_input_rel_x, username_input_rel_y,
                                     username_input_rel_width, username_input_rel_height)
        self.components["username_input_box"] = username_input_box

        # password text input box
        password_input_rel_x = 1 / 2
        password_input_rel_y = 3 / 5
        password_input_rel_width = 1 / 3
        password_input_rel_height = 1 / 16
        password_input_box = TextInput("password_input_box", screen, password_input_rel_x, password_input_rel_y,
                                     password_input_rel_width, password_input_rel_height)
        self.components["password_input_box"] = password_input_box

    # how do the page react to events?
    def page_function(self, triggered_component_list):
        for triggered_component in triggered_component_list:
            if triggered_component in ["sign_in_button", "username_input_box", "password_input_box"]:
                self.data["username"] = self.components["username_input_box"].input
                self.data["password"] = self.components["password_input_box"].input
                #using placeholder for now
                if self.data["username"] == "username" and self.data["password"] == "password":
                    return self.data
                else:
                    print("login failed")

