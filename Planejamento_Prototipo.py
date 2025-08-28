import time
import pyautogui as py
import pandas as pd

time.sleep(5)
py.PAUSE = 1
print (py.position())

# Browser - Point(x=881, y=748)
# Nova janela - Point(x=833, y=556)
# Write ('link')
# Press enter
# Double click - Point(x=1156, y=29)
# Botão direito - Point(x=337, y=405)
# Aperta seta para cima 7 vezes
# Aperta enter
# Write ('1')
# Aperta enter
# Fechar a pagina - (x=1345, y=20)

#----------------------#
# Aqui entra o scrip de postagem no instagram
#----------------------#

#CHAVE

#Variaveis testes
#tabela = pd.read_csv('produtos (1).csv')
#links = (tabela['links']).values
#nomes = (tabela['nome']).values


#for link in links:
#    print (f'O link é {link}ááááá')
#aqui entra script puxar imagens

#for nome in nomes:
#    print (f'O nome é {nome}')
#aqui entra script puxar imagens

py.rightClick (x=928, y=746)#LOCAL DO CHROME (MUDAR POSITION SE NECESSARIO)
py.click (x=857, y=554)
py.doubleClick (x=1110, y=36)
py.write ('https://www.instagram.com/')
py.press ('Enter')
time.sleep (5)
py.click (x=88, y=548) #click em postar (Atualizar sempre)
py.click (x=92, y=608) #click em postar (Atualizar sempre)
py.click (x=671, y=506) #upload
py.click (x=226, y=411) #seleciona barra de pesquisa
