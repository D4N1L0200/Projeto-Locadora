from modelos.usuario import Usuario, CRUD_Usuario
from modelos.locacao import Locacao, CRUD_Locacao
from modelos.veiculo import Veiculo, CRUD_Veiculo


class View:
    @staticmethod
    def carregar_arquivos():
        CRUD_Locacao.abrir()
        CRUD_Usuario.abrir()
        CRUD_Veiculo.abrir()

    @staticmethod
    def criar_admin():
        for usuario in CRUD_Usuario.listar():
            if usuario.get_nome() == "admin":
                return

        admin = Usuario(0, "admin", "1234")
        CRUD_Usuario.inserir(admin)

    @staticmethod
    def usuario_inserir(nome, senha):
        usuario = Usuario(0, nome, senha)
        CRUD_Usuario.inserir(usuario)

    @staticmethod
    def usuario_listar():
        return CRUD_Usuario.listar()

    @staticmethod
    def usuario_listar_id(id):
        return CRUD_Usuario.listar_id(id)

    @staticmethod
    def usuario_atualizar(id, nome, senha):
        usuario = Usuario(id, nome, senha)
        CRUD_Usuario.atualizar(usuario)

    @staticmethod
    def usuario_excluir(id):
        CRUD_Usuario.excluir(id)

    @staticmethod
    def locacao_inserir(
        id_veiculo, id_usuario, duracao, valor, data_requisicao, data_locacao
    ):
        locacao = Locacao(
            0, id_veiculo, id_usuario, duracao, valor, data_requisicao, data_locacao
        )
        CRUD_Locacao.inserir(locacao)

    @staticmethod
    def locacao_listar():
        return CRUD_Locacao.listar()

    @staticmethod
    def locacao_listar_id(id):
        return CRUD_Locacao.listar_id(id)

    @staticmethod
    def locacao_atualizar(
        id,
        id_veiculo,
        id_usuario,
        duracao,
        valor,
        data_requisicao,
        data_locacao,
    ):
        locacao = Locacao(
            id, id_veiculo, id_usuario, duracao, valor, data_requisicao, data_locacao
        )
        CRUD_Locacao.atualizar(locacao)

    @staticmethod
    def locacao_excluir(id):
        CRUD_Locacao.excluir(id)

    @staticmethod
    def veiculo_inserir(tipo, marca, modelo, placa, valor_diario, situacao):
        veiculo = Veiculo(0, tipo, marca, modelo, placa, valor_diario, situacao)
        CRUD_Veiculo.inserir(veiculo)

    @staticmethod
    def veiculo_listar():
        return CRUD_Veiculo.listar()

    @staticmethod
    def veiculo_listar_id(id):
        return CRUD_Veiculo.listar_id(id)

    @staticmethod
    def veiculo_listar_marca(marca):
        veiculos = []
        for veiculo in CRUD_Veiculo.listar():
            if veiculo.get_marca() == marca:
                veiculos.append(veiculo)

        return veiculos

    @staticmethod
    def veiculo_atualizar(id, tipo, marca, modelo, placa, valor_diario, situacao):
        veiculo = Veiculo(id, tipo, marca, modelo, placa, valor_diario, situacao)
        CRUD_Veiculo.atualizar(veiculo)

    @staticmethod
    def veiculo_excluir(id):
        CRUD_Veiculo.excluir(id)

    @staticmethod
    def autenticar_usuario(nome, senha):
        usuarios = CRUD_Usuario.listar()
        for usuario in usuarios:
            if usuario.get_nome() == nome and usuario.get_senha() == senha:
                return {"id": usuario.get_id(), "nome": usuario.get_nome()}

        return None
