import unittest

from llista import ordenarLista


llista = [7, 3, 13, 6, 8, 5, 1, 2, 4, 15, 9, 10, 12, 14, 11]

resultats = [1,2,3,4]

buida = []


class TestList(unittest.TestCase):

    def test_1 (self):
        self.assertEqual(ordenarLista(llista),(resultats))
    
    def test_2 (self):

        self.assertAlmostEqual(ordenarLista(llista),resultats)

    def test_3 (self):

        self.assertGreater(ordenarLista(llista),resultats)
    
    def test_4 (self):
        self.assertLessEqual(ordenarLista(llista),resultats)
    
    def test_5 (self):
        self.assertEqual(ordenarLista(llista),buida)
    
    """ def test_6 (self):
        self.assertNotEqual(ordenarLista(llista),buida)"""
    


        




if __name__ == '__main__': # evitem a la linia de comandes haver de posar " python -m unittest test.py --> python test.py i obtenim el mateix resultat"
    unittest.main()