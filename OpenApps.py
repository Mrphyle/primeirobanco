import os
import time
import webbrowser
import pyperclip as pc
import pyautogui as pa
def whatappopen():
    pc.copy("https://chat.openai.com/")
    os.system('cls' if os.name == 'nt' else 'clear')
    WhatAppOpen = input("_________________________________\nNavegadores(Exibe lista de navegadors)\nNavegador P(Padrão)\nSpotify\nDeepl\nAbrir um site\nSpeedtest\nAudacity\nQual destes acima deseja iniciar? ")
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
        while True:
            navegs()
            restartcont = input("\nDeseja abrir outro navegador? ")
            if not restartcont.lower() in ['yes','sim','1']:
                print("________________________\n")
                break
    if WhatAppOpen.lower() == 'navegador p':
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
    if WhatAppOpen.lower() == 'abrir site':
        webs = input("\nRadio Garden\nDigite um destes sites acima ou digite uma url: ")
        if webs.lower() == 'radio garden':
            web = "https://radio.garden/listen/country-101-1/B34md32h"
            webbrowser.open(web)
            print(f"\nAbrindo o site:{webs}")
        elif webs.lower() == 'teams':
            pc.copy("goncalves1807")
            web = "teams.microsoft.com/v2/#/school/teams-grid/General?ctx=teamsGrid"
            pa.hotkey('alt','tab')
            pa.hotkey('ctrl','t')
            time.sleep(2)
            pa.write(web)
            pa.hotkey('enter')
            time.sleep(30)
            pa.click(x=1861, y=137)
            time.sleep(10)
            pa.click(x=1128, y=553)
            time.sleep(30)
            pa.click(x=70, y=350)
            print(f"\nAbrindo o site:{webs}")
    if WhatAppOpen.lower() == 'audacity':
        os.startfile(r"C:\Program Files\Audacity\Audacity.exe")
        print("\nAbrindo audacity....")
while True:
    whatappopen()
    restartcont = input("\nDeseja abrir outro aplicativo? ")
    if not restartcont.lower() in ['yes','sim','1']:
        print('___________________\nComando finalizado')
        break
