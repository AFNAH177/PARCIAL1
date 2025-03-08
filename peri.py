def perimetro_rectangulo(base: float, altura: float) -> float:
    """Calcula el perímetro de un rectángulo."""
    if base <= 0 or altura <= 0:
        raise ValueError("La base y la altura deben ser mayores que cero.")
    return 2 * (base + altura)

def main():
    try:
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        perimetro = perimetro_rectangulo(base, altura)
        print(f"El perímetro del rectángulo es: {perimetro}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

import unittest

class TestPerimetroRectangulo(unittest.TestCase):
    def test_perimetro_valido(self):
        self.assertEqual(perimetro_rectangulo(5, 10), 30)
        self.assertEqual(perimetro_rectangulo(3, 7), 20)
        self.assertEqual(perimetro_rectangulo(2.5, 4), 13)
    
    def test_perimetro_cero_o_negativo(self):
        with self.assertRaises(ValueError):
            perimetro_rectangulo(0, 5)
        with self.assertRaises(ValueError):
            perimetro_rectangulo(5, 0)
        with self.assertRaises(ValueError):
            perimetro_rectangulo(-3, 7)
        with self.assertRaises(ValueError):
            perimetro_rectangulo(4, -8)

if __name__ == "__main__":
    unittest.main()
