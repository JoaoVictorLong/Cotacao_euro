import requests, time, pygame
valormaior = 6.50
pygame.init()
while True:
    api = requests.get("https://economia.awesomeapi.com.br/all/EUR-BRL").json()
    result = round(float(api['EUR']['ask']), 2)
    if result <= valormaior:
        print(result)
        pygame.mixer.music.load('C:\\Users\\Joao\\PycharmProjects\\Cotacao_euro\\Music\\teste2.mp3')
        pygame.mixer.music.play()
        time.sleep(20)
    else:
        print("O valor atual é {}".format(result))
    time.sleep(60)