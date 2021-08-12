import pyautogui
import keyboard
import time
import os
import pyautogui
import pymsgbox
import zipfile
import win32

sign = '05225012302'
ttt = '4578Bra'

#os.chdir('C:\\'
#         'Users\\'
#         'Grupo Mateus\\'
#         'downloads\\')

if os.path.exists('C:\\' 'Users\\'
                  'Grupo Mateus\\'
                  'downloads\\D1021WMS_EstoquePickingWMS.zip'):
    pyautogui.alert("Já existe! Removendo D1021WMS_EstoquePickingWMS.zip...", timeout=3000)

    os.remove('C:\\'
              'Users\\'
              'Grupo Mateus\\'
              'downloads\\'
              'D1021WMS_EstoquePickingWMS.zip')
    pyautogui.alert("arquivo removido", timeout=3000)

pass

if os.path.exists('C:\\' 'Users\\'
                  'Grupo Mateus\\'
                  'downloads\\'
                  'D1021Auditoria_AuditoriaDaReposicaoWMS.zip'):

    pyautogui.alert("Já existe! Removendo Auditoria_AuditoriaDaReposicaoWMS.zip...", timeout=3000)

    os.remove('C:\\'
              'Users\\'
              'Grupo Mateus\\'
              'downloads\\'
              'D1021Auditoria_AuditoriaDaReposicaoWMS.zip')

    pyautogui.alert("arquivo removido", timeout=3000)



else:
    print("tem nada lá")

#baixando primeiro arquivo
#pyautogui.moveTo(305, 615)
#pyautogui.click()
#time.sleep(1)
#pyautogui.moveTo(666, 342)
#pyautogui.click()

#baixando segundo arquivo
#pyautogui.moveTo(305, 615)
#pyautogui.click()
#pyautogui.moveTo(302, 660)
#pyautogui.click()
#time.sleep(1)
#pyautogui.moveTo(666, 342)
#pyautogui.click()




