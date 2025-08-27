import time
import hmac
import hashlib
import requests
import pyautogui

#credenciais api

partner_id = 'sua id de afiliado'
partner_key = 'sua chave de acesso'
shop_id = 'id da loja'

#Assinatura

def sign (path, timestamp):
    raw = f'{partner_id}{path}{timestamp}{shop_id}'
    return hmac.new (partner_key.encode(), raw.encode(), hashlib.sha256).hexdigest()



