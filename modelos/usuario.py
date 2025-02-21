import json
from modelos.crud import CRUD


class Usuario:
    def __init__(self, id, nome, senha) -> None:
        self.__id = 0
        self.__nome = ""
        self.__senha = ""

        self.set_id(id)
        self.set_nome(nome)
        self.set_senha(senha)

    def set_id(self, id):
        self.__id = id

    def get_id(self):
        return self.__id

    def set_nome(self, nome):
        self.__nome = nome

    def get_nome(self):
        return self.__nome

    def set_senha(self, senha):
        self.__senha = senha

    def get_senha(self):
        return self.__senha

    def __str__(self):
        return (
            f"ID: {self.get_id()} - Nome: {self.get_nome()} - Senha: {self.get_senha()}"
        )


class CRUD_Usuario(CRUD):
    @classmethod
    def salvar(cls):
        cls.dados = []

        for obj in cls.objetos:
            cls.dados.append(
                {"id": obj.get_id(), "nome": obj.get_nome(), "senha": obj.get_senha()}
            )

        with open("usuarios.json", "w") as f:
            json.dump(cls.dados, f)

    @classmethod
    def abrir(cls) -> None:
        with open("usuarios.json", "r") as f:
            dados = json.load(f)

        cls.limpar()

        for obj in dados:
            cls.inserir(Usuario(obj["id"], obj["nome"], obj["senha"]))


if __name__ == "__main__":
    usuario1 = Usuario(0, "Emilly", "senha123")
    CRUD_Usuario.inserir(usuario1)

    usuario2 = Usuario(0, "Analy", "senha456")
    CRUD_Usuario.inserir(usuario2)

    print("Usuários:")
    for usuario in CRUD_Usuario.listar():
        print(usuario)

    usuario = CRUD_Usuario.listar_por_id(1)
    print("Usuário 1:")
    print(usuario)

    novo_usuario = Usuario(2, "Igor", "senha789")
    CRUD_Usuario.atualizar(novo_usuario)

    print("Usuários depois de atualizar:")
    for usuario in CRUD_Usuario.listar():
        print(usuario)

    CRUD_Usuario.excluir(1)

    print("Usuários depois de deletar:")
    for usuario in CRUD_Usuario.listar():
        print(usuario)
