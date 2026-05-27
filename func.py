import json

class Livro:

    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.__isbn = isbn

    def get_mostrar_isbn(self):
        return self.__isbn

    def exibir(self):
        print(f"{self.titulo}, {self.autor}")


class Livrodigital(Livro):

    def __init__(self, titulo, autor, isbn, formato):
        super().__init__(titulo, autor, isbn)
        self.formato = formato

    def exibir(self):
        print(f"{self.titulo}, {self.autor}, {self.formato}")


class Livrofisico(Livro):

    def __init__(self, titulo, autor, isbn, prateleira):
        super().__init__(titulo, autor, isbn)
        self.prateleira = prateleira

    def exibir(self):
        print(f"{self.titulo}, {self.autor}, {self.prateleira}")


def validacao(obj):

    if isinstance(obj, Livrodigital):

        if not obj.formato:
            print("Campo formato vazio")
            return False

    if isinstance(obj, Livrofisico):

        if not obj.prateleira:
            print("Campo prateleira vazio")
            return False

    if not obj.titulo:
        print("Campo título vazio")
        return False

    if not obj.autor:
        print("Campo autor vazio")
        return False

    if len(obj.titulo) < 3:
        print("Título deve conter ao menos 3 caracteres")
        return False

    if len(obj.autor) < 3:
        print("Autor deve conter ao menos 3 caracteres")
        return False

    return True

def menu():

    print("Seja bem vindo ao seu sistema de livros")
    print("="*50)
    print("1-Cadastrar")
    print("2-Consultar")
    print("3-Remover")
    print("4-Editar")
    print("5-Listar todos")
    print("6-Encerrar programa")

def cadastrar_digital(lista):

    try:

        titulo=input("Titulo:").strip()
        autor=input("Autor:").strip()
        isbn=int(input("Isbn:"))
        formato=input("Formato:").strip()

    except ValueError:
        print("Digite apenas dados compátiveis")
        return False

    livro_digital=Livrodigital(titulo,autor,isbn,formato)

    if validacao(livro_digital):
        lista.append(livro_digital)
        return True

    return False


def cadastrar_fisico(lista):

    try:

        titulo = input("Titulo:").strip()
        autor = input("Autor:").strip()
        isbn = int(input("Isbn:"))
        prateleira = input("Prateleira:").strip()

    except ValueError:
        print("Digite apenas dados compátiveis")
        return False

    livro_fisico = Livrofisico(titulo, autor, isbn, prateleira)

    if validacao(livro_fisico):
        lista.append(livro_fisico)
        return True

    return False

def buscar_isbn(lista, isbn):

    for livro in lista:
        if livro.get_mostrar_isbn() == isbn:
            return livro

    print("Livro não encontrado")

    return None


def consultar_livro(lista, isbn):
    return buscar_isbn(lista, isbn)


def remover_livro(lista, isbn):
    encontrado = buscar_isbn(lista, isbn)

    if encontrado:
        lista.remove(encontrado)
        print("Livro removido com sucesso")
        return True

    else:
        return False

def listar_todos(lista):
    if not lista:
        print("Lista vazia")
        return False

    for livro in lista:
        livro.exibir()
    return True

def salvar_dados(lista):

    dados = []

    for livro in lista:

        if isinstance(livro, Livrodigital):

            dados.append({"titulo": livro.titulo, "autor": livro.autor,
                          "ibns": livro.get_mostrar_isbn(), "formato": livro.formato})

        elif isinstance(livro, Livrofisico):

            dados.append({"titulo": livro.titulo, "autor": livro.autor,
                          "ibns": livro.get_mostrar_isbn(), "prateleira": livro.prateleira})

    with open("livros.json", "w", encoding="utf-8") as arq:
        json.dump(dados, arq, indent=4, ensure_ascii=False)

def carregar_dados():

    try:

        with open("livros.json", "r", encoding="utf-8") as arq:
            livros = json.load(arq)
        lista_2 = []

        for livro in livros:

            if "prateleira" in livro:
                lista_2.append(Livrofisico(livro["titulo"], livro["autor"], livro["ibns"], livro["prateleira"]))

            elif "formato" in livro:
                lista_2.append(Livrodigital(livro["titulo"], livro["autor"], livro["ibns"], livro["formato"]))

        return lista_2

    except FileNotFoundError:
        return []

def editar(lista, isbn):

    encontrado = buscar_isbn(lista, isbn)

    if not encontrado:
        return False

    extra = ''

    titulo = input("Título: ").strip()
    autor = input("Autor: ").strip()

    if isinstance(encontrado, Livrodigital):
            
        extra = input("Formato: ").strip()

        if not extra:
            print("Campo não pode ser vázio")
            return False

    elif isinstance(encontrado, Livrofisico):

        extra = input("Prateleira: ").strip()

        if not extra:
            print("Campo não pode ser vazio")
            return False



    if not titulo:
        print("Campo titulo vázio")
        return False

    if len(titulo) < 3:
        print("Titulo deve conter ao menos 3 caracteres")
        return False

    if not autor:
        print("Campo autor vázio")
        return False

    if len(autor) < 3:
        print("autor deve conter ao menos 3 caracteres")
        return False

    encontrado.titulo = titulo
    encontrado.autor = autor

    if isinstance(encontrado, Livrodigital):
        encontrado.formato = extra

    elif isinstance(encontrado, Livrofisico):
        encontrado.prateleira = extra

    return True

def mensagem_de_erro():
    print("Digite apenas dados compátiveis")