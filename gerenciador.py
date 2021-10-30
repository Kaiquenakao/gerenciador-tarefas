import PySimpleGUI as sg
import platform
import socket
import psutil
import time

info = dict()
info['platform'] = platform.system()
info['platform-release'] = platform.release()
info['platform-version'] = platform.version()
info['architecture'] = platform.machine()
info['hostname'] = socket.gethostname()
info['processor'] = platform.processor()

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
        font=('Arial', 11))],
        [sg.Text(f"Arquitetura: {info['architecture']}",
                 font=('Arial', 11))],
        [sg.Text(f"Processador: {info['processor']}",
                 font=('Arial', 11))]
    ]
    return sg.Window(
        "Gerenciador",
        layout=layout,
        finalize=True,
        size=(500, 200),
        grab_anywhere=True
    )


janela = interface()

while True:
    window, event, value = sg.read_all_windows()

    if event == sg.WINDOW_CLOSED:
        break

