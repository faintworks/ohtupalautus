from rich.console import Console
from rich.table import Table
from player import PlayerReader, PlayerStats

def get_user_input():
    nationality = input("Anna kansalaisuus (esim. FIN): ")
    return nationality

def create_table(title, players):
    table = Table(title=title)
    table.add_column("Nimi", justify="left", style="cyan", no_wrap=True)
    table.add_column("Joukkue", justify="center", style="magenta")
    table.add_column("Maalit", justify="right", style="green")
    table.add_column("Syötöt", justify="right", style="yellow")
    table.add_column("Pisteet", justify="right", style="white")

    for player in players:
        table.add_row(player.name, player.team, str(player.goals), str(player.assists), str(player.goals + player.assists))

    return table

def main():
    nationality = get_user_input()
    season = "2024-25"
    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"

    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality(nationality)

    console = Console()
    table = create_table(f"Pelaajat kansalaisuudelta {nationality}", players)
    console.print(table)

if __name__ == "__main__":
    main()
