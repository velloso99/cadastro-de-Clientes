from importacion import *

######################################################################

janela = Tk()
janela.title("Carteira de Clientes")
janela.geometry("800x800")
janela.configure(background= co4)
janela.resizable(FALSE,FALSE)
largura_root = 800
altura_root = 800
#obter tamanho da tela
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()
# Calcular posição para centralizar
pos_x = ( largura_tela-largura_root )//2
pos_y = (altura_tela - altura_root)//2
# Definir geometria da janela (LxA+X+Y)
janela.geometry(f"{largura_root}x{altura_root}+{pos_x}+{pos_y}")
############################################################################    












janela.mainloop()