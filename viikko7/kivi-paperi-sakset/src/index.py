from pelitehdas import luo_peli

def main():
    while True:
        print(
            "Valitse pelataanko\n"
            " (a) Ihmistä vastaan\n"
            " (b) Tekoälyä vastaan\n"
            " (c) Parannettua tekoälyä vastaan\n"
            "Muilla valinnoilla lopetetaan"
        )

        valinta = input()
        peli = luo_peli(valinta)

        if not peli:
            break

        print(
            "Peli loppuu kun pelaaja antaa virheellisen siirron "
            "eli jonkun muun kuin k, p tai s, tai kun jompikumpi pelaajista "
            "saavuttaa 5 voittoa"
        )

        peli.pelaa()

if __name__ == "__main__":
    main()
