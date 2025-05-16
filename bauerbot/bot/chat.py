from langchain.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from config.groq_config import api_key, model

chat = ChatGroq(model=model)

def resposta_bot(mensagens, documento):
    mensagem_system = '''Você é um assistente amigável chamado BauerBot.
    Você utiliza as seguintes informações para formular as suas respostas: {informacoes}'''
    mensagens_modelo = [('system', mensagem_system)]
    mensagens_modelo += mensagens
    template = ChatPromptTemplate.from_messages(mensagens_modelo)
    chain = template | chat
    return chain.invoke({'informacoes': documento}).content