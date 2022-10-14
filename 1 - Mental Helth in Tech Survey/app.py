import streamlit as st

def main():
    options = ['Homepage','Consulta','Previsão']
    page_option = st.sidebar.selectbox['Options', options]
    
    if page_option == 'Homepage':
        homepage()
    elif page_option == 'Consulta':
        consulta()
    elif page_option == 'Previsão':
        previsao()

if __name__ == '__main__':
    main()