from get_high_score import get_score


class GameStats():
    """track statistics for alien invasion"""

    def __init__(self, ai_setting):
        """initialize statistics"""
        self.ai_setting = ai_setting
        self.reset_stats()

        # start aliens invasion in an inactive state.
        self.game_active = False

        # high score should never be reset
        self.high_score = get_score()

    def reset_stats(self):
        """initialize statistics that can change during the game"""
        self.ship_left = self.ai_setting.ship_limit
        self.score = 0
        self.level = 1
