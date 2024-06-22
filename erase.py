import os
import glob
from pathlib import Path

ROOT_FOLDER = /G/Meu Drive/Modulo6/python

def clean_latex_directory(directory):
    # Extensões comuns de arquivos auxiliares do LaTeX
    extensions = [
        "*.aux", "*.log", "*.toc", "*.out", "*.bbl", "*.blg", "*.nav",
        "*.snm", "*.fls", "*.fdb_latexmk", "*.synctex.gz", "*.vrb",
        "*.lof", "*.lot", "*.lol"
    ]
    
    # Percorre todas as extensões e remove os arquivos correspondentes
    for ext in extensions:
        for file in glob.glob(os.path.join(directory, ext)):
            try:
                os.remove(file)
                print(f"Removed: {file}")
            except OSError as e:
                print(f"Error removing {file}: {e}")

if __name__ == "__main__":
     latex_directory = ROOT_FOLDER
        
     # Chama a função para limpar o diretório
     clean_latex_directory(latex_directory)
