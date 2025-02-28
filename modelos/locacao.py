import json
from datetime import datetime
from modelos.crud import CRUD


class Locacao:
    def __init__(
        self, id, id_veiculo, id_usuario, duracao, valor, data_requisicao, data_locacao
    ) -> None:
        self.__id = 0
        self.__id_veiculo = 0
        self.__id_usuario = 0
        self.__duracao = 0
        self.__valor = 0.0
        self.__data_requisicao = None
        self.__data_locacao = None

        self.set_id(id)
        self.set_id_veiculo(id_veiculo)
        self.set_id_usuario(id_usuario)
        self.set_duracao(duracao)
        self.set_valor(valor)
        self.set_data_requisicao(data_requisicao)
        self.set_data_locacao(data_locacao)

    def set_id(self, id):
        self.__id = id

    def get_id(self):
        return self.__id

    def set_id_veiculo(self, id_veiculo):
        self.__id_veiculo = id_veiculo

    def get_id_veiculo(self):
        return self.__id_veiculo

    def set_id_usuario(self, id_usuario):
        self.__id_usuario = id_usuario

    def get_id_usuario(self):
        return self.__id_usuario

    def set_duracao(self, duracao):
        self.__duracao = duracao

    def get_duracao(self):
        return self.__duracao

    def set_valor(self, valor):
        self.__valor = valor

    def get_valor(self):
        return self.__valor

    def set_data_requisicao(self, data_requisicao):
        self.__data_requisicao = data_requisicao

    def get_data_requisicao(self):
        return self.__data_requisicao

    def set_data_locacao(self, data_locacao):
        self.__data_locacao = data_locacao

    def get_data_locacao(self):
        return self.__data_locacao

    def __str__(self):
        data_requisicao = self.get_data_requisicao()
        if data_requisicao is not None:
            data_requisicao = data_requisicao.strftime("%Y-%m-%d %H:%M:%S")
        else:
            data_requisicao = "--"

        data_locacao = self.get_data_locacao()
        if data_locacao is not None:
            data_locacao = data_locacao.strftime("%Y-%m-%d %H:%M:%S")
        else:
            data_locacao = "--"

        return (
            f"ID: {self.get_id()} - ID Veículo: {self.get_id_veiculo()} - ID Usuário: {self.get_id_usuario()} "
            f"- Duração: {self.get_duracao()} dias - Valor: {self.get_valor()} "
            f"- Data Requisição: {data_requisicao} "
            f"- Data Locação: {data_locacao}"
        )


class CRUD_Locacao(CRUD):
    @classmethod
    def salvar(cls):
        cls.dados = []

        for obj in cls.objetos:
            data_requisicao = obj.get_data_requisicao()
            if data_requisicao is not None:
                data_requisicao = data_requisicao.strftime("%Y-%m-%d %H:%M:%S")
            else:
                data_requisicao = "--"

            data_locacao = obj.get_data_locacao()
            if data_locacao is not None:
                data_locacao = data_locacao.strftime("%Y-%m-%d %H:%M:%S")
            else:
                data_locacao = "--"

            cls.dados.append(
                {
                    "id": obj.get_id(),
                    "id_veiculo": obj.get_id_veiculo(),
                    "id_usuario": obj.get_id_usuario(),
                    "duracao": obj.get_duracao(),
                    "valor": obj.get_valor(),
                    "data_requisicao": data_requisicao,
                    "data_locacao": data_locacao,
                }
            )

        with open("locacoes.json", "w") as f:
            json.dump(cls.dados, f)

    @classmethod
    def abrir(cls) -> None:
        with open("locacoes.json", "r") as f:
            dados = json.load(f)

        cls.limpar()

        for obj in dados:
            data_requisicao = obj["data_requisicao"]
            if data_requisicao != "--":
                data_requisicao = datetime.strptime(
                    data_requisicao, "%Y-%m-%d %H:%M:%S"
                )
            else:
                data_requisicao = None

            data_locacao = obj["data_locacao"]
            if data_locacao != "--":
                data_locacao = datetime.strptime(data_locacao, "%Y-%m-%d %H:%M:%S")
            else:
                data_locacao = None

            cls.inserir(
                Locacao(
                    obj["id"],
                    obj["id_veiculo"],
                    obj["id_usuario"],
                    obj["duracao"],
                    obj["valor"],
                    data_requisicao,
                    data_locacao,
                )
            )


if __name__ == "__main__":
    locacao1 = Locacao(
        0,
        1,
        1,
        5,
        750.0,
        datetime(2024, 10, 1, 10, 0, 0),
        datetime(2024, 10, 2, 10, 0, 0),
    )
    CRUD_Locacao.inserir(locacao1)

    locacao2 = Locacao(
        0,
        2,
        2,
        3,
        300.0,
        datetime(2024, 10, 3, 12, 0, 0),
        datetime(2024, 10, 4, 12, 0, 0),
    )
    CRUD_Locacao.inserir(locacao2)

    print("Locações:")
    for locacao in CRUD_Locacao.listar():
        print(locacao)

    locacao = CRUD_Locacao.listar_por_id(1)
    print("Locação 1:")
    print(locacao)

    nova_locacao = Locacao(
        2,
        1,
        1,
        7,
        1050.0,
        datetime(2024, 10, 5, 14, 0, 0),
        datetime(2024, 10, 6, 14, 0, 0),
    )
    CRUD_Locacao.atualizar(nova_locacao)

    print("Locações depois de atualizar:")
    for locacao in CRUD_Locacao.listar():
        print(locacao)

    CRUD_Locacao.excluir(1)

    print("Locações depois de deletar:")
    for locacao in CRUD_Locacao.listar():
        print(locacao)
