import os
import webbrowser
import pyperclip
import time
def whatappopen():
    pyperclip.copy("https://chat.openai.com/")
    WhatAppOpen = input("Google\nSpotify\nDeepl\nAbrir um site\nSpeedtest\nEDGE/TEAMS\nQual destes acima deseja iniciar? ")
    if WhatAppOpen.lower() == 'google':
        caminho_aplicativo = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        os.startfile(caminho_aplicativo)
        print("Abrindo Google chorome....")
    elif WhatAppOpen.lower() in ['discord','dc']:
        FileLocation = r"C:\Users\hoolf\Desktop\aplicativos\Apps em geral\Discord"
        os.startfile(FileLocation)
        print("Abrindo discord....")
    elif WhatAppOpen.lower() == 'spotify':
        caminho_aplicativo = r"C:\Users\hoolf\AppData\Roaming\Spotify\Spotify.exe"
        os.startfile(caminho_aplicativo)
        print("Abrindo spotify....")
    elif WhatAppOpen.lower() == 'deepl':
        caminho_aplicativo = r"C:\Users\hoolf\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\DeepL"
        os.startfile(caminho_aplicativo)
        print("Abrindo Deepl....")
    elif WhatAppOpen.lower() == 'speedtest':
        openapp = r"C:\Program Files\Speedtest\Speedtest.exe"
        os.startfile(openapp)
        print("Abrindo speedtest")
    elif WhatAppOpen.lower() in ['edge','teams']:
        def openteams():
            pyperclip.copy("goncalves1807")
            teams_url = "https://teams.microsoft.com/_?culture=pt-br&country=br#/school/teams-grid/General?ctx=teamsGrid"
            edge = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
            webbrowser.get(edge).open(teams_url)
            print('Teams está abrindo com sucesso!')
        if __name__ == "__main__":
            openteams()
    else:
        
        webbrowser.open(WhatAppOpen)
        print(f"Abrindo o site:{WhatAppOpen}")
while True:
    whatappopen()
    restartcont = input("Deseja abrir outro aplicativo? (Yes/No): ")
    print("___________________")
    if restartcont.lower() != 'yes':
        print('Comando finalizado')
        break