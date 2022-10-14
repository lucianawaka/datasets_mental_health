import streamlit as st
import pickle
import numpy as np
import joblib

def main():
    options = ['Homepage','Consulta','Previsão']
    page_option = st.sidebar.selectbox('Options', options)
    
    if page_option == 'Homepage':
        homepage()
    elif page_option == 'Consulta':
        consulta()
    elif page_option == 'Previsão':
        previsao()


# Home page

def homepage():
    pass

def consulta():
    pass

def previsao():
    if st.button('Submeter'):
        print('Previsão dados')
        Modelo = joblib.load('RandomForestClassifier_v1.pkl')
        print(Modelo)
        meus_dados = [[25,  0,  0,  1,  0,  1,  1,  1,  0,  0,  1,  0,  0,  2,  1,  0,
         0,  2,  0,  3,  3,  0]]
        meus_dados_n = np.array(meus_dados).reshape(1, -1)
        predict_treatment = Modelo.predict(meus_dados_n).astype(int)
        dict_result = {0:'Não',1:'Sim'}
        predict_treatment_t = dict_result[predict_treatment[0]]
        st.markdown(f"""{predict_treatment_t}""")
        
if __name__ == '__main__':
    main()