from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, All, Not, HasFewerThan, Or

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    print("Test: All matcher returns all players (should print 899)")
    filtered_with_all = stats.matches(All())
    print(len(filtered_with_all))

    print("\nTest: Not(HasAtLeast(2, 'goals')) and PlaysIn('NYR')")
    matcher_nyr_not_2_goals = And(
        Not(HasAtLeast(2, "goals")),
        PlaysIn("NYR")
    )
    for player in stats.matches(matcher_nyr_not_2_goals):
        print(player)

    print("\nTest: HasFewerThan(2, 'goals') and PlaysIn('NYR')")
    matcher_nyr_fewer_2_goals = And(
        HasFewerThan(2, "goals"),
        PlaysIn("NYR")
    )
    for player in stats.matches(matcher_nyr_fewer_2_goals):
        print(player)

    print("\nTest: Or(HasAtLeast(45, 'goals'), HasAtLeast(70, 'assists'))")
    matcher_or_goals_assists = Or(
        HasAtLeast(45, "goals"),
        HasAtLeast(70, "assists")
    )
    for player in stats.matches(matcher_or_goals_assists):
        print(player)

    print("\nTest: And(HasAtLeast(70, 'points'), Or(PlaysIn('COL'), PlaysIn('FLA'), PlaysIn('BOS')))" )
    matcher_and_points_or_teams = And(
        HasAtLeast(70, "points"),
        Or(
            PlaysIn("COL"),
            PlaysIn("FLA"),
            PlaysIn("BOS")
        )
    )
    for player in stats.matches(matcher_and_points_or_teams):
        print(player)

if __name__ == "__main__":
    main()
