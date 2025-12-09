class Summa:
    def __init__(self, logiikka, syote_funktio):
        self._logiikka = logiikka
        self._syote_funktio = syote_funktio
        self._edellinen_arvo = None

    def suorita(self):
        try:
            arvo = int(self._syote_funktio())
        except:
            arvo = 0

        self._edellinen_arvo = self._logiikka.arvo()

        self._logiikka.plus(arvo)

    def kumoa(self):
        if self._edellinen_arvo is not None:
            self._logiikka.aseta_arvo(self._edellinen_arvo)


class Erotus:
    def __init__(self, logiikka, syote_funktio):
        self._logiikka = logiikka
        self._syote_funktio = syote_funktio
        self._edellinen_arvo = None

    def suorita(self):
        try:
            arvo = int(self._syote_funktio())
        except:
            arvo = 0

        self._edellinen_arvo = self._logiikka.arvo()
        self._logiikka.miinus(arvo)

    def kumoa(self):
        if self._edellinen_arvo is not None:
            self._logiikka.aseta_arvo(self._edellinen_arvo)


class Nollaus:
    def __init__(self, logiikka, syote_funktio=None):
        self._logiikka = logiikka
        self._edellinen_arvo = None

    def suorita(self):
        self._edellinen_arvo = self._logiikka.arvo()
        self._logiikka.nollaa()

    def kumoa(self):
        if self._edellinen_arvo is not None:
            self._logiikka.aseta_arvo(self._edellinen_arvo)


class Kumoa:
    def __init__(self, logiikka, syote_funktio=None):
        self._logiikka = logiikka

    def suorita(self):
        pass

    def kumoa(self):
        pass
