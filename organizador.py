import os
import shutil

# Caminho da pasta Downloads (automático)
pasta_downloads = os.path.join(os.path.expanduser("~"), "Downloads")

# Tipos de arquivos
tipos = {
    "Imagens": [".png", ".jpg", ".jpeg", ".gif"],
    "Documentos": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv"],
    "Programas": [".exe", ".msi"],
    "Compactados": [".zip", ".rar"]
}

def organizar():
    for arquivo in os.listdir(pasta_downloads):
        caminho_arquivo = os.path.join(pasta_downloads, arquivo)

        if os.path.isfile(caminho_arquivo):
            for pasta, extensoes in tipos.items():
                if any(arquivo.lower().endswith(ext) for ext in extensoes):
                    pasta_destino = os.path.join(pasta_downloads, pasta)

                    if not os.path.exists(pasta_destino):
                        os.makedirs(pasta_destino)

                    shutil.move(caminho_arquivo, os.path.join(pasta_destino, arquivo))
                    print(f"Movido: {arquivo} → {pasta}")
                    break

if __name__ == "__main__":
    organizar()
