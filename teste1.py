'''
#----CAIXA DE SELEÇÃO-----
import streamlit as st
import numpy as np
import pandas as pd

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data



#-----CAIXA DE SELEÇÃO PARA OÇÕES
import streamlit as st
import pandas as pd

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option



#-----WIDGET - BARRA LATERAL---------
import streamlit as st

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)


# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

'''

#st.table(df)   #----Gráfico de tabela
#st.dataframe(df)   #----Gráfico de tabela
#st.line_chart(df)  #---Gráfico de linhas
#st.bar_chart(df)   #----Gráfico de barras









import streamlit as st

st.title('Olá usuário!')

st.markdown('''Olá esse é um título em markdown''')

st.header('Este é um texto header')

st.subheader('Este é um texto subheader')

st.success('Esta é uma mensagem de sucesso!')



st.info('Esta é uma mensagem de informação', icon="ℹ️")

st.warning('Esta é uma mensagem de atenção', icon="⚠️")

st.error('Esta é uma messagem de erro', icon="🚨")



# função radio

genre = st.radio(
    "Qual seu gênero de filme favorito:",
    ('Comédia', 'Drama', 'Documentário'))

if genre == 'Comédia':
    st.write('Você selecionou Comédia.')
else:
    st.write("Você não selecionou comédia.")
#######



st.text('Esta é uma mensagem de texto!')




# função multi select

options = st.multiselect(
    'Selecione sua cor favorita',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red'])

st.write('Você selecionou:', options)
    
########



# função botão
if st.button('Clique aqui'):
    st.write('Você clicou')
else:
    st.write('Botão não clicado')
################



# Entrada de texto
title = st.text_input('Título do filme', 'A vida de Brian')
st.write('O título do fime atual é:', title)





