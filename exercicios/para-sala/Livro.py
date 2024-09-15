class Livro:
    """Classe biblioteca.
    
    Recebe no construtor os parametros nome e autor como o exemplo:
    
    livro = Livro("nome livro","autor livro")
    """
    def __init__(self, nome, autor):        
        self.nome = nome
        """propriedade nome do livro"""
        self.autor = autor
        """propriedade autor do livro"""
        self.esta_emprestado = False
        """propriedade esta_emprestado. Valor padrão é falso"""