from future.moves import tkinter
from tkinter import *
from pytube import YouTube

sach = Tk()
sach.geometry('500x300')
sach.resizable(0,0)
sach.title("sach youtube downloader")

Label(sach,text = 'Youtube Video Downloader', font ='arial 20 bold').pack()

link = StringVar()

Label(sach, text = 'Paste Link Here:', font = 'arial 15 bold').place(x= 160 , y = 60)
link_enter = Entry(sach, width = 70,textvariable = link).place(x = 32, y = 90)


def Downloader():
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(sach, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210)

Button(sach,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = Downloader).place(x=180 ,y = 150)

sach.mainloop()