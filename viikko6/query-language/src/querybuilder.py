from matchers import All, And, PlaysIn, HasAtLeast, HasFewerThan, Or

class QueryBuilder:
    def __init__(self, matcher=None):
        self._matcher = matcher or All()

    def plays_in(self, team):
        return QueryBuilder(And(self._matcher, PlaysIn(team)))

    def has_at_least(self, value, attr):
        return QueryBuilder(And(self._matcher, HasAtLeast(value, attr)))

    def has_fewer_than(self, value, attr):
        return QueryBuilder(And(self._matcher, HasFewerThan(value, attr)))

    def one_of(self, *builders):
        matchers = [b.build() for b in builders]
        return QueryBuilder(Or(*matchers))

    def build(self):
        return self._matcher
