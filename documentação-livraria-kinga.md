# Gerenciamento de Estoque de Livros

## 📖 Sobre o Projeto
Este projeto é um sistema simples de gerenciamento de estoque de livros que permite adicionar títulos, verificar a quantidade disponível e calcular a porcentagem de livros por gênero.

## 🚀 Funcionalidades
- Adicionar livros ao estoque com verificação de limite por gênero.
- Exibir o estoque atualizado.
- Calcular a porcentagem de livros de cada gênero no estoque.
- Evitar adição de livros acima do limite permitido por gênero.

## 📌 Gêneros e Limites de Quantidade
Cada gênero tem um limite máximo de livros que pode ser adicionado ao estoque:

| Gênero     | Limite Máximo |
|------------|--------------|
| Ficção     | 10           |
| Romance    | 12           |
| Biografia  | 8            |
| Mistério   | 6            |

## 🛠 Tecnologias Utilizadas
- **Python** (linguagem principal)

## 📂 Estrutura do Código
- **Definição de constantes** para os limites de cada gênero.
- **Lista `estoque`** para armazenar os livros cadastrados.
- **Funções principais:**
  - `calcular_total_estoque()`: Calcula o total de livros disponíveis.
  - `calcular_porcentagem_genero(genero)`: Retorna a porcentagem de livros de um determinado gênero no estoque.
  - `adicionar_livro(titulo, genero, quantidade)`: Adiciona livros ao estoque considerando os limites de cada gênero.
  - `mostrar_estoque()`: Exibe todos os livros disponíveis.
  - `main()`: Função principal que gerencia o fluxo de interação com o usuário.

## 🎯 Como Executar o Programa
1. **Clone o repositório**
   ```bash
   git clone https://github.com/seu-usuario/estoque-livros.git
   cd estoque-livros
   ```

2. **Execute o programa**
   ```bash
   python estoque_livros.py
   ```

3. **Interaja com o sistema**
   - Insira o título do livro.
   - Escolha um dos gêneros disponíveis.
   - Defina a quantidade de exemplares.
   - O sistema informará se a quantidade excede o limite e ajustará automaticamente.
   - O estoque será exibido após cada adição.

## 📌 Exemplo de Uso
```
Digite o título do livro (ou 'sair' para encerrar): O Pequeno Príncipe
Digite o gênero (Ficção, Romance, Biografia, Mistério): Ficção
Digite a quantidade de exemplares: 15
A quantidade máxima para Ficção é 10. A quantidade será ajustada.

Estoque total: 10 livr
Título: O Pequeno Príncipe, Gênero: Ficção, Quantidade: 10

Deseja adicionar outro livro? (sim/não): não

Porcentagem de Ficção: 100.00%
Porcentagem de Romance: 0.00%
Porcentagem de Biografia: 0.00%
Porcentagem de Mistério: 0.00%
```

## 📝 Contribuição
Se quiser contribuir com melhorias, siga os passos:
1. **Fork o repositório**
2. **Crie uma branch para sua modificação** (`git checkout -b minha-modificacao`)
3. **Commit suas alterações** (`git commit -m 'Minha melhoria'`)
4. **Faça um push para a branch** (`git push origin minha-modificacao`)
5. **Abra um Pull Request**

---