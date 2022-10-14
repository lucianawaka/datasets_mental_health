import streamlit as st
import pickle

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
        model = pickle.load(open("model/RandomForestClassifier_v1.pkl"))
        meus_dados = [[31,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,4,0]]
        predict_treatment = model.predict(meus_dados)
        predict_treatment_t = type(predict_treatment)
        st.markdown(f"""Previsão:{predict_treatment} 
                    Tipo: {predict_treatment_t}
                    """)
        
if __name__ == '__main__':
    main()