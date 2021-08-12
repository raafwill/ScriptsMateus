import os
import pyautogui
import zipfile
import pathlib
import shutil
import copy

lista = ['R1021Portaria_Portaria.zip',
         'D1021Venda_VCLGeral.zip',
         'PERDAS.zip',
         'D1021WMS_Corte_Separacao.zip',
         'D1021Estoque_Pendentes_lojas.zip',
         'perdas.zip',
         'PESO.BALANCA.zip',
         'R422Estoque_Sintetico.zip',
         'R1021Portaria_TransitoXML.zip']

directory = "C:\\Users\\Grupo Mateus\\Downloads"
tmp = "C:\\Users\\Grupo Mateus\\Downloads\\tmp\\"
acao = 0
tortoise = "C:\\mateus\\"
b = "R1021Portaria_TransitoXML.csv"
diretorio = pathlib.Path(tortoise)

for i in os.listdir(directory):
    if i in lista:
        arquivo = directory+"/"+i
        items = []
        items.append(i)
        items_current = copy.deepcopy(items)
        # print(arquivo)

        with zipfile.ZipFile(arquivo) as zip_ref:
            zip_ref.extractall(directory)

        for all in os.listdir(tmp):
            local = diretorio.glob('**/' + all)
            for loc in local:
                print(loc)
                os.remove(loc)
                os.system('"TortoiseProc.exe" /command:update /path:C:\\mateus\\17.GMCORE /closeonend:1')
                os.remove(loc)
                acao += 1

                # if acao == 1:
                #     item1 = i
                # elif acao == 2:
                #     item2 = i
                # elif acao == 3:
                #     item3 = i
                # elif acao == 4:
                #     item4 = i
                # elif acao == 5:
                #     item5 = i
                # elif acao == 6:
                #     item6 = i
                # elif acao == 7:
                #     item7 = i
                # elif acao == 8:
                #     item8 = i
                # elif acao == 9:
                #     item9 = i

                shutil.move(tmp+all, loc)

print("adicionados:" + '\n'.join(map(str, items_current)))

os.system('"TortoiseProc.exe" /command:commit /path:C:\\mateus\\17.GMCORE /closeonend:1')

pyautogui.alert("Processo Finalizado", timeout=5000)










