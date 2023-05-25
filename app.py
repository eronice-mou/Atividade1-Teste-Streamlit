import streamlit as st
import pandas as pd
import numpy as np

#######################################
nome = st.text_input('Nome de usuário')
#st.write('O nome é:', nome)

nome = st.text_input('Email')
#st.write('O nome é:', nome)


########################################
agree = st.checkbox('Manter conectado')

if agree:
    st.write('Great!')


menu = st.sidebar.header("Menu")

var_grafico = st.sidebar.selectbox(
    "Visualização de gráficos",
    ("Selecionar", "Gráfico 1", "Gráfico 2", "Gráfico 3")
)

if var_grafico == 'Selecionar':
    st.text('')

if var_grafico == "Gráfico 1":
    df = pd.DataFrame(
    np.random.rand(10, 1),
    columns=['Visualização de gráfico'])
    st.markdown('''### Visualização de gráfico ''')
    st.line_chart(df)

    st.write('Lorem ipsum dolor sit amet. Et error amet et distinctio assumenda et quos adipisci sit rerum cumque et illo animi. Et dolores iusto rem illum consectetur ut voluptate magni et quae velit non nulla quaerat et magnam provident. Aut corporis alias eum cupiditate dolor ex omnis velit non necessitatibus magni 33 excepturi consectetur et ratione Quis. Ad aliquid beatae non nihil quas ea repudiandae necessitatibus?')

    if st.button('Clique aqui'):
        st.success('Gráfico gerado com sucesso')
    else:
        st.warning('Não deixe de concluir esta ação', icon="⚠️")

    


elif var_grafico == "Gráfico 2":
    df = pd.DataFrame(
    np.random.rand(10, 1),
    columns=['Visualização de gráfico'])
    st.markdown('''### Visualização de gráfico ''')
    st.bar_chart(df)

    st.write('Qui internos recusandae ut quae aliquam sit expedita nobis. Ea expedita tempora id dolor pariatur non accusantium harum. Ut sunt quia in beatae vero sed commodi saepe eum dicta culpa. Et architecto minus et facilis pariatur est iste doloremque.')

    options = st.multiselect(
        'Selecionar opções',
        ['Opção 1', 'Opção 2', 'Opção 3', 'Opção 4'])

    #st.write('Você selecionou:', options)




elif var_grafico == "Gráfico 3":
    df = pd.DataFrame(
    np.random.rand(10, 1),
    columns=['Taxa de crescimento'])
    st.markdown('''### Visualização de gráfico ''')
    st.table(df)

    st.write('Ex ducimus ducimus vel reiciendis voluptatem est culpa officiis aut vitae quisquam qui rerum deserunt non voluptate officia non expedita error. Aut veritatis temporibus hic autem unde et earum porro est libero voluptatem. Sed eligendi perspiciatis qui neque quod in soluta quas sit nobis veniam et impedit rerum in ipsam suscipit et obcaecati recusandae.')

    genre = st.radio(
    "Selecionar uma opção:",
    ('Opção 1', 'Opção 2', 'Opção 3'))

    if genre == 'Opção 1':
        if st.button('Clique aqui'):
            st.warning('Esta é uma mensagem de atenção', icon="⚠️")
        else:
            st.write('Botão não clicado')
        

    elif genre == 'Opção 2':
        if st.button('Exibir mensagem'):
            st.info('Esta é uma mensagem de informação', icon="ℹ️")
        else:
            st.write('Botão não clicado')
        


    elif genre == 'Opção 3':
        if st.button('Concluir'):
            st.error('Esta é uma messagem de erro', icon="🚨")
        else:
            st.write('Botão não clicado')




###########################################################################
var_dashboard = st.sidebar.selectbox(
    "Dashboard",
    ("Selecionar", "Dashboard 1", "Dashboard 2", "Dashboard 3")
)

#Dashboard 1
if var_dashboard == 'Selecionar':
    st.text(' ')

if var_dashboard == 'Dashboard 1':


    with st.container():
        st.write("Dashboard 1")
    st.bar_chart(np.random.randn(50, 3))

    st.write("Visualização da Dashboard 1")


#Dashboard 2
if var_dashboard == 'Dashboard 2':

    st.text('Você selecionou Dashboard 2')


#Dashboard 3
if var_dashboard == 'Dashboard 3':

    st.text('Você selecionou Dashboard 3')





##################################################################
var_aplicacao = st.sidebar.selectbox(
    "Configurações",
    ("Selecionar", "Aplicação", "Tabelas", "Gráficos", "Usuários")
)

if var_aplicacao == 'Selecionar':
    st.text(' ')

if var_aplicacao == 'Aplicação':
    st.text('Você selecionou Aplicação')

if var_aplicacao == 'Tabelas':
    st.text('Você selecionou Tabelas')

if var_aplicacao == 'Gráficos':
    st.text('Você selecioou Gráficos')

if var_aplicacao == 'Usuários':
    st.text('Você selecionou Usuários')
















