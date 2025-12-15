import unittest

def armstrong_szam(num):
    szam_l = []
    n = len(str(num))

    for i in range(len(str(num))):
        szam_l.append(int(str(num)[i]))
    
    test = 0
    for i in szam_l:
        test += i**n

    return test == num

print(armstrong_szam(45))

class TestArmstrong_Numbers(unittest.TestCase):
    def test_one(self):
        fgv = armstrong_szam(153)
        self.assertEqual(fgv, True)

    def test_two(self):
        fgv = armstrong_szam(8208)
        self.assertEqual(fgv, True)

    def test_zeroeth(self):
        fgv = armstrong_szam(199)
        self.assertEqual(fgv, False)

unittest.main()