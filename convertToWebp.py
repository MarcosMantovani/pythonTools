import os
import shutil
from PIL import Image

# Diretório onde as imagens originais estão localizadas
diretorio_entrada = "input"

# Diretório onde as imagens convertidas serão salvas
diretorio_saida = "output"

# Formatos de imagem suportados
formatos_suportados = ('.png', '.jpg', '.jpeg', '.gif', '.bmp')

# Função para limpar o diretório de saída
def limpar_diretorio_saida():
    if os.path.exists(diretorio_saida) and os.listdir(diretorio_saida):
        resposta = input(f"Existem arquivos no diretório '{diretorio_saida}'. Deseja excluí-los e continuar? (s/n): ").lower()
        if resposta == 's':
            shutil.rmtree(diretorio_saida)
            os.makedirs(diretorio_saida)
            print(f"Diretório '{diretorio_saida}' limpo.")
        else:
            print("Operação cancelada.")
            exit()
    elif not os.path.exists(diretorio_saida):
        os.makedirs(diretorio_saida)

# Limpa o diretório de saída
limpar_diretorio_saida()

# Contador para nomear os arquivos
contador = 0

# Percorre todos os arquivos no diretório de entrada
for arquivo in os.listdir(diretorio_entrada):
    if arquivo.lower().endswith(formatos_suportados):
        caminho_completo = os.path.join(diretorio_entrada, arquivo)
        
        # Abre a imagem
        with Image.open(caminho_completo) as img:
            # Cria o nome do novo arquivo com 5 algarismos
            novo_nome = f"{contador:05d}.webp"
            novo_caminho = os.path.join(diretorio_saida, novo_nome)
            
            # Converte e salva a imagem em formato WebP no diretório de saída
            img.save(novo_caminho, 'webp')
        
        print(f"Convertido: {arquivo} -> {novo_nome}")
        contador += 1

print(f"Conversão concluída! {contador} imagens foram convertidas.")
