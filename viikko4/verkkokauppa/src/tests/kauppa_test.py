import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viite_mock = Mock()
        self.varasto_mock = Mock()

        # jokaisessa testissä viite = 42
        self.viite_mock.uusi.return_value = 42

        # kaupan tili on kovakoodattu luokassa
        self.kaupan_tili = "33333-44455"

    def test_yksi_tuote_ostos_kutsuu_tilisiirtoa_oikeilla_arvoilla(self):
        # varasto: yksi tuote löytyy
        self.varasto_mock.saldo.side_effect = lambda id: 10 if id == 1 else 0
        self.varasto_mock.hae_tuote.side_effect = lambda id: Tuote(1, "maito", 5)

        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viite_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("matti", "11111")

        self.pankki_mock.tilisiirto.assert_called_with(
            "matti",
            42,             # viite
            "11111",        # asiakkaan tili
            self.kaupan_tili,
            5               # summa
        )

    def test_kaksi_eri_tuotetta_kutsuu_tilisiirtoa_oikealla_sumalla(self):
        # kaksi tuotetta varastossa
        def saldo(id):
            if id in (1, 2):
                return 10
            return 0

        def hae(id):
            if id == 1:
                return Tuote(1, "maito", 5)
            if id == 2:
                return Tuote(2, "leipä", 3)

        self.varasto_mock.saldo.side_effect = saldo
        self.varasto_mock.hae_tuote.side_effect = hae

        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viite_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("matti", "11111")

        self.pankki_mock.tilisiirto.assert_called_with(
            "matti",
            42,
            "11111",
            self.kaupan_tili,
            5 + 3
        )

    def test_kaksi_samaa_tuotetta_kutsuu_tilisiirtoa_oikealla_sumalla(self):
        # saldo riittää kahdelle samalle tuotteelle
        self.varasto_mock.saldo.side_effect = lambda id: 10 if id == 1 else 0
        self.varasto_mock.hae_tuote.side_effect = lambda id: Tuote(1, "maito", 5)

        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viite_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("matti", "11111")

        self.pankki_mock.tilisiirto.assert_called_with(
            "matti",
            42,
            "11111",
            self.kaupan_tili,
            10    # 5 + 5
        )

    def test_toinen_tuote_loppu_summa_oikein(self):
        # 1 löytyy, 2 on loppu
        def saldo(id):
            return 10 if id == 1 else 0

        def hae(id):
            if id == 1:
                return Tuote(1, "maito", 5)
            if id == 2:
                return Tuote(2, "leipä", 3)

        self.varasto_mock.saldo.side_effect = saldo
        self.varasto_mock.hae_tuote.side_effect = hae

        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viite_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)  # tämä onnistuu
        kauppa.lisaa_koriin(2)  # saldo=0 → ei lisätä
        kauppa.tilimaksu("matti", "11111")

        self.pankki_mock.tilisiirto.assert_called_with(
            "matti",
            42,
            "11111",
            self.kaupan_tili,
            5      # vain ensimmäinen tuote lasketaan
        )