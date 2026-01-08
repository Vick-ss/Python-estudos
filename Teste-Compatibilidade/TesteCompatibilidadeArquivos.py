from PyPDF2 import PdfReader
from sentence_transformers import SentenceTransformer, util

def extrair_texto(pdf_path):
    reader = PdfReader(pdf_path)
    texto = ""
    for page in reader.pages:
        texto += page.extract_text() + "\n"
    return texto.strip()

def calcular_compatibilidade(texto1, texto2):
    modelo = SentenceTransformer("all-MiniLM-L6-v2")
    emb1 = modelo.encode(texto1, convert_to_tensor=True)
    emb2 = modelo.encode(texto2, convert_to_tensor=True)

    score = util.cos_sim(emb1, emb2).item()
    return score

texto1 = extrair_texto("arquivos/Ux-aula01.pdf") 
texto2 = extrair_texto("arquivos/Ux-aula02.pdf")

compatibilidade = calcular_compatibilidade(texto1, texto2)
print(f"Compatibilidade: {compatibilidade:.2f}")

