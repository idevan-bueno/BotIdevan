import requests
import configparser
import logging

config = configparser.ConfigParser()
config.read('config.ini')

logger = logging.getLogger('TelegramBot')

base_url = 'https://api.hgbrasil.com/finance'
hgbrasil_key = config['HGBRASIL']['API_KEY']

def get_quotations(is_taxa):
    logger.info('Entrou no moedas.py -> get_quotations -> is_taxa = ' + str(is_taxa))

    endpoint = ''
    if is_taxa:
        endpoint = '/taxes'
    else:
        endpoint = '/quotations'

    parameters = '?' + 'key=' + hgbrasil_key
    final_url = base_url + endpoint + parameters

    logger.info(' -> final_url ' + final_url)

    response = requests.get(final_url).json()

    arr_moedas = []
    arr = ''

    if is_taxa:
        taxas = response['results'][0]

        arr = 'data..........: ' + taxas['date']
        arr_moedas.append(arr)
        arr = 'cdi............: ' + str(taxas['cdi'])
        arr_moedas.append(arr)
        arr = 'selic..........: ' + str(taxas['selic'])
        arr_moedas.append(arr)
        arr = 'cdi diaria....: ' + str(taxas['cdi_daily'])
        arr_moedas.append(arr)
        arr = 'selic diaria..: ' + str(taxas['selic_daily'])
        arr_moedas.append(arr)
    else:
        moedas = response['results']['currencies']

        for md in moedas:
            dadosmd = moedas[md]
            if type(dadosmd) is dict:
                arr = 'moeda....: ' + dadosmd['name']
                arr_moedas.append(arr)
                arr = 'compra...: ' + str(dadosmd['buy'])
                arr_moedas.append(arr)
                arr = 'venda.....: ' + str(dadosmd['sell'])
                arr_moedas.append(arr)
                arr = 'variação..: ' + str(dadosmd['variation'])
                arr_moedas.append(arr)
                arr = ' '
                arr_moedas.append(arr)

    return arr_moedas


def get_ibovespa(is_baixa):
    logger.info('Entrou no moedas.py -> get_ibovespa -> is_baixa =' + str(is_baixa))

    endpoint = ''
    symbol_hg = ''

    if is_baixa:
        symbol_hg = '&symbol=get-low'
        endpoint  = '/stock_price'
    else:
        symbol_hg = '&symbol=get-high'
        endpoint  = '/stock_price'

    parameters = '?' + 'key=' + hgbrasil_key

    final_url = base_url + endpoint + parameters + symbol_hg

    logger.info(' -> final_url ' + final_url)

    response = requests.get(final_url).json()

    arr_ibovespa = []
    arr = ''

    ibovespa = response['results']

    for empresa in ibovespa:
        dados_acao = ibovespa[empresa]
        if type(dados_acao) is dict:
            arr = 'simbolo.....: ' + dados_acao['symbol']
            arr_ibovespa.append(arr)
            arr = 'empresa.....: ' + dados_acao['name']
            arr_ibovespa.append(arr)
            arr = 'preço........: ' + str(dados_acao['price'])
            arr_ibovespa.append(arr)
            arr = 'percentual..: ' + str(dados_acao['change_percent'])
            arr_ibovespa.append(arr)
            arr = 'market cap..: ' + str(dados_acao['market_cap'])
            arr_ibovespa.append(arr)
            arr = ' '
            arr_ibovespa.append(arr)

    return arr_ibovespa


