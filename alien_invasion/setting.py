class Setting():
    """a class to store all settings for Alien Invation"""

    def __init__(self):
        """initialize the game's static settings."""
        self.screen_width = 720
        self.screen_height = 540
        self.bg_color = (230, 230, 230)

        # Ship srtting
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # snip
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 3

        # alien setting
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

        # how quickly the speeds up
        self.speedup_scale = 1.1
        # how quickly the alien pont values increase
        self.score_scale = 1.5

        self.initialize_dynamic_setting()

    def initialize_dynamic_setting(self):
        """initialize settings that change throughout the game."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # scoring
        self.alien_points = 10

    def increase_speed(self):
        """increase speed settings and aliens point values."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
