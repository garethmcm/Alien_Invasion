class Settings():
    """ A class to store all settings in game """

    def __init__(self):
        """ initialise the game settings """
        # screen settings
        self.screen_width = 1200
        self.screen_height = 650
        self.bg_colour = (230, 230, 230)

        # Ship settings
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # Bullet springs
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = 60, 60, 60
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 5
        # fleet direction of 1 represents right -1 left
        self.fleet_direction = 1