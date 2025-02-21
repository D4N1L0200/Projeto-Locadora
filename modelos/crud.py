from abc import ABC, abstractmethod


class CRUD(ABC):
    objetos = []

    @classmethod
    def limpar(cls):
        cls.objetos = []
        cls.salvar()

    @classmethod
    def inserir(cls, obj):
        if obj.get_id() == 0:
            id = 0

            for o in cls.objetos:
                if o.get_id() > id:
                    id = o.get_id()

            obj.set_id(id + 1)

        cls.objetos.append(obj)

        cls.salvar()

    @classmethod
    def listar(cls):
        return cls.objetos

    @classmethod
    def listar_por_id(cls, id):
        for o in cls.objetos:
            if o.get_id() == id:
                return o

    @classmethod
    def atualizar(cls, obj):
        for o in cls.objetos:
            if o.get_id() == obj.get_id():
                idx = cls.objetos.index(o)
                cls.objetos[idx] = obj

        cls.salvar()

    @classmethod
    def excluir(cls, id: int) -> None:
        for o in cls.objetos:
            if o.get_id() == id:
                idx = cls.objetos.index(o)
                del cls.objetos[idx]

        cls.salvar()

    @classmethod
    @abstractmethod
    def salvar(cls) -> None:
        pass

    @classmethod
    @abstractmethod
    def abrir(cls) -> None:
        pass
