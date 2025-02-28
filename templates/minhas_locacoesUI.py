import streamlit as st
import pandas as pd
import time
from view import View
from modelos.veiculo import Veiculo


class MinhasLocacoesUI:
    @staticmethod
    def main():
        st.header("Minhas locações")
        tab1, tab2 = st.tabs(["Requisições", "Locações"])
        with tab1:
            MinhasLocacoesUI.requisicoes()
        with tab2:
            MinhasLocacoesUI.locacoes()

    @staticmethod
    def requisicoes():
        locacoes = View.locacao_listar()
        requisicoes = [
            locacao for locacao in locacoes if locacao.get_data_locacao() is None
        ]
        if len(requisicoes) == 0:
            st.write("Nenhuma requisição pendente")
        else:
            dic = []
            for locacao in locacoes:
                data_requisicao = locacao.get_data_requisicao()
                if data_requisicao is not None:
                    data_requisicao = data_requisicao.strftime("%Y-%m-%d %H:%M:%S")
                else:
                    data_requisicao = None

                data_locacao = locacao.get_data_locacao()
                if data_locacao is not None:
                    data_locacao = data_locacao.strftime("%Y-%m-%d %H:%M:%S")
                else:
                    data_locacao = None

                dic.append(
                    {
                        "id": locacao.get_id(),
                        "id_veiculo": locacao.get_id_veiculo(),
                        "id_usuario": locacao.get_id_usuario(),
                        "duracao": locacao.get_duracao(),
                        "valor": locacao.get_valor(),
                        "data_requisicao": data_requisicao,
                        "data_locacao": data_locacao,
                    }
                )
            df = pd.DataFrame(dic)
            st.dataframe(df, hide_index=True)

    @staticmethod
    def locacoes():
        locacoes = View.locacao_listar()
        locacoes = [
            locacao for locacao in locacoes if locacao.get_data_locacao() is not None
        ]
        if len(locacoes) == 0:
            st.write("Nenhuma locação cadastrada")
        else:
            dic = []
            for locacao in locacoes:
                data_requisicao = locacao.get_data_requisicao()
                if data_requisicao is not None:
                    data_requisicao = data_requisicao.strftime("%Y-%m-%d %H:%M:%S")
                else:
                    data_requisicao = None

                data_locacao = locacao.get_data_locacao()
                if data_locacao is not None:
                    data_locacao = data_locacao.strftime("%Y-%m-%d %H:%M:%S")
                else:
                    data_locacao = None

                dic.append(
                    {
                        "id": locacao.get_id(),
                        "id_veiculo": locacao.get_id_veiculo(),
                        "id_usuario": locacao.get_id_usuario(),
                        "duracao": locacao.get_duracao(),
                        "valor": locacao.get_valor(),
                        "data_requisicao": data_requisicao,
                        "data_locacao": data_locacao,
                    }
                )
            df = pd.DataFrame(dic)
            st.dataframe(df, hide_index=True)
