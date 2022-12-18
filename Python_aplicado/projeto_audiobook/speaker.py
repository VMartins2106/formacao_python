import pyttsx3
import pdfplumber

# Inicializando a engine de NLP
engine = pyttsx3.init()

# Lendo o arquivo PDF
pdf = pdfplumber.open("O elefante em apuros.pdf")

# Gerando lista de páginas --DESEJADAS--
paginas = pdf.pages[2:-3]

# Extraindo texto para apenas uma string
texto_livro = ''
for pagina in paginas:
    texto_livro += pagina.extract_text()

# Tratando a string, para ler como queremos
texto_final = texto_livro.replace('.', '. ').replace(',',', ')

engine.save_to_file(texto_final, "audiobook.mp3")
engine.runAndWait()