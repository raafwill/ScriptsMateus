# deeclarando variáveis e funções importantes
import keyboard
import pyautogui
import time
import os
import webbrowser

cpf           = "05225012302" #Var cpf
senhagmcore   = "4578abc" #var senha gmcore
rotina1021    = "1021" #var rotina 10 21
rotina422     = "422" #var rotina 422
rotina999     = "999" #var rotina 999
R1021_lista   = list(rotina1021) #var da lista de rotina 1021
R422_lista    = list(rotina422) #var da lista de rotina 422
R999_lista    = list(rotina999) #var da lista de rotina 999
cpflist       = list(cpf)  #var da lista de cpf
senhalista    = list(senhagmcore)  #var da lista de senha
gerenciador   = "http://192.168.6.47/"
chrome        = 'C:\Program Files\Google\Chrome\Application\chrome.exe %s'


# deeclarando variáveis de credenciais e rotinas
# # abrir gmcore

def abrir_gmcore():
    os.startfile("C:\Program Files (x86)\Remote Desktop Organizer\RDO.exe")
    time.sleep(5)

def acessar_credenciais():
    abrir_gmcore()
    # # abre o estoque
    time.sleep(4)
    pyautogui.moveTo(38, 36)
    pyautogui.click()
    pyautogui.moveTo(61, 130)
    pyautogui.doubleClick()
    time.sleep(4)
    # # digitar credenciais
    pyautogui.moveTo(421, 291)
    pyautogui.click()
    time.sleep(3)

    for c in cpflist:
        keyboard.press(c)
    pyautogui.alert("digitado o " + cpf, "VALIDAÇÃO DE CREDENCIAL", "Confirma, meu?", timeout=3000)

    keyboard.press('enter')

    for s in senhalista:
        keyboard.press(s)
    time.sleep(4)

    keyboard.press('enter')
    time.sleep(4)
    pyautogui.moveTo(389, 192)
    pyautogui.click()
    time.sleep(12)

def acesso_menu():
    time.sleep(10)
    pyautogui.moveTo(98, 752)
    pyautogui.click()
    time.sleep(3)
    pyautogui.moveTo(407, 200)
    pyautogui.click()

def acesso_R1021():
    # acessando rotina 1021
    time.sleep(15)
    for r in R1021_lista:
        keyboard.press(r)
    time.sleep(2)
    keyboard.press_and_release('enter')

def acesso_R422():
    # acessando rotina 1021
    time.sleep(15)
    for r in rotina422:
        keyboard.press(r)
    time.sleep(2)
    keyboard.press_and_release('enter')

def abrir_gerenciador():
    webbrowser.get(chrome).open(gerenciador)
