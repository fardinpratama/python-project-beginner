import tkinter
from tkinter import (Tk, Label, PhotoImage, Button, Entry,
                    StringVar, Radiobutton, OptionMenu,
                    filedialog, W, E)
from tkinter.ttk import Progressbar
from PIL import ImageTk, Image
from pytube import YouTube
import threading


class VideoYtDownload(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.configure(background='#fff')
        self.title('YouTube Video Downloader With Python')
        self.geometry('500x400')

        # logo
        self.logo = PhotoImage(file='logo.png')
        self.iconphoto(False, self.logo)

        # header
        self.photo = ImageTk.PhotoImage(Image.open("header.png"))
        self.header = Label(self, image=self.photo)
        self.header.grid(row=0, column=0, columnspan=4)
        self.header.configure(background='#fff')

        self.get_folder()
        self.form_input_url()

    def get_folder(self):
        open_folder = Button(self, text="Select folder",
                             command=self.select_folder)
        open_folder.grid(row=1, column=3, ipadx=15, padx=5)
        self.folder = StringVar()
        self.folder.set("select folder")
        self.input_folder = Entry(self, textvariable=self.folder)
        self.input_folder.grid(
            row=1, column=1, columnspan=2, padx=0, pady=10, ipadx=110)

    def select_folder(self):
        directory = filedialog.askdirectory()
        self.folder.set(directory)

    def form_input_url(self):
        # form input
        label_url = Label(self, text="URL")
        label_url.grid(row=2, column=0)
        label_url.configure(background='#fff')
        self.input_link = Entry(self)
        self.input_link.grid(row=2, column=1, columnspan=2,
                             padx=0, pady=10, ipadx=110)
        # button download1
        button_1 = Button(self, text="Get URL", command=self.get_link)
        button_1.grid(row=2, column=3, ipadx=27, padx=10)

    # get link
    def get_link(self):
        url = self.input_link.get()
        self.get_list(url)
        self.get_type(self.list_video)
        self.get_filter(self.list_video, self.list_type)

        button_2 = Button(self, text="Download", command=self.on_download)
        button_2.grid(row=5, column=3, ipadx=20)

    # get list
    def get_list(self, url):
        self.your_video = YouTube(url)
        self.list_video = self.your_video.streams

    # get type
    def get_type(self, list_video):
        list_type = []
        for video in list_video:
            list_type.append(video.type)
        list_type = set(list_type)
        self.list_type = list(list_type)

    # get filter
    def get_filter(self, list_video=[], list_type=[]):
        if list_video:
            # Initialize Canvas
            # radio button
            if len(self.your_video.title) > 50:
                self.title_video = "Title: " + \
                    self.your_video.title[:50] + "..."
            else:
                self.title_video = "Title: " + self.your_video.title
            label_title = Label(self, text=self.title_video)
            label_title.grid(row=3, column=0, columnspan=3, padx=5)
            label_title.configure(background='#fff')
            label_save_as = Label(self, text="Save as")
            label_save_as.grid(row=4, column=1, sticky=W, padx=10)
            label_save_as.configure(background='#fff')

            self.choose = StringVar()
            for id, value in enumerate(sorted(list_type)):
                if id == 0:
                    self.choose.set(value)
                R1 = Radiobutton(self, text=value, variable=self.choose,
                                 value=value, command=self.choose_save_as)
                R1.grid(row=5+id, column=1, sticky=W, padx=10)
                R1.configure(background='#fff')

            # menu dorpdown
            label_quality = Label(self, text="Quality")
            label_quality.grid(row=4, column=2, sticky=W)
            label_quality.configure(background='#fff')

            # list quality
            label_quality_select = Label(self)
            label_quality_select.grid(row=5, column=2, sticky=W, padx=10)
            label_quality_select.configure(background='#fff')

    def choose_save_as(self):
        quality_list = []
        self.choose_type = str(self.choose.get())
        if self.choose_type == 'audio':
            quality_list = self.get_audio(self.list_video)
        elif self.choose_type == 'video':
            quality_list = self.get_video(self.list_video)

        if quality_list:
            self.variable_quality = StringVar()
            self.variable_quality.set(quality_list[0])
            opt = OptionMenu(self, self.variable_quality, *quality_list)
            opt.config(width=15)
            opt.grid(row=5, column=2, sticky=W)

            self.variable_quality.trace("w", self.callback)

    def callback(self, *args):
        selection = str(self.variable_quality.get())
        if self.choose_type == 'video':
            resolution = selection.split('/')[0]
            mime_type = "video"+"/" + selection.split('/')[-1]
            your_choice = self.your_video.streams.filter(
                type='video', resolution=resolution, mime_type=mime_type)
        elif self.choose_type == 'audio':
            abr = selection.split('/')[-1]
            mime_type = "audio"+"/"+selection.split('/')[0]
            your_choice = self.your_video.streams.filter(
                type="audio", abr=abr, mime_type=mime_type)
        self.your_choice = your_choice

    # fungsi audio
    def get_audio(self, list_video):
        audio_quality = []
        for audio in list_video:
            if audio.type == 'audio' and audio.abr != None:
                qualilty = audio.mime_type.split('/')[-1] + "/" + audio.abr
                audio_quality.append(qualilty)
        audio_quality = set(audio_quality)
        audio_quality = list(audio_quality)
        return audio_quality

    # fungsi video
    def get_video(self, list_video):
        video_quality = []
        for video in list_video:
            if video.type == 'video' and video.resolution != None:
                qualilty = video.resolution + "/" + \
                    video.mime_type.split('/')[-1]
                video_quality.append(qualilty)
        video_quality = set(video_quality)
        video_quality = list(video_quality)
        return video_quality

    def show_progress_bar(self, stream, chunk, bytes_remaining):
        # loadingPercent label and bar configure value %
        self.progress['value'] = self.maxsizefile - bytes_remaining
        remaining = str(round(self.progress['value'] /
                              (1024**2), 2)) + "MB/" + str(round(self.maxsizefile/(1024**2), 2)) + "MB"
        self.label_remaining_download.config(text=remaining)
        self.loadingPercent.config(
            text=str(int(100 - (100*(bytes_remaining/self.maxsizefile)))) + " %")
        # show button 'done'
        if self.progress['value'] == self.maxsizefile:
            Button(self, text="Done", command=self.quit).grid(
                row=7, column=3, padx=5)

    def quit(self):
        self.destroy()

    def download(self):
        self.down.download(self.folder_downlaod)

    # on download
    def on_download(self):
        self.down = self.your_choice.first()
        if self.input_folder.get() != "select folder":
            self.folder_downlaod = self.input_folder.get()
        else:
            self.folder_downlaod = None

        self.maxsizefile = self.down.filesize

        # label loading percent
        self.loadingPercent = Label(
            self, text="0", fg="green", font=("Agency FB", 12))
        self.loadingPercent.grid(row=7, column=3, sticky=W)
        self.loadingPercent.configure(background='#fff')

        # to use progress bar
        self.progress = Progressbar(
            self, orient="horizontal", mode='determinate')
        self.progress.grid(row=7, column=1, columnspan=2,
                           sticky='nsew', padx=10, pady=10)
        self.progress['value'] = 0
        self.progress['maximum'] = self.maxsizefile

        # label remaining download
        self.remaining_download = "0MB/" + \
            str(round(self.maxsizefile/(1024**2), 2)) + "MB"
        self.label_remaining_download = Label(
            self, text=self.remaining_download)
        self.label_remaining_download.grid(row=8,  column=1, columnspan=2)
        self.label_remaining_download.configure(background='#fff')

        threading.Thread(target=self.your_video.register_on_progress_callback(
            self.show_progress_bar)).start()
        threading.Thread(target=self.download).start()


# Initialize APP
app = VideoYtDownload()
app.mainloop()
