from pytube import *
from tkinter.filedialog import *
from tkinter import *
from tkinter.messagebox import *
from threading import *
from tkinter.ttk import *

url = "https://www.youtube.com/watch?v=hip-_JbR888"

ob= YouTube(url)
path_to_save_video = "C:\\Users\\Rc\\Desktop"
strms= ob.streams.first()
'''for s in strms:
    print(s)
    '''
print(strms)
file_size=strms.filesize
print(file_size)
