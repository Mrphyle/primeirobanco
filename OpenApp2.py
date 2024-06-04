import os
import tkinter as tk
class Buttontype:
    @staticmethod
    def spotify_location():
        spotifile = r"C:\Users\hoolf\AppData\Roaming\Spotify\Spotify.exe"
        os.startfile(spotifile)
    @staticmethod
    def chrome_location():
        chromefile = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        os.startfile(chromefile)
    @staticmethod
    def Obs_location():
        obsfile = r"C:\Program Files\obs-studio\bin\64bit\obs64.exe"
        os.startfile(obsfile)
    @staticmethod
    def Wallpaperengine_location():
        wallpaperenfile = r"C:\Users\hoolf\Desktop\Wallpaper Engine.url"
        os.startfile(wallpaperenfile)
    @staticmethod
    def Clippaint_location():
        clipstudiofile = r"C:\Program Files\CELSYS\CLIP STUDIO 1.5\CLIP STUDIO PAINT\CLIPStudioPaint.exe"
        os.startfile(clipstudiofile)
    @staticmethod
    def Huionh64_locate():
        huionhs64file = r"C:\Program Files\HuionTablet\HuionTablet.exe"
        os.startfile(huionhs64file)
    @staticmethod
    def steam_locate():
        steamfile= r"C:\Program Files (x86)\Steam\steam.exe"
        os.startfile(steamfile)
# Criar a janela principal
root = tk.Tk()
root.geometry("800x600")
root.title("Abridor de aplicativos 2.0")
root.configure(bg='gray20')
button_style = {
    'bg': 'gray30',
    'fg': 'white',
    'activebackground': 'gray50',
    'activeforeground': 'white',
    'height': 3,
    'width': 20
}
#Titulo
title_text = tk.Text(root, height=1, bg='gray20', fg='white', font=('Helvetica', 16), bd=0)
title_text.pack(pady=20)
title_text.insert(tk.END, "Clique no app que deseja abrir abaixo:")
title_text.configure(state='disabled')
# Spotify
spotify_button = tk.Button(root, text="Spotify", command=Buttontype.spotify_location, **button_style)
spotify_button.place(x=20,y=1*75)
# Chrome
chrome_button = tk.Button(root, text="Google Chrome", command=Buttontype.chrome_location, **button_style)
chrome_button.place(x=20,y=2*75)
#Obs_location
obs_button = tk.Button(root,text="OBS",command=Buttontype.Obs_location,**button_style)
obs_button.place(x=20,y=3*75)
#wallpaperengine
wallpprengbutton = tk.Button(root,text="wallpaper\nengine",command=Buttontype.Wallpaperengine_location,**button_style)
wallpprengbutton.place(x=225,y=3*75)
#clipstudio
clipstudiopaint_button = tk.Button(root, text="ClipStudio\nPaint",command=Buttontype.Clippaint_location, **button_style)
clipstudiopaint_button.place(x=225,y=75)
#huionsoftuware
huionhs64_button = tk.Button(root,text="Huion hs64\nSoftuware",command=Buttontype.Huionh64_locate,**button_style)
huionhs64_button.place(x=225,y=2*75)
#steam
steam_button = tk.Button(root,text="Steam",command=Buttontype.steam_locate,**button_style)
steam_button.place(x=225,y=4*75)
root.mainloop()