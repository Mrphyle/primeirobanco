import os
import webbrowser
import pyperclip as ctrlC
def whatappopen():
    pyperclip.copy("https://chat.openai.com/")
    os.system('cls' if os.name == 'nt' else 'clear')
    WhatAppOpen = input("_________________________________\nNavegadores(Exibe lista de navegadors)\nNavegador P(Padrão)\nSpotify\nDeepl\nAbrir um site\nSpeedtest\nQual destes acima deseja iniciar? ")
    os.system('cls' if os.name == 'nt' else 'clear')
    if WhatAppOpen.lower() == 'navegadores':
        def navegs():
            os.system('cls' if os.name == 'nt' else 'clear')
            BrownserOps = input("Google\nOperaGX\nEdge\nQual dos navegadores disponiveis acima deseja? ")
            if BrownserOps.lower() == 'google' :
                os.startfile(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
                print("\nAbrindo Google chorome....")
            elif BrownserOps.lower() in ['opera gx','operagx']:
                os.startfile(r"C:\Users\hoolf\AppData\Local\Programs\Opera GX\launcher.exe")
                print("\nAbrindo Opera Gx....")
            else:
                
                ctrlC.copy("goncalves1807")
                
                print('\nAbrindo Microsoft Edge.....')
        while True:
            navegs()
            restartcont = input("\nDeseja abrir outro navegador? ")
            if not restartcont.lower() in ['yes','sim','1']:
                print("________________________\n")
                break
    if WhatAppOpen.lower() == 'Navegador P(Padrão)':
        os.startfile(r"C:\Users\hoolf\AppData\Local\Programs\Opera GX\launcher.exe")
        print("\nAbrindo Opera Gx....")
    if WhatAppOpen.lower() == 'spotify':
        os.startfile(r"C:\Users\hoolf\AppData\Roaming\Spotify\Spotify.exe")
        print("\nAbrindo spotify....")
    if WhatAppOpen.lower() == 'deepl':
        os.startfile(r"C:\Users\hoolf\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\DeepL")
        print("\nAbrindo Deepl....")
    if WhatAppOpen.lower() == 'speedtest':
        os.startfile(r"C:\Program Files\Speedtest\Speedtest.exe")
        print("\nAbrindo speedtest")
    if WhatAppOpen.lower() == 'site':
        web = input("Digite a url")
        webbrowser.open(web)
        print(f"\nAbrindo o site:{web}")
while True:
    whatappopen()
    restartcont = input("\nDeseja abrir outro aplicativo? ")
    if not restartcont.lower() in ['yes','sim','1']:
        print('___________________\nComando finalizado')
        break
