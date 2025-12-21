import web_app


def test_pelaa_kierros_human_vs_human_draw():
    result, p2, error = web_app._pelaa_kierros("a", "k", "k")
    assert error is None
    assert p2 == "k"
    assert result == "Tasapeli"


def test_pelaa_kierros_invalid_move_returns_error():
    result, p2, error = web_app._pelaa_kierros("a", "x", "k")
    assert result is None
    assert p2 is None or p2 == "k"  # p2 is not important here
    assert error is not None
    assert "Siirtojen tulee olla" in error


def test_pelaa_kierros_requires_second_player_move_in_mode_a():
    result, p2, error = web_app._pelaa_kierros("a", "k", None)
    assert result is None
    assert p2 is None
    assert error is not None
    assert "Toisen pelaajan siirto puuttuu" in error
