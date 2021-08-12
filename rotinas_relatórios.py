from skripts import variaveis as v
from skripts import baixando as b
import pyautogui

def resumo_gerenciais():
    v.abrir_gmcore()

    v.acessar_credenciais()
    v.acesso_R1021()
    b.estoque_perdas()

    v.acesso_menu()
    v.acesso_R1021()
    b.estoque_pendentes_lojas()

    v.acessar_credenciais()
    v.acesso_R1021()
    b.corte_separacao()

    v.acesso_menu()
    v.acesso_R422()
    b.estoque_sintetico()

def previsao_estoque():
    v.abrir_gmcore()

    v.acessar_credenciais()
    v.acesso_R422()
    b.estoque_sintetico()

    v.acesso_menu()
    v.acesso_R1021()
    b.portaria_portariaXML()
    v.acesso_R1021()
    b.portaria_portaria()
    pyautogui.alert("Finalizando Previsão de Estoque em...", timeout=3000)
    pyautogui.alert("3", title="Previsão de estoque", timeout=1000)
    pyautogui.alert("2", timeout=1000)
    pyautogui.alert("1", timeout=1000)






