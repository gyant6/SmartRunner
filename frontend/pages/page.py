import pygame


# parent class for pages
# python.Surface screen - screen the page is to be displayed
class Page:
    def __init__(self, screen):
        self.name = "page_constructor"              # name of page
        self.run = True                             # if the page is running
        self.screen = screen                        # screen the page to display on
        self.screen_width = screen.get_width()      # screen width
        self.screen_height = screen.get_height()    # screen height
        self.data = {                               # data to and from other pages
            "current_page": self.name,
            "exit": False
        }
        self.components = {}                        # all components within the page

    # initialize all components and add them to component list
    def set_components(self):
        pass
    '''
    draw all components within component list
    '''
    def draw_components(self):
        for component in self.components.values():
            component.draw()


    '''
    resize every component in page to scale with current screen dimensions
    '''
    def resize_components(self):
        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        new_screen = pygame.display.set_mode((self.screen_width, self.screen_height),
                                             pygame.RESIZABLE)
        for component in self.components.values():
            component.resize(new_screen)
            component.draw()
    '''
    main logic of page in reaction to event
    will be kept running once page starts running
    '''
    def page_function(self, event):
        pass

    # start running the page
    def start(self, screen):
        self.data["current_page"] = self.name
        self.set_components(screen)
        while self.run:
            self.draw_components()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.data["exit"] = True
                    return self.data
                if event.type == pygame.VIDEORESIZE:
                    self.resize_components()
                triggered_component_list = []
                for component in self.components.values():
                    if component.mouse_function:
                        if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
                            if component.trigger(event):
                                print(component.name)
                                triggered_component_list.append(component.name)
                    if component.keyboard_function:
                        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                            if component.trigger(event):
                                print(component.name)
                                triggered_component_list.append(component.name)
                self.page_function(triggered_component_list)

            pygame.display.update()
