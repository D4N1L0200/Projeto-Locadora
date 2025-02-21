import streamlit as st
import pandas as pd
from view import View
import time


class CadastroUsuariosUI:
    @staticmethod
    def main():
        st.header("Cadastro de usuários")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1:
            CadastroUsuariosUI.listar()
        with tab2:
            CadastroUsuariosUI.inserir()
        with tab3:
            CadastroUsuariosUI.atualizar()
        with tab4:
            CadastroUsuariosUI.excluir()

    @staticmethod
    def listar():
        usuarios = View.usuario_listar()
        if len(usuarios) == 0:
            st.write("Nenhum usuário cadastrado")
        else:
            dic = []
            for usuario in usuarios:
                dic.append(
                    {
                        "id": usuario.get_id(),
                        "nome": usuario.get_nome(),
                        "senha": usuario.get_senha(),
                    }
                )
            df = pd.DataFrame(dic)
            st.dataframe(df, hide_index=True)

    @staticmethod
    def inserir():
        nome = st.text_input("Informe o nome do usuário")
        senha = st.text_input("Informe a senha", type="password")

        if st.button("Inserir"):
            try:
                View.usuario_inserir(nome, senha)
                st.success("Usuário inserido com sucesso.")
                time.sleep(2)
                st.rerun()
            except ValueError as e:
                st.error(str(e))

    @staticmethod
    def atualizar():
        usuarios = View.usuario_listar()
        if len(usuarios) == 0:
            st.write("Nenhum usuário cadastrado")
        else:
            op = st.selectbox("Atualização de usuário", usuarios)
            nome = st.text_input("Informe o novo nome do usuário", op.get_nome())
            senha = st.text_input(
                "Informe a nova senha", op.get_senha(), type="password"
            )
            if st.button("Atualizar"):
                try:
                    View.usuario_atualizar(op.get_id(), nome, senha)
                    st.success("Usuário atualizado com sucesso")
                    time.sleep(2)
                    st.rerun()
                except ValueError as e:
                    st.error(str(e))

    @staticmethod
    def excluir():
        usuarios = View.usuario_listar()
        if len(usuarios) == 0:
            st.write("Nenhum usuário cadastrado.")
        else:
            usuarios_para_excluir = {}
            for usuario in usuarios:
                usuarios_para_excluir[str(usuario)] = usuario.get_id()
            usuario_escolhido = st.selectbox(
                "Exclusão de usuário", list(usuarios_para_excluir.keys())
            )
            if st.button("Excluir"):
                try:
                    View.usuario_excluir(
                        usuarios_para_excluir[usuario_escolhido]
                    )
                    st.success("Usuário excluído com sucesso.")
                    time.sleep(2)
                    st.rerun()
                except ValueError as e:
                    st.error(str(e))
