def whatappopen():
    WhatAppOpen = input("Google\nSpotify\nDeepl\nAbrir um site\nSpeedtest\nEDGE/TEAMS\nQual destes acima deseja iniciar? ")
    if WhatAppOpen.lower() == 'google':
        import os
        caminho_aplicativo = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        os.startfile(caminho_aplicativo)
        print("Abrindo Google chorome....")
    elif WhatAppOpen.lower() == 'spotify':
        import os
        caminho_aplicativo = r"C:\Users\hoolf\AppData\Roaming\Spotify\Spotify.exe"
        os.startfile(caminho_aplicativo)
        print("Abrindo spotify....")
    elif WhatAppOpen.lower() == 'deepl':
        import os
        caminho_aplicativo = r"C:\Users\hoolf\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\DeepL"
        os.startfile(caminho_aplicativo)
        print("Abrindo Deepl....")
    elif WhatAppOpen.lower() == 'speedtest':
        import os
        openapp = r"C:\Program Files\Speedtest\Speedtest.exe"
        os.startfile(openapp)
        print("Abrindo speedtest")
    elif WhatAppOpen.lower() == 'edge' or 'teams':
        import webbrowser

        def openteams():
            teams_url = "https://teams.microsoft.com/_?culture=pt-br&country=br#/school/teams-grid/General?ctx=teamsGrid"
            edge = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
            webbrowser.get(edge).open(teams_url)
            print('Teams está abrindo com sucesso!')

        if __name__ == "__main__":
            openteams()
    else:
        import webbrowser
        webbrowser.open(WhatAppOpen)
        print(f"Abrindo o site:{WhatAppOpen}")
        '''urls prontas:
        https://github.com/Mrphyle/sincpython
        https://chat.openai.com/
        https://teams.microsoft.com/_?culture=pt-br&country=br#/school/teams-grid/General?ctx=teamsGrid
        https://encurtador.com.br/bpqQ5
        '''
while True:
    whatappopen()
    restartcont = input("Deseja abrir outro aplicativo? (Yes/No): ")
    print("___________________")
    if restartcont.lower() != 'yes':
        break