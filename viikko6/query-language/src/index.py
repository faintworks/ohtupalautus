from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, All, Not, HasFewerThan, Or
from querybuilder import QueryBuilder

def main():
    print("\nTest: QueryBuilder one_of PHI/EDM")
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)
    query = QueryBuilder()
    matcher = (
        query.one_of(
            QueryBuilder()
                .plays_in("PHI")
                .has_at_least(10, "assists")
                .has_fewer_than(10, "goals"),
            QueryBuilder()
                .plays_in("EDM")
                .has_at_least(50, "points")
        ).build()
    )
    for player in sorted(stats.matches(matcher), key=lambda p: p.name):
        print(player)

    print("\nTest: QueryBuilder NYR, 10-20 goals")
    query = QueryBuilder()
    matcher = (
        query
        .plays_in("NYR")
        .has_at_least(10, "goals")
        .has_fewer_than(20, "goals")
        .build()
    )
    for player in sorted(stats.matches(matcher), key=lambda p: p.name):
        print(player)

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
