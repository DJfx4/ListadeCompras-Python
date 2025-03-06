import uuid


def gerar_id():
    return str(uuid.uuid4())[:8]  # Gera um ID único de 8 caracteres


#Exibe uma introdução para o cliente

def exibir_cabecalho():
    print("\n" + "-" * 49)
    print(" |🛒 BEM-VINDO À LISTA DE COMPRAS SIMPLES 🛒|")
    print("-" * 49 + "\n")


#Mostra a lista atual do cliente

def exibir_lista(lista):
    if not lista:
        print("📌 Sua lista de compras está vazia!\n")
    else:
        print("📝 Lista de Compras:")
        print("ID        | Nome        | Quantidade | Unidade    | Descrição")
        print("-" * 60)
        for produto in lista:
            print(
                f"{produto['id']} | {produto['nome']:<10} | {produto['quantidade']:<9} | {produto['unidade']:<10} | {produto['descricao']}")
        print("-" * 60 + "\n")

#Adiciona um produto na lista compras do cliente

def adicionar_produto(lista):
    print("➕ Adicionar Produto")
    nome = input("🔹 Nome do produto: ").strip()
    if not nome:
        print("⚠️ Nome não pode ser vazio ⚠️\n")
        return

#Define a unidade de medida do produto

    unidades = ["Quilograma", "Grama", "Litro", "Mililitro", "Unidade", "Metro", "Centímetro"]
    print("\n📏 Escolha a unidade de medida:")
    for i, unidade in enumerate(unidades, 1):
        print(f"{i}. {unidade}")

    try:
        escolha = int(input("🔹 Opção: "))
        unidade = unidades[escolha - 1]
    except (ValueError, IndexError):
        print("⚠️ Opção inválida ⚠️ \n")
        return

    try:
        quantidade = float(input("🔹 Quantidade: "))
    except ValueError:
        print("⚠️ Quantidade inválida ⚠️ \n")
        return

    descricao = input("🔹 Descrição do produto: ").strip()
    produto = {"id": gerar_id(), "nome": nome, "quantidade": quantidade, "unidade": unidade, "descricao": descricao}
    lista.append(produto)
    print("✅ Produto adicionado com sucesso!\n")

#Remove um produto da lista do cliente
def remover_produto(lista):
    print("🗑️ Remover Produto")
    id_produto = input("🔹 Digite o ID do produto a ser removido: ").strip()
    for produto in lista:
        if produto['id'] == id_produto:
            lista.remove(produto)
            print("✅ Produto removido com sucesso!\n")
            return
    print("⚠️Produto não encontrado ⚠️ \n")

#Pesquisa por produtos que estão na lista do cliente
def pesquisar_produto(lista):
    print("🔍 Pesquisar Produto")
    termo = input("🔹 Digite o nome ou parte do nome do produto: ").strip().lower()
    resultados = [p for p in lista if termo in p['nome'].lower()]

    if resultados:
        print("\n🔎 Produtos encontrados:")
        for produto in resultados:
            print(
                f"{produto['id']} | {produto['nome']:<10} | {produto['quantidade']:<9} | {produto['unidade']:<10} | {produto['descricao']}")
        print(f"📊 Total encontrados: {len(resultados)}\n")
    else:
        print("⚠️ Nenhum produto encontrado ⚠️ \n")

#Exibe os comandos para que o cliente possa iniciar sua lista.
def menu():
    lista_compras = []
    while True:
        exibir_cabecalho()
        exibir_lista(lista_compras)
        print("[1]  Adicionar Produto")
        print("[2]  Pesquisar Produto")
        print("[3]  Remover Produto")
        print("[4]  Sair")
        opcao = input("🔹 Escolha uma opção: ")

        if opcao == "1":
            adicionar_produto(lista_compras)
        elif opcao == "2":
            pesquisar_produto(lista_compras)
        elif opcao == "3":
            remover_produto(lista_compras)
        elif opcao == "4":
            print("👋 Encerrando o programa...")
            break
        else:
            print("⚠️ Opção inválida ⚠️\n")


if __name__ == "__main__":
    menu()
