from bot.chat import resposta_bot
from bot.loaders import carrega_site, carrega_pdf, carrega_youtube

print('Bem-vindo ao BauerBot')

texto_selecao = '''Digite 1 se você quiser conversar com um site
Digite 2 se você quiser conversar com um pdf
Digite 3 se você quiser conversar com um vídeo de youtube '''

while True:
    selecao = input(texto_selecao)
    if selecao == '1':
        documento = carrega_site()
        break
    if selecao == '2':
        documento = carrega_pdf()
        break
    if selecao == '3':
        documento = carrega_youtube()
        break
    print('Digite um valor entre 1 e 3')

mensagens = []
while True:
    pergunta = input('Usuario: ')
    if pergunta.lower() == 'x':
        break
    mensagens.append(('user', pergunta))
    resposta = resposta_bot(mensagens, documento)
    mensagens.append(('assistant', resposta))
    print(f'Bot: {resposta}')

print('Muito obrigado por usar o BauerBot')