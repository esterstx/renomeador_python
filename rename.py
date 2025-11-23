import os

# Defina o caminho da pasta onde estão os arquivos
pasta = r"coloque_aqui_o_caminho_da_pasta"

# Defina a extensão desejada
extensao_desejada = '.txt'

# Defina o prefixo desejado
prefixo = 'OK_'

arquivos = os.listdir(pasta)

for arquivo in arquivos:
    caminho_completo = os.path.join(pasta, arquivo)
   
    if os.path.isfile(caminho_completo) and arquivo.endswith(extensao_desejada):  # Só renomeia se for arquivo e tiver a extensão desejada
        novo_nome = prefixo + arquivo
        novo_caminho = os.path.join(pasta, novo_nome)
        # Antes de renomear, opcional: checar se novo arquivo já existe

        if not os.path.exists(novo_caminho):
            os.rename(caminho_completo, novo_caminho)
            print(f'Renomeado: {arquivo} -> {novo_nome}')

        else:
            print(f'PULADO: {novo_nome} já existe')
