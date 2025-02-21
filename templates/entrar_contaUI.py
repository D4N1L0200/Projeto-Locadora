import streamlit as st
import time
from view import View


class EntrarContaUI:
    @staticmethod
    def main():
        st.header("Entrar no Sistema")
        EntrarContaUI.entrar()

    @staticmethod
    def entrar():
        nome = st.text_input("Informe o nome")
        senha = st.text_input("Informe a senha", type="password")
        if st.button("Entrar"):
            usuario = View.autenticar_usuario(nome, senha)
            if usuario is None:
                st.error("Nome ou senha inválidos")
            else:
                st.session_state["usuario_id"] = usuario["id"]
                st.session_state["usuario_nome"] = usuario["nome"]
                st.success("Login realizado com sucesso!")
                time.sleep(2)
                st.rerun()
