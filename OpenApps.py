import os
import webbrowser
import pyperclip
def whatappopen():
    pyperclip.copy("https://chat.openai.com/")
    WhatAppOpen = input("_________________________________\nGoogle\nSpotify\nzotube music\nDeepl\nAbrir um site\nSpeedtest\nEDGE/TEAMS\nQual destes acima deseja iniciar? ")
    if WhatAppOpen.lower() == 'google':
        caminho_aplicativo = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        os.startfile(caminho_aplicativo)
        print("\nAbrindo Google chorome....")
    elif WhatAppOpen.lower() in ['discord','dc']:
        FileLocation = r"C:\Users\hoolf\Desktop\aplicativos\Apps em geral\Discord"
        os.startfile(FileLocation)
        print("\nAbrindo discord....")
    elif WhatAppOpen.lower() == 'spotify':
        caminho_aplicativo = r"C:\Users\hoolf\AppData\Roaming\Spotify\Spotify.exe"
        os.startfile(caminho_aplicativo)
        print("\nAbrindo spotify....")
    elif WhatAppOpen.lower() == 'zotube music':
        webbrowser.open("https://music.youtube.com/")
        print("\nAbrindo spotify2....")
    elif WhatAppOpen.lower() == 'deepl':
        caminho_aplicativo = r"C:\Users\hoolf\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\DeepL"
        os.startfile(caminho_aplicativo)
        print("\nAbrindo Deepl....")
    elif WhatAppOpen.lower() == 'speedtest':
        OpenApp = r"C:\Program Files\Speedtest\Speedtest.exe"
        os.startfile(OpenApp)
        print("\nAbrindo speedtest")
    elif WhatAppOpen.lower() in ['edge','teams']:
        def openteams():
            pyperclip.copy("goncalves1807")
            teams_url = "https://teams.microsoft.com/_?culture=pt-br&country=br#/school/teams-grid/General?ctx=teamsGrid"
            edge = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
            webbrowser.get(edge).open(teams_url)
            print('\nTeams está abrindo com sucesso!')
        if __name__ == "__main__":
            openteams()
    else:
        
        webbrowser.open(WhatAppOpen)
        print(f"\nAbrindo o site:{WhatAppOpen}")
while True:
    whatappopen()
    restartcont = input("\nDeseja abrir outro aplicativo? (Yes/No): ")
    if restartcont.lower() != 'yes':
        print('___________________\nComando finalizado')
        break