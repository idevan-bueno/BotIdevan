# BotIdevan
Trabalho ChatBot - Ações - Voz - Telegram

Chatbot de consulta de dados financeiros:
- cambio - dolar, euro, peso, libra, bitcoin
- taxas  - cdi e selic
- açoes  - maiores altas ou baixas ibovespa

Utiliza o Watson Assistant como gerenciador e a API da HG Brasil para consultas.

## Branches

* Master: branch original que utiliza o long polling do Telegram

## Configurações

configure as chaves das apis no arquivo de configuração config.ini 

## Bugs conhecidos

* Tratamento das sugestões retornadas pelo assistant - key text error
