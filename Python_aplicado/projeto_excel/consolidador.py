import pandas as pd
import os
import datetime

data = datetime.datetime.now()

# CRIANDO UM DATAFRAME VAZIO COM A ESTRUTURA FINAL DO CONSOLIDADO
colunas = [
    'Segmento',
    'País',
    'Produto',
    'Qtde de Unidades Vendidas',
    'Preço Unitário',
    'Valor Total',
    'Desconto',
    'Valor Total c/ Desconto',
    'Custo Total',
    'Lucro',
    'Data',
    'Mês',
    'Ano'
]
consolidado = pd.DataFrame(columns=colunas)

# BUSCA O NOME DOS ARQUIVOS A SEREM CONSOLIDADOS
arquivos = os.listdir(r"C:\Users\Win10\Desktop\python_empowerdata\Python_aplicado\projeto_excel\planilhas")

# REALIZA A CONSOLIDAÇÃO DOS ARQUIVOS .XLSX
for arquivo in arquivos:

    if arquivo.endswith('.xlsx'):
        dados_arquivo = arquivo.split('-')
        segmento = dados_arquivo[0]
        pais = dados_arquivo[1].replace(".xlsx", "")
        try:
            df = pd.read_excel(f'planilhas\\{arquivo}')
            df.insert(0,"Segmento", segmento)
            df.insert(1,"País", pais)
            consolidado = consolidado.append(df)
        except:
            with open('log_erros.txt','w') as file:
                file.write(f'Erro ao tentar consolidar o arquivo "{arquivo}"')
    else: 
        with open('log_erros.txt','w') as file:
                file.write(f'O arquivo "{arquivo}" não é um arquivo Excel Válido!')

# FORMATA A COLUNA DATA
consolidado["Data"] = consolidado["Data"].dt.strftime("%d/%m/%Y")

# ESPORTA O DATAFRAME CONSOLIDADO PARA UM ARQUIVO EXCEL
consolidado.to_excel(f"Report-consolidado-{data.strftime('%d-%m-%Y')}.xlsx",
                    index=False,
                    sheet_name="Report consolidado"                    
                    )