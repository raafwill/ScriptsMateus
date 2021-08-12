import pyautogui
import time
import keyboard
import os
import shutil
import zipfile
from skripts import variaveis as var

def estoque_perdas():
    ##(PERDAS)
    time.sleep(20)
    pyautogui.moveTo(142, 163)
    pyautogui.click()
    time.sleep(10)
    pyautogui.moveTo(47, 204)
    pyautogui.click()
    time.sleep(15)

    pyautogui.moveTo(300, 352) # movendo para selecionar filiais
    time.sleep(2 )
    pyautogui.click()
    time.sleep(3)
    keyboard.press('space')
    time.sleep(7)

    # press = 0 #nesse campo sempre iniciando com 0
    # campos = 12 #inserir aqui a quantidade de campos a ser marcado
    # #loop para seleção de campos
    # while press <= campos:
    #     keyboard.press('down')
    #     keyboard.press_and_release('space')
    #     press += 1

    time.sleep(5)
    pyautogui.moveTo(1246, 666)
    pyautogui.click()

    #loop para selecionar os dados a serem exportados
    pyautogui.alert("AGORA VAMOS PARA OS CAMPOS DE EXTRAÇÃO", timeout=4000)
    time.sleep(5)
    press = 0
    campos = 21 #quantidade de campos
    while (press <= campos):
        if press <= 14:
            keyboard.press('down')
            keyboard.press('space')
            press += 1
        elif press == 15:
            keyboard.press('down')
            press += 1
        elif press <19:
            keyboard.press('down')
            keyboard.press('space')
            press += 1
        elif press ==19:
            keyboard.press('tab')
            keyboard.press('space')
            press += 1
        elif press >19:
            keyboard.press('down')
            keyboard.press('space')
            press += 1

    time.sleep(2)
    pyautogui.moveTo(927, 538)
    pyautogui.click()
    arquivoname = "perdas"

    time.sleep(5)
    for a in arquivoname:
        keyboard.press(a)

    keyboard.press_and_release('enter')
    time.sleep(40)
    ####------- fim extração de PERDAS-----------------------------------------------------------------------------#####

def estoque_pendentes_lojas():
    #INICIANDO EXTRAÇÃO DE PENDENTES LOJAS
    ## extraindo primeiro arquivo (PENDENTES.LOJAS)
    # clicando em abas ESTOQUE>PENDENTES LOJAS
    time.sleep(20)
    pyautogui.moveTo(142, 163)
    pyautogui.click()
    time.sleep(7)
    pyautogui.moveTo(740, 206)
    pyautogui.click()
    time.sleep(15)

    pyautogui.moveTo(300, 352) # movendo para selecionar filiais
    time.sleep(2 )
    pyautogui.click()
    time.sleep(3)
    keyboard.press('space')
    time.sleep(7)

    # press = 0 #nesse campo sempre iniciando com 0
    # campos = 12 #inserir aqui a quantidade de campos a serem marcados
    # #loop para seleção de campos
    # while press <= campos:
    #     keyboard.press('down')
    #     keyboard.press_and_release('space')
    #     press += 1

    time.sleep(5)
    pyautogui.moveTo(1246, 666)
    pyautogui.click()


    #loop para selecionar os dados a serem exportados
    pyautogui.alert("AGORA VAMOS PARA OS CAMPOS DE EXTRAÇÃO", timeout=4000)
    time.sleep(5)
    press = 0
    campos = 21 #quantidade de campos
    while (press <= campos):

        if press <13:
            keyboard.press('down')
            keyboard.press('space')
            press += 1
        elif press ==13:
            keyboard.press('tab')
            keyboard.press('space')
            press += 1
        elif press >13:
            keyboard.press('down')
            keyboard.press('space')
            press += 1

    time.sleep(2)
    pyautogui.moveTo(927, 538)
    pyautogui.click()
    arquivoname = "pendentes.lojas"

    time.sleep(5)
    for a in arquivoname:
        keyboard.press(a)

    keyboard.press_and_release('enter')
    time.sleep(60)

def corte_separacao():
    #selecionando abas
    time.sleep(20)
    pyautogui.moveTo(219, 171)
    pyautogui.click()
    time.sleep(5)
    pyautogui.moveTo(107, 203)
    pyautogui.click()
    time.sleep(15)

    pyautogui.moveTo(300, 352) # movendo para selecionar filiais
    time.sleep(2 )
    pyautogui.click()
    time.sleep(3)
    keyboard.press('space')
    time.sleep(7)

    # pyautogui.moveTo(50, 356) #movendo para selecionar filiais
    # pyautogui.click()
    # time.sleep(15)
    #
    # press = 0 #nesse campo sempre 0
    # campos = 12 #inserir aqui a quantidade de campos a serem marcados
    #
    # #loop para seleção de campos
    # while press <= campos:
    #     keyboard.press('down')
    #     keyboard.press_and_release('space')
    #     press += 1

    time.sleep(5)
    pyautogui.moveTo(1246, 666)
    pyautogui.click()


    #loop para selecionar os dados a serem exportados
    pyautogui.alert("AGORA VAMOS PARA OS CAMPOS DE EXTRAÇÃO", timeout=4000)
    time.sleep(5)
    press = 0
    campos = 35 #quantidade de campos
    while (press <= campos):
        if press <= 14:
            keyboard.press('down')
            keyboard.press('space')
            press += 1
        elif press == 15:
            keyboard.press('down')
            press += 1
        elif press <19:
            keyboard.press('down')
            keyboard.press('space')
            press += 1
        elif press ==19:
            keyboard.press('tab')
            keyboard.press('space')
            press += 1
        elif press >19:
            keyboard.press('down')
            keyboard.press('space')
            press += 1

    time.sleep(15)
    pyautogui.moveTo(927, 538)
    pyautogui.click()
    arquivoname = "corte.da.separacao"

    time.sleep(5)
    for a in arquivoname:
        keyboard.press(a)

    keyboard.press_and_release('enter')
    time.sleep(60)
    # fim extração de PENDENTES.LOJAS

def estoque_sintetico():
    #selecionando abas
    time.sleep(20)
    pyautogui.moveTo(1342, 170)
    clicks = range(6)
    for c in clicks:
        pyautogui.click()

    pyautogui.moveTo(940, 172)
    pyautogui.click()
    time.sleep(4)

    pyautogui.moveTo(299, 325) # movendo para selecionar filiais
    time.sleep(2)
    pyautogui.click()
    time.sleep(1)
    keyboard.press('space')
    time.sleep(3)


    # pyautogui.moveTo(50, 326) #movendo para selecionar filiais
    # pyautogui.click()
    # time.sleep(15)
    #
    # press = 0 #nesse campo sempre 0
    # campos = 12 #inserir aqui a quantidade de campos a serem marcados
    #
    # #loop para seleção de campos
    # while press <= campos:
    #     keyboard.press('down')
    #     keyboard.press_and_release('space')
    #     press += 1

    time.sleep(1)
    pyautogui.moveTo(1246, 666)
    pyautogui.click()

    #loop para selecionar os dados a serem exportados
    pyautogui.alert("Campos de extração de dados", timeout=4000)
    press = 0
    campos = 8 #quantidade de campos
    while (press <= campos):
        if press <6:
            keyboard.press('down')
            keyboard.press('space')
            press += 1
        elif press ==6:
            keyboard.press('tab')
            keyboard.press('space')
            press += 1
        elif press >6:
            keyboard.press('down')
            keyboard.press('space')
            press += 1

    time.sleep(4)
    pyautogui.moveTo(927, 538)
    pyautogui.click()
    arquivoname = "estoque.sintetico"

    time.sleep(5)
    for a in arquivoname:
        keyboard.press(a)

    keyboard.press_and_release('enter')
    time.sleep(60)
    keyboard.press('enter')

def portaria_portaria():
    #selecionando abas
    time.sleep(20)
    pyautogui.moveTo(413, 168)
    pyautogui.click()
    time.sleep(5)
    pyautogui.moveTo(47, 202)
    pyautogui.click()
    time.sleep(5)

    pyautogui.moveTo(300, 352) # movendo para selecionar filiais
    time.sleep(2 )
    pyautogui.click()
    time.sleep(2)
    keyboard.press('space')
    time.sleep(3)

    # pyautogui.moveTo(50, 356) #movendo para selecionar filiais
    # pyautogui.click()
    # time.sleep(15)
    #
    # press = 0 #nesse campo sempre 0
    # campos = 12 #inserir aqui a quantidade de campos a serem marcados
    #
    # #loop para seleção de campos
    # while press <= campos:
    #     keyboard.press('down')
    #     keyboard.press_and_release('space')
    #     press += 1

    time.sleep(1)
    pyautogui.moveTo(1246, 666)
    pyautogui.click()


    #loop para selecionar os dados a serem exportados
    pyautogui.alert("AGORA VAMOS PARA OS CAMPOS DE EXTRAÇÃO", timeout=4000)
    press = 0
    campos = 33 #quantidade de campos
    while (press <= campos):
        if press < 2:
            keyboard.press('down')
            keyboard.press('space')
            press += 1
        elif press >= 2 and press <=4:
            keyboard.press('down')
            press += 1
        elif press <9:
            keyboard.press('space')
            keyboard.press('down')
            press += 1
        elif press >=9 and press <=13:
            keyboard.press('down')
            press +=1
        elif press <16:
            keyboard.press('space')
            keyboard.press('down')
            press += 1
        elif press >=16 and press <=17:
            keyboard.press('down')
            press +=1
        elif press <20:
            keyboard.press('space')
            keyboard.press('down')
            press += 1
        elif press ==20:
            keyboard.press('tab')
            press +=1
        elif press >20:
            keyboard.press('space')
            keyboard.press('down')
            press +=1


    time.sleep(4)
    pyautogui.moveTo(927, 538)
    pyautogui.click()
    arquivoname = "portaria_portaria"

    time.sleep(5)
    for a in arquivoname:
        keyboard.press(a)

    keyboard.press_and_release('enter')
    time.sleep(200)
    keyboard.press('enter')
    # fim extração de PENDENTES.LOJAS

def portaria_portariaXML():
    #selecionando abas
    time.sleep(20)
    pyautogui.moveTo(407, 173)
    pyautogui.click()
    time.sleep(5)
    pyautogui.moveTo(133, 201)
    pyautogui.click()
    time.sleep(5)

    pyautogui.moveTo(299, 325) # movendo para selecionar filiais
    time.sleep(2)
    pyautogui.click()
    time.sleep(2)
    keyboard.press('space')
    time.sleep(4)


    # pyautogui.moveTo(50, 326) #movendo para selecionar filiais
    # pyautogui.click()
    # time.sleep(15)
    #
    # press = 0 #nesse campo sempre 0
    # campos = 12 #inserir aqui a quantidade de campos a serem marcados
    #
    # #loop para seleção de campos
    # while press <= campos:
    #     keyboard.press('down')
    #     keyboard.press_and_release('space')
    #     press += 1

    pyautogui.moveTo(1246, 666)
    pyautogui.click()

    #loop para selecionar os dados a serem exportados
    pyautogui.alert("Campos de extração de dados", timeout=4000)
    press = 0
    campos = 25 #quantidade de campos
    while (press <= campos):
        if press <18:
            keyboard.press('down')
            keyboard.press('space')
            press += 1
        elif press ==18:
            keyboard.press('tab')
            keyboard.press('space')
            press += 1
        elif press >18:
            keyboard.press('down')
            keyboard.press('space')
            press += 1

    time.sleep(4)
    pyautogui.moveTo(927, 538)
    pyautogui.click()
    arquivoname = "portaria_portariaXML"

    time.sleep(5)
    for a in arquivoname:
        keyboard.press(a)

    keyboard.press_and_release('enter')
    time.sleep(200)
    keyboard.press('enter')












#  #alerta download
#  time.sleep(110)
# k eyboard.press('enter')
#
#  ###BAIXANDO AGORA O ARQUIVO DE AUDITORIAS
# p yautogui.moveTo(1206, 184)
# py autogui.click()
# tim e.sleep(3)
#
#  pyautogui.moveTo(1022, 217)
# p yautogui.click()
# ti me.sleep(3)
#
#  #selecionando filiais
# p yautogui.moveTo(74, 373)
# py autogui.click()
# tim e.sleep(1)
#
#  #selecionando datas
# p yautogui.moveTo(1165, 333)
# py autogui.click()
# key board.write("18042021")
#
#  #extraindo
# p yautogui.moveTo(1276, 635)
# ti me.sleep(2)
# pya utogui.click()
#
#  #selecionando campos
# p yautogui.moveTo(445, 205)
# py autogui.click()
# key board.press('space')
# keyb oard.press('down')
# keybo ard.press('space')
# keyboa rd.press('down')
# keyboar d.press('space')
# keyboard .press('down')
# keyboard. press('space')
# keyboard.p ress('down')
# keyboard.pr ess('space')
#
#  keyboard.press('tab')
# k eyboard.press('space')
# ke yboard.press('down')
# key board.press('space')
# keyb oard.press('down')
# keybo ard.press('space')
# keyboa rd.press('down')
# keyboar d.press('space')
# keyboard .press('down')
# keyboard. press('space')
# keyboard.p ress('down')
# keyboard.pr ess('space')
# keyboard.pre ss('down')
# keyboard.pres s('space')
# keyboard.press ('down')
# keyboard.press( 'space')
# keyboard.press(' down')
# keyboard.press('s pace')
# keyboard.press('do wn')
# keyboard.press('spa ce')
# keyboard.press('down ')
# keyboard.press('space ')
# time.sleep(10)
#
#  #configurando arquivo
# p yautogui.moveTo(937, 531)
# py autogui.click()
# tim e.sleep(2)
# keyb oard.write('D1021Auditoria_AuditoriaDaReposicaoWMS')
# keybo ard.press('enter')
#
#  #alerta download
# t ime.sleep(110)
# ke yboard.press('enter')
#
#  #definindo variáveis
# s ign = '05225012302'
# tt t = '4578Bra'
#
#  #abrindo chrome para baixar arquivos
# o s.startfile("chrome")
# ti me.sleep(2)
#
#  #acessando gerenciador
# p yautogui.write("http://192.168.6.47/")
# ti me.sleep(2)
# pya utogui.press('Enter')
# time .sleep(3)
#
#  #baixando arquivos no gerenciador
# p yautogui.press('tab')
# py autogui.press('tab')
# pya utogui.write(sign)
# pyau togui.press('tab')
# time. sleep(2)
# pyauto gui.write(ttt)
# pyautog ui.press('enter')
# time.sle ep(3)
#
#  #limpando pastas de download
#
#  if os.path.exists('C:\\' 'Users\\'
#                    'Grupo Mateus\\'
#                    'downloads\\D1021WMS_EstoquePickingWMS.zip'):
#
#      pyautogui.alert("Já existe! Removendo D1021WMS_EstoquePickingWMS.zip...", timeout=3000)
#
#      os.remove('C:\\'
#                'Users\\'
#                'Grupo Mateus\\'
#                'downloads\\'
#                'D1021WMS_EstoquePickingWMS.zip')
#     p yautogui.alert("arquivo removido", timeout=3000)
#
#  pass
#
#  if os.path.exists('C:\\' 'Users\\'
#                    'Grupo Mateus\\'
#                    'downloads\\'
#                    'D1021Auditoria_AuditoriaDaReposicaoWMS.zip'):
#
#      pyautogui.alert("Já existe! Removendo Auditoria_AuditoriaDaReposicaoWMS.zip...", timeout=3000)
#
#
#      os.remove('C:\\'
#                'Users\\'
#                'Grupo Mateus\\'
#                'downloads\\'
#                'D1021Auditoria_AuditoriaDaReposicaoWMS.zip')
#
#      pyautogui.alert("arquivo removido", timeout=3000)
#
#  pass
#
#  if os.path.exists('C:\\' 'Users\\'
#                    'Grupo Mateus\\'
#                    'downloads\\tmp'):
#
#      shutil.rmtree('C:\\' 'Users\\'
#                     'Grupo Mateus\\'
#                     'downloads\\tmp')
# pas s
#
#
#
#  #baixando primeiro arquivo
# p yautogui.moveTo(305, 615)
# py autogui.click()
# tim e.sleep(1)
# pyau togui.moveTo(666, 342)
# pyaut ogui.click()
#
#  #baixando segundo arquivo
# p yautogui.moveTo(305, 615)
# py autogui.click()
# pya utogui.moveTo(302, 660)
# pyau togui.click()
# time. sleep(1)
# pyauto gui.moveTo(666, 342)
# pyautog ui.click()
#
#  time.sleep(70)
#
#  with zipfile.ZipFile('C:\\' 'Users\\'
#                       'Grupo Mateus\\'
#                       'downloads\\'
#                       'D1021Auditoria_AuditoriaDaReposicaoWMS.zip') as zip_ref:
#
#      zip_ref.extractall('C:\\'
#                         'Users\\'
#                         'Grupo Mateus\\'
#                         'downloads\\')
#
#  with zipfile.ZipFile('C:\\' 'Users\\'
#                       'Grupo Mateus\\'
#                       'downloads\\'
#                       'D1021WMS_EstoquePickingWMS.zip') as zip_ref:
#
#      zip_ref.extractall('C:\\'
#                         'Users\\'
#                         'Grupo Mateus\\'
#                         'downloads\\')
#
#
#
#  os.remove('C:\\Mateus\\17.GMCORE\\D1021Auditoria_AuditoriaDaReposicaoWMS.csv')
# o s.remove('C:\\Mateus\\17.GMCORE\\D1021WMS_EstoquePickingWMS.csv')
#
#  shutil.move('C:\\Users\\Grupo Mateus\\downloads\\tmp\\D1021Auditoria_AuditoriaDaReposicaoWMS.csv',
#              'C:\\Mateus\\17.GMCORE\\')
# sh util.move('C:\\Users\\Grupo Mateus\\downloads\\tmp\\D1021WMS_EstoquePickingWMS.csv',
#              'C:\\Mateus\\17.GMCORE\\')
#
#  os.system('"TortoiseProc.exe" /command:update /path:C:\\mateus\\17.GMCORE /closeonend:1')
# o s.system('"TortoiseProc.exe" /command:commit /path:C:\\mateus\\17.GMCORE /closeonend:1')
#
