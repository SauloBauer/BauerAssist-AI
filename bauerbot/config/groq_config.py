import os

api_key = 'sua_chave_aqui'  # Substitua por variável de ambiente se quiser mais segurança
os.environ['GROQ_API_KEY'] = api_key

model = 'llama-3.1-70b-versatile'