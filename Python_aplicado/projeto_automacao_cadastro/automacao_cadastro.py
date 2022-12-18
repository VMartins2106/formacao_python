import pandas as pd
import robo

# Lendo o arquivo Excel
df = pd.read_excel('cadastro_clientes.xlsx') 
robo.cadastro_web(df)