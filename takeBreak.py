import webbrowser
import tkinter
from tkinter import filedialog
import time
import pygame
from pygame import mixer

COUNT_BREAK = int(input('How many breaks do you want to take?: '))
BREAK_PERIOD = float(input('How much time do you want between breaks in hours? :'))
LOCATION_MUSIC = int(input('Where is your song located? Press "0" for local and "1" for an Internet URL: '))

if LOCATION_MUSIC == 0:
    def local():
        root = tkinter.Tk()
        root.withdraw()
        music_local = filedialog.askopenfilename(parent=root,title='Open music to play')
        BREAK_COUNT = 0
        while(BREAK_COUNT < COUNT_BREAK):
            time.sleep(BREAK_PERIOD * 60 * 60)
            print('Break has started at: ', time.ctime())
            pygame.mixer.init()
            pygame.mixer.music.load(music_local)
            pygame.mixer.music.play()
            BREAK_COUNT += 1
    local()

else:
    def youtube():
        music_link = input('Please enter the Youtube URL of your song: ')
        BREAK_COUNT = 0
        while(BREAK_COUNT < COUNT_BREAK):
            time.sleep(BREAK_PERIOD * 60 * 60)
            print('Break has started at: ', time.ctime())
            webbrowser.open(music_link)
            wenbrowser.close()
            BREAK_COUNT += 1

    youtube()
