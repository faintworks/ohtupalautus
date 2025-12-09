from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, All, Not, HasFewerThan

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    filtered_with_all = stats.matches(All())
    print(len(filtered_with_all))

    matcher_nyr_not_2_goals = And(
        Not(HasAtLeast(2, "goals")),
        PlaysIn("NYR")
    )
    for player in sorted(stats.matches(matcher_nyr_not_2_goals), key=lambda p: p.name):
        print(player)

    matcher_nyr_fewer_2_goals = And(
        HasFewerThan(2, "goals"),
        PlaysIn("NYR")
    )
    for player in sorted(stats.matches(matcher_nyr_fewer_2_goals), key=lambda p: p.name):
        print(player)

if __name__ == "__main__":
    main()
