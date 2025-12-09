class Summa:
    def __init__(self, logiikka, syote_funktio):
        self._logiikka = logiikka
        self._syote_funktio = syote_funktio

    def suorita(self):
        try:
            arvo = int(self._syote_funktio())
        except:
            arvo = 0
        self._logiikka.plus(arvo)


class Erotus:
    def __init__(self, logiikka, syote_funktio):
        self._logiikka = logiikka
        self._syote_funktio = syote_funktio

    def suorita(self):
        try:
            arvo = int(self._syote_funktio())
        except:
            arvo = 0
        self._logiikka.miinus(arvo)


class Nollaus:
    def __init__(self, logiikka, syote_funktio=None):
        self._logiikka = logiikka

    def suorita(self):
        self._logiikka.nollaa()


class Kumoa:
    def __init__(self, logiikka, syote_funktio=None):
        self._logiikka = logiikka

    def suorita(self):
        # Tätä EI tarvitse toteuttaa tässä tehtävässä!
        pass
