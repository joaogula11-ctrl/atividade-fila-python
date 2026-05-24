"""
Módulo contendo a implementação de uma Fila (Queue) baseada no conceito FIFO (First-In, First-Out).
"""

class Queue:
    """
    Uma implementação de Fila (FIFO) usando listas padrão do Python.
    """

    def __init__(self, max_size=None):
        """
        Cria uma fila vazia.
        """
        self._elementos = []
        self.max_size = max_size

    def enqueue(self, elemento):
        """
        Adiciona um elemento no final da fila.
        """
        if self.is_full():
            raise OverflowError(f"Falha ao enfileirar: A fila atingiu seu limite máximo de {self.max_size} elementos.")
        self._elementos.append(elemento)

    def dequeue(self):
        """
        Remove e retorna o primeiro elemento da fila.
        """
        if self.is_empty():
            raise IndexError("Falha ao desenfileirar: A fila está vazia.")
        return self._elementos.pop(0)

    def peek(self):
        """
        Retorna o primeiro elemento da fila sem removê-lo.
        """
        if self.is_empty():
            raise IndexError("Falha ao visualizar: A fila está vazia e não contém elementos.")
        return self._elementos[0]

    def is_empty(self):
        """
        Verifica se a fila está vazia.
        """
        return len(self._elementos) == 0

    def is_full(self):
        """
        Verifica se a fila está cheia.
        """
        if self.max_size is None:
            return False
        return len(self._elementos) >= self.max_size

    def size(self):
        """
        Retorna o número atual de elementos na fila.
        """
        return len(self._elementos)

    def clear(self):
        """
        Remove todos os elementos, esvaziando a fila completamente.
        """
        self._elementos.clear()