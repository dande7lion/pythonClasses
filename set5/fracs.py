import fractions

def is_fraction_correct(frac):
    return True if frac[1] is not 0 else False

def convert_fractions_to_a_common_denominator(frac1, frac2):
    least_common_multiplier = frac1[1]*frac2[1] // fractions.gcd(frac1[1], frac2[1])
    multiplier_1 = least_common_multiplier//frac1[1]
    multiplier_2 = least_common_multiplier//frac2[1]
    frac1[0] = frac1[0]*multiplier_1
    frac2[0] = frac2[0]*multiplier_2
    frac1[1] = least_common_multiplier
    frac2[1] = least_common_multiplier
    return [frac1, frac2]

# e.g. [-11, -15] -> [11, 15] (both are correct, the second form is used by default)
def convert_negative_to_positive(frac):
    if frac[0] < 0 and frac[1] < 0:
        frac[0] = abs(frac[0])
        frac[1] = abs(frac[1])
    return frac

# frac1 + frac2
def add_frac(frac1, frac2):
    if not is_fraction_correct(frac1) or not is_fraction_correct(frac2):
        raise TypeError("Denominator can not be zero!")
    frac1, frac2 = convert_fractions_to_a_common_denominator(frac1, frac2)  
    return convert_negative_to_positive([frac1[0] + frac2[0],frac1[1]])

# frac1 - frac2
def sub_frac(frac1, frac2):
    frac1, frac2 = convert_fractions_to_a_common_denominator(frac1, frac2)  
    return convert_negative_to_positive([frac1[0] - frac2[0], frac1[1]])

def mul_frac(frac1, frac2): pass        # frac1 * frac2

def div_frac(frac1, frac2): pass        # frac1 / frac2

def is_positive(frac): pass             # bool, czy dodatni

def is_zero(frac): pass                 # bool, typu [0, x]

def cmp_frac(frac1, frac2): pass        # -1 | 0 | +1

def frac2float(frac): pass              # konwersja do float

f1 = [-1, 2]                  # -1/2
f2 = [0, 1]                   # zero
f3 = [3, 1]                   # 3
f4 = [6, 2]                   # 3 (niejednoznaczność)
f5 = [0, 2]                   # zero (niejednoznaczność)

import unittest

class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([3, 5], [4, 3]), [29, 15])
        self.assertEqual(add_frac([17, 83], [54, 18]), [4788, 1494])
        self.assertEqual(add_frac([3, -5], [4, -3]), [29, -15])
        with self.assertRaises(TypeError):
            add_frac([5, 0], [4, 8])

    def test_sub_frac(self):
        self.assertEqual(sub_frac([3, 5], [4, 3]), [-11, 15])
        self.assertEqual(sub_frac([17, 83], [54, 18]), [-4176, 1494])
        self.assertEqual(sub_frac([3, -5], [4, -3]), [11, 15])
        with self.assertRaises(TypeError):
            add_frac([5, 0], [4, 8])

    def test_mul_frac(self): pass

    def test_div_frac(self): pass

    def test_is_positive(self): pass

    def test_is_zero(self): pass

    def test_cmp_frac(self): pass

    def test_frac2float(self): pass

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()
