import unittest
from exibirMensagem import hello


class TestHelloFunction(unittest.TestCase):
    
 
    def test_hello(self):
        resultado = hello()
        
       
        self.assertEqual(resultado, ["Hello, DevOps!", "200"])


if __name__ == "__main__":
    unittest.main()
