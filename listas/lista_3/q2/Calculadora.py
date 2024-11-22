class Calculadora:
    def add(self,x : float,y : float) -> float:
        """Soma dois números
        Args:
            x (float): O primeiro número
            y (float): O segundo número
        Returns:
            float: Soma dos dois números.
        """
        return (x+y)
    def sub(self,x : float,y : float) -> float:
        """Subtrai dois números
        Args:
            x (float): O primeiro número
            y (float): O segundo número
        Returns:
            float: Subtração dos dois números.
        """
        return (x-y),
    def mult(self,x:float ,y:float) -> float:
        """Multiplica dois números
        Args:
            x (float): O primeiro número
            y (float): O segundo número
        Returns:
            float: Multiplicação dos dois números.
        """
        return x*y
    def div(self,x : float,y : float) -> float:
        """Divide dois números
        Args:
            x (float): O primeiro número
            y (float): O segundo número
        Returns:
            float: Divisão dos dois números.
        """
        return x / y
    def potencia(self,x : int) -> int:
        """Quadrado de um número
        Args:
            x (float): O primeiro número
        Returns:
            float: O quadrado do número.
        """
        return x*x