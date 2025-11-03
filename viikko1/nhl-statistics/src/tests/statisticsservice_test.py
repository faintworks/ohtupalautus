import unittest
from statistics_service import StatisticsService
from player import Player
from statistics_service import SortBy

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54),  # 45+54 = 99
            Player("Kurri", "EDM", 37, 53),    # 37+53 = 90
            Player("Yzerman", "DET", 42, 56),  # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)   # 35+89 = 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_player_found(self):
        player = self.stats.search("Lemieux")
        self.assertIsNotNone(player)
        self.assertEqual(player.name, "Lemieux")

    def test_search_player_not_found(self):
        player = self.stats.search("Nonexistent Player")
        self.assertIsNone(player)

    def test_team_players(self):
        edm_players = self.stats.team("EDM")
        self.assertEqual(len(edm_players), 3)  # Semenko, Kurri, Gretzky
        self.assertIn("Semenko", [player.name for player in edm_players])
        self.assertIn("Kurri", [player.name for player in edm_players])
        self.assertIn("Gretzky", [player.name for player in edm_players])

    def test_top_scorers_by_points(self):
        top_players = self.stats.top(3, SortBy.POINTS)
        self.assertEqual(len(top_players), 3)
        self.assertEqual(top_players[0].name, "Gretzky")  # 124 points
        self.assertEqual(top_players[1].name, "Lemieux")  # 99 points
        self.assertEqual(top_players[2].name, "Yzerman")  # 98 points

    def test_top_scorers_by_goals(self):
        top_players = self.stats.top(3, SortBy.GOALS)
        self.assertEqual(len(top_players), 3)
        self.assertEqual(top_players[0].name, "Lemieux")  # 45 goals
        self.assertEqual(top_players[1].name, "Yzerman")  # 42 goals
        self.assertEqual(top_players[2].name, "Kurri")    # 37 goals

    def test_top_scorers_by_assists(self):
        top_players = self.stats.top(3, SortBy.ASSISTS)
        self.assertEqual(len(top_players), 3)
        self.assertEqual(top_players[0].name, "Gretzky")  # 89 assists
        self.assertEqual(top_players[1].name, "Yzerman")   # 56 assists
        self.assertEqual(top_players[2].name, "Lemieux")   # 54 assists

    def test_top_scorers_less_than_requested(self):
        top_players = self.stats.top(10)  # Requesting more than available
        self.assertEqual(len(top_players), 5)  # Should return all players

    def test_invalid_sorting_criterion(self):
        with self.assertRaises(ValueError) as context:
            self.stats.top(3, "INVALID_CRITERION")  # Invalid criterion
        self.assertEqual(str(context.exception), "Invalid sorting criterion")

if __name__ == "__main__":
    unittest.main()