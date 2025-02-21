import streamlit as st
from view import View
from modelos.veiculo import Veiculo


class BuscarVeiculosUI:
    @staticmethod
    def main():
        st.header("Buscar veículos")
        tab1, tab2 = st.tabs(["Buscar", "Filtrar"])
        with tab1:
            BuscarVeiculosUI.buscar()
        with tab2:
            BuscarVeiculosUI.filtrar()

    @staticmethod
    def buscar():
        pass

    @staticmethod
    def filtrar():
        pass
