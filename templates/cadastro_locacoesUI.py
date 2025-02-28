import streamlit as st
import pandas as pd
from view import View
from modelos.situacao import Situacao
import time
from datetime import datetime


class CadastroLocacoesUI:
    @staticmethod
    def main():
        st.header("Cadastro de locações")
        tab1, tab2, tab3, tab4, tab5 = st.tabs(
            ["Listar", "Requisições", "Inserir", "Atualizar", "Excluir"]
        )
        with tab1:
            CadastroLocacoesUI.listar()
        with tab2:
            CadastroLocacoesUI.requisicoes()
        with tab3:
            CadastroLocacoesUI.inserir()
        with tab4:
            CadastroLocacoesUI.atualizar()
        with tab5:
            CadastroLocacoesUI.excluir()

    @staticmethod
    def listar():
        locacoes = View.locacao_listar()
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

    @staticmethod
    def requisicoes():
        locacoes = View.locacao_listar()
        requisicoes = []
        for locacao in locacoes:
            if (
                locacao.get_data_requisicao() is not None
                and locacao.get_data_locacao() is None
            ):
                requisicoes.append(locacao)

        if len(requisicoes) == 0:
            st.write("Nenhuma requisição pendente")
        else:
            op = st.selectbox("Requisição pendente", requisicoes)
            if st.button("Confirmar"):
                try:
                    View.locacao_atualizar(
                        op.get_id(),
                        op.get_id_veiculo(),
                        op.get_id_usuario(),
                        op.get_duracao(),
                        op.get_valor(),
                        op.get_data_requisicao(),
                        datetime.now(),
                    )
                    veiculo = View.veiculo_listar_id(op.get_id_veiculo())
                    View.veiculo_atualizar(
                        veiculo.get_id(),
                        veiculo.get_tipo(),
                        veiculo.get_marca(),
                        veiculo.get_modelo(),
                        veiculo.get_placa(),
                        veiculo.get_valor_diario(),
                        Situacao.LOCADO,
                    )
                    st.success("Locação confirmada com sucesso.")
                    time.sleep(2)
                    st.rerun()
                except ValueError as e:
                    st.error(str(e))

    @staticmethod
    def inserir():
        id_veiculo = st.number_input("Informe o id do veículo")
        id_usuario = st.number_input("Informe o id do usuário")
        duracao = st.number_input("Informe a duração em dias")
        valor = st.number_input("Informe o valor")
        data_requisicao = st.date_input(
            "Informe a data de requisição (DD/MM/YYYY)", format="DD/MM/YYYY"
        )
        locado = st.checkbox("Locado")
        data_locacao = st.date_input(
            "Informe a data de locação (DD/MM/YYYY)",
            format="DD/MM/YYYY",
            disabled=not locado,
        )

        if st.button("Inserir"):
            try:
                View.locacao_inserir(
                    id_veiculo,
                    id_usuario,
                    duracao,
                    valor,
                    data_requisicao,
                    data_locacao if locado else None,
                )
                st.success("Locação inserida com sucesso.")
                time.sleep(2)
                st.rerun()
            except ValueError as e:
                st.error(str(e))

    @staticmethod
    def atualizar():
        locacoes = View.locacao_listar()
        if len(locacoes) == 0:
            st.write("Nenhuma locação cadastrada")
        else:
            op = st.selectbox("Atualização de locação", locacoes)
            id_veiculo = st.number_input(
                "Informe o novo id do veículo", op.get_id_veiculo()
            )
            id_usuario = st.number_input(
                "Informe o novo id do usuário", op.get_id_usuario()
            )
            duracao = st.number_input(
                "Informe a nova duração em dias", op.get_duracao()
            )
            valor = st.number_input("Informe o novo valor", op.get_valor())
            data_requisicao = st.date_input(
                "Informe a nova data de requisição (DD/MM/YYYY)", format="DD/MM/YYYY"
            )
            data_locacao = st.date_input(
                "Informe a nova data de locação (DD/MM/YYYY)", format="DD/MM/YYYY"
            )
            if st.button("Atualizar"):
                try:
                    View.locacao_atualizar(
                        op.get_id(),
                        id_veiculo,
                        id_usuario,
                        duracao,
                        valor,
                        data_requisicao,
                        data_locacao,
                    )
                    st.success("Locação atualizada com sucesso")
                    time.sleep(2)
                    st.rerun()
                except ValueError as e:
                    st.error(str(e))

    @staticmethod
    def excluir():
        locacoes = View.locacao_listar()
        if len(locacoes) == 0:
            st.write("Nenhuma locação cadastrada.")
        else:
            locacao_para_excluir = {}
            for locacao in locacoes:
                locacao_para_excluir[str(locacao)] = locacao.get_id()
            locacao_escolhida = st.selectbox(
                "Exclusão de locação", list(locacao_para_excluir.keys())
            )
            if st.button("Excluir"):
                try:
                    View.locacao_excluir(locacao_para_excluir[locacao_escolhida])
                    st.success("Locação excluída com sucesso.")
                    time.sleep(2)
                    st.rerun()
                except ValueError as e:
                    st.error(str(e))
