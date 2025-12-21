from kivi_paperi_sakset import KiviPaperiSakset

class KPSTekoaly(KiviPaperiSakset):
    def __init__(self, tekoaly):
        self._tekoaly = tekoaly

    def _toisen_siirto(self, ensimmaisen_siirto):
        siirto = self._tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {siirto}")
        self._tekoaly.aseta_siirto(ensimmaisen_siirto)
        return siirto
