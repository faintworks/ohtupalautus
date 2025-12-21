from flask import Flask, render_template, request

from tuomari import Tuomari, WINNING_SCORE
from tekoaly import Tekoaly
from tekoaly_parannettu import TekoalyParannettu

app = Flask(__name__, template_folder="templates")


# Ylläpidetään pelimuotokohtaisia pistetilanteita prosessin elinkaaren ajan.
_SCOREBOARDS: dict[str, Tuomari] = {
    "a": Tuomari(),
    "b": Tuomari(),
    "c": Tuomari(),
}


def _pelaa_kierros(mode: str, p1_move: str, p2_move: str | None = None):
    p1 = p1_move

    if mode == "a":
        # Ihminen vs. ihminen
        if not p2_move:
            return None, None, "Toisen pelaajan siirto puuttuu"
        p2 = p2_move
    elif mode == "b":
        # Ihminen vs. yksinkertainen tekoäly
        ai = Tekoaly()
        p2 = ai.anna_siirto()
        ai.aseta_siirto(p1)
    elif mode == "c":
        # Ihminen vs. parannettu tekoäly
        ai = TekoalyParannettu(10)
        ai.aseta_siirto(p1)
        p2 = ai.anna_siirto()
    else:
        return None, None, "Tuntematon pelimuoto"

    if p1 not in ("k", "p", "s") or p2 not in ("k", "p", "s"):
        return None, None, "Siirtojen tulee olla k, p tai s"

    # Haetaan tai alustetaan valitun pelimuodon kumulatiivinen pistetilanne.
    scoreboard = _SCOREBOARDS.get(mode)
    if scoreboard is None:
        scoreboard = Tuomari()
        _SCOREBOARDS[mode] = scoreboard

    # Jos jompikumpi pelaajista on jo saavuttanut voittorajan,
    # peli on tämän pelimuodon osalta päättynyt eikä uusia kierroksia pelata.
    if scoreboard.peli_loppunut():
        return "Peli on jo päättynyt", p2, None

    # Päätellään yksittäisen kierroksen tulos käyttäen olemassa olevaa Tuomari-luokkaa
    kierros_tuomari = Tuomari()
    kierros_tuomari.kirjaa_siirto(p1, p2)

    if kierros_tuomari.tasapelit == 1:
        result = "Tasapeli"  # yksi kierros, joten tasapelit==1 tarkoittaa tasapeliä
    elif kierros_tuomari.ekan_pisteet == 1:
        result = "Ensimmäinen pelaaja voitti"
    else:
        result = "Toinen pelaaja voitti"

    scoreboard.kirjaa_siirto(p1, p2)

    return result, p2, None


@app.route("/", methods=["GET", "POST"])
def index():
    mode = request.form.get("mode", "a")
    p1_move = request.form.get("p1_move", "k")
    p2_move = request.form.get("p2_move", "k")

    result = None
    error = None
    p2_move_display = p2_move

    if request.method == "POST":
        result, resolved_p2_move, error = _pelaa_kierros(mode, p1_move, p2_move)
        if resolved_p2_move is not None:
            p2_move_display = resolved_p2_move

    # Haetaan valitun pelimuodon pistetilanne Tuomari-luokan merkkijonoesityksenä
    scoreboard_obj = _SCOREBOARDS.get(mode)
    scoreboard_text = str(scoreboard_obj) if scoreboard_obj is not None else None

    victory_popup_message = None
    if request.method == "POST" and scoreboard_obj is not None and scoreboard_obj.peli_loppunut():
        # Näytetään erillinen voittoviesti vain sillä kierroksella,
        # jolla joku pelaajista saavuttaa voittorajan.
        if result is not None and result != "Peli on jo päättynyt":
            if scoreboard_obj.ekan_pisteet >= WINNING_SCORE and scoreboard_obj.tokan_pisteet < WINNING_SCORE:
                voittaja = "Ensimmäinen pelaaja"
            elif scoreboard_obj.tokan_pisteet >= WINNING_SCORE and scoreboard_obj.ekan_pisteet < WINNING_SCORE:
                voittaja = "Toinen pelaaja"
            else:
                voittaja = "Peli"

            victory_popup_message = f"{voittaja} saavutti {WINNING_SCORE} voittoa! Peli on päättynyt."

    return render_template(
        "index.html",
        mode=mode,
        p1_move=p1_move,
        p2_move=p2_move,
        p2_move_display=p2_move_display,
        result=result,
        error=error,
        scoreboard=scoreboard_text,
        victory_popup_message=victory_popup_message,
    )


if __name__ == "__main__":
    app.run(debug=True)
