class Stats:
    """Tracking player statistics (lives)"""

    def __init__(self):
        """Displaying statistics on the screen"""
        self.reset_stats()
        self.run_game = True
        self.hight_score = 0

    def reset_stats(self):
        """stats changing during the game"""
        self.hero_left = 2
        self.score = 0