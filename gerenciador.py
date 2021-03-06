import platform
import socket
import psutil
import wmi
import PySimpleGUI as sg


computer = wmi.WMI()
proc_info = computer.Win32_Processor()[0]
gpu_info = computer.Win32_VideoController()[0]

info = dict()
info['platform'] = platform.system()
info['platform-release'] = platform.release()
info['platform-version'] = platform.version()
info['architecture'] = platform.machine()
info['hostname'] = socket.gethostname()
info['processor'] = proc_info.Name
info['ram'] = str(round(psutil.virtual_memory().total / (1024.0 ** 3)))
info['graphics-card'] = gpu_info.Name


estilo = ('Arial', 11)


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
                font=estilo)],
    [sg.Text(f"Processador: {info['processor']}",
                font=estilo)],
    [sg.Text(f"Hostname: {info['hostname']}",
                font=estilo)],
    [sg.Text(f"Memória RAM: {info['ram']} GB",
            font=estilo)],
    [sg.Text(f"Placa de Vídeo: {info['graphics-card']}",
            font=estilo)],
    [sg.Text(f'Memória usada:', 
            font=estilo),
    sg.Text(key="memory", size=(5, None), font=estilo)],
]

window =  sg.Window(
    "Gerenciador",
    layout=layout,
    finalize=True,
    size=(500, 250),
    grab_anywhere=True
)



while True:
    event, values = window.read(timeout=100)


    window['memory'].update(f'{psutil.virtual_memory()[2]} %')

    if event == sg.WINDOW_CLOSED:
        break

