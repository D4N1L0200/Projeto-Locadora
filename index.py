import streamlit as st
from view import View
from templates.entrar_contaUI import EntrarContaUI
from templates.criar_contaUI import CriarContaUI
from templates.cadastro_usuariosUI import CadastroUsuariosUI
from templates.cadastro_veiculosUI import CadastroVeiculosUI
from templates.cadastro_locacoesUI import CadastroLocacoesUI
from templates.buscar_veiculosUI import BuscarVeiculosUI
from templates.minhas_locacoesUI import MinhasLocacoesUI


class IndexUI:
    @staticmethod
    def menu_anonimo():
        op = st.sidebar.selectbox("Menu", ["Entrar em Conta", "Criar Conta"])
        if op == "Entrar em Conta":
            EntrarContaUI.main()
        if op == "Criar Conta":
            CriarContaUI.main()

    @staticmethod
    def menu_admin():
        op = st.sidebar.selectbox(
            "Menu",
            [
                "Cadastro de Usuários",
                "Cadastro de Veículos",
                "Cadastro de Locações",
            ],
        )
        if op == "Cadastro de Usuários":
            CadastroUsuariosUI.main()
        if op == "Cadastro de Veículos":
            CadastroVeiculosUI.main()
        if op == "Cadastro de Locações":
            CadastroLocacoesUI.main()

    @staticmethod
    def menu_usuario():
        op = st.sidebar.selectbox("Menu", ["Buscar Veículos", "Minhas Locações"])
        if op == "Buscar Veículos":
            BuscarVeiculosUI.main()
        if op == "Minhas Locações":
            MinhasLocacoesUI.main()

    @staticmethod
    def sair_do_sistema():
        if st.sidebar.button("Sair"):
            del st.session_state["usuario_id"]
            del st.session_state["usuario_nome"]
            st.rerun()

    @staticmethod
    def sidebar():
        if "usuario_id" not in st.session_state:
            IndexUI.menu_anonimo()
        else:
            admin = st.session_state["usuario_nome"] == "admin"
            st.sidebar.write("Bem-vindo(a), " + st.session_state["usuario_nome"])
            if admin:
                IndexUI.menu_admin()
            else:
                IndexUI.menu_usuario()
            IndexUI.sair_do_sistema()

    @staticmethod
    def main():
        View.carregar_arquivos()
        View.criar_admin()
        IndexUI.sidebar()


IndexUI.main()
