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
    st.markdown(f"""
                ### Target: treatment: Have you sought treatment for a mental health condition?
                <ol>
                'Age'
                'Gender'
                <li>self_employed: Are you self-employed?</li>
                <li>family_history: Do you have a family history of mental illness?</li>
                <li>remote_work: Do you work remotely (outside of an office) at least 50% of the time?</li>
                <li>tech_company: Is your employer primarily a tech company/organization?</li>
                <li>benefits: Does your employer provide mental health benefits?</li>
                <li>care_options: Do you know the options for mental health care your employer provides?</li>
                <li>wellness_program: Has your employer ever discussed mental health as part of an employee wellness program?</li>
                <li>seek_help: Does your employer provide resources to learn more about mental health issues and how to seek help?</li>
                <li>anonymity: Is your anonymity protected if you choose to take advantage of mental health or substance abuse treatment resources?</li>
                'mental_health_consequence'
                'phys_health_consequence'
                'coworkers'
                'supervisor'
                'mental_health_interview'
                'phys_health_interview'
                'mental_vs_physical'
                'obs_consequence'
                'work_interfere_num'
                'no_employees_num'
                <li>leave: How easy is it for you to take medical leave for a mental health condition?</li>
                </ol>              
                
                """)

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