# API de Biblioteca Virtual

Esta API funciona como uma biblioteca virtual, permitindo realizar operações para consultar, editar, criar e excluir livros. Abaixo, você encontrará uma explicação detalhada de como o código da API funciona.

## 1. Estrutura inicial

O código usa o **Flask**, um framework em Python, para criar a API. Veja os principais componentes:

```python
from flask import Flask, jsonify, request
```

- **Flask**: Framework utilizado para construir a API.
- **jsonify**: Converte as respostas da API para o formato JSON, facilitando a comunicação com outros sistemas.
- **request**: Permite acessar os dados enviados pelo usuário (como as informações de um novo livro ou uma alteração em um livro existente).

Em seguida, criamos a instância do Flask para configurar nossa "biblioteca" (API):

```python
app = Flask(__name__)
```

## 2. Lista de livros

Abaixo, temos uma lista de livros como exemplo. Cada livro é um dicionário contendo um `id`, `título` e `autor`.

```python
livros = [
    {'id': 1, 'título': 'O Senhor dos Anéis - A Sociedade do Anel', 'autor': 'J.R.R Tolkien'},
    {'id': 2, 'título': 'Harry Potter e a Pedra Filosofal', 'autor': 'J.K Rowling'},
    {'id': 3, 'título': 'Hábitos Atômicos', 'autor': 'James Clear'}
]
```

## 3. Consultar todos os livros (GET)

A operação **GET** permite que o usuário consulte todos os livros disponíveis na "biblioteca":

```python
@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)
```

- **GET**: Ao acessar o endpoint `/livros`, a API retorna todos os livros no formato JSON.

## 4. Consultar livro por ID (GET)

A operação **GET** também pode ser usada para consultar um livro específico pelo seu `id`:

```python
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livros_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
```

- O `int:id` permite que a API capture o `id` do livro e busque o livro correspondente.

## 5. Editar livro (PUT)

A operação **PUT** permite editar os detalhes de um livro específico:

```python
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
```

- **PUT**: O usuário envia os dados modificados do livro (como título ou autor) no corpo da requisição, e a API atualiza o livro correspondente.

## 6. Criar um novo livro (POST)

A operação **POST** é usada para adicionar um novo livro à biblioteca:

```python
@app.route('/livros', methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)
```

- **POST**: O usuário envia os dados de um novo livro (com título, autor e id) e a API adiciona esse livro à lista de livros.

## 7. Excluir livro (DELETE)

A operação **DELETE** permite excluir um livro específico da biblioteca:

```python
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
    return jsonify(livros)
```

- **DELETE**: O usuário pode excluir um livro fornecendo seu `id`. O livro será removido da lista e a API retornará a lista atualizada de livros.

## 8. Rodando a API

Para rodar a API no seu ambiente local, use o seguinte comando:

```python
app.run(port=5000, host='localhost', debug=True)
```

- A API estará disponível em `localhost:5000` e o parâmetro `debug=True` permitirá visualizar erros facilmente durante o desenvolvimento.

## Conclusão

Com esta API, você pode realizar as seguintes operações:

- **GET**: Consultar todos os livros ou um livro específico.
- **POST**: Criar um novo livro.
- **PUT**: Editar os dados de um livro existente.
- **DELETE**: Excluir um livro da biblioteca.

A API funciona como uma biblioteca digital, permitindo o gerenciamento dos livros de forma simples e eficiente.