import streamlit as st
import pickle
import numpy as np
import joblib

def main():
    options = ['Homepage','Previsão']
    page_option = st.sidebar.selectbox('Options', options)
    
    if page_option == 'Homepage':
        homepage()
    elif page_option == 'Previsão':
        previsao()


# Home page

def homepage():
    st.markdown(f"""
                #### Nosso conjunto de dados é composto da saúde mental e frequência de distúrbios de saúde mental no local de trabalho de tecnologia.

                ### Pergunta a ser respondida:
                A pessoa faria um tratamento para saúde mental?
                - Quais são as características mais influentes?
                - Neste conjunto de dados é possível responder se uma pessoa irá procurar um tratamento ou não?

                #### O conjunto de dados:
                Tamanho: 1259 linhas e 27 colunas

                Sim: 50.595711
                Não: 49.404289

                #### Conjunto de dados Saúde Mental em TI
                "Este conjunto de dados é de uma pesquisa de 2014 que mede as atitudes em relação à saúde mental e a frequência de distúrbios de saúde mental no local de trabalho de tecnologia." (De Kanggle)

                Link: [Fonte de dados do Kanggle](https://www.kaggle.com/datasets/osmi/mental-health-in-tech-survey?resource=download&select=survey.csv)

                Versão 1.0 - 15/12/2022          
                
                """)
    
def previsao():
    Modelo = joblib.load('model/RandomForestClassifier_v1.pkl')

    st.title("Previsão se a pessoa iria fazer um tratamento de saúde mental:")
    st.markdown("Responda o questionário e envie os dados para realizar a previsão.")
    age = st.slider('Idade',14,95)
    gender = st.radio('Sexo',['Feminino','Masculino','Outro'])
    self_employed = st.radio('Você é autônomo?',['Sim','Não','Prefiro não informar'])
    family_history = st.radio('Você tem histórico familiar de doença mental?',['Sim','Não'])  
    remote_work =st.radio('Você trabalha remotamente (fora de um escritório) pelo menos 50% do tempo?',['Sim','Não'])
    tech_company =st.radio('Seu empregador é uma empresa/organização de tecnologia?',['Sim','Não'])
    benefits =st.radio('Seu empregador oferece benefícios de saúde mental?',['Sim','Não','Não sabe informar'])   
    care_options =st.radio('Você conhece as opções de cuidados de saúde mental que seu empregador oferece?',['Sim','Não','Não sabe informar'])
    wellness_program =st.radio('Seu empregador já discutiu a saúde mental como parte de um programa de bem-estar dos funcionários?',['Sim','Não','Não sabe informar'])
    seek_help =st.radio('Seu empregador fornece recursos para aprender mais sobre problemas de saúde mental e como procurar ajuda?',['Sim','Não','Não sabe informar'])
    anonymity =st.radio('Seu anonimato está protegido se você optar por tirar proveito dos recursos de tratamento de saúde mental ou abuso de substâncias?',['Sim','Não','Não sabe informar'])
    mental_health_consequence =st.radio('Você acha que discutir um problema de saúde mental com seu empregador teria consequências negativas?',['Sim','Não','Talvez'])
    physhealth_consequence =st.radio('Você acha que discutir um problema de saúde física com seu empregador teria consequências negativas?',['Sim','Não','Talvez'])  
    coworkers =st.radio('Você estaria disposto a discutir um problema de saúde mental com seus colegas de trabalho?',['Sim','Não','Alguns deles'])
    supervisor =st.radio('Você estaria disposto a discutir um problema de saúde mental com seu(s) supervisor(es) direto(s)?',['Sim','Não','Alguns deles'])  
    mental_health_interview =st.radio('Você falaria sobre um problema de saúde mental com um potencial empregador em uma entrevista?',['Sim','Não','Talvez'])
    physhealth_interview =st.radio('Você falaria sobre um problema de saúde física com um potencial empregador em uma entrevista?',['Sim','Não','Talvez'])  
    mental_vs_physical =st.radio('Você acha que seu empregador leva a saúde mental tão a sério quanto a saúde física?',['Sim','Não','Não sabe informar'])
    obs_consequence =st.radio('Você já ouviu falar ou observou consequências negativas para colegas de trabalho com problemas de saúde mental em seu local de trabalho?',['Sim','Não'])
    work_interfere =st.radio('Se você tem uma condição de saúde mental, você sente que isso interfere no seu trabalho?',['Frequentemente','Raramente', 'Nunca', 'Algumas vezes', 'Não sabe informar'])
    no_employees =st.radio('Quantos funcionários sua empresa ou organização tem?',['1-5','6-25','26-100','100-500','500-1000','Mais que 1000'])
    leave =st.radio('Quão fácil é para você tirar licença médica por uma condição de saúde mental?',['Dificilmente', 'Facilmente','Um pouco fácil','Um pouco difícil','Não sabe informar'])
    
    dict_gender={'Feminino':0, 'Masculino':1, 'Outro':2}
    dict_self_employed={'Sim':1, 'Não':0,'Prefiro não informar':2}
    dict_family_history={'Sim':1,'Não':0}
    dict_remote_work={'Sim':1,'Não':0}
    dict_tech_company={'Sim':1,'Não':0}
    dict_benefits={'Sim':1,'Não':0,'Não sabe informar':2}
    dict_care_options={'Sim':1,'Não':0,'Não sabe informar':2}  
    dict_wellness_program={'Sim':1,'Não':0,'Não sabe informar':2}
    dict_seek_help={'Sim':1,'Não':0,'Não sabe informar':2}
    dict_anonymity={'Sim':1,'Não':0,'Não sabe informar':2}
    dict_mental_health_consequence={'Sim':1,'Não':0,'Talvez':2}
    dict_physhealth_consequence={'Sim':1,'Não':0,'Talvez':2}
    dict_coworkers={'Sim':1,'Não':0,'Alguns deles':2}
    dict_supervisor={'Sim':1,'Não':0,'Alguns deles':2}
    dict_mental_health_interview={'Sim':1,'Não':0,'Talvez':2}
    dict_physhealth_interview={'Sim':1,'Não':0,'Talvez':2}
    dict_mental_vs_physical={'Sim':1,'Não':0,'Não sabe informar':2}
    dict_obs_consequence={'Sim':1,'Não':0}
    dict_work_interfere={'Frequentemente':0, 'Raramente':1, 'Nunca':2, 'Algumas vezes':3, 'Não sabe informar':4}
    dict_no_employees={'1-5':0,'6-25':1,'26-100':2,'100-500':3,'500-1000':4,'Mais que 1000':5}
    dict_leave={'Dificilmente':3, 'Facilmente':4,'Um pouco fácil':0,'Um pouco difícil':2,'Não sabe informar':1}
   
   
   
   
    meus_dados = [[
                    age,  dict_gender[gender],  dict_self_employed[self_employed],  dict_family_history[family_history], \
                    dict_remote_work[remote_work],  dict_tech_company[tech_company],  dict_benefits[benefits], \
                    dict_care_options[care_options], dict_wellness_program[wellness_program],  dict_seek_help[seek_help], dict_anonymity[anonymity],  \
                    dict_mental_health_consequence[mental_health_consequence], dict_physhealth_consequence[physhealth_consequence],  dict_coworkers[coworkers],  \
                    dict_supervisor[supervisor], dict_mental_health_interview[mental_health_interview], dict_physhealth_interview[physhealth_interview],  \
                    dict_mental_vs_physical[mental_vs_physical],  dict_obs_consequence[obs_consequence],\
                    dict_work_interfere[work_interfere],  dict_no_employees[no_employees],  dict_leave[leave]
                ]]
    
    if st.button("Enviar"):
        meus_dados_n = np.array(meus_dados).reshape(1, -1)

        predict_treatment = Modelo.predict(meus_dados_n).astype(int)
        dict_result = {0:'NÃO IRIA',1:'IRIA'}
        predict_treatment_t = dict_result[predict_treatment[0]]
        print(predict_treatment)
        st.markdown(f"""A pessoa {predict_treatment_t} submeter-se a um tratamento de saúde mental""")
        
if __name__ == '__main__':
    main()