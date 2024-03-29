def whatappopen():
    WhatAppOpen = input("Google\nSpotify\nDeepl\nAbrir um site\nSpeedtest\nQual destes acima deseja iniciar? ")
    if WhatAppOpen.lower() == 'google':
        import os
        caminho_aplicativo = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        os.startfile(caminho_aplicativo)
        print("Abrindo Google chorome....")
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
    else:
        import webbrowser
        InputUrl = input("Digite a URL: ")
        webbrowser.open(InputUrl)
        print(f"Abrindo o site:{InputUrl}")
        '''urls prontas:
        https://github.com/Mrphyle/sincpython
        https://chat.openai.com/
        https://teams.microsoft.com/_?culture=pt-br&country=br#/school/teams-grid/General?ctx=teamsGrid
        https://encurtador.com.br/bpqQ5
        '''
while True:
    whatappopen()
    restartcont = input("Deseja abrir outro aplicativo? (Yes/No): ")
    if restartcont.lower() != 'yes':
        break