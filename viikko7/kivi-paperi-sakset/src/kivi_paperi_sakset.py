from tuomari import Tuomari, WINNING_SCORE


class KiviPaperiSakset:
    def pelaa(self):
        tuomari = Tuomari()

        ekan = self._ensimmaisen_siirto()
        tokan = self._toisen_siirto(ekan)

        while (
            self._onko_ok_siirto(ekan)
            and self._onko_ok_siirto(tokan)
            and not tuomari.peli_loppunut()
        ):
            tuomari.kirjaa_siirto(ekan, tokan)
            print(tuomari)

            ekan = self._ensimmaisen_siirto()
            tokan = self._toisen_siirto(ekan)

        print("Kiitos!")
        print(tuomari)

    def _ensimmaisen_siirto(self):
        return input("Ensimmäisen pelaajan siirto: ")

    def _toisen_siirto(self, ensimmaisen_siirto):
        raise NotImplementedError

    @staticmethod
    def _onko_ok_siirto(siirto):
        return siirto in ("k", "p", "s")
