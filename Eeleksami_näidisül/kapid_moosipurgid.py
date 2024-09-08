def loo_kapid(järjend):
    ridade_arv = järjend[-2]
    veergude_arv = järjend[-1]
    maatriks = []
    for _ in range(ridade_arv):
        rida_list = []
        for _ in range(veergude_arv):
            rida_list.append(0)
        maatriks.append(rida_list)
    for i, koht in enumerate(järjend):
        if isinstance(koht, tuple):
            maatriks[koht[0]-1][koht[1]-1] = koht[2]
        else:
            pass
    return maatriks


def ekraanile(kapid): #kapid on maatriks
    kapid_sõne = ""
    for i, rida in enumerate(kapid):
        kapid_sõne += f"{' '.join(map(str, rida))}"
        if i != len(kapid)-1:
            kapid_sõne += "\n"
    return kapid_sõne


def nihuta_paremale(masiiv):
    pikkus = len(masiiv[0])-1
    for i, rida in enumerate(masiiv):
        for j, num in enumerate(rida):
            if j < pikkus:
                if rida[-1-j] == 0:
                    rida[-1-j] = rida[-2-j]
                    rida[-2-j] = 0
            else:
                pass
    return masiiv

def nihuta_alla(masiiv):
    pikkus = len(masiiv)-1
    for i, rida in enumerate(masiiv):
        for j, num in enumerate(rida):
            if masiiv[pikkus-i][j] == 0:
                if pikkus-i-1 == -1:
                    pass
                else:
                    masiiv[pikkus-i][j] = masiiv[pikkus-i-1][j]
                    masiiv[pikkus-i-1][j] = 0
    return masiiv   
    
maatriks = loo_kapid([(1,2,1), (1,3,2), (1,4,4,), 
                 (3,1,5), (3,2,6), (2,1,2),
                 (2,3,8), (2,4,4), 3, 5])
print(ekraanile(maatriks))
while True:
    tegevus = input("paremale - P/p\nalla - A/a\nlõpeta - L/l\n")
    if tegevus == "P" or tegevus == "p":
        maatriks = nihuta_paremale(maatriks)
        print(ekraanile(maatriks))
    elif tegevus == "A" or tegevus == "a":
        maatriks = nihuta_alla(maatriks)
        print(ekraanile(maatriks))
    elif tegevus == "L" or tegevus == "l":
        break
    else:
        print("Sisestus polnud sobiv!")

#1h 50min