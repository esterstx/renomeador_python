📝 Renomeador de Arquivos em Lote — Python

Este projeto é um script simples e direto feito para renomear vários arquivos de uma pasta automaticamente, adicionando um prefixo personalizado apenas aos arquivos com a extensão desejada.
É perfeito para quem precisa organizar documentos, relatórios, logs ou qualquer conjunto de arquivos rapidamente.

🚀 O que este script faz?

Percorre todos os arquivos de uma pasta.
Verifica quais possuem a extensão que você escolher (por padrão, .txt).
Adiciona um prefixo (por padrão, OK_) ao nome desses arquivos.
Evita sobrescrever arquivos: se o nome novo já existir, ele pula com segurança.
Exibe no terminal quais arquivos foram renomeados e quais foram ignorados.

📂 Como usar

Escolha a pasta onde estão os arquivos que deseja renomear.
No código, substitua:

pasta = r"coloque_aqui_o_caminho_da_pasta"


Defina a extensão dos arquivos que você quer renomear:

extensao_desejada = '.txt'

Escolha o prefixo que será adicionado:
prefixo = 'OK_'


🤝 Contribuições

Fique à vontade para melhorar o código, adicionar novas funcionalidades ou abrir issues.
Toda sugestão é bem-vinda! 🚀
