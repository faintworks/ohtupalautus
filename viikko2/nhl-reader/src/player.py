import requests

class Player:
    def __init__(self, player_dict):
        self.name = player_dict['name']
        self.team = player_dict['team']
        self.goals = player_dict['goals']
        self.assists = player_dict['assists']
        self.nationality = player_dict['nationality']
    
    def __str__(self):
        return f"{self.name:20} {self.team}   {self.goals} + {self.assists} = {self.goals + self.assists}"

class PlayerReader:
    def __init__(self, url):
        self.url = url
        self.players = self.get_players()

    def get_players(self):
        response = requests.get(self.url).json()
        players = [Player(player_dict) for player_dict in response]
        return players
    
class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        filtered_players = filter(lambda player: player.nationality == nationality, self.reader.players)
        sorted_players = sorted(filtered_players, key=lambda player: player.goals + player.assists, reverse=True)
        return sorted_players