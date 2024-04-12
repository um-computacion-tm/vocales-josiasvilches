import unittest

def contar_vocales(mi_string):
    vocales = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U', 'á', 'é', 'í', 'ó', 'ú', 'Á', 'É', 'Í', 'Ó', 'Ú')
    resultado = {}
    for letra in mi_string:
        # if letra in 'aeiou':
        if letra in vocales:
            if letra not in resultado:
                resultado[letra] = 0
            resultado[letra] += 1
    return resultado


class TestContarVocales(unittest.TestCase):
    def test_nada(self):
        resultado = contar_vocales('ConSTRUcCIón')
        self.assertEqual(resultado, {'I': 1, 'o': 1, 'U': 1, 'ó': 1})

    def test_contar_a(self):
        resultado = contar_vocales('Cassie')
        self.assertEqual(resultado, {'a': 1, 'e': 1, 'i': 1})

    def test_contar_aa(self):
        resultado = contar_vocales('casa')
        self.assertEqual(resultado, {'a': 2})

    def test_contar_bese(self):
        resultado = contar_vocales('besé')
        self.assertEqual(resultado, {'e': 1, 'é': 1})

    def test_contar_besa(self):
        resultado = contar_vocales('besa')
        self.assertEqual(resultado, {'a': 1, 'e': 1})

    def test_contar_casanova(self):
        resultado = contar_vocales('casanova')
        self.assertEqual(resultado, {'a': 3, 'o': 1})

    def test_contar_mUrciElago(self):
        resultado = contar_vocales('mUrciElago')
        self.assertEqual(resultado, {'a': 1, 'E': 1, 'i': 1, 'o': 1, 'U': 1})


unittest.main()
