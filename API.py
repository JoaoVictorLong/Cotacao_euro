from requests import get, exceptions
from time import sleep
from os import system
from datetime import datetime
from pygame import mixer
count = 0
valormaior = 6.10
mixer.init()
system('cls')
system("title 'Cotacao do euro'")
while True:
    try:
        api = get("http://economia.awesomeapi.com.br/all/EUR-BRL").json()
    except exceptions.RequestException:
        print("Erro ao tentar conexão")
        break
    result = round(float(api['EUR']['ask']), 2)
    if result <= valormaior:
        system("msg * FICOU MAIS BARATO: {}".format(result))
        mixer.music.load('C:\\Users\\joao.victor.longo\\OneDrive - Accenture\\Desktop\\Cotacao_euro\\Music\\teste2.mp3')
        mixer.music.play()
        sleep(20)
    else:
        count += 1
        from datetime import datetime
        now = datetime.now()
        frase = "Executando as: {}:{}:{}".format(now.hour,now.minute,now.second)
        print("O valor atual é {:.2f}".format(result))
        print(frase, count)
    sleep(100)