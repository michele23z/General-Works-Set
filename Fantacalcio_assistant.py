# Extraction values from file
def leggi_file(nome_file):
    file = open(nome_file, "r", encoding="utf-8")
    elenco_giocatori = []
    for riga in file:
        campi = riga.split(",")
        record = {"nome": campi[0].strip(),
                  "squadra": campi[1].strip(),
                  "ruolo": campi[2].strip(),
                  "costo": campi[3].strip()
                  }

        elenco_giocatori.append(record)

    file.close()

    return elenco_giocatori


# functions to buy players by their role and settings specific parameters for each.

def compra_portiere(prev):
    squadra = []

    B = 20
    c_max = 0
    np = 0
    for g in prev:
        if np == 2:
            B = B - y
            squadra.append(mio_max)
            np = np + 1
            return squadra
        else:
            y = int(g.get("costo"))
            if B > 3:
                if y > c_max:
                    mio_max = g
                    c_max = y

                elif y == 1:
                    mio = g
                    B = B - y
                    squadra.append(mio)
                    np = np + 1
    return squadra


def compra_difensori(prev):
    nd = 0
    B = 40
    squadra = []
    c_max = 0
    for g in prev:
        if nd == 7:
            squadra.append(mio_max)
            nd = nd + 1
            B = B - c_max

            return squadra
        else:
            y = int(g.get("costo"))

            if y <= B - 7:
                if y > c_max:
                    mio_max = g
                    c_max = y

                elif y == 1:
                    mio = g
                    B = B - y
                    squadra.append(mio)
                    nd = nd + 1
    return squadra


def compra_centrocampisti(prev):
    nc = 0
    B = 80
    c_max = 0
    squadra = []
    for g in prev:
        if nc == 7:
            squadra.append(mio_max)
            nc = nc + 1
            B = B - c_max
            # print(f"dif{squadra}")
            return squadra
        else:
            y = int(g.get("costo"))

            if y <= B - 7:
                if y > c_max:
                    mio_max = g
                    c_max = y

                elif y == 1:
                    mio = g
                    B = B - y
                    squadra.append(mio)
                    nc = nc + 1
    return squadra


def compra_attaccanti(prev):
    squadra = []
    na = 0
    B = 120
    c_max = 0
    for g in prev:
        if na == 5:
            squadra.append(mio_max)
            na = na + 1
            B = B - c_max
            return squadra
        else:
            y = int(g.get("costo"))

            if y <= B - 7:
                if y > c_max:
                    mio_max = g
                    c_max = y

                elif y == 1:
                    mio = g
                    B = B - y
                    squadra.append(mio)
                    na = na + 1
    return squadra

# Divide players by role and apply functions to buy it.
def forma_squadra(elenco_giocatori):
    fantasquadra = []
    portieri = []
    difensori = []
    centrocampisti = []
    attaccanti = []

    for x in elenco_giocatori:
        y = x.get("ruolo")
        if y == "portiere":
            portieri.append(x)
        else:
            if y == "difensore":
                difensori.append(x)
            else:
                if y == "centrocampista":
                    centrocampisti.append(x)
                else:
                    if y == "attaccante":
                        attaccanti.append(x)

    por = compra_portiere(portieri)
    fantasquadra.append(por)
    dif = compra_difensori(difensori)
    fantasquadra.append(dif)
    cen = compra_centrocampisti(centrocampisti)
    fantasquadra.append(cen)
    att = compra_attaccanti(attaccanti)
    fantasquadra.append(att)

    return fantasquadra


def main():
    giocatori = leggi_file("fantacalcio.txt")
    fantasquadra = forma_squadra(giocatori)
    for i in fantasquadra:
        for el in i:
            print(el, end="\n")


main()
