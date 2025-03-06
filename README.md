## Lista de Compra Simples em Python

## 📋 Como Usar

1. O programa exibe automaticamente a lista de compras existente.
2. Você pode escolher entre as seguintes opções:
   - **1️⃣ Adicionar um novo produto**: Insira nome, unidade de medida, quantidade e descrição.
   - **2️⃣ Pesquisar um produto**: Busque um item pelo nome ou parte do nome.
   - **3️⃣ Remover um produto**: Digite o ID do produto para removê-lo.
   - **4️⃣ Sair**: Encerra o programa.

---

## 📂 Estrutura do Código

O código está organizado em funções para melhor legibilidade e manutenção:

- `gerar_id()`: Gera um ID único de 8 caracteres.
- `exibir_cabecalho()`: Exibe o cabeçalho estilizado do programa.
- `exibir_lista(lista)`: Formata e exibe a lista de compras.
- `adicionar_produto(lista)`: Adiciona um novo produto com entrada validada.
- `remover_produto(lista)`: Remove um item da lista pelo ID.
- `pesquisar_produto(lista)`: Busca produtos pelo nome e exibe os resultados.
- `menu()`: Controla o fluxo principal do programa.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **Biblioteca `uuid`** (para geração de IDs únicos)
