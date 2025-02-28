import streamlit as st
import pandas as pd
import time
from datetime import datetime
from view import View
from modelos.veiculo import Veiculo
from modelos.situacao import Situacao


class BuscarVeiculosUI:
    @staticmethod
    def main():
        st.header("Buscar veículos")
        tab1, tab2 = st.tabs(["Requisitar veículos", "Filtrar por marca"])
        with tab1:
            BuscarVeiculosUI.requisitar()
        with tab2:
            BuscarVeiculosUI.filtrar()

    @staticmethod
    def requisitar():
        veiculos = View.veiculo_listar()
        if len(veiculos) == 0:
            st.write("Nenhum veículo cadastrado")
        else:
            veiculo = st.selectbox(
                "Selecione o veículo",
                [
                    veiculo
                    for veiculo in veiculos
                    if veiculo.get_situacao() == Situacao.DISPONIVEL
                ],
            )
            duracao = st.number_input("Digite a duração em dias", min_value=1)
            valor_total = veiculo.get_valor_diario() * duracao
            st.write(f"Valor total: {valor_total}")

            if st.button("Requisitar"):
                try:
                    View.locacao_inserir(
                        veiculo.get_id(),
                        st.session_state["usuario_id"],
                        duracao,
                        valor_total,
                        datetime.now(),
                        None,
                    )
                    View.veiculo_atualizar(
                        veiculo.get_id(),
                        veiculo.get_tipo(),
                        veiculo.get_marca(),
                        veiculo.get_modelo(),
                        veiculo.get_placa(),
                        veiculo.get_valor_diario(),
                        Situacao.REQUISITADO,
                    )
                    st.success("Veículo requisitado com sucesso.")
                    time.sleep(2)
                    st.rerun()
                except Exception as e:
                    st.error(str(e))

    @staticmethod
    def filtrar():
        marcas = []
        for veiculo in View.veiculo_listar():
            if veiculo.get_marca() not in marcas:
                marcas.append(veiculo.get_marca())

        marca = st.selectbox("Selecione a marca", marcas)
        veiculos = View.veiculo_listar_marca(marca)
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
