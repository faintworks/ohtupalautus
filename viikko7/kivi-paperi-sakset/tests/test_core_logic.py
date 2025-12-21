import web_app
from tuomari import WINNING_SCORE


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


def test_game_ends_after_five_wins_for_first_player():
    # Pelataan niin monta kierrosta, että ensimmäinen pelaaja saavuttaa voittorajan.
    for _ in range(WINNING_SCORE):
        result, p2, error = web_app._pelaa_kierros("a", "k", "s")
        assert error is None
        assert result == "Ensimmäinen pelaaja voitti"

    # Tämän jälkeen peli on päättynyt, eikä tulosta enää päivitetä.
    result, p2, error = web_app._pelaa_kierros("a", "k", "s")
    assert error is None
    assert "Peli on jo päättynyt" in result

    scoreboard = web_app._SCOREBOARDS["a"]
    assert scoreboard.ekan_pisteet == WINNING_SCORE
    assert scoreboard.tokan_pisteet == 0
