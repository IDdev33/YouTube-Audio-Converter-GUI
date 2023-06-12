from tkinter import *
from tkinter import ttk
from pytube import YouTube
from tkinter.messagebox import showinfo, showerror
import threading
from PIL import Image
from PIL import ImageTk
import ttkbootstrap as ttkb
from ttkbootstrap.constants import *
import os


#Functionality

def download_audio():
    mp3_link = entry.get()
    if mp3_link == '':
        showerror(title='Error', message='Please enter the MP3 URL')   
    else:
        try:
             showinfo(title='Download In Progress', message='Your file is being downloaded. Please wait.')
             audio = YouTube(mp3_link)     
             output = audio.streams.get_audio_only().download()
             base, ext = os.path.splitext(output)
             new_file = base + '.mp3'
             os.rename(output, new_file)
             showinfo(title='Download Complete', message='MP3 has been downloaded successfully.')
        except:
            showerror(title='Download Error', message='An error occurred while trying to ' \
                    'download the MP3\nThe following could ' \
                    'be the causes:\n->Invalid link\n->No internet connection\n'\
                     'Make sure you have stable internet connection and the MP3 link is valid') 


#Threading
def downloadThread():
    t1 = threading.Thread(target=download_audio)
    t1.start() 

#GUI Section Start

#Window Layout
window = ttkb.Window(themename='cosmo')
window.geometry("450x500")
window.title("YouTube Audio Converter")
window.resizable(height=FALSE, width=FALSE)

#Canva for holding image + header
canvas = Canvas(window, width=400, height=200, highlightthickness=0)
canvas.place(anchor='center', relx=0.5, rely=0.1)
img= (Image.open("audio.png"))
resized_image= img.resize((200,130), Image.LANCZOS)
new_image= ImageTk.PhotoImage(resized_image)
canvas.create_text(200,135, fill='red', text='YouTube Audio Downloader', font=('Calibri 19 bold') )
canvas.create_image(200,68, image=new_image)
canvas.pack()

#Frame
frame = Frame(window, width=350, height=250, highlightbackground ="red", highlightthickness=1)
frame.place(anchor='center', relx=0.5, rely=0.7)

#Entry and label
label = ttkb.Label(frame, text='Paste The Link:', style='primary.Tlabel', font=('Helbetica 15 italic'))
label.place(relx=0.05, rely=0.07)
entry = ttkb.Entry(frame, font=('Calibri 15 italic'), style='primary.TEntry', width=30)
entry.place(relx=0.05, rely=0.20)

#Download Button
button = ttkb.Button(frame, takefocus=False, text='Download', style='primary.Outline.TButton', command=downloadThread)
Style = ttk.Style()
Style.configure('primary.Outline.TButton', font=('Calibri 20 bold'))
button.place(relx=0.29, rely=0.6)

#GUI Section End.

window.mainloop()