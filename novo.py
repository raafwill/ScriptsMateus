import pyautogui
import keyboard
import time
import os
import pyautogui
import pymsgbox
import zipfile
import shutil

sign = '05225012302'
ttt = '4578Bra'

#os.chdir('C:\\'
#         'Users\\'
#         'Grupo Mateus\\'
#         'downloads\\')

baixando primeiro arquivo
pyautogui.moveTo(305, 615)
pyautogui.click()
time.sleep(1)
pyautogui.moveTo(666, 342)
pyautogui.click()

baixando segundo arquivo
pyautogui.moveTo(305, 615)
pyautogui.click()
pyautogui.moveTo(302, 660)
pyautogui.click()
time.sleep(1)
pyautogui.moveTo(666, 342)
pyautogui.click()

with zipfile.ZipFile('C:\\' 'Users\\'
                     'Grupo Mateus\\'
                     'downloads\\'
                     'D1021Auditoria_AuditoriaDaReposicaoWMS.zip') as zip_ref:

    zip_ref.extractall('C:\\'
                       'Users\\'
                       'Grupo Mateus\\'
                       'downloads\\')

with zipfile.ZipFile('C:\\' 'Users\\'
                     'Grupo Mateus\\'
                     'downloads\\'
                     'D1021WMS_EstoquePickingWMS.zip') as zip_ref:

    zip_ref.extractall('C:\\'
                       'Users\\'
                       'Grupo Mateus\\'
                       'downloads\\')



os.remove('C:\\Mateus\\17.GMCORE\\D1021Auditoria_AuditoriaDaReposicaoWMS.csv')
os.remove('C:\\Mateus\\17.GMCORE\\D1021WMS_EstoquePickingWMS.csv')

shutil.move('C:\\Users\\Grupo Mateus\\downloads\\tmp\\D1021Auditoria_AuditoriaDaReposicaoWMS.csv',
            'C:\\Mateus\\17.GMCORE\\')
shutil.move('C:\\Users\\Grupo Mateus\\downloads\\tmp\\D1021WMS_EstoquePickingWMS.csv',
            'C:\\Mateus\\17.GMCORE\\')
