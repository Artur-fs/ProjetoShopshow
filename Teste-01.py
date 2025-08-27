import time
import hmac
import hashlib
import requests
import pyautogui

#credenciais api e variaveis

partner_id = 'sua id de afiliado'
partner_key = 'sua chave de acesso'
shop_id = 'id da loja'
base_url = "https://partner.shopeemobile.com/api/v2"

#Assinatura

def sign (path, timestamp):
    raw = f'{partner_id}{path}{timestamp}{shop_id}'
    return hmac.new (partner_key.encode(), raw.encode(), hashlib.sha256).hexdigest()

#puxar produtos

def get_products():
    path = '/product/get_item_list'
    timestamp = int(time.time())
    sign_val = sign (path,timestamp)
    url = f'{base_url}{path}?partner_id=&timestamp={timestamp}&sign={sign_val}&shop_id={shop_id}&item_status = normal'
    r = requests.get (url)
    return r.json ()

#detalhes do produto
def get_product_info(item_id):
    path = '/product/get_item_base_info'
    timestamp = int(time.time())
    sign_val = sign(path, timestamp)
    url = f'{base_url}{path}?partner_id={partner_id}&timestamp={timestamp}&sign={sign_val}&shop_id={shop_id}&item_id_list={item_id}'
    r = requests.get (url)
    return r.json

