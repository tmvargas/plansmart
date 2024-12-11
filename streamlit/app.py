import streamlit as st
import pandas as pd
from time import sleep
from streamlit_option_menu import option_menu

container = st.empty()

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login():
    container_login = st.container(height=250, border=True)
    username = container_login.text_input("Usuário", key="username")
    password = container_login.text_input("Senha:", type="password")
    button = container_login.button("Login")

    if button:
        if username == 'user' and password == 'qwe123':
            st.success("Login bem-sucedido!")
            sleep(0.3)
            

            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("Usuário ou senha inválidos. Tente novamente.")

def logout():
    if container.button("Encerrar Sessão"):
        st.session_state.logged_in = False
        st.rerun()

def quadro_de_obra():
    nome_spe = {
        'Emopreendimento': 
        ['Incorporadora Moinhos Senior Residence SPE Ltda.',
        'Incorporadora Almirante Tamandaré SPE Ltda.',
        'Incorporadora Barbosa Gonçalves SPE Ltda.',
        'Incorporadora Alfa SPE Ltda.',
        'Incorporadora Gonçalves dias SPE Ltda.',
        'Incorporadora Magno Menino Deus SPE Ltda.',
        'Incorporadora Washington Luiz SPE Ltda'
        ]
    }

    df = pd.DataFrame(nome_spe)
    st.dataframe(df, use_container_width=True)
def home():
    with st.sidebar:
        menu_selected = option_menu('Menu', ['Home', 'Quadro de Obras', 'Sair'], default_index=0)

        if menu_selected == 'Sair':
            logout()
        if menu_selected == 'Home':
            container.title('Seja Bem-vindo(a)!')
        if menu_selected == 'Quadro de Obras':
            col1_, col2_ = container.columns([2,1], gap='large')
            with col1_:
                st.button('Quadro de Obras')
                quadro_de_obra()
            with col2_:
                st.link_button('Gerar Relatório', url="https://drive.google.com/uc?export=download&id=1hKyoJEkRgW_YL2aQ_mN8hQzFOliRSu8f")

login_page = st.Page(login, title="Log in")
logout_page = st.Page(logout, title="Log out")
home_page = st.Page(home, title="Home")

if st.session_state.logged_in:
    pg = st.navigation([home_page])
else:
    pg = st.navigation([login_page])

pg.run()