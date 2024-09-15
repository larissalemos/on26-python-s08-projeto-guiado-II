# Exercício de Casa 🏠 

## Criar método exibir_livros
Critérios de aceitação:
- O método deve ter ao menos 1 (um) teste associado
- O método deve não tem parâmetro além do self (contém apenas o self obrigatório)
- O método deve exibir todos os livros que foram adicionados
(dica retorne a lista e valide se contém todos os livros adicionados)

## Criar método emprestar_livro
Critérios de aceitação:
- O método deve ter ao menos 1 (um) teste associado
- O método deve receber como parâmetro o nome do livro a ser emprestado
- O método deve marcar o valor de esta_emprestado como `True`


*******

## Opcional

### Criar método remover_livro 
Critérios de aceitação:
- O método deve ter ao menos 1 (um) teste associado
- O método deve receber como parâmetro o nome do livro e remover da propriedade Books
- O método deve remover apenas 1 (um) livro por vez
- Caso o livro não seja encontrado o método não deve dar erro ou exceções
- Apenas livros não emprestados podem ser removidos (opcional)

### Criar método buscar_livro
Critérios de aceitação:
- O método deve ter ao menos 1 (um) teste associado
- O método deve receber como parâmetro o nome do livro a ser buscado e retornar o nome do livro, autor e informação se livro está disponível ou emprestado
- Caso o livro não seja encontrado o método deve retornar a mensagem "Livro não encontrado"

## Criar método devolver_livro 
Critérios de aceitação:
- O método deve ter ao menos 1 (um) teste associado
- O método deve receber como parâmetro o nome do livro a ser devolvido e mudar o status do livro para não emprestado na propriedade Livros
- Caso o livro não seja encontrado o método deve apenas exibir a mensagem "Livro não encontrado"

---

Terminou o exercício? Dá uma olhada nessa checklist e confere se tá tudo certinho, combinado?!

- [ ] Fiz o fork do repositório.
- [ ] Clonei o fork na minha máquina (`git clone url-do-meu-fork`).
- [ ] Resolvi o exercício.
- [ ] Adicionei as mudanças. (`git add .` para adicionar todos os arquivos, ou `git add nome_do_arquivo` para adicionar um arquivo específico)
- [ ] Commitei a cada mudança significativa ou na finalização do exercício (`git commit -m "Mensagem do commit"`)
- [ ] Pushei os commits na minha branch (`git push origin nome-da-branch`)
- [ ] Criei um Pull Request seguindo as orientaçoes que estao nesse [documento](https://github.com/reprograma/on26-python-s08-projeto-guiado-II/blob/main/exercicios/para-casa/instrucoes-pull-request.md).
