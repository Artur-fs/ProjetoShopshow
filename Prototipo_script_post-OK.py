import time
import pyautogui as py
import pandas as pd
import pyperclip
import datetime

time.sleep(3)
py.PAUSE = 1

tabela = pd.read_csv('produtos_teste.csv')
links = (tabela['links']).values
nomes = (tabela['nome']).values
linhas = ['1', '2','3','4']
horarios = ['11:55', '13:00', '18:20', '22:30']

#PROCESSO DE POSTAGEM

for i, nome in enumerate(nomes, start =1):
    #PROGRAMAÇÃO DE POSTAGEM COM HORARIO - prototipo teste

    horario_alvo = horarios [i-1]
    hora, minuto = map (int, horario_alvo.split(':'))

    agora = datetime.datetime.now()
    alvo = agora.replace(hour=hora, minute=minuto, second=0, microsecond=0)

    print ('='*50)
    print(f"⏳ Aguardando até {alvo.strftime('%H:%M')} para iniciar postagem {i}...")
    print ('='*50)

    while datetime.datetime.now() < alvo:
        time.sleep (10)
    
    #INICIANDO POSTAGEM
    print("="*20, "\nIniciando postagem...\n","="*20)
    
    time.sleep (5)
                
    py.rightClick (x=925, y=741)#LOCAL DO CHROME (MUDAR POSITION SE NECESSARIO)
    py.click (x=857, y=554)
    py.doubleClick (x=1110, y=36)
    py.write ('https://www.instagram.com/')
    py.press ('Enter')
    time.sleep (5)
    py.click (x=88, y=548) #click em postar (Atualizar sempre)
    py.click (x=92, y=608) #click em postar (Atualizar sempre)
    py.click (x=671, y=506) #upload
    py.click (x=226, y=411) #seleciona barra de pesquisa

    py.write (str(i)) #Nome do arquivo
    py.press ('Enter') #upload
    time.sleep (5) #aguarda carregamento
    py.click (x=516, y=594) #escolhe formato
    py.click (x=536, y=392) #escolhe formato
    py.click (x=830, y=231) #SHARE
    py.click (x=997, y=229) #NEXT
    py.click (x=826, y=376) #seleciona area de descrição
    
    texto = f'🔥C0mente "{nome}" para receber os l1nks 🚨 Garanta já o seu!\nConfere na ABA DE SOLICITAÇÕES de mensagens do seu direct!'

    pyperclip.copy(texto)
    time.sleep(0.5)

    py.hotkey ('Ctrl', 'v')
    py.click (x=997, y=229) #post

    time.sleep (150)

    py.press ('Esc')

    time.sleep (1)

    py.press ('F5')

    time.sleep (3)

    py.doubleClick (x=647, y=20)   #FECHANDO JANELA
    py.click (x=1338, y=28)        #  =

    print("="*20, "\nPostagem concluida!\n", "="*20)