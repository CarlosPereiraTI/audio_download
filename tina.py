from cProfile import label
from logging import PlaceHolder
from operator import contains
from tkinter import *
from tkinter import ttk
import tkinter
from turtle import title, width
import webbrowser
import os
from pytube import YouTube

root = Tk()
frm = ttk.Frame(root, padding=5)
frm.grid()

url = StringVar()


# =====================================================================
# Window title and icon
root.geometry("495x145")
root.resizable(0, 0)
photo = PhotoImage(file="icons/descargando.png")
root.iconphoto(True, photo)
frm.master.title("Tina | Youtube Downloader")

# =====================================================================
# URL entry
ttk.Label(frm, text='URL').grid(column=0, row=0)
url_field = Entry(frm, width=60, textvariable=url, borderwidth=2)
url_field.grid(column=1, row=0, padx=10, pady=10, columnspan=3)
url_field.config(fg='red')


# =====================================================================
# Abre carpeta con la ubicacion del archivo
def open():
    os.system("start C:/Tina_Download/")

ttk.Button(frm, text="Open Folder", command=open).grid(column=4, row=1)



var = IntVar()


# =====================================================================
# Audio download
# def download_audio():
#     yt_audio = YouTube(str(url.get()))
#     audio = yt_audio.streams.filter(only_audio=True).first()
#     out_file = audio.download(output_path = 'C:\\Tina_Download\\Audio')
#     base, ext = os.path.splitext(out_file)
#     new_file = base + '.mp3'
#     os.rename(out_file, new_file)
#     tkinter.messagebox.showinfo(title="Tina | Youtube Downloader", message="Your audio has been downloaded successfully!")

# ttk.Button(frm, text="Download Audio MP3", command=download_audio).grid(column=3, row=2)

# =====================================================================
# Video download
# def video_download():
#     yt_video = YouTube(str(url.get()))
#     video = yt_video.streams.filter(only_audio=False, res="720p").first()
#     out_file = video.download(output_path = 'C:\\Tina_Download\\Video')
#     base, ext = os.path.splitext(out_file)
#     new_file = base + '.mp4'
#     os.rename(out_file, new_file)
#     tkinter.messagebox.showinfo(title="Tina | Youtube Downloader", message="Your video has been downloaded successfully!")

# ttk.Button(frm, text="Download Video MP4", command=video_download).grid(column=3, row=3)


def selection():
    option = var.get()
    # selection = f"Your selection is {option}"
    # print(option)
    return option

# opt_mp3 = Radiobutton(frm, text="Download Audio MP3", variable=var, value=1, command=download_audio).grid(column=1, row=2)
# opt_mp4 = Radiobutton(frm, text="Download Video MP4", variable=var, value=2, command=video_download).grid(column=1, row=3)

opt_mp3 = Radiobutton(frm, text="Download Audio MP3", variable=var, value=1, command=selection).grid(column=1, row=1)
opt_mp4 = Radiobutton(frm, text="Download Video MP4", variable=var, value=2, command=selection).grid(column=1, row=2)



# # download_button

def download():
    if (selection() == 1):
        yt_audio = YouTube(str(url.get()))
        audio = yt_audio.streams.filter(only_audio=True).first()
        out_file = audio.download(output_path = 'C:\\Tina_Download\\Audio')
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        tkinter.messagebox.showinfo(title="Tina | Youtube Downloader", message="Your audio has been downloaded successfully!")
    elif (selection() == 2):
        yt_video = YouTube(str(url.get()))
        video = yt_video.streams.filter(only_audio=False, res="720p").first()
        out_file = video.download(output_path = 'C:\\Tina_Download\\Video')
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp4'
        os.rename(out_file, new_file)
        tkinter.messagebox.showinfo(title="Tina | Youtube Downloader", message="Your video has been downloaded successfully!")
    else:
        tkinter.messagebox.showinfo(title="Tina | Youtube Downloader", message="Please, select an option: Audio MP3 or Video MP4!")

# download_button
ttk.Button(frm, text="Download", command=download).grid(column=4, row=0)

# https://www.youtube.com/watch?v=BLVSGZVgOkc

# video test
# https://www.youtube.com/watch?v=uqJZWLlnSqs


# =====================================================================
# File menu
menu_bar = Menu(root)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)
root.config(menu=menu_bar)

# Help Menu
def about():
    tkinter.messagebox.showinfo(title="About", message="Tina | Youtube Downloader v1.0.2\n Your files are available in C:/Tina_Download")

help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=about)
menu_bar.add_cascade(label="Help", menu=help_menu)


# =====================================================================
# status bar
status = Label(root, text="Running version 1.0.2 ", bd=1, relief=SUNKEN, anchor=E)
status.grid(row=4, column=0, columnspan=3, sticky=W+E)

# =====================================================================
# End program
ttk.Button(frm, text='Close', command=root.destroy).grid(column=4, row=5)
root.mainloop()