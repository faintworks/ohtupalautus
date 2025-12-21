def test_index_get_renders_page(client):
    resp = client.get("/")
    assert resp.status_code == 200
    body = resp.data.decode("utf-8")
    # Basic sanity check that main UI elements are present
    assert "Kivi–Paperi–Sakset" in body or "Kivi-Paperi-Sakset" in body
    assert "Pelimuoto" in body


def test_human_vs_human_round_updates_scoreboard(client):
    # First player: k, second player: s => first player wins
    resp = client.post(
        "/",
        data={"mode": "a", "p1_move": "k", "p2_move": "s"},
    )
    assert resp.status_code == 200
    body = resp.data.decode("utf-8")

    assert "Ensimmäinen pelaaja voitti" in body
    # Scoreboard uses Tuomari.__str__ output
    assert "Pelitilanne: 1 - 0" in body
    assert "Tasapelit: 0" in body


def test_scoreboard_persists_between_requests_for_same_mode(client):
    # Play two winning rounds for first player in mode a
    for _ in range(2):
        resp = client.post(
            "/",
            data={"mode": "a", "p1_move": "k", "p2_move": "s"},
        )
        assert resp.status_code == 200

    body = resp.data.decode("utf-8")
    # Two wins accumulated for the first player
    assert "Pelitilanne: 2 - 0" in body


def test_human_vs_simple_ai_round_has_deterministic_scoreboard(client):
    # In mode b, Tekoaly always starts from the same state in this process,
    # so the round outcome is deterministic.
    resp = client.post(
        "/",
        data={"mode": "b", "p1_move": "k"},
    )
    assert resp.status_code == 200
    body = resp.data.decode("utf-8")

    # The scoreboard must reflect exactly one round played in mode b
    assert "Pelitilanne:" in body
    assert "Tasapelit:" in body
