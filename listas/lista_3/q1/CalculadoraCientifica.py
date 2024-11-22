class CalculadoraCientifica:
    def quadrado(self,x : int) -> int:
        """Quadrado de um número
        Args:
            x (int): O primeiro número
        Returns:
            int: O quadrado do número.
        """
        return x*x
    def potencia(self,x : int, y : int) -> int:
        """Quadrado de um número
        Args:
            x (int): O primeiro número
            y (int): A potencia que deseja elevar
        Returns:
            int: O número elevando na potencia y.
        """
        resultado = 1
        for i in range(int(y)):
            resultado = resultado * x
        return resultado