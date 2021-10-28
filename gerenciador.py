import PySimpleGUI as sg
import platform
import psutil
import time


def interface():
    """Layout do gerenciador de tarefas"""
    sg.theme("DarkAmber")
    layout = [
        [sg.Text(
            "Gerenciador de Tarefas",
            font=('Arial', 13, 'bold'),
            size=(100,1),
            justification='center')],
    ]

    return sg.Window(
        "Gerenciador",
        layout=layout,
        finalize=True,
        size=(400, 200),
        grab_anywhere=True
    )


janela = interface()

while True:
    window, event, value = sg.read_all_windows()

    if event == sg.WINDOW_CLOSED:
        break

    if event == 'Enviar':
        sg.Popup("f")
