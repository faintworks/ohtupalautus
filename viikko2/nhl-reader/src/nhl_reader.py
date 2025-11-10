from player import PlayerReader, PlayerStats
from rich.console import Console
from rich.table import Table

def main():
    nationality = input("Anna kansalaisuus (esim. FIN): ")
    season = "2024-25"
    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"

    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality(nationality)

    console = Console()
    table = Table(title=f"Pelaajat kansalaisuudelta {nationality}")

    table.add_column("Nimi", justify="left", style="cyan", no_wrap=True)
    table.add_column("Joukkue", justify="center", style="magenta")
    table.add_column("Maalit", justify="right", style="green")
    table.add_column("Syötöt", justify="right", style="yellow")
    table.add_column("Pisteet", justify="right", style="white")

    for player in players:
        table.add_row(player.name, player.team, str(player.goals), str(player.assists), str(player.goals + player.assists))

    console.print(table)

if __name__ == "__main__":
    main()