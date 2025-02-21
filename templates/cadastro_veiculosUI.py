import streamlit as st
import pandas as pd
from view import View
from modelos.situacao import Situacao
import time


class CadastroVeiculosUI:
    @staticmethod
    def main():
        st.header("Cadastro de veículos")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1:
            CadastroVeiculosUI.listar()
        with tab2:
            CadastroVeiculosUI.inserir()
        with tab3:
            CadastroVeiculosUI.atualizar()
        with tab4:
            CadastroVeiculosUI.excluir()

    @staticmethod
    def listar():
        veiculos = View.veiculo_listar()
        if len(veiculos) == 0:
            st.write("Nenhum veículo cadastrado")
        else:
            dic = []
            for veiculo in veiculos:
                dic.append(
                    {
                        "id": veiculo.get_id(),
                        "tipo": veiculo.get_tipo(),
                        "marca": veiculo.get_marca(),
                        "modelo": veiculo.get_modelo(),
                        "placa": veiculo.get_placa(),
                        "valor_diario": veiculo.get_valor_diario(),
                        "situacao": veiculo.get_situacao().name,
                    }
                )
            df = pd.DataFrame(dic)
            st.dataframe(df, hide_index=True)

    @staticmethod
    def inserir():
        tipo = st.text_input("Informe o tipo do veículo")
        marca = st.text_input("Informe a marca do veículo")
        modelo = st.text_input("Informe o modelo do veículo")
        placa = st.text_input("Informe a placa do veículo")
        valor_diario = st.number_input("Informe o valor diário do veículo")
        situacao = st.selectbox(
            "Informe a situação do veículo", ["DISPONIVEL", "REQUISITADO", "LOCADO"]
        )

        if st.button("Inserir"):
            try:
                View.veiculo_inserir(
                    tipo, marca, modelo, placa, valor_diario, Situacao[situacao]
                )
                st.success("Veículo inserido com sucesso.")
                time.sleep(2)
                st.rerun()
            except ValueError as e:
                st.error(str(e))

    @staticmethod
    def atualizar():
        veiculos = View.veiculo_listar()
        if len(veiculos) == 0:
            st.write("Nenhum veículo cadastrado")
        else:
            op = st.selectbox("Atualização de veículo", veiculos)
            tipo = st.text_input("Informe o novo tipo do veículo", op.get_tipo())
            marca = st.text_input("Informe a nova marca do veículo", op.get_marca())
            modelo = st.text_input("Informe o novo modelo do veículo", op.get_modelo())
            placa = st.text_input("Informe a nova placa do veículo", op.get_placa())
            valor_diario = st.number_input(
                "Informe o novo valor diário do veículo", op.get_valor_diario()
            )
            situacao = st.selectbox(
                "Informe a nova situação do veículo",
                ["DISPONIVEL", "REQUISITADO", "LOCADO"],
                index=op.get_situacao().value,
            )
            if st.button("Atualizar"):
                try:
                    View.veiculo_atualizar(
                        op.get_id(),
                        tipo,
                        marca,
                        modelo,
                        placa,
                        valor_diario,
                        Situacao[situacao],
                    )
                    st.success("Veículo atualizado com sucesso")
                    time.sleep(2)
                    st.rerun()
                except ValueError as e:
                    st.error(str(e))

    @staticmethod
    def excluir():
        veiculos = View.veiculo_listar()
        if len(veiculos) == 0:
            st.write("Nenhum veículo cadastrado.")
        else:
            veiculos_para_excluir = {}
            for veiculo in veiculos:
                veiculos_para_excluir[str(veiculo)] = veiculo.get_id()
            veiculo_escolhido = st.selectbox(
                "Exclusão de veículo", list(veiculos_para_excluir.keys())
            )
            if st.button("Excluir"):
                try:
                    View.veiculo_excluir(veiculos_para_excluir[veiculo_escolhido])
                    st.success("Veículo excluído com sucesso.")
                    time.sleep(2)
                    st.rerun()
                except ValueError as e:
                    st.error(str(e))
