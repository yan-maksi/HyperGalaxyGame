class Stats:
    def __init__(self):
        """Displaying statistics on the screen"""
        self.score = 0
        self.hero_left = 2
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

    def check_height_score(self, sc):
        """"Check for new records"""
        if self.score > self.height_score:
            self.height_score = self.score
            sc.image_height_score()
            with open('../highest_score.txt', 'w') as f:
                f.write(str(self.height_score))
