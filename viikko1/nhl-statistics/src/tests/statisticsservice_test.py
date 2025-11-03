import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri", "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
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

    def test_top_scorers(self):
        top_players = self.stats.top(3)
        self.assertEqual(len(top_players), 3)
        self.assertEqual(top_players[0].name, "Gretzky")  # 124 points
        self.assertEqual(top_players[1].name, "Lemieux")  # 99 points
        self.assertEqual(top_players[2].name, "Yzerman")  # 98 points

    def test_top_scorers_less_than_requested(self):
        top_players = self.stats.top(10)  # Requesting more than available
        self.assertEqual(len(top_players), 5)  # Should return all players

if __name__ == "__main__":
    unittest.main()