import pyautogui
import time

# pyautogui.click
# pyautogui.press -> apertar 1 tecla
# pyautogui.write -> escrever 1 texto
# pyautogui.hotkey -> combinação de teclas
# pyautogui.scroll -> rolar a tela (>0 sobe, <0 desce)

pyautogui.PAUSE = 0.5

# Passo 1: Entrar no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Abrir o chrome
pyautogui.press("win") 
pyautogui.write("chrome")
pyautogui.press("enter") 

# Digitar o site
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# esperar 3 segundos
time.sleep(3)

# Passo 2: Fazer login
# preencher email
pyautogui.click(x=614, y=470)
pyautogui.write("teste@teste.com")

# preencher senha
pyautogui.press("tab")
pyautogui.write("asenha12345")

# botão logar
pyautogui.press("tab")
pyautogui.press("enter")

# esperar 3 segundos
time.sleep(3)

# Passo 3: Importar a base de dados
import pandas 

tabela = pandas.read_csv("produtos.csv")

print(tabela)

# Passo 4: Cadastrar 1 produto
'''pyautogui.click(x=617, y=324)

codigo = "MOLO000251"
pyautogui.write(codigo)
pyautogui.press("tab")

marca = "Logitech"
pyautogui.write(marca)
pyautogui.press("tab")

tipo = "Mouse"
pyautogui.write(tipo)
pyautogui.press("tab")

categoria = "1"
pyautogui.write(categoria)
pyautogui.press("tab")

preco_unitario = "25.95"
pyautogui.write(preco_unitario)
pyautogui.press("tab")

custo = "6.5 "
pyautogui.write(custo)
pyautogui.press("tab")

obs = ""
pyautogui.write(obs)
pyautogui.press("tab")
pyautogui.press("enter")

pyautogui.scroll(10000)
'''
# Passo 5: Repetir para todos os produtos

for linha in tabela.index: # index = lista contendo o número de linhas
    pyautogui.click(x=617, y=324)

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")

    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)
    pyautogui.press("tab")

    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")

    categoria = str(tabela.loc[linha, "categoria"]) # transformando em string
    pyautogui.write(categoria)
    pyautogui.press("tab")

    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")

    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
        
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(10000)

# (21) 96721-8715 dúvidas técnicas Jornada Python

# pyautogui -> automações com Python (controlar mouse, teclado e tela do computador)

