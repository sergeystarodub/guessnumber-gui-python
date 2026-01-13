from tkinter import *

window = Tk()
window.title("Игра Угадай число")
window.geometry('400x600')

# Разместил lblNameGame по центру по горизонтали
#lblNameGame.grid(column=0, row=0, sticky='nsew')
# 1. Label по центру (занимает 2 колонки)
# sticky="" (без параметров) или "n s e w" вместе с columnspan центрирует текст
lblNameGame = Label(window, text='Игра Угадай число. Поиграем?')
lblNameGame.grid(column=0, row=0, columnspan=2, pady=10, sticky="we")
# Настраиваем веса колонок, чтобы они расширялись и делили экран пополам
window.grid_columnconfigure(0, weight=1)
#window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)

# 2. Label и Entry на следующей строке (каждый в своей колонке)
lblNumberPlayers = Label(window, text='Укажите количество игроков ')
#старый код для сравнения с новым - потом удалить
#lblNumberPlayers.grid(column=0, row=1)
#txtNumberPlayers = Entry(window, width=5)
#txtNumberPlayers.grid(column=1, row=1)

# прижат к правому краю колонки
lblNumberPlayers.grid(column=0, row=1, padx=5, pady=5, sticky="e")
txtNumberPlayers = Entry(window, width=5)
# прижат к левому краю колонки
txtNumberPlayers.grid(column=1, row=1, padx=5, pady=5, sticky="w")


window.mainloop()