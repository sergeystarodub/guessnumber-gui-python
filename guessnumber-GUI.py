from tkinter import *

window = Tk()
window.title("Игра Угадай число")
window.geometry('400x600')
lblNameGame = Label(window, text='Игра Угадай число. Поиграем?')
# Разместил lblNameGame по центру по горизонтали
lblNameGame.grid(column=0, row=0, sticky='nsew')
window.grid_columnconfigure(0, weight=1)
#window.grid_rowconfigure(0, weight=1)
window.mainloop()