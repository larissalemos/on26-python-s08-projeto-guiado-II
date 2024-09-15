from Biblioteca import Biblioteca 
from Livro import Livro 

# Exemplo de como utilizar as classes criadas durante a aula

# Atribuindo valores às variáveis
nome_livro = "O mito da beleza"
autor_livro = "Naomi Wolf"

# Instanciando o objeto livro_objeto da classe Livro 
# passando as variáveis nome_livro e autor_livro
livro_objeto = Livro(nome = nome_livro,autor = autor_livro)
print(f"Criamos o objeto livro_objeto da classe Livro com os valores nome = {livro_objeto.nome} e autor = {livro_objeto.autor}\n")

# Instanciando o objeto biblioteca_objeto da classe Biblioteca 
print("Criamos o objeto biblioteca_objeto da classe Biblioteca\n")
biblioteca_objeto = Biblioteca()

# Exibindo o valor da propriedade livros do objeto biblioteca_objeto
print("Exibindo valores da propriedade livros do objeto biblioteca_objeto:")
print(biblioteca_objeto.livros)

# Cadastrando o livro criado anteriormente no objeto livro_objeto
# passamos o objeto livro_objeto para o método adicionar_livro do objeto biblioteca_objeto
# que por sua vez adiciona o objeto livro_objeto na lista de livros
print("Adicionamos o livro_objeto criado à biblioteca_objeto através do método adicionar_livro\n")
biblioteca_objeto.adicionar_livro(livro_objeto)

# Para cada item dentro da lista de livros do objeto biblioteca_objeto
# Exibimos os valores de nome e autor do livro cadastrado
print("Exibindo o valor da propriedade livros de biblioteca_objeto")
for livro in biblioteca_objeto.livros:
    print(livro.nome)
    print(livro.autor)