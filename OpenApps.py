import os
import webbrowser
import pyperclip
def whatappopen():
    pyperclip.copy("https://chat.openai.com/")
    os.system('cls' if os.name == 'nt' else 'clear')
    WhatAppOpen = input("_________________________________\nNavegadores(Exibe lista de navegadors)\nNavegador P(Padrão)\nSpotify\nDeepl\nAbrir um site\nSpeedtest\nQual destes acima deseja iniciar? ")
    os.system('cls' if os.name == 'nt' else 'clear')
    if WhatAppOpen.lower() == 'navegadores':
        BrownserOps = input("            Google\n            OperaGX\n            Edge\nQual dos navegadores disponiveis acima deseja? ")
        if BrownserOps.lower() == 'google' :
            caminho_aplicativo = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
            os.startfile(caminho_aplicativo)
            print("\nAbrindo Google chorome....")
        elif BrownserOps.lower() in ['OperaGx','OperaGx']:
            caminho_aplicativo = r"C:\Users\hoolf\AppData\Local\Programs\Opera GX\launcher.exe"
            os.startfile(caminho_aplicativo)
            print("\nAbrindo Opera Gx....")
        else:
            def openteams():
                pyperclip.copy("goncalves1807")
                teams_url = "https://teams.microsoft.com/_?culture=pt-br&country=br#/school/teams-grid/General?ctx=teamsGrid"
                edge = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
                webbrowser.get(edge).open(teams_url)
            print('\nAbrindo Microsoft Edge.....')
        if __name__ == "__main__":
            openteams()    
    elif WhatAppOpen.lower() == 'Navegador P(Padrão)':
        caminho_aplicativo = r"C:\Users\hoolf\AppData\Local\Programs\Opera GX\launcher.exe"
        os.startfile(caminho_aplicativo)
        print("\nAbrindo Opera Gx....")
    elif WhatAppOpen.lower() in ['discord','dc']:
        FileLocation = r"C:\Users\hoolf\Desktop\aplicativos\Apps em geral\Discord"
        os.startfile(FileLocation)
        print("\nAbrindo discord....")
    elif WhatAppOpen.lower() == 'spotify':
        caminho_aplicativo = r"C:\Users\hoolf\AppData\Roaming\Spotify\Spotify.exe"
        os.startfile(caminho_aplicativo)
        print("\nAbrindo spotify....")
    elif WhatAppOpen.lower() == 'deepl':
        caminho_aplicativo = r"C:\Users\hoolf\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\DeepL"
        os.startfile(caminho_aplicativo)
        print("\nAbrindo Deepl....")
    elif WhatAppOpen.lower() == 'speedtest':
        OpenApp = r"C:\Program Files\Speedtest\Speedtest.exe"
        os.startfile(OpenApp)
        print("\nAbrindo speedtest")
    elif WhatAppOpen.lower() == 'site':
        web = input("Digite a url")
        webbrowser.open(web)
        print(f"\nAbrindo o site:{web}")
while True:
    whatappopen()
    restartcont = input("\nDeseja abrir outro aplicativo? (Yes/No): ")
    if restartcont.lower() != 'yes':
        print('___________________\nComando finalizado')
        break