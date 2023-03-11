import PySimpleGUI as sg
from pathlib import Path
import csv

# sg.theme('DarkBlue14')
sg.theme('Reddit')


#definicion de Ventana principal(Menu)
def Menu():
    layout = [
    [sg.Text('Hola,en que linea estas trabajando?')],
    [sg.Push(),sg.Button('Linea 1',size=(10,1),border_width=5),sg.Push()],
    [sg.Push(),sg.Button('Linea 2',size=(10,1),border_width=5),sg.Push()],
    [sg.Push(),sg.Button('Linea 3',size=(10,1),border_width=5),sg.Push()],
    [sg.Push(),sg.Button('Linea 4',size=(10,1),border_width=5),sg.Push()]
]
    return sg.Window('App TPM',layout,finalize=True,resizable=True)#,location=(500,100))


#definicion de Ventana(Equipos por linea)
def window_linea_1():
    layouts = [
        [sg.Text('Selecciona la maquina a la cual le daras el TPM')],
        [sg.Push(),sg.Button('CP11',border_width=5),sg.Button('CP12',border_width=5),sg.Button('QP11',border_width=5),sg.Push()],
        [sg.Push(),sg.Button('QP12',border_width=5),sg.Button('DEK1',border_width=5),sg.Button('HORNO1',border_width=5),sg.Push()],
        [sg.Push(),sg.Button('Regresar',key='-BACK-',border_width=5),sg.Push()]
    ]
    return sg.Window('Linea 1',layouts,finalize=True)#,no_titlebar=False)#,location=(470,300))

def window_linea_2():
    layouts = [
        [sg.Text('Selecciona la maquina a la cual le daras el TPM')],
        [sg.Push(),sg.Button('CP21',border_width=5),sg.Button('CP22',border_width=5),sg.Button('QP21',border_width=5),sg.Push()],
        [sg.Push(),sg.Button('QP22',border_width=5),sg.Button('DEK2',border_width=5),sg.Button('HORNO2',border_width=5),sg.Push()],
        [sg.Push(),sg.Button('Regresar',key='-BACK-',border_width=5),sg.Push()]
    ]
    return sg.Window('Linea 2',layouts,finalize=True)#,no_titlebar=True)


def window_linea_3():
    layouts = [
        [sg.Text('Selecciona la maquina a la cual le daras el TPM')],
        [sg.Push(),sg.Button('CP31',border_width=5),sg.Button('CP32',border_width=5),sg.Button('QP31',border_width=5),sg.Push()],
        [sg.Push(),sg.Button('QP32',border_width=5),sg.Button('DEK3',border_width=5),sg.Button('HORNO3',border_width=5),sg.Push()],
        [sg.Push(),sg.Button('Regresar',key='-BACK-',border_width=5),sg.Push()]
    ]
    return sg.Window('Linea 3',layouts,finalize=True)#,no_titlebar=True)


def window_linea_4():
    layouts = [
        [sg.Text('Selecciona la maquina a la cual le daras el TPM')],
        [sg.Push(),sg.Button('CP41',border_width=5),sg.Button('QP41',border_width=5),sg.Push()],
        [sg.Push(),sg.Button('DEK4',border_width=5),sg.Button('HORNO4',border_width=5),sg.Push()],
        [sg.Push(),sg.Button('Regresar',key='-BACK-',border_width=5),sg.Push()]
    ]
    return sg.Window('Linea 4',layouts,finalize=True)#,no_titlebar=True)

#definicion de Ventana(individual por equipo)
#LINEA 1
def CP11():
    layout = [
    [sg.Push(),sg.Text("Ingresa tu Nombre:"),sg.Input(size=(10,1),key='-NACP11-',enable_events=True),sg.Push()],
    [sg.Push(),sg.Text("Numero de empleado:"),sg.Input(size=(6,1),key='-NOCP11-',enable_events=True),sg.Push()],
    [sg.Push(),sg.Text("Numero semana del año:"),sg.Input(size=(3,1),key='-NSCP11-',enable_events=True),sg.Push()],
    [sg.Push(),sg.Button('Guardar',key='-SVCP11-'),sg.Button('Exit'),sg.Push()]
    ]
    return sg.Window('CP11',layout,finalize=True,no_titlebar=False)


def CP12():
    layout = [
    [sg.Push(),sg.Text("Ingresa tu Nombre: "),sg.Input(size=(10,1),key='-NACP12-',enable_events=True),sg.Push()],
    [sg.Push(),sg.Text("Numero de empleado: "),sg.Input(size=(6,1),key='-NOCP12-',enable_events=True),sg.Push()],
    [sg.Push(),sg.Text("Numero semana del año: "),sg.Input(size=(3,1),key='-NSCP12-',enable_events=True),sg.Push()],
    [sg.Push(),sg.Button('Guardar',key='-SVCP12-'),sg.Button('Exit'),sg.Push()]
    ]
    return sg.Window('CP12',layout,finalize=True,no_titlebar=False)

def QP11():
    layout = [
    [sg.Push(),sg.Text("Ingresa tu Nombre: "),sg.Input(size=(10,1),key='-NAQP11-',enable_events=True),sg.Push()],
    [sg.Push(),sg.Text("Numero de empleado: "),sg.Input(size=(6,1),key='-NOQP11-',enable_events=True),sg.Push()],
    [sg.Push(),sg.Text("Numero semana del año: "),sg.Input(size=(3,1),key='-NSQP11-',enable_events=True),sg.Push()],
    [sg.Push(),sg.Button('Guardar',key='-SVQP11-'),sg.Button('Exit'),sg.Push()]
    ]
    return sg.Window('QP11',layout,finalize=True,no_titlebar=False)

def QP12():
    layout = [
    [sg.Push(),sg.Text("Ingresa tu Nombre: "),sg.Input(size=(10,1),key='-NAQP12-',enable_events=True),sg.Push()],
    [sg.Push(),sg.Text("Numero de empleado: "),sg.Input(size=(6,1),key='-NOQP12-',enable_events=True),sg.Push()],
    [sg.Push(),sg.Text("Numero semana del año: "),sg.Input(size=(3,1),key='-NSQP12-',enable_events=True),sg.Push()],
    [sg.Push(),sg.Button('Guardar',key='-SVQP12-'),sg.Button('Exit'),sg.Push()]
    ]
    return sg.Window('QP12',layout,finalize=True,no_titlebar=False)

def DEK1():
    layout = [
    [sg.Push(),sg.Text("Ingresa tu Nombre: "),sg.Input(size=(10,1),key='-NADEK1-',enable_events=True),sg.Push()],
    [sg.Push(),sg.Text("Numero de empleado: "),sg.Input(size=(6,1),key='-NODEK1-',enable_events=True),sg.Push()],
    [sg.Push(),sg.Text("Numero semana del año: "),sg.Input(size=(3,1),key='-NSDEK1-',enable_events=True),sg.Push()],
    [sg.Push(),sg.Button('Guardar',key='-SVDEK1-'),sg.Button('Exit'),sg.Push()]
    ]
    return sg.Window('DEK1',layout,finalize=True,no_titlebar=False)

def HORNO1():
    layout = [
    [sg.Push(),sg.Text("Ingresa tu Nombre: "),sg.Input(size=(10,1),key='-NAHOR1-',enable_events=True),sg.Push()],
    [sg.Push(),sg.Text("Numero de empleado: "),sg.Input(size=(6,1),key='-NOHOR1-',enable_events=True),sg.Push()],
    [sg.Push(),sg.Text("Numero semana del año: "),sg.Input(size=(3,1),key='-NSHOR1-',enable_events=True),sg.Push()],
    [sg.Push(),sg.Button('Guardar',key='-SVHOR1-'),sg.Button('Exit'),sg.Push()]
    ]
    return sg.Window('HORNO1',layout,finalize=True,no_titlebar=False)

#LINEA 2
def CP21():
    layout = [
    [sg.Push(),sg.Text("Ingresa tu Nombre: "),sg.Input(size=(10,1),key='-NACP21-',enable_events=True),sg.Push()],
    [sg.Push(),sg.Text("Numero de empleado: "),sg.Input(size=(6,1),key='-NOCP21-',enable_events=True),sg.Push()],
    [sg.Push(),sg.Text("Numero semana del año: "),sg.Input(size=(3,1),key='-NSCP21-',enable_events=True),sg.Push()],
    [sg.Push(),sg.Button('Guardar',key='-SVCP21-'),sg.Button('Exit'),sg.Push()]
    ]
    return sg.Window('CP21',layout,finalize=True,no_titlebar=False)

def CP22():
    layout = [
    [sg.Push(),sg.Text("Ingresa tu Nombre: "),sg.Input(size=(10,1),key='-NACP22-',enable_events=True),sg.Push()],
    [sg.Push(),sg.Text("Numero de empleado: "),sg.Input(size=(6,1),key='-NOCP22-',enable_events=True),sg.Push()],
    [sg.Push(),sg.Text("Numero semana del año: "),sg.Input(size=(3,1),key='-NSCP22-',enable_events=True),sg.Push()],
    [sg.Push(),sg.Button('Guardar',key='-SVCP22-'),sg.Button('Exit'),sg.Push()]
    ]
    return sg.Window('CP22',layout,finalize=True,no_titlebar=False)

def QP21():
    layout = [
    [sg.Push(),sg.Text("Ingresa tu Nombre: "),sg.Input(size=(10,1),key='-NAQP21-',enable_events=True),sg.Push()],
    [sg.Push(),sg.Text("Numero de empleado: "),sg.Input(size=(6,1),key='-NOQP21-',enable_events=True),sg.Push()],
    [sg.Push(),sg.Text("Numero semana del año: "),sg.Input(size=(3,1),key='-NSQP21-',enable_events=True),sg.Push()],
    [sg.Push(),sg.Button('Guardar',key='-SVQP21-'),sg.Button('Exit'),sg.Push()]
    ]
    return sg.Window('QP21',layout,finalize=True,no_titlebar=False)

def QP22():
    layout = [
    [sg.Push(),sg.Text("Ingresa tu Nombre: "),sg.Input(size=(10,1),key='-NAQP22-',enable_events=True),sg.Push()],
    [sg.Push(),sg.Text("Numero de empleado: "),sg.Input(size=(6,1),key='-NOQP22-',enable_events=True),sg.Push()],
    [sg.Push(),sg.Text("Numero semana del año: "),sg.Input(size=(3,1),key='-NSQP22-',enable_events=True),sg.Push()],
    [sg.Push(),sg.Button('Guardar',key='-SVQP22-'),sg.Button('Exit'),sg.Push()]
    ]
    return sg.Window('QP22',layout,finalize=True,no_titlebar=False)

def DEK2():
    layout = [
    [sg.Push(),sg.Text("Ingresa tu Nombre: "),sg.Input(size=(10,1),key='-NADEK2-',enable_events=True),sg.Push()],
    [sg.Push(),sg.Text("Numero de empleado: "),sg.Input(size=(6,1),key='-NODEK2-',enable_events=True),sg.Push()],
    [sg.Push(),sg.Text("Numero semana del año: "),sg.Input(size=(3,1),key='-NSDEK2-',enable_events=True),sg.Push()],
    [sg.Push(),sg.Button('Guardar',key='-SVDEK2-'),sg.Button('Exit'),sg.Push()]
    ]
    return sg.Window('DEK2',layout,finalize=True,no_titlebar=False)

def HORNO2():
    layout = [
    [sg.Push(),sg.Text("Ingresa tu Nombre: "),sg.Input(size=(10,1),key='-NAHOR2-',enable_events=True),sg.Push()],
    [sg.Push(),sg.Text("Numero de empleado: "),sg.Input(size=(6,1),key='-NOHOR2-',enable_events=True),sg.Push()],
    [sg.Push(),sg.Text("Numero semana del año: "),sg.Input(size=(3,1),key='-NSHOR2-',enable_events=True),sg.Push()],
    [sg.Push(),sg.Button('Guardar',key='-SVHOR2-'),sg.Button('Exit'),sg.Push()]
    ]
    return sg.Window('HORNO2',layout,finalize=True,no_titlebar=False)
#LINEA 3
def CP31():
    layout = [
    [sg.Push(),sg.Text("Ingresa tu Nombre: "),sg.Input(size=(10,1),key='-NACP31-',enable_events=True),sg.Push()],
    [sg.Push(),sg.Text("Numero de empleado: "),sg.Input(size=(6,1),key='-NOCP31-',enable_events=True),sg.Push()],
    [sg.Push(),sg.Text("Numero semana del año: "),sg.Input(size=(3,1),key='-NSCP31-',enable_events=True),sg.Push()],
    [sg.Push(),sg.Button('Guardar',key='-SVCP31-'),sg.Button('Exit'),sg.Push()]
    ]
    return sg.Window('CP31',layout,finalize=True,no_titlebar=False)

def CP32():
    layout = [
    [sg.Push(),sg.Text("Ingresa tu Nombre: "),sg.Input(size=(10,1),key='-NACP32-',enable_events=True),sg.Push()],
    [sg.Push(),sg.Text("Numero de empleado: "),sg.Input(size=(6,1),key='-NOCP32-',enable_events=True),sg.Push()],
    [sg.Push(),sg.Text("Numero semana del año: "),sg.Input(size=(3,1),key='-NSCP32-',enable_events=True),sg.Push()],
    [sg.Push(),sg.Button('Guardar',key='-SVCP32-'),sg.Button('Exit'),sg.Push()]
    ]
    return sg.Window('CP32',layout,finalize=True,no_titlebar=False)

def QP31():
    layout = [
    [sg.Push(),sg.Text("Ingresa tu Nombre: "),sg.Input(size=(10,1),key='-NAQP31-',enable_events=True),sg.Push()],
    [sg.Push(),sg.Text("Numero de empleado: "),sg.Input(size=(6,1),key='-NOQP31-',enable_events=True),sg.Push()],
    [sg.Push(),sg.Text("Numero semana del año: "),sg.Input(size=(3,1),key='-NSQP31-',enable_events=True),sg.Push()],
    [sg.Push(),sg.Button('Guardar',key='-SVQP31-'),sg.Button('Exit'),sg.Push()]
    ]
    return sg.Window('QP31',layout,finalize=True,no_titlebar=False)

def QP32():
    layout = [
    [sg.Push(),sg.Text("Ingresa tu Nombre: "),sg.Input(size=(10,1),key='-NAQP32-',enable_events=True),sg.Push()],
    [sg.Push(),sg.Text("Numero de empleado: "),sg.Input(size=(6,1),key='-NOQP32-',enable_events=True),sg.Push()],
    [sg.Push(),sg.Text("Numero semana del año: "),sg.Input(size=(3,1),key='-NSQP32-',enable_events=True),sg.Push()],
    [sg.Push(),sg.Button('Guardar',key='-SVQP32-'),sg.Button('Exit'),sg.Push()]
    ]
    return sg.Window('QP32',layout,finalize=True,no_titlebar=False)

def DEK3():
    layout = [
    [sg.Push(),sg.Text("Ingresa tu Nombre: "),sg.Input(size=(10,1),key='-NADEK3-',enable_events=True),sg.Push()],
    [sg.Push(),sg.Text("Numero de empleado: "),sg.Input(size=(6,1),key='-NODEK3-',enable_events=True),sg.Push()],
    [sg.Push(),sg.Text("Numero semana del año: "),sg.Input(size=(3,1),key='-NSDEK3-',enable_events=True),sg.Push()],
    [sg.Push(),sg.Button('Guardar',key='-SVDEK3-'),sg.Button('Exit'),sg.Push()]
    ]
    return sg.Window('DEK3',layout,finalize=True,no_titlebar=False)

def HORNO3():
    layout = [
    [sg.Push(),sg.Text("Ingresa tu Nombre: "),sg.Input(size=(10,1),key='-NAHOR3-',enable_events=True),sg.Push()],
    [sg.Push(),sg.Text("Numero de empleado: "),sg.Input(size=(6,1),key='-NOHOR3-',enable_events=True),sg.Push()],
    [sg.Push(),sg.Text("Numero semana del año: "),sg.Input(size=(3,1),key='-NSHOR3-',enable_events=True),sg.Push()],
    [sg.Push(),sg.Button('Guardar',key='-SVHOR3-'),sg.Button('Exit'),sg.Push()]
    ]
    return sg.Window('HORNO3',layout,finalize=True,no_titlebar=False)

#LINEA 4
def CP41():
    layout = [
    [sg.Push(),sg.Text("Ingresa tu Nombre:"),sg.Input(size=(10,1),key='-NACP41-',enable_events=True),sg.Push()],
    [sg.Push(),sg.Text("Numero de empleado:"),sg.Input(size=(6,1),key='-NOCP41-',enable_events=True),sg.Push()],
    [sg.Push(),sg.Text("Numero semana del año:"),sg.Input(size=(3,1),key='-NSCP41-',enable_events=True),sg.Push()],
    [sg.Push(),sg.Button('Guardar',key='-SVCP41-'),sg.Button('Exit'),sg.Push()]
    ]
    return sg.Window('CP41',layout,finalize=True,no_titlebar=False)

def QP41():
    layout = [
    [sg.Push(),sg.Text("Ingresa tu Nombre:"),sg.Input(size=(10,1),key='-NAQP41-',enable_events=True),sg.Push()],
    [sg.Push(),sg.Text("Numero de empleado:"),sg.Input(size=(6,1),key='-NOQP41-',enable_events=True),sg.Push()],
    [sg.Push(),sg.Text("Numero semana del año:"),sg.Input(size=(3,1),key='-NSQP41-',enable_events=True),sg.Push()],
    [sg.Push(),sg.Button('Guardar',key='-SVQP41-'),sg.Button('Exit'),sg.Push()]
    ]
    return sg.Window('QP41',layout,finalize=True,no_titlebar=False)

def DEK4():
    layout = [
    [sg.Push(),sg.Text("Ingresa tu Nombre:"),sg.Input(size=(10,1),key='-NADEK4-',enable_events=True),sg.Push()],
    [sg.Push(),sg.Text("Numero de empleado:"),sg.Input(size=(6,1),key='-NODEK4-',enable_events=True),sg.Push()],
    [sg.Push(),sg.Text("Numero semana del año:"),sg.Input(size=(3,1),key='-NSDEK4-',enable_events=True),sg.Push()],
    [sg.Push(),sg.Button('Guardar',key='-SVDEK4-'),sg.Button('Exit'),sg.Push()]
    ]
    return sg.Window('DEK4',layout,finalize=True,no_titlebar=False)

def HORNO4():
    layout = [
    [sg.Push(),sg.Text("Ingresa tu Nombre:"),sg.Input(size=(10,1),key='-NAHOR4-',enable_events=True),sg.Push()],
    [sg.Push(),sg.Text("Numero de empleado:"),sg.Input(size=(6,1),key='-NOHOR4-',enable_events=True),sg.Push()],
    [sg.Push(),sg.Text("Numero semana del año:"),sg.Input(size=(3,1),key='-NSHOR4-',enable_events=True),sg.Push()],
    [sg.Push(),sg.Button('Guardar',key='-SVHOR4-'),sg.Button('Exit'),sg.Push()]
    ]
    return sg.Window('HORNO4',layout,finalize=True,no_titlebar=False)


#definicion de ventana de guardado
def ventana_guardado():
    layout = [
            [sg.Text('Datos Guardados')],
            [sg.Push(),sg.Button('Exit',key='-DATOS-'),sg.Push()]]
    return sg.Window('Guardado',layout,finalize=True)

#Setup(Corre App)/loop(Corre App)
def main():
    window1,window2,window3,window4 = Menu(),None,None,None
    while True:
        window,event,values = sg.read_all_windows()
        if event == sg.WIN_CLOSED or event == 'Exit':
            window.close()
            if window == window2:
                window2 = None
            elif window == window3:
                window3 = None
            elif window == window4:
                window4 = None
            elif window == window1:
                break
        elif event == 'Linea 1':
            window2 = window_linea_1()
        elif event == 'Linea 2':
            window2 = window_linea_2()
        elif event == 'Linea 3':
            window2 = window_linea_3()
        elif event == 'Linea 4':
            window2 = window_linea_4()
        if event == '-BACK-':
            window.close()


        #ventana emergente
        if event == 'CP11':
            window3 = CP11()
        elif event == 'CP12':
            CP12()
        elif event == 'QP11':
            QP11()
        elif event == 'QP12':
            QP12()
        elif event == 'CP21':
            CP21()
        elif event == 'CP22':
            CP22()
        elif event == 'QP21':
            QP21()
        elif event == 'QP22':
            QP22()
        elif event == 'CP31':
            CP31()
        elif event == 'CP32':
            CP32()
        elif event == 'QP31':
            QP31()
        elif event == 'QP32':
            QP32()
        elif event == 'CP41':
            CP41()
        elif event == 'QP41':
            QP41()
        elif event == 'DEK1':
            DEK1()
        elif event == 'HORNO1':
            HORNO1()
        elif event == 'DEK2':
            DEK2()
        elif event == 'HORNO2':
            HORNO2()
        elif event == 'DEK3':
            DEK3()
        elif event == 'HORNO3':
            HORNO3()
        elif event == 'DEK4':
            DEK4()
        elif event == 'HORNO4':
            HORNO4()
            
    
        #almacenar datos de operador
        # if event == 'Guardar':
        #     file_path = sg.popup_get_file('Save as',no_window = True, save_as = True) + '.txt'
        #     file = Path(file_path)
        #     file.write_text(values['-INCP11-'])\
            
        if event == '-SVCP11-':
            with open(r'H:\Temporal\Echevarria\proyects\PysimpleGUI\Proyectos\app_tpm\LINEA 1\Datos Operadores.csv','a') as f:
                f.write(values['-NACP11-']+ "," + values['-NOCP11-']+ "," +values['-NSCP11-'] + '\n')
                ventana_guardado()
                
        if event == '-SVCP12-':
            with open(r'H:\Temporal\Echevarria\proyects\PysimpleGUI\Proyectos\app_tpm\LINEA 1\Datos Operadores.csv','a') as f:
                f.write(values['-NACP12-']+ "," + values['-NOCP12-']+ "," +values['-NSCP12-'] + '\n')
                ventana_guardado()
                
        if event == '-SVQP11-':
            with open(r'H:\Temporal\Echevarria\proyects\PysimpleGUI\Proyectos\app_tpm\LINEA 1\Datos Operadores.csv','a') as f:
                f.write(values['-NAQP11-']+ "," + values['-NOQP11-']+ "," +values['-NSQP11-'] + '\n')
                ventana_guardado()
                
        if event == '-SVQP12-':
            with open(r'H:\Temporal\Echevarria\proyects\PysimpleGUI\Proyectos\app_tpm\LINEA 1\Datos Operadores.csv','a') as f:
                f.write(values['-NAQP12-']+ "," + values['-NOQP12-']+ "," +values['-NSQP12-'] + '\n')
                ventana_guardado()
                
        if event == '-SVDEK1-':
            with open(r'H:\Temporal\Echevarria\proyects\PysimpleGUI\Proyectos\app_tpm\LINEA 1\Datos Operadores.csv','a') as f:
                f.write(values['-NADEK1-']+ "," + values['-NODEK1-']+ "," +values['-NSDEK1-'] + '\n')
                ventana_guardado()
                
        if event == '-SVHOR1-':
            with open(r'H:\Temporal\Echevarria\proyects\PysimpleGUI\Proyectos\app_tpm\LINEA 1\Datos Operadores.csv','a') as f:
                f.write(values['-NAHOR1-']+ "," + values['-NOHOR1-']+ "," +values['-NSHOR1-'] + '\n')
                ventana_guardado()
                
        if event == '-SVCP21-':
            with open(r'H:\Temporal\Echevarria\proyects\PysimpleGUI\Proyectos\app_tpm\LINEA 2\Datos Operadores.csv','a') as f:
                f.write(values['-NACP21-']+ "," + values['-NOCP21-']+ "," +values['-NSCP21-'] + '\n')
                ventana_guardado()
                
        if event == '-SVCP22-':
            with open(r'H:\Temporal\Echevarria\proyects\PysimpleGUI\Proyectos\app_tpm\LINEA 2\Datos Operadores.csv','a') as f:
                f.write(values['-NACP22-']+ "," + values['-NOCP22-']+ "," +values['-NSCP22-'] + '\n')
                ventana_guardado()
                
        if event == '-SVQP21-':
            with open(r'H:\Temporal\Echevarria\proyects\PysimpleGUI\Proyectos\app_tpm\LINEA 2\Datos Operadores.csv','a') as f:
                f.write(values['-NAQP21-']+ "," + values['-NOQP21-']+ "," +values['-NSQP21-'] + '\n')
                ventana_guardado()
                
        if event == '-SVQP22-':
            with open(r'H:\Temporal\Echevarria\proyects\PysimpleGUI\Proyectos\app_tpm\LINEA 2\Datos Operadores.csv','a') as f:
                f.write(values['-NAQP22-']+ "," + values['-NOQP22-']+ "," +values['-NSQP22-'] + '\n')
                ventana_guardado()
                
        if event == '-SVDEK2-':
            with open(r'H:\Temporal\Echevarria\proyects\PysimpleGUI\Proyectos\app_tpm\LINEA 2\Datos Operadores.csv','a') as f:
                f.write(values['-NADEK2-']+ "," + values['-NODEK2-']+ "," +values['-NSDEK2-'] + '\n')
                ventana_guardado()
                
        if event == '-SVHOR2-':
            with open(r'H:\Temporal\Echevarria\proyects\PysimpleGUI\Proyectos\app_tpm\LINEA 2\Datos Operadores.csv','a') as f:
                f.write(values['-NAHOR2-']+ "," + values['-NOHOR2-']+ "," +values['-NSHOR2-'] + '\n')
                ventana_guardado()
        
        if event == '-SVCP31-':
            with open(r'H:\Temporal\Echevarria\proyects\PysimpleGUI\Proyectos\app_tpm\LINEA 3\Datos Operadores.csv','a') as f:
                f.write(values['-NACP31-']+ "," + values['-NOCP31-']+ "," +values['-NSCP31-'] + '\n')
                ventana_guardado()
        
        if event == '-SVCP32-':
            with open(r'H:\Temporal\Echevarria\proyects\PysimpleGUI\Proyectos\app_tpm\LINEA 3\Datos Operadores.csv','a') as f:
                f.write(values['-NACP32-']+ "," + values['-NOCP32-']+ "," +values['-NSCP32-'] + '\n')
                ventana_guardado()
        
        if event == '-SVQP31-':
            with open(r'H:\Temporal\Echevarria\proyects\PysimpleGUI\Proyectos\app_tpm\LINEA 3\Datos Operadores.csv','a') as f:
                f.write(values['-NAQP31-']+ "," + values['-NOQP31-']+ "," +values['-NSQP31-'] + '\n')
                ventana_guardado()
                
        if event == '-SVQP32-':
            with open(r'H:\Temporal\Echevarria\proyects\PysimpleGUI\Proyectos\app_tpm\LINEA 3\Datos Operadores.csv','a') as f:
                f.write(values['-NAQP32-']+ "," + values['-NOQP32-']+ "," +values['-NSQP32-'] + '\n')
                ventana_guardado()
                
        if event == '-SVDEK3-':
            with open(r'H:\Temporal\Echevarria\proyects\PysimpleGUI\Proyectos\app_tpm\LINEA 3\Datos Operadores.csv','a') as f:
                f.write(values['-NADEK3-']+ "," + values['-NODEK3-']+ "," +values['-NSDEK3-'] + '\n')
                ventana_guardado()
        
        if event == '-SVHOR3-':
            with open(r'H:\Temporal\Echevarria\proyects\PysimpleGUI\Proyectos\app_tpm\LINEA 3\Datos Operadores.csv','a') as f:
                f.write(values['-NAHOR3-']+ "," + values['-NOHOR3-']+ "," +values['-NSHOR3-'] + '\n')
                ventana_guardado()
        
        if event == '-SVCP41-':
            with open(r'H:\Temporal\Echevarria\proyects\PysimpleGUI\Proyectos\app_tpm\LINEA 4\Datos Operadores.csv','a') as f:
                f.write(values['-NACP41-']+ "," + values['-NOCP41-']+ "," +values['-NSCP41-'] + '\n')
                ventana_guardado()
                
        if event == '-SVQP41-':
            with open(r'H:\Temporal\Echevarria\proyects\PysimpleGUI\Proyectos\app_tpm\LINEA 4\Datos Operadores.csv','a') as f:
                f.write(values['-NAQP41-']+ "," + values['-NOQP41-']+ "," +values['-NSQP41-'] + '\n')
                ventana_guardado()
                
        if event == '-SVDEK4-':
            with open(r'H:\Temporal\Echevarria\proyects\PysimpleGUI\Proyectos\app_tpm\LINEA 4\Datos Operadores.csv','a') as f:
                f.write(values['-NADEK4-']+ "," + values['-NODEK4-']+ "," +values['-NSDEK4-'] + '\n')
                ventana_guardado()
        
        if event == '-SVHOR4-':
            with open(r'H:\Temporal\Echevarria\proyects\PysimpleGUI\Proyectos\app_tpm\LINEA 4\Datos Operadores.csv','a') as f:
                f.write(values['-NAHOR4-']+ "," + values['-NOHOR4-']+ "," +values['-NSHOR4-'] + '\n')
                ventana_guardado()
        
        if event == '-DATOS-':
            exit()

                    











if __name__ == '__main__':
    main()




# while True:
#     event, values = window.read()
#     if event in (None, 'Cancel'):
#         break

#     if event == 'Linea 1':
#         window_linea_1()
#     if event == 'Linea 2':
#         sg.popup('Hola,en la linea 2')
#     if event == 'Linea 3':
#         sg.popup('Hola,en la linea 3')
#     if event == 'Linea 4':
#         sg.popup('Hola,en la linea 4')


# # 5 - Close window
# window.close()