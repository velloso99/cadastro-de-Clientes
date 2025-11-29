from importacion import *

######################################################################

janela = Tk()
janela.title("Carteira de Clientes")
janela.geometry("800x800")
janela.configure(background= co5)
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

style = ttk.Style(janela)
style.theme_use("clam")
############################################################################    

frame_cima= Frame(janela, width=800, height=50, bg=co4, relief="flat")
frame_cima.grid(row=0, column=0, sticky=NSEW)

frame_btn= Frame(janela, width=800, height=50, bg=co4, relief="flat")
frame_btn.grid(row=1, column=0, sticky=NSEW)

frame_Baixo= Frame(janela, width=800, height=750, bg=co4, relief="flat")
frame_Baixo.grid(row=2, column=0, sticky=NSEW)

frame_tabela= Frame(janela, width=800, height=750, bg=co4, relief="flat")
frame_tabela.grid(row=2, column=0, sticky=NSEW)
#################################################################################################


#####################################################################################
#Titulo
t_titulo= Label(frame_cima, text="Sistema de Cadastro de Clientes", bg=co4, fg=co6, font=("Ivy 16 bold"), anchor= CENTER)
t_titulo.place(x=250, y=10)

####################################################################################
# Botões de navegação

btn_cadastrar =Button(frame_btn, text="Cadastrar", width=10, height=2, bg=co11, fg=co5, font=("Ivy 10 bold"), relief=RAISED, overrelief=RIDGE, )
btn_cadastrar.grid(row=0, column=0)

btn_atualiza =Button(frame_btn, text="Atualizar", width=10, height=2, bg=co11, fg=co5, font=("Ivy 10 bold"), relief=RAISED, overrelief=RIDGE, )
btn_atualiza.grid(row=0, column=1)

btn_deletar =Button(frame_btn, text="Deletar", width=10, height=2, bg=co11, fg=co5, font=("Ivy 10 bold"), relief=RAISED, overrelief=RIDGE, )
btn_deletar.grid(row=0, column=2)

btn_cad_bairros =Button(frame_btn, text="Cadastrar Bairros", width=15, height=2, bg=co11, fg=co5, font=("Ivy 10 bold"), relief=RAISED, overrelief=RIDGE, command=lambda:bairros())
btn_cad_bairros.grid(row=0, column=3)

###########################################################################################################
# Cadastrar Bairros
def bairros():

    janela_bairros = Toplevel()
    janela_bairros.title("Cadastro de Bairros")
    janela_bairros.geometry("500x500")
    janela_bairros.configure(background= co5)
    janela_bairros.resizable(FALSE,FALSE)
    largura_root = 500
    altura_root = 500
    #obter tamanho da tela
    largura_tela = janela_bairros.winfo_screenwidth()
    altura_tela = janela_bairros.winfo_screenheight()
    # Calcular posição para centralizar
    pos_x = ( largura_tela-largura_root )//2
    pos_y = (altura_tela - altura_root)//2
    # Definir geometria da janela (LxA+X+Y)
    janela_bairros.geometry(f"{largura_root}x{altura_root}+{pos_x}+{pos_y}")

    frame_cima= Frame(janela_bairros, width=500, height=50, bg=co4, relief="flat")
    frame_cima.grid(row=0, column=0, sticky=NSEW)

    frame_btn= Frame(janela_bairros, width=500, height=50, bg=co4, relief="flat")
    frame_btn.grid(row=1, column=0, sticky=NSEW)

    frame_Baixo= Frame(janela_bairros, width=500, height=200, bg=co4, relief="flat")
    frame_Baixo.grid(row=2, column=0, sticky=NSEW)

    frame_tabela= Frame(janela_bairros, width=500, height=250, bg=co4, relief="flat")
    frame_tabela.grid(row=3, column=0, sticky=NSEW)
    #Titulo
    t_titulo= Label(frame_cima, text="Cadstrar Bairros", bg=co4, fg=co6, font=("Ivy 16 bold"), anchor= CENTER)
    t_titulo.place(x=150, y=5)

    btn_cadastrar =Button(frame_btn, text="Cadastrar", width=10, height=2, bg=co11, fg=co5, font=("Ivy 10 bold"), relief=RAISED, overrelief=RIDGE, )
    btn_cadastrar.grid(row=0, column=0)

    btn_atualiza =Button(frame_btn, text="Atualizar", width=10, height=2, bg=co11, fg=co5, font=("Ivy 10 bold"), relief=RAISED, overrelief=RIDGE, )
    btn_atualiza.grid(row=0, column=1)

    btn_deletar =Button(frame_btn, text="Deletar", width=10, height=2, bg=co11, fg=co5, font=("Ivy 10 bold"), relief=RAISED, overrelief=RIDGE, )
    btn_deletar.grid(row=0, column=2)


    ###################################################################################################################################################








janela.mainloop()