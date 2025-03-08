import unittest
from area_rec import area_rectangulo   # type: ignore

class TestAreaRectangulo(unittest.TestCase):
    def test_area_valida(self):
        self.assertEqual(area_rectangulo(5, 10), 50)
        self.assertEqual(area_rectangulo(3, 7), 21)
        self.assertEqual(area_rectangulo(2.5, 4), 10)
    
    def test_area_cero_o_negativo(self):
        with self.assertRaises(ValueError):
            area_rectangulo(0, 5)
        with self.assertRaises(ValueError):
            area_rectangulo(5, 0)
        with self.assertRaises(ValueError):
            area_rectangulo(-3, 7)
        with self.assertRaises(ValueError):
            area_rectangulo(4, -8)

if __name__ == "__main__":
    unittest.main()
