import os
import tkinter as tk

spotifile = r"C:\Users\hoolf\AppData\Roaming\Spotify\Spotify.exe"
def start_spotify():
    os.startfile(spotifile)
root = tk.Tk()
root.geometry("800x600")
spotifybutton = tk.Button(root, text="Spotify", command=start_spotify)
spotifybutton.pack()
root.mainloop()
