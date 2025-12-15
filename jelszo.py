import unittest

def jelszo_erosseg(passw):
    strength = 1
    if len(passw) >= 5 : strength += 1
    if len(passw) >= 8 : strength += 2
    for char in passw:
        if char == "_" or char == "-" or char == ".": strength += 2

    if "jelszo" in passw or "123" in passw:
        strength = 0
    if len(passw) == 0: strength = 0

    return strength

class TestArmstrong_Numbers(unittest.TestCase):
    def test_strong(self):
        fgv = jelszo_erosseg('hazi.macska_4_life')
        self.assertEqual(fgv, 10)

    def test_weak(self):
        fgv = jelszo_erosseg("ez1feltorhetetlenjelszo")
        self.assertEqual(fgv, 0)

    def test_zero(self):
        fgv = jelszo_erosseg('Bármi_erős_kulcs_123')
        self.assertLessEqual(fgv, 0)

unittest.main()