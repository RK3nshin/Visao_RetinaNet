import os

# Lista de nomes de arquivos a serem procurados
nomes_arquivos = [
    "Image03793",
    "Image01149",
    "Image03281",
    "Image02001",
    "Image02089",
    "Image00801",
    "Image00985",
    "Image02073",
    "Image01409",
    "Image00609",
    "Image01921",
    "Image00993",
    "Image03753",
    "Image00625",
    "Image01101",
    "Image00457",
    "Image01193",
    "Image02129",
    "Image00905",
    "Image01125",
    "Image02561",
    "Image01053",
    "Image00841",
    "Image00601",
    "Image01145",
    "Image02145",
    "Image01065",
    "Image02537",
    "Image00681",
    "Image03161",
    "Image01369",
    "Image01077",
    "Image00473",
    "Image00529",
    "Image02105",
    "Image00665",
    "Image00561",
    "Image03121",
    "Image01049",
    "Image02041",
    "Image01169",
    "Image00465",
    "Image03513",
    "Image01241",
    "Image00777",
    "Image00545",
    "Image01161",
    "Image00969",
    "Image02033",
    "Image01129",
    "Image01089",
    "Image01121",
    "Image00809",
    "Image01249",
    "Image00769",
    "Image01069",
    "Image01141",
    "Image00553",
    "Image01073",
    "Image00889",
    "Image01153",
    "Image01185",
    "Image01529",
    "Image01393",
    "Image00785",
    "Image01045",
    "Image01017",
    "Image00793",
    "Image00593",
    "Image01041 (1)",
    "Image01057",
    "Image00881"
]

extensoes = ['.xml']
# Diretório de origem
diretorio_origem = 'Annotations'

# Função para procurar os nomes de arquivos nos diretórios
# Função para procurar arquivos com o mesmo nome e diferentes extensões
def procurar_arquivos(diretorio, nome, extensoes):
    arquivos_faltando = []
    for extensao in extensoes:
        arquivo = f"{nome}{extensao}"
        if not any(arquivo in files for root, dirs, files in os.walk(diretorio)):
            arquivos_faltando.append(arquivo)

    return arquivos_faltando

# Procura arquivos com o mesmo nome e diferentes extensões para cada nome na lista
for nome_arquivo in nomes_arquivos:
    arquivos_faltando = procurar_arquivos(diretorio_origem, nome_arquivo, extensoes)

    # Exibe os arquivos que estão faltando para cada nome
    if arquivos_faltando:
        print(f"\nArquivos faltando para {nome_arquivo}:")
        for arquivo in arquivos_faltando:
            print(arquivo)