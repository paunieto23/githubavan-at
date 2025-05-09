from solucio03 import *
from solucio04 import *
import unittest

class TestSolucio3(unittest.TestCase):
    """
    Classe per provar les funcions definides a la solució 3.
    """

    def test1(self):
        """
        Prova per comprovar les funcions de mínim i màxim.
        Comprova que el mínim i màxim de les marques de rendiment es calculen bé.
        """
        resultat = trobar_min_max_rendiment(10.50, 12.00, 15.00)
        self.assertEqual(resultat, (10.50, 15.00))  # El mínim és 10.50 i el màxim és 15.00

        resultat = trobar_min_max_rendiment()  # Sense paràmetres, ha de retornar (0, 0)
        self.assertEqual(resultat, (1, 0))

    def test2(self):
        """
        Prova per comptar el nombre d'estudiants al diccionari.
        Comprova que el nombre d'estudiants és correcte.
        """
        resultat = comptar_estudiants(notes_estudiants)
        self.assertEqual(resultat, 4)  # Ha de retornar 4 estudiants

    def test3(self):
        """
        Prova per comptar els estudiants en una matèria específica.
        Comprova que es compten correctament els estudiants en "Matemàtiques".
        """
        resultat = comptar_estudiants_matèria_v2(notes_estudiants, "Matemàtiques")
        self.assertEqual(resultat, 3)  # Hi ha 3 estudiants en "Matemàtiques"


class TestSolucio4(unittest.TestCase):
    """
    Classe per provar les funcions definides a la solució 4.
    """

    def setUp(self):
        """
        Inicialitza les variables abans de cada prova.
        Aquesta matriu s'utilitza per a les proves de transformació i altres operacions.
        """
        self.matriu = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    def test1(self):
        """
        Prova per cercar un element en una matriu.
        Comprova si un element existeix a la matriu i la seva posició.
        """
        resultat = cercar_el(self.matriu, 5)
        self.assertEqual(resultat, (True, None))  # El 5 existeix, però no es mostra la posició per defecte

        resultat = cercar_el(self.matriu, 5, mostrar_posicio=True)
        self.assertEqual(resultat, (True, (1, 1)))  # El 5 està a la posició (1, 1)

        resultat = cercar_el(self.matriu, 10)
        self.assertEqual(resultat, (False, None))  # El 10 no existeix a la matriu

    def test2(self):
        """
        Prova per sumar els elements d'una fila de la matriu.
        Comprova que la suma de la fila 1 és correcta.
        """
        resultat = sumar_fila(self.matriu, 1)
        self.assertEqual(resultat, 15)  # La fila 1 és [4, 5, 6], la suma és 4 + 5 + 6 = 15

        resultat = sumar_fila(self.matriu, 5)
        self.assertIsNone(resultat)  # La fila 5 no existeix, ha de retornar None

    def test3(self):
        """
        Prova per sumar tots els elements de la matriu.
        Comprova que la suma total de la matriu és correcta.
        """
        resultat = sumar_matriu(self.matriu)
        self.assertEqual(resultat, 45)  # La suma total és 1+2+3+4+5+6+7+8+9 = 45

    def test4(self):
        """
        Prova per transformar els elements de la matriu.
        Comprova si les operacions +, -, *, / funcionen correctament.
        """
        # Sumar 10 a tots els elements
        resultat = transformar(self.matriu, 10, "+")
        self.assertEqual(self.matriu, [[11, 12, 13], [14, 15, 16], [17, 18, 19]])

        # Restar 10 a tots els elements
        resultat = transformar(self.matriu, 10, "-")
        self.assertEqual(self.matriu, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])

        # Multiplicar tots els elements per 10
        resultat = transformar(self.matriu, 10, "*")
        self.assertEqual(self.matriu, [[10, 20, 30], [40, 50, 60], [70, 80, 90]])

        # Dividir tots els elements per 10
        resultat = transformar(self.matriu, 10, "/")
        self.assertEqual(self.matriu, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])


if __name__ == "__main__":
    unittest.main()