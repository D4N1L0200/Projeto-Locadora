import streamlit as st
import time
from view import View


class CriarContaUI:
    @staticmethod
    def main():
        st.header("Criar Conta no Sistema")
        CriarContaUI.criar()

    @staticmethod
    def criar():
        nome = st.text_input("Informe o nome")
        senha = st.text_input("Informe a senha", type="password")

        if st.button("Criar"):
            try:
                View.usuario_inserir(nome, senha)
                st.success("Conta criada com sucesso!")
                time.sleep(2)
                st.rerun()
            except ValueError as e:
                st.error(f"Erro ao criar conta: {str(e)}")
