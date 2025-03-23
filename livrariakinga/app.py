# Definindo as constantes para o limite de quantidade de livros por gênero
GENERO_FICCAO = 10
GENERO_ROMANCE = 12
GENERO_BIOGRAFIA = 8
GENERO_MISTERIO = 6

# Lista de livros no estoque
estoque = []

# Função para calcular o total de livros no estoque
def calcular_total_estoque():
    return sum(livro['quantidade'] for livro in estoque)

# Função para calcular a porcentagem de livros de um gênero no estoque
def calcular_porcentagem_genero(genero):
    total_estoque = calcular_total_estoque()
    quantidade_genero = sum(livro['quantidade'] for livro in estoque if livro['genero'] == genero)
    
    if total_estoque == 0:  # Evitar divisão por zero
        return 0
    
    porcentagem = (quantidade_genero / total_estoque) * 100
    return porcentagem

# Função para adicionar livros ao estoque com verificação do limite
def adicionar_livro(titulo, genero, quantidade):
    # Verificando a quantidade permitida por gênero
    if genero == 'Ficção':
        if quantidade > GENERO_FICCAO:
            print(f"A quantidade máxima para {genero} é {GENERO_FICCAO}. A quantidade será ajustada.")
            quantidade = GENERO_FICCAO
    elif genero == 'Romance':
        if quantidade > GENERO_ROMANCE:
            print(f"A quantidade máxima para {genero} é {GENERO_ROMANCE}. A quantidade será ajustada.")
            quantidade = GENERO_ROMANCE
    elif genero == 'Biografia':
        if quantidade > GENERO_BIOGRAFIA:
            print(f"A quantidade máxima para {genero} é {GENERO_BIOGRAFIA}. A quantidade será ajustada.")
            quantidade = GENERO_BIOGRAFIA
    elif genero == 'Mistério':
        if quantidade > GENERO_MISTERIO:
            print(f"A quantidade máxima para {genero} é {GENERO_MISTERIO}. A quantidade será ajustada.")
            quantidade = GENERO_MISTERIO

    # Adicionando o livro ao estoque
    estoque.append({'titulo': titulo, 'genero': genero, 'quantidade': quantidade})

# Função para mostrar o estoque
def mostrar_estoque():
    total_estoque = calcular_total_estoque()
    print(f"\nEstoque total: {total_estoque} livros")
    for livro in estoque:
        print(f"Título: {livro['titulo']}, Gênero: {livro['genero']}, Quantidade: {livro['quantidade']}")
    print("\n")

# Função principal
def main():
    while True:
        # Coletando informações do usuário
        titulo = input("Digite o título do livro (ou 'sair' para encerrar): ")
        if titulo.lower() == 'sair':
            break  # Encerra o loop

        genero = input("Digite o gênero (Ficção, Romance, Biografia, Mistério): ").capitalize()
        while genero not in ['Ficção', 'Romance', 'Biografia', 'Mistério']:
            print("Gênero inválido! Por favor, escolha entre: Ficção, Romance, Biografia, Mistério.")
            genero = input("Digite o gênero (Ficção, Romance, Biografia, Mistério): ").capitalize()

        try:
            quantidade = int(input("Digite a quantidade de exemplares: "))
        except ValueError:
            print("Quantidade inválida! Por favor, insira um número.")
            continue

        # Adicionando o livro ao estoque
        adicionar_livro(titulo, genero, quantidade)

        # Mostrando o estoque após a adição
        mostrar_estoque()

        # Perguntar se o usuário quer continuar
        continuar = input("Deseja adicionar outro livro? (sim/não): ").lower()
        if continuar != 'sim':
            break

    # Calculando a porcentagem de livros de cada gênero no estoque
    print(f"\nPorcentagem de Ficção: {calcular_porcentagem_genero('Ficção'):.2f}%")
    print(f"Porcentagem de Romance: {calcular_porcentagem_genero('Romance'):.2f}%")
    print(f"Porcentagem de Biografia: {calcular_porcentagem_genero('Biografia'):.2f}%")
    print(f"Porcentagem de Mistério: {calcular_porcentagem_genero('Mistério'):.2f}%")

if __name__ == "__main__":
    main()
