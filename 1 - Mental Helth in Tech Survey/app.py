import streamlit as st
import pickle
import numpy as np

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
        model = pickle.load(open('RandomForestClassifier_v1.pkl', 'rb'))
        print(model)
        meus_dados = [31,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,4,0]
        meus_dados_n = np.array(meus_dados).reshape(1, -1)
        #predict_treatment = model.predict_proba(meus_dados_n)
        #predict_treatment_t = type(predict_treatment)
        #print(predict_treatment)
        #print(predict_treatment_t)
        
if __name__ == '__main__':
    main()