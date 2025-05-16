from langchain_community.document_loaders import WebBaseLoader, YoutubeLoader, PyPDFLoader

def carrega_site():
    url_site = input('Digite a url do site: ')
    loader = WebBaseLoader(url_site, headers={"User-Agent": "asimobot/1.0"})
    lista_documentos = loader.load()
    return ''.join([doc.page_content for doc in lista_documentos])

def carrega_pdf():
    caminho = '/content/drive/MyDrive/curso_ia_python/arquivos/RoteiroViagemEgito.pdf'
    loader = PyPDFLoader(caminho)
    lista_documentos = loader.load()
    return ''.join([doc.page_content for doc in lista_documentos])

def carrega_youtube():
    url_youtube = input('Digite a url do vídeo: ')
    loader = YoutubeLoader.from_youtube_url(url_youtube, language=['pt'])
    lista_documentos = loader.load()
    return ''.join([doc.page_content for doc in lista_documentos])