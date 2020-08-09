import moedas
import logging

logger = logging.getLogger('TelegramBot')

def action_handler(action, parameters, return_var):
    return_values = {}

    if  action == 'quotations':
            # cotacoes de moedas
            return_values = get_quotations(parameters, return_var)
    elif action == 'ibovespa':
            # cotacoes de acoes - altas e baixas
            return_values = get_ibovespa(parameters, return_var)

    return {
            'skills': {
                'main skill': {
                    'user_defined': return_values
                }
            }
        }

def get_quotations(parameters, return_var):
    # cotaçoes para moedas ( dolar, euro, libra, peso, bitcoin )
    #           ou
    # cotacoes para taxas ( cdi e selic )

    logger.info('Entrou no actions.py -> get_quotations')

    is_taxa = ((parameters['tipo_cotacao'] == 'taxas') or
               (parameters['tipo_cotacao'] == 'taxa'))

    quotation_data = moedas.get_quotations(is_taxa)

    moeda_string = '\n\n'
    for moeda in quotation_data:
        moeda_string += moeda + '\n'

    return {
        return_var: moeda_string
    }

def get_ibovespa(parameters, return_var):
    # cotaçoes de açoes - altas e baixas

    logger.info('Entrou no actions.py -> get_ibovespa')
    is_baixa = ((parameters['tipo_ibovespa'] == 'baixas') or
                (parameters['tipo_ibovespa'] == 'baixa'))
    ibovespa_data = moedas.get_ibovespa(is_baixa)

    bolsa_string = '\n\n'
    for bolsa in ibovespa_data:
        bolsa_string += bolsa + '\n'

    return {
        return_var: bolsa_string
    }

