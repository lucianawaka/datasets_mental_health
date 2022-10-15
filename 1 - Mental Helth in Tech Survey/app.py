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
                
                - Age: Idade.
                - Gender: Gênero.
                - self_employed: Are you self-employed?
                - family_history: Do you have a family history of mental illness?
                - remote_work: Do you work remotely (outside of an office) at least 50% of the time?
                - tech_company: Is your employer primarily a tech company/organization?
                - benefits: Does your employer provide mental health benefits?
                - care_options: Do you know the options for mental health care your employer provides?
                - wellness_program: Has your employer ever discussed mental health as part of an employee wellness program?
                - seek_help: Does your employer provide resources to learn more about mental health issues and how to seek help?
                - anonymity: Is your anonymity protected if you choose to take advantage of mental health or substance abuse treatment resources?
                - mental health consequence: Do you think that discussing a mental health issue with your employer would have negative consequences?
                - physhealthconsequence: Do you think that discussing a physical health issue with your employer would have negative consequences?
                - coworkers: Would you be willing to discuss a mental health issue with your coworkers?
                - supervisor: Would you be willing to discuss a mental health issue with your direct supervisor(s)?
                - mental health interview: Would you bring up a mental health issue with a potential employer in an interview?
                - physhealth interview: Would you bring up a physical health issue with a potential employer in an interview?
                - mental vs physical: Do you feel that your employer takes mental health as seriously as physical health?
                - obs_consequence: Have you heard of or observed negative consequences for coworkers with mental health conditions in your workplace?
                - work_interfere: If you have a mental health condition, do you feel that it interferes with your work?
                - no_employees: How many employees does your company or organization have?
                - leave: How easy is it for you to take medical leave for a mental health condition?             
                
                """)

def consulta():
    pass

def previsao():
    Modelo = joblib.load('model/RandomForestClassifier_v1.pkl')

    st.title("Previsão se a pessoa vai procurar tratamento para uma condição de saúde mental:")
    age = st.slider('Idade',14,95)
    gender = st.radio('Sexo',['Feminino','Masculino','Outro'])
    self_employed = st.radio('Você é autônomo?',['Sim','Não'])
    family_history = st.radio('Você tem histórico familiar de doença mental?',['Sim','Não'])
        
    meus_dados = [[age,  gender,  self_employed,  family_history,  0,  1,  1,  1,  0,  0,  1,  0,  0,  2,  1,  0,
    0,  2,  0,  3,  3,  0]]
    meus_dados_n = np.array(meus_dados).reshape(1, -1)

    predict_treatment = Modelo.predict(meus_dados_n).astype(int)
    dict_result = {0:'Não',1:'Sim'}
    predict_treatment_t = dict_result[predict_treatment[0]]
    st.markdown(f"""{predict_treatment_t}""")
        
if __name__ == '__main__':
    main()