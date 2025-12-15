import unittest

def lepes(mozgas: str):
    vert = 0
    hor = 0
    for move in mozgas:
        if move == "F": vert += 1
        if move == "L": vert -= 1
        if move == "J": hor += 1
        if move == "B": hor -= 1
    
    out = ""
    if hor > 0:
        out+=f"{hor} lépés jobbra"
    elif hor < 0:
        out+=f"{hor*-1} lépés balra"

    if len(out) != 0: out+= ", "

    if vert > 0:
        out+=f"{vert} lépés fel"
    elif vert < 0:
        out+=f"{vert*-1} lépés le"
    
    if vert == 0 and hor == 0:
        out += "Nem mentünk sehova"

    return out

class TestArmstrong_Numbers(unittest.TestCase):
    def test_one(self):
        fgv = lepes("JJFBFFFFFFBBBL")
        self.assertEqual(fgv, '2 lépés balra, 6 lépés fel')

    def test_two(self):
        fgv = lepes("FBLLLJLLJ")
        self.assertEqual(fgv, '1 lépés jobbra, 4 lépés le')

    def test_three(self):
        fgv = lepes("FFF")
        self.assertEqual(fgv, '3 lépés fel')

    def test_four(self):
        fgv = lepes("FFLLBBJJ")
        self.assertEqual(fgv, 'Nem mentünk sehova')

unittest.main()