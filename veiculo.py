import json
from situacao import Situacao
from crud import CRUD


class Veiculo:
    def __init__(self, id, tipo, marca, modelo, placa, valor_diario, situacao) -> None:
        self.__id = 0
        self.__tipo = ""
        self.__marca = ""
        self.__modelo = ""
        self.__placa = ""
        self.__valor_diario = 0.0
        self.__situacao = Situacao.DISPONIVEL

        self.set_id(id)
        self.set_tipo(tipo)
        self.set_marca(marca)
        self.set_modelo(modelo)
        self.set_placa(placa)
        self.set_valor_diario(valor_diario)
        self.set_situacao(situacao)

    def set_id(self, id):
        self.__id = id

    def get_id(self):
        return self.__id

    def set_tipo(self, tipo):
        self.__tipo = tipo

    def get_tipo(self):
        return self.__tipo

    def set_marca(self, marca):
        self.__marca = marca

    def get_marca(self):
        return self.__marca

    def set_modelo(self, modelo):
        self.__modelo = modelo

    def get_modelo(self):
        return self.__modelo

    def set_placa(self, placa):
        self.__placa = placa

    def get_placa(self):
        return self.__placa

    def set_valor_diario(self, valor_diario):
        self.__valor_diario = valor_diario

    def get_valor_diario(self):
        return self.__valor_diario

    def set_situacao(self, situacao):
        self.__situacao = situacao

    def get_situacao(self):
        return self.__situacao

    def __str__(self):
        return (
            f"ID: {self.get_id()} - Tipo: {self.get_tipo()} - Marca: {self.get_marca()} "
            f"- Modelo: {self.get_modelo()} - Placa: {self.get_placa()} - Valor Diário: {self.get_valor_diario()} "
            f"- Situação: {self.get_situacao().name}"
        )


class CRUD_Veiculo(CRUD):
    @classmethod
    def salvar(cls):
        cls.dados = []

        for obj in cls.objetos:
            cls.dados.append(
                {
                    "id": obj.get_id(),
                    "tipo": obj.get_tipo(),
                    "marca": obj.get_marca(),
                    "modelo": obj.get_modelo(),
                    "placa": obj.get_placa(),
                    "valor_diario": obj.get_valor_diario(),
                    "situacao": obj.get_situacao().value,
                }
            )

        with open("veiculos.json", "w") as f:
            json.dump(cls.dados, f)

    @classmethod
    def abrir(cls) -> None:
        with open("veiculos.json", "r") as f:
            dados = json.load(f)

        cls.limpar()

        for obj in dados:
            cls.inserir(
                Veiculo(
                    obj["id"],
                    obj["tipo"],
                    obj["marca"],
                    obj["modelo"],
                    obj["placa"],
                    obj["valor_diario"],
                    Situacao(obj["situacao"]),
                )
            )


if __name__ == "__main__":
    veiculo1 = Veiculo(
        0, "Carro", "Toyota", "Corolla", "ABC-1234", 150.0, Situacao.DISPONIVEL
    )
    CRUD_Veiculo.inserir(veiculo1)

    veiculo2 = Veiculo(0, "Moto", "Honda", "CB500", "XYZ-5678", 100.0, Situacao.LOCADO)
    CRUD_Veiculo.inserir(veiculo2)

    print("Veículos:")
    for veiculo in CRUD_Veiculo.listar():
        print(veiculo)

    veiculo = CRUD_Veiculo.listar_por_id(1)
    print("Veículo 1:")
    print(veiculo)

    novo_veiculo = Veiculo(
        2, "SUV", "Ford", "Ecosport", "DEF-4321", 180.0, Situacao.REQUISITADO
    )
    CRUD_Veiculo.atualizar(novo_veiculo)

    print("Veículos depois de atualizar:")
    for veiculo in CRUD_Veiculo.listar():
        print(veiculo)

    CRUD_Veiculo.delete(1)

    print("Veículos depois de deletar:")
    for veiculo in CRUD_Veiculo.listar():
        print(veiculo)
