class Stats:
    """Tracking player statistics (lives)"""

    def __init__(self):
        """Displaying statistics on the screen"""
        self.reset_stats()
        self.run_game = True
        try:
            with open('highest_score.txt', 'r') as f:
                self.height_score = int(f.readline())
        except Exception as e:
            with open('highest_score.txt', 'w') as g:
                g.write(str(0))
                self.height_score = 0

    def reset_stats(self):
        """stats changing during the game"""
        self.hero_left = 2
        self.score = 0
