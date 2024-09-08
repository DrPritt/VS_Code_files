"""Harmooniline keskmine"""

import sys

def harmooniline_keskmine(a, b, c, d):
    pöördväärtus_a = 1/a
    pöördväärtus_b = 1/b
    pöördväärtus_c = 1/c
    pöördväärtus_d = 1/d
    return (4/(pöördväärtus_a + pöördväärtus_b + pöördväärtus_c + pöördväärtus_d))

def harmoniseerimine(list):
    ridade_arv = int(len(list))
    veergude_arv = int(len(list[0]))
    if veergude_arv < 2 or ridade_arv < 2:
        sys.exit("[[0]]")
    if veergude_arv // 2 != 0:
        veergude_arv -= 1
        if veergude_arv == 1:
            veergude_arv += 1
    if ridade_arv // 2 != 0:
        ridade_arv -= 1
        if ridade_arv == 1:
            ridade_arv += 1
    boxes_x = int(ridade_arv / 2)
    boxes_y = int(veergude_arv / 2)
    x = 0
    y = 0
    new_list = []
    for x in range(boxes_x): #0, 1
        x = x * 2
        ajutine = []
        for y in range(boxes_y): #0, 1, 2
            y = y * 2
            harmoonia = harmooniline_keskmine(list[x][y], list[x][y+1], list[x+1][y], list[x+1][y+1])
            ajutine.append(harmoonia)
        new_list.append(ajutine)
    print(new_list)
    harmoniseerimine(new_list)
    
    
print(harmoniseerimine([[1, 3, 4, 6, 3, 4, 6],[4, 5, 6, 4, 1, 5, 1],[4, 2, 2, 5, 6, 7, 4],[1, 3, 4, 5, 1, 6, 5],[2, 3, 3, 5, 2, 6, 2]]))

#Kui ma nüüd teen siin väikese muudatuse, vat aga teeme veel ühe muudatuse!!!!!!!!!!!!!!!!