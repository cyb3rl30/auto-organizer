import os
import shutil

print("=== ORGANIZADOR LOCAL SEGURO ===")

# Pasta local (cada usuário usa a própria)
BASE_DIR = os.path.join(os.path.expanduser("~"), "Downloads")

# Tipos permitidos (somente seguros)
TIPOS = {
    "Imagens": [".png", ".jpg", ".jpeg"],
    "Videos": [".mp4", ".mkv"],
    "Programas": [".exe", ".msi"],
    "Compactados": [".zip", ".rar"]
}

# Palavras sensíveis (ignorar)
PROTEGIDOS = [
    "senha", "password", "backup",
    "recovery", "token", "key",
    "secret", "auth"
]

def seguro(nome):
    nome = nome.lower()
    return not any(p in nome for p in PROTEGIDOS)

def listar():
    print("\n🔎 SIMULAÇÃO (nada será movido):\n")
    acoes = []

    for arquivo in os.listdir(BASE_DIR):
        caminho = os.path.join(BASE_DIR, arquivo)

        if not os.path.isfile(caminho):
            continue

        # ignora arquivos sensíveis
        if not seguro(arquivo):
            print(f"🔒 Ignorado: {arquivo}")
            continue

        for pasta, extensoes in TIPOS.items():
            if any(arquivo.lower().endswith(ext) for ext in extensoes):
                print(f"{arquivo} → {pasta}")
                acoes.append((arquivo, pasta))
                break

    return acoes

def mover(acoes):
    for arquivo, pasta in acoes:
        origem = os.path.join(BASE_DIR, arquivo)
        destino_pasta = os.path.join(BASE_DIR, pasta)

        if not os.path.exists(destino_pasta):
            os.makedirs(destino_pasta)

        destino = os.path.join(destino_pasta, arquivo)
        shutil.move(origem, destino)

        print(f"✅ Movido: {arquivo} → {pasta}")

def main():
    acoes = listar()

    if not acoes:
        print("\nNada para organizar.")
        return

    confirm = input("\nConfirmar organização? (s/n): ").lower()

    if confirm == "s":
        mover(acoes)
        print("\n✔ Organização concluída com segurança.")
    else:
        print("\n❌ Cancelado.")

if __name__ == "__main__":
    main()
