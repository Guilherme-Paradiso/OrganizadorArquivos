#PROJETO PARA ORGANIZAR ARQUIVOS AUTOMATICAMENTE
import os #manipular os arquivos do computador
from tkinter.filedialog import askdirectory 

caminho = askdirectory (title = "Selecione uma Pasta") #Seleciona a pasta do computador
print (caminho)

listaArquivos = os.listdir(caminho)

locais = { #Dicionário de arquivos (Para onde vai cada arquivo, de acordo com sua extensão)
    "imagens": [".png", ".jpg", ".jpeg"],
    "planilhas": [".xlsx"],
    "pdfs": [".pdf"],
    "documentos": [".docx", ".txt"],
    "csv": [".csv"],
    "curso": [".html", ".css", ".py", ".java", ".asta", ".json"],
    "outros": [".zip", ".exe", ".rar"]
}

for arquivo in listaArquivos:
    nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
    for pasta in locais:
        if extensao in locais[pasta]:
            if not os.path.exists(f"{caminho}/{pasta}"):
                os.mkdir(f"{caminho}/{pasta}")
            os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")