import pandas as pd
import streamlit as st


def Dividendos():

    indices = ['10 Maiores Pagodores de Dividendos','Previsão de futuros Dividendos']
    st.sidebar.radio('Escolha', indices)
    st.title('10 Maiores Pagodores de Dividendos')
    st.markdown('-----')
    st.subheader('Essas são as 10 Empresas com maior Dividend Yield nos ultimos 14 anos.')

div ={
    'CMIN3':'12.72%',
    'BRAP4':'11.20%',
    'TAEE11':'8.63%',
    'CMIG4':'8.54%',
    'PETR4':'8.36%',
    'PETR3':'7.53%',
    'VIVT3'	:'7.47%',
    'BBSE3'	:'6.88%',
    'ELET6'	:'6.67%',
    'BBAS3':'6.34%'
    }

st.write(div)

def Previsão():
    st.title('Previsão para os proximos DIVIDENDOS')
    st.subheader('Previsão para os proximos pagementos de dividendos para as 10 maiores empresas'
                 'pagodores de dividendo ')
    



def main():
    st.title('Mapa de Dividenos')
    st.markdown('-----')
    #st.sidebar.image('brasil.jpg',caption='Mapa Econômico', width=200)

    indices = ['10 Maiores Pagodores de Dividendos','Previsão de futuros Dividendos']
    st.sidebar.radio('Escolha', indices)
    

    if indices == 'Dividendos':
        Dividendos()

    if indices == 'Previsão':
        Previsão()


main()    