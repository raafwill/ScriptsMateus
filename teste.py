import pyautogui
import time
import keyboard
import os
import shutil
import zipfile
import webbrowser

# abrir gmcore
os.startfile("C:\Program Files (x86)\Remote Desktop Organizer\RDO.exe")
time.sleep(5)

# abre o estoque
time.sleep(2)
pyautogui.moveTo(38,36)
pyautogui.click()
pyautogui.moveTo(61,130)
pyautogui.doubleClick()
time.sleep(4)

# digitar credenciais
pyautogui.moveTo(421, 291)
pyautogui.click()
time.sleep(2)

pyautogui.write("teste")
keyboard.write('05225012302')
pyautogui.moveTo(500, 362)
pyautogui.click()

keyboard.write("4578Bra")
pyautogui.moveTo(891, 403)
pyautogui.click()
time.sleep(4)
pyautogui.moveTo(427, 313)
pyautogui.click()
time.sleep(7)

#acessando rotina 1021
keyboard.write("1021")
keyboard.press_and_release('enter')

#clicando em abas wms>estoquePicking
time.sleep(5)
pyautogui.moveTo(243, 180)
pyautogui.click()
time.sleep(2)
pyautogui.moveTo(731, 212)
pyautogui.click()

#selecionando filiais
time.sleep(3)
pyautogui.moveTo(76, 374)
time.sleep(4)
pyautogui.click()
time.sleep(4)

#extraindo
pyautogui.moveTo(1276, 635)
time.sleep(2)
pyautogui.click()

#selecionando campos
pyautogui.moveTo(445, 205)
pyautogui.click()
keyboard.press('space')
keyboard.press('down')
keyboard.press('space')
keyboard.press('down')
keyboard.press('space')
keyboard.press('down')
keyboard.press('space')
keyboard.press('down')
keyboard.press('space')
keyboard.press('down')
keyboard.press('space')
keyboard.press('down')
keyboard.press('space')
keyboard.press('down')
keyboard.press('space')

keyboard.press('tab')
keyboard.press('space')
keyboard.press('down')
keyboard.press('space')
keyboard.press('down')
keyboard.press('space')
keyboard.press('down')
keyboard.press('space')
keyboard.press('down')
keyboard.press('space')
keyboard.press('down')
keyboard.press('space')
keyboard.press('down')
keyboard.press('space')
keyboard.press('down')
keyboard.press('space')
keyboard.press('down')
keyboard.press('space')
keyboard.press('down')
keyboard.press('space')
keyboard.press('down')
keyboard.press('space')
keyboard.press('down')
keyboard.press('space')
keyboard.press('down')
keyboard.press('space')
keyboard.press('down')
keyboard.press('space')
keyboard.press('down')
keyboard.press('space')
time.sleep(10)

#configurando arquivo
pyautogui.moveTo(937, 531)
pyautogui.click()
time.sleep(2)
keyboard.write('D1021WMS_EstoquePickingWMS')
keyboard.press('enter')

#alerta download
time.sleep(110)
keyboard.press('enter')

###BAIXANDO AGORA O ARQUIVO DE AUDITORIAS
pyautogui.moveTo(1206, 184)
pyautogui.click()
time.sleep(3)

pyautogui.moveTo(1022, 217)
pyautogui.click()
time.sleep(3)

#selecionando filiais
pyautogui.moveTo(74, 373)
pyautogui.click()
time.sleep(1)

#selecionando datas
pyautogui.moveTo(1165, 333)
pyautogui.click()
keyboard.write("18042021")

#extraindo
pyautogui.moveTo(1276, 635)
time.sleep(2)
pyautogui.click()

#selecionando campos
pyautogui.moveTo(445, 205)
pyautogui.click()
keyboard.press('space')
keyboard.press('down')
keyboard.press('space')
keyboard.press('down')
keyboard.press('space')
keyboard.press('down')
keyboard.press('space')
keyboard.press('down')
keyboard.press('space')

keyboard.press('tab')
keyboard.press('space')
keyboard.press('down')
keyboard.press('space')
keyboard.press('down')
keyboard.press('space')
keyboard.press('down')
keyboard.press('space')
keyboard.press('down')
keyboard.press('space')
keyboard.press('down')
keyboard.press('space')
keyboard.press('down')
keyboard.press('space')
keyboard.press('down')
keyboard.press('space')
keyboard.press('down')
keyboard.press('space')
keyboard.press('down')
keyboard.press('space')
keyboard.press('down')
keyboard.press('space')
time.sleep(10)

#configurando arquivo
pyautogui.moveTo(937, 531)
pyautogui.click()
time.sleep(2)
keyboard.write('D1021Auditoria_AuditoriaDaReposicaoWMS')
keyboard.press('enter')

#alerta download
time.sleep(110)
keyboard.press('enter')

#definindo variáveis
sign = '05225012302'
ttt = '4578Bra'

#abrindo chrome para baixar arquivos
os.startfile("chrome")
time.sleep(2)

#acessando gerenciador
pyautogui.write("http://192.168.6.47/")
time.sleep(2)
pyautogui.press('Enter')
time.sleep(3)

#baixando arquivos no gerenciador
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.write(sign)
pyautogui.press('tab')
time.sleep(2)
pyautogui.write(ttt)
pyautogui.press('enter')
time.sleep(3)

#limpando pastas de download

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

pass

if os.path.exists('C:\\' 'Users\\'
                  'Grupo Mateus\\'
                  'downloads\\tmp'):

    shutil.rmtree('C:\\' 'Users\\'
                   'Grupo Mateus\\'
                   'downloads\\tmp')

pass



#baixando primeiro arquivo
pyautogui.moveTo(305, 615)
pyautogui.click()
time.sleep(1)
pyautogui.moveTo(666, 342)
pyautogui.click()

#baixando segundo arquivo
pyautogui.moveTo(305, 615)
pyautogui.click()
pyautogui.moveTo(302, 660)
pyautogui.click()
time.sleep(1)
pyautogui.moveTo(666, 342)
pyautogui.click()

time.sleep(70)

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

os.system('"TortoiseProc.exe" /command:update /path:C:\\mateus\\17.GMCORE /closeonend:1')
os.system('"TortoiseProc.exe" /command:commit /path:C:\\mateus\\17.GMCORE /closeonend:1')


