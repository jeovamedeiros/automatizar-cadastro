# Passo a passo do projeto"
# Passo 1: Entrar no site - site teste
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

# pip install pyautogui  = cmd
import pyautogui

# clicar: pyautogui.click
# escrever: pyautogui.write
# apertar uma tecla: pyautogui.press
# apertar atalho: pyautogui.hotkey("ctrl","C")
# scroll(rolar a pagina): pyautogui.scroll

# Fazer o programa rodar um pouco mais devagar
pyautogui.PAUSE = 1
# Começar o processo
# Apertar a tecla do windows
pyautogui.press("win")
# Esperar 2 segundos
pyautogui.sleep(2)
# Digitar o nome do programa(chrome)
pyautogui.write("chrome")
# Apertar a tecla enter
pyautogui.press("enter")
# Esperar 2 segundos
pyautogui.sleep(2)
pyautogui.click(x=251, y=63)
# Digitar o link do site
# Variável para armazenar o link
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
# Apertar a tecla enter
pyautogui.press("enter")


# Passo 2: Fazer o login no site teste
pyautogui.click(x=658, y=347)
pyautogui.write("jeovateste@hotmail.com") # Escrever meu e-amil
pyautogui.press("tab") # Pular para o campo logo abaixo
pyautogui.write("jeova123") # Escrever minha senha 
pyautogui.press("tab")
pyautogui.press("enter")
pyautogui.sleep(2)
# Passo 3:  Importar a base de dados
#pip install pandas numpy openpyxl = cmd
import pandas
tabela = pandas.read_csv("produtos.csv")
print(tabela)

# Laço de repetição
for linha in tabela.index:

    # Passo 4: Cadastrar um produto
    # Clicar no campo de código
    pyautogui.click(x=619, y=242)
    # Pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")
    # MarcaLogitech Mouse   1MOLO000251
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    # Tipo
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    # Categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    # Preco
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    # Custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    # OBS
    obs = tabela.loc[linha, "obs"]
    # Se a observação estiver vazia irá pular (é vazio=isna)
    if not pandas.isna(obs):
        pyautogui.write(obs)


    # Enviar o produto
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # Scroll para cima
    pyautogui.scroll(5000)

# Passo 5: Repetir isso até acabar a base de dados 