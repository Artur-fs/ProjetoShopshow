import time
import hmac
import hashlib
import requests
import urllib.parse

#credenciais api e variaveis

partner_id = 18337240041
partner_key = 'JAB2W36BLTHWLI67ZX2NT3AF47LXVYOK'
base_url = "https://partner.shopeemobile.com/api/v2"
category_id = 11059983
redirect_url = "https://seusite.com/callback"
#Antes da atualização X1 - shop_id = 'id da loja'
#PS:'shop_id' não será mais usado e será substituido por 'category_id'. - Atualização X2

#Assinatura digital

def generate_signature(path, timestamp):
    '''
    gera assinatura HMAC-SHA256
    path = endpoint da API (ex: /products/get_item_list)
    body = string com query + body
    '''
    #path = "/product/get_item_list"
    #timestamp = str(int(time.time()))
    #sign = generate_signature(path, timestamp)
    
    base_string = f'{partner_id}{path}{timestamp}'
    return hmac.new(
        partner_key.encode(),
        base_string.encode(),
        hashlib.sha256
    ).hexdigest()

#puxar produtos (request)

def shopee_request(path, params=None):
    '''
    requisição para a API
    '''
    
    if params is None:
        params = {}
    
    timestamp = int(time.time())
    query = f'partner_id={partner_id}&timestamp={timestamp}'
    sign = generate_signature(path, query)
    url = f'{base_url}{path}?{query}&sign={sign}'
    
    response = requests.get(url,params=params)
    return response.json()

#puxa produto por categoria
def get_product_by_category(category_id, page_size=10, offset=0):
    path = '/product/get_item_list'
    params = {
        'category_id': category_id,
        'offset': offset,
        'page_size': page_size
    }
    
    data = shopee_request (path, params)
    if 'error' in data :
        print ('Erro:', data ['error'])
        return []
    return data.get ('response', {}).get ('item', [])

#puxando detalhes

def get_product_detail (item_id_list):
    path = '/product/get_item_base_info'
    params = {
        'item_id_list': ','.join ([str(i) for i in item_id_list])
    }

    data = shopee_request(path, params)
    return data.get('response' , {}).get ('item_list', [])

#APLICAÇÃO

if __name__ == '__main__':
    category_id = 'id da categoria desejada'
    print("📦 Buscando produtos...")
    items = get_product_by_category(category_id, page_size=5)
    if not items:
        print ('Nenhum produto encontrado!')
    else:
        item_ids = [item['item_id'] for item in items]
        details = get_product_detail(item_ids)

        for d in details:
            print ('='*50)
            print ('Iniciando...')
            print ('nome:', d.get('item_name'))
            print ('imagens:',d.get('image', {}).get('image_url_list', []))
            print ('link da shopee:', f"https://shopee.com.br/product/{d['shopid']}/{d['item_id']}")
            print ('='*50)
            print (f'🔥C0mente "{d.get('item_name')}" para receber os l1nks\n🚨 Garanta já o seu!')

