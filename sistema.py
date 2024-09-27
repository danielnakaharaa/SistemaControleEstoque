produto = []  
def Menu():
    """
    Função que exibe o menu principal e captura as escolhas do usuário
    para direcionar as funcionalidades do sistema de cadastro de produtos.
    """
    Listar()
    while True:
        print("Bem vindo ao sistema de cadastro de produto")
        print("Escolha uma opção:")
        print("1 - Adicionar produto")
        print("2 - Remover produto")
        print("3 - Atualizar produto")
        print("4 - Listar produtos")
        print("5 - Buscar produto")
        print("6 - Ordenar produtos por quantidade")
        print("7 - Consultar produtos esgotados")
        print("8 - Filtrar produtos com baixa quantidade")
        print("9 - Calcular valor total do estoque")
        print("10 - Relatório geral do estoque")
        print("11 - Sair")
        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            AdicionarProduto()
        elif opcao == "2":
            Remover(produto)
        elif opcao == "3":
            AtualizarProduto()
        elif opcao == "4":
            Listar()
        elif opcao == "5":
            BuscarProduto()
        elif opcao == "6":
            OrdenarPorQuantidade()
        elif opcao == "7":
            ConsultarProdutosEsgotados()
        elif opcao == "8":
            FiltrarProdutosBaixaQuantidade()
        elif opcao == "9":
            CalcularTotalEstoque()
        elif opcao == "10":
            RelatorioGeralEstoque()  
        elif opcao == "11":
            break
        else:
            print("Opção inválida")

def Listar():
  
    estoque_inicial = (
        "Notebook Dell;201;15;3200.00;4500.00#"
        "Notebook Lenovo;202;10;2800.00;4200.00#"
        "Mouse Logitech;203;50;70.00;150.00#"
        "Mouse Razer;204;40;120.00;250.00#"
        "Monitor Samsung;205;0;800.00;1200.00#"
        "Monitor LG;206;8;750.00;1150.00#"
        "Teclado Mecânico Corsair;207;30;180.00;300.00#"
        "Teclado Mecânico Razer;208;25;200.00;350.00#"
        "Impressora HP;209;5;400.00;650.00#"
        "Impressora Epson;210;3;450.00;700.00#"
        "Monitor Dell;211;12;850.00;1250.00#"
        "Monitor AOC;212;7;700.00;1100.00"
    )

    produtos = estoque_inicial.split("#")
    for produto_info in produtos:
        nome, codigo, quantidade, preco_custo, preco_venda = produto_info.split(";")
        produto.append({
            "nome": nome,
            "codigo": codigo,
            "quantidade": int(quantidade),
            "preco_custo": float(preco_custo),
            "preco_venda": float(preco_venda)
        })
    # Exibir os produtos após o carregamento
    for item in produto:
        print(f"Produto: {item['nome']}, Código: {item['codigo']}, "
              f"Quantidade: {item['quantidade']}, Preço de Custo: R${item['preco_custo']:.2f}, "
              f"Preço de Venda: R${item['preco_venda']:.2f}")
        lucro(item)
def AdicionarProduto():
    """
    Função para adicionar produtos à lista global de produtos.
    Captura nome, código, quantidade, custo e preço de venda.
    """
    while True:
        AddNomeProduto = input("Adicionar Produto: ")
        AddCodigo = input("Adicionar Código: ")
        AddQtd = input("Adicionar Quantidade: ")
        AddCusto = input("Adicionar Custo: ")
        AddVenda = input("Adicionar Preço de Venda: ")

        produto.append({
            "nome": AddNomeProduto,
            "codigo": AddCodigo,
            "quantidade": int(AddQtd),
            "preco_custo": float(AddCusto),
            "preco_venda": float(AddVenda)
        })
        continuar = input("Deseja adicionar mais produtos? nao/sim ").strip().lower()
        if continuar == "nao":
            break

def Remover(lista):
    """
    Função para remover um produto da lista pelo código.
    """
    codigo_remover = input("Digite o código do produto que deseja remover: ")
    nova_lista = []
    for item in lista:
        if item["codigo"] != codigo_remover:
            nova_lista.append(item)

    if len(nova_lista) != len(lista):
        lista[:] = nova_lista
        print(f"Produto com código {codigo_remover} removido com sucesso.")
    else:
        print(f"Produto com código {codigo_remover} não encontrado.")

def AtualizarProduto():
    """
    Função para atualizar a quantidade e o preço de venda de um produto
    já existente no estoque. A busca é feita pelo código.
    """
    codigo = input("Digite o código do produto a ser atualizado: ")
    for item in produto:
        if item['codigo'] == codigo:
            item['quantidade'] = int(input("Nova quantidade: "))
            item['preco_venda'] = float(input("Novo preço de venda: "))
            print(f"Produto {item['nome']} atualizado com sucesso.")
            return
    print("Produto não encontrado.")

def BuscarProduto():
    """
    Função para buscar produtos pelo nome ou código.
    Exibe os produtos encontrados ou uma mensagem de erro.
    """
    if not produto:  # Verifica se a lista está vazia
        print("Não há produtos cadastrados.")
        return

    termo = input("Digite o nome ou código do produto: ").strip().lower()

    encontrados = [
        item for item in produto
        if termo in item['nome'].lower() or termo == str(item['codigo'])
    ]

    if encontrados:
        for item in encontrados:
            print(f"Encontrado: Nome: {item['nome']}, Código: {item['codigo']}, "
                  f"Quantidade: {item['quantidade']}, Preço de Venda: R${item['preco_venda']:.2f}")
    else:
        print("Produto não encontrado.")




def OrdenarPorQuantidade():
    """
    Função para ordenar os produtos por quantidade em ordem crescente ou decrescente.
    """
    ordem = input("Deseja ordenar por quantidade (asc/desc)? ").lower()
    produtos_ordenados = produto.copy()

    def ordenacao(produto):
        return int(produto["quantidade"])

    produtos_ordenados.sort(key=ordenacao, reverse=(ordem == "desc"))

    for item in produtos_ordenados:
        print(f"Nome: {item['nome']}, Quantidade: {item['quantidade']}")

def ConsultarProdutosEsgotados():
    """
    Função que exibe todos os produtos com quantidade igual a zero (esgotados).
    """
    esgotados = [item for item in produto if item['quantidade'] == 0]
    if esgotados:
        print("Produtos esgotados:")
        for item in esgotados:
            print(f"Nome: {item['nome']}, Código: {item['codigo']}")
    else:
        print("Nenhum produto esgotado.")

def FiltrarProdutosBaixaQuantidade():
    """
    Função para filtrar produtos com quantidade abaixo de um limite.
    O limite padrão é 5 se o usuário não informar outro valor.
    """
    limite = input("Digite a quantidade mínima para filtrar (pressione Enter para usar o valor padrão de 5): ")
    limite = int(limite) if limite else 5

    baixa_qtd = [item for item in produto if item['quantidade'] < limite]

    if baixa_qtd:
        print("Produtos com baixa quantidade:")
        for item in baixa_qtd:
            print(f"Nome: {item['nome']}, Quantidade: {item['quantidade']}")
    else:
        print("Nenhum produto com quantidade abaixo do limite.")

def CalcularTotalEstoque():
    """
    Função para calcular o valor total do estoque. O cálculo é feito
    multiplicando a quantidade pela preço de venda de cada produto.
    """
    valor_total = sum(item['quantidade'] * item['preco_venda'] for item in produto)
    print(f"Valor total do estoque: R${valor_total:.2f}")




def lucro(produto):
    """
    Função que calcula o lucro de um produto.
    """
    precoCusto = float(produto["preco_custo"])
    precoVenda = float(produto["preco_venda"])
    lucro_por_produto = precoVenda - precoCusto
    print(f"Produto: {produto['nome']}, Lucro: R${lucro_por_produto:.2f}")

def RelatorioGeralEstoque():
    """
    Função para exibir um relatório geral do estoque com a descrição,
    código, quantidade, custo, preço de venda e valor total por item.
    O relatório é formatado para melhor visualização.
    """
    print("Relatório Geral do Estoque")
    print(f"{'Descrição'.ljust(25)}{'Código'.rjust(10)}{'Quantidade'.rjust(15)}{'Custo'.rjust(15)}{'Preço Venda'.rjust(15)}{'Valor Total'.rjust(15)}")

    custo_total = 0
    faturamento_total = 0

    for item in produto:
        valor_total_item = item['quantidade'] * item['preco_venda']
        custo_total += item['quantidade'] * item['preco_custo']
        faturamento_total += valor_total_item
        print(f"{item['nome'].ljust(25)}{item['codigo'].rjust(10)}{str(item['quantidade']).rjust(15)}"
              f"{str(item['preco_custo']).rjust(15)}{str(item['preco_venda']).rjust(15)}{str(valor_total_item).rjust(15)}")

    print("\n")
    print(f"{'Custo total:'.ljust(65)}R${custo_total:.2f}")
    print(f"{'Faturamento total:'.ljust(65)}R${faturamento_total:.2f}")

if __name__ == "__main__":
    Menu()
