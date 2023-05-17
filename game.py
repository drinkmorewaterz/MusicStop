import tkinter as tk
import pygame
import threading
import time
import random

pygame.init()
pygame.mixer.init()
root = tk.Tk()

def play_music():
    pygame.mixer.music.load(r'C:\Users\monke\Desktop\PYYYY\thegame\yo.mp3')
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def start_game():
    play_music()
    t = threading.Thread(target=stop_after_delay)
    t.start()

def stop_after_delay():
    global beg, over
    beg = int(entry_beg.get())
    over = int(entry_over.get())
    time.sleep(5)
    delay = random.randint(beg, over)
    time.sleep(delay)
    stop_music()

#Настраиваем окно
root.title("пампам")
root.geometry("1006x950")
bg_image = tk.PhotoImage(file=r"C:\Users\monke\Desktop\PYYYY\thegame\frogaga.png")
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0)

#Кнопка плей
play_image = tk.PhotoImage(file=r"C:\Users\monke\Desktop\PYYYY\thegame\p.png").subsample(2)
button_play = tk.Button(root, image=play_image, borderwidth=0, command=start_game)
button_play.place(x=300, y=200)

#Кнопка стоп
stop_image = tk.PhotoImage(file=r"C:\Users\monke\Desktop\PYYYY\thegame\s.png").subsample(2)
button_stop = tk.Button(root, image=stop_image, command=stop_music, borderwidth=0)
button_stop.place(x=600, y=200)

#задаем интервал
# label_beg = tk.Label(root, text="beg:")
# label_beg.place(x=0, y=0)
beg = 1
entry_beg = tk.Entry(root, text = 1, width=3)
entry_beg.insert(0, str(beg))
entry_beg.place(x=2, y=2)
entry_beg.config(bg="lightgreen")
# label_over = tk.Label(root, text="over:")
# label_over.place(x=0, y=30)
over = 20
entry_over = tk.Entry(root, text = 20)
entry_over.insert(0, str(over))
entry_over.config(bg="pink")
entry_over.place(x=2, y=25, width=22)

root.mainloop()