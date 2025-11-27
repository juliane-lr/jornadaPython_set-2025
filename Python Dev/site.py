# titulo
# input do chat
# a cada mensagem enviada:
    # mostrar a mensagem que o usuario enviou
    # gerar uma resposta com IA
    # mostrar a resposta da IA

# aplicação web: streamlit (frontend e backend)
    # pip install streamlit


import streamlit as st
from openai import OpenAI

modelo = OpenAI(api_key = "xxx") # modelo de inteligência da Open AI 

st.write("### ChatBot com IA") # formato markdown 

# session_state = memória do streamlit

if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] = []  # lista para armazenar as mensagens do chat, começa vazia

# para adicionar uma mensagem na lista:
# st.session_state["lista_mensagens"].append(mensagem)

# exibir o histórico de mensagens:
for mensagem in st.session_state["lista_mensagens"]:
    quem = mensagem["role"]  # user ou assistant
    texto = mensagem["content"]  # conteúdo da mensagem
    st.chat_message(quem).write(texto)


mensagem_usuario = st.chat_input("Digite sua mensagem:")  # input do chat

if mensagem_usuario:
    # user -> ser humano
    # assistant -> IA
    st.chat_message("user").write(mensagem_usuario)  # mostrar a mensagem que o usuario enviou  
    mensagem = {"role": "user", "content": mensagem_usuario}
    st.session_state["lista_mensagens"].append(mensagem)  # adicionar mensagem do usuario na lista

    # resposta da IA
    resposta_modelo = modelo.chat.completions.create(
        messages = st.session_state["lista_mensagens"],
        model = "gpt-3.5-turbo" # modelo de IA usado
    )

    print(resposta_modelo)
    resposta_ia = "Você quis dizer: " + mensagem_usuario 

    # exibir a resposta da IA
    st.chat_message("assistant").write(resposta_ia)  # mostrar a resposta da IA    
    mensagem_ia = {"role": "assistant", "content": resposta_ia}
    st.session_state["lista_mensagens"].append(mensagem_ia)  # adicionar
