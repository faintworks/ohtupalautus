from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly
from tekoaly import Tekoaly
from tekoaly_parannettu import TekoalyParannettu


def luo_peli(valinta):
    if valinta == "a":
        return KPSPelaajaVsPelaaja()

    if valinta == "b":
        return KPSTekoaly(Tekoaly())

    if valinta == "c":
        return KPSParempiTekoaly(TekoalyParannettu(10))

    return None
