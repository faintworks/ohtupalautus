class TennisGame:
    POINT_NAMES = ["Love", "Fifteen", "Thirty", "Forty"]

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.score1 = 0
        self.score2 = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.score1 = self.score1 + 1
        else:
            self.score2 = self.score2 + 1

    def is_tie(self):
        return self.score1 == self.score2

    def _tie_score(self):
        if self.score1 >= 3:
            return "Deuce"

        return f"{self.POINT_NAMES[self.score1]}-All"

    def _advantage_or_win(self):
        diff = self.score1 - self.score2

        if diff == 1:
            return f"Advantage {self.player1_name}"
        if diff == -1:
            return f"Advantage {self.player2_name}"
        if diff >= 2:
            return f"Win for {self.player1_name}"

        return f"Win for {self.player2_name}"

    def _normal_score(self):
        return f"{self.POINT_NAMES[self.score1]}-{self.POINT_NAMES[self.score2]}"

    def get_score(self):
        if self.is_tie():
            return self._tie_score()

        elif self.score1 >= 4 or self.score2 >= 4:
            return self._advantage_or_win()
        else:
            return self._normal_score()
