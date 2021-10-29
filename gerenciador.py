import PySimpleGUI as sg
import platform
import psutil
import time

info = {}
info['platform'] = platform.system()
info['platform-release'] = platform.release()
info['platform-version'] = platform.version()

def interface():
    """Layout do gerenciador de tarefas"""
    sg.theme("DarkAmber")
    layout = [
        [sg.Text(
            "Gerenciador de Tarefas",
            font=('Arial', 13, 'bold'),
            size=(100,1),
            justification='center')],
        [sg.Text(
            f"Sistema operacional: {info['platform']} {info['platform-release']} - {info['platform-version']}",
        font=('Arial', 11))]
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
