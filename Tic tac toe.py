tahvel = ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
def KuvaTahvel(tahvel): 
    TühiTahvel = """
_______________________________
|         |         |         |
|    7    |    8    |    9    |
|_________|_________|_________|
|         |         |         |
|    4    |    5    |    6    |
|_________|_________|_________|
|         |         |         |
|    1    |    2    |    3    |
|_________|_________|_________|
"""
    for i in range(1,10):
        if tahvel[i] == "O" or tahvel[i] == "X":
            TühiTahvel = TühiTahvel.replace(str(i), tahvel[i])
        else:
            TühiTahvel = TühiTahvel.replace(str(i), ' ')
    print(TühiTahvel)
def mängija_valik():
    mängija2 = ""
    mängija1 = input("Vali X või O(täht): ")
    mängija1 = mängija1.upper()
    if mängija1 == "X":
        mängija2 = "O"
        return mängija2, mängija1
    if mängija1 == "O":
        mängija2 = "X"
        return mängija2, mängija1

def märgi_sisestamine(tahvel, marker, asend):
    tahvel[asend] = marker
    return tahvel

def koha_kontroll(tahvel, asend):
    return tahvel[asend] == "#"

def koha_valik(tahvel):
    valik = int(input("Valik koht 1-9'ni: "))
    while not koha_kontroll(tahvel, int(valik)):
        valik = int(input("See koht ei ole vaba. Vali muu koht 1-9'ni: "))
    return valik

def full_board_check(tahvel):
    return len([x for x in tahvel if x == '#']) == 1

while True:
    i = 1
    mängijad = mängija_valik()
    game_on = full_board_check(tahvel)
    while not game_on:
        asend = koha_valik(tahvel)
        if i % 2 == 0:
            marker = mängijad[1]
        else:
            marker = mängijad[0]
        märgi_sisestamine(tahvel, marker, int(asend))
        KuvaTahvel(tahvel)
        i += 1
        game_on = full_board_check(tahvel)
