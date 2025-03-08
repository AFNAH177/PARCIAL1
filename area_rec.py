def area_rectangulo(base: float, altura: float) -> float:
    """Calcula el área de un rectángulo."""
    if base <= 0 or altura <= 0:
        raise ValueError("La base y la altura deben ser mayores que cero.")
    return base * altura

def main():
    try:
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        area = area_rectangulo(base, altura)
        print(f"El área del rectángulo es: {area}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

import unittest

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