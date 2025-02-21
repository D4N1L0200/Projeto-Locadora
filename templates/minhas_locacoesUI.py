import streamlit as st
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
        pass

    @staticmethod
    def locacoes():
        pass
