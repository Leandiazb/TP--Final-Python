import unittest
from .services import calcular_emisiones_carbono

#agregar comentario de metodos y docstring 
class TestCalculoEmisiones(unittest.TestCase):

    """
    Conjunto de pruebas unitarias para auditar el funcionamiento 
    del algoritmo de cálculo de emisiones de carbono.

    """
    def test_calculo_nominal_default(self) -> None: #con el None nos aseguramos que no devuelva ningun valor.
        """
        Verifica el cálculo correcto de emisiones utilizando el factor por defecto (0.4).
        """
    
        resultado = calcular_emisiones_carbono(100) 
        self.assertEqual(resultado, 40.0) #esto es el resultado esperado

    def test_calculo_factorpersonalizado(self) -> None:
        """
        Verifica el cálculo de emisiones cuando se especifica un factor de emisión personalizado.
        """

        resultado = calcular_emisiones_carbono(250, factor_emision=0.5) 
        self.assertEqual(resultado, 125)

    def test_consumo_cero(self) -> None:
        """
        Verifica que un consumo de 0 kWh devuelva exactamente 0.0 emisiones.
        """

        resultado = calcular_emisiones_carbono(0)
        self.assertEqual(resultado, 0)

    def test_consumo_negativo(self) -> None:
        """
        Verifica que se eleve la excepción ValueError al ingresar un consumo negativo.
        """

        with self.assertRaises(ValueError):
            calcular_emisiones_carbono(-50)