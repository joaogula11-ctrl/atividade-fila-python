import unittest
from queue import Queue  # Importa a classe do seu arquivo queue.py

class TestarFila(unittest.TestCase):

    def testar_fluxo_normal_enfileirar_desenfileirar(self):
        """1. Teste de fluxo normal: enfileirar e desenfileirar (FIFO)."""
        fila = Queue()
        fila.enqueue("A")
        fila.enqueue("B")
        self.assertEqual(fila.dequeue(), "A")
        self.assertEqual(fila.dequeue(), "B")
        self.assertTrue(fila.is_empty())

    def testar_visualizar_e_tamanho(self):
        """2. Teste dos métodos peek e size para garantir que não alteram a fila."""
        fila = Queue()
        fila.enqueue(10)
        fila.enqueue(20)
        self.assertEqual(fila.size(), 2)
        self.assertEqual(fila.peek(), 10)
        self.assertEqual(fila.size(), 2)  # O tamanho deve continuar 2 após o peek

    def testar_excecoes_fila_vazia(self):
        """3. Teste de tratamento de erro: desenfileirar ou espiar fila vazia."""
        fila = Queue()
        with self.assertRaises(IndexError):
            fila.dequeue()
        with self.assertRaises(IndexError):
            fila.peek()

    def testar_excecao_fila_cheia(self):
        """4. Teste de tratamento de erro: enfileirar além do limite (Overflow)."""
        fila = Queue(max_size=2)
        fila.enqueue("X")
        fila.enqueue("Y")
        self.assertTrue(fila.is_full())
        with self.assertRaises(OverflowError):
            fila.enqueue("Z")

    def testar_limpar_fila(self):
        """5. Teste da função clear para esvaziar a fila inteira."""
        fila = Queue()
        fila.enqueue(1)
        fila.enqueue(2)
        fila.enqueue(3)
        fila.clear()
        self.assertTrue(fila.is_empty())
        self.assertEqual(fila.size(), 0)

if __name__ == '__main__':
    unittest.main()