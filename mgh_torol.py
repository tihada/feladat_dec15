import unittest

def maganhangzot_torol(text: str):
    mgh = "aáeéoóöőuúüűií" # attól hogy garantáltan nem szerepl ékezetes így egyszerűbb nekem, csak ki kell venni innen az ékezeteseket

    for char in mgh:
        text = text.replace(char, "")
    mgh = mgh.upper()
    for char in mgh:
        text = text.replace(char, "")

    return text

class TestArmstrong_Numbers(unittest.TestCase):
    def test_eq(self):
        fgv = maganhangzot_torol('Iden Java szigeten voltunk nyaralni. Nem is tudtam, hogy elneveztek egy helyet egy programozasi nyelvrol.')
        self.assertEqual(fgv, "dn Jv szgtn vltnk nyrln. Nm s tdtm, hgy lnvztk gy hlyt gy prgrmzs nylvrl.")

unittest.main()