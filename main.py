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

btn_cadastrar =Button(frame_btn, text="Cadastrar", width=10, height=2, bg=co11, fg=co5, font=("Ivy 10 bold"), relief=RAISED, overrelief=RIDGE )
btn_cadastrar.grid(row=0, column=0)

btn_atualiza =Button(frame_btn, text="Atualizar", width=10, height=2, bg=co11, fg=co5, font=("Ivy 10 bold"), relief=RAISED, overrelief=RIDGE, )
btn_atualiza.grid(row=0, column=1)

btn_deletar =Button(frame_btn, text="Deletar", width=10, height=2, bg=co11, fg=co5, font=("Ivy 10 bold"), relief=RAISED, overrelief=RIDGE, )
btn_deletar.grid(row=0, column=2)

btn_cad_bairros =Button(frame_btn, text="Cadastrar Bairros", width=15, height=2, bg=co11, fg=co5, font=("Ivy 10 bold"), relief=RAISED, overrelief=RIDGE, command=lambda:bairros())
btn_cad_bairros.grid(row=0, column=3)

btn_closed =Button(frame_btn, command=janela.destroy, text="Fechar", width=10, height=2, bg=co11, fg=co5, font=("Ivy 10 bold"), relief=RAISED, overrelief=RIDGE, )
btn_closed.grid(row=0, column=4)

###########################################################################################################
# Cadastrar Bairros
def bairros():

    janela_bairros = Toplevel()
    janela_bairros.title("Cadastro de Bairros")
    janela_bairros.geometry("500x400")
    janela_bairros.configure(background= co5)
    janela_bairros.resizable(FALSE,FALSE)
    largura_root = 500
    altura_root = 400
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
    t_titulo= Label(frame_cima, text="Cadastrar Bairros", bg=co4, fg=co6, font=("Ivy 16 bold"), anchor= CENTER)
    t_titulo.place(x=150, y=5)


    def cad_bairros():

        bairro=e_bairro.get()

        lista=[bairro]
        #verificar se os valores estão corretos
        for i in lista:
            if i =="":
                messagebox.showerror("Erro", "Por favor preencha todos os campos!")
                return
        #inserir dadsos
        criar_bairro(lista)
        #mostrando mensagem de sucesso
        messagebox.showinfo("Sucesso", "Bairro cadastrado com sucesso!")
        #limpar campos
        e_bairro.delete(0, END)
        #atualizar tabela
        mostrar_bairros()



    ####################################################################################################################################################
    btn_cadastrar =Button(frame_btn,command=cad_bairros, text="Cadastrar", width=10, height=2, bg=co11, fg=co5, font=("Ivy 10 bold"), relief=RAISED, overrelief=RIDGE )
    btn_cadastrar.grid(row=0, column=0)

    btn_atualiza =Button(frame_btn, text="Atualizar", width=10, height=2, bg=co11, fg=co5, font=("Ivy 10 bold"), relief=RAISED, overrelief=RIDGE, )
    btn_atualiza.grid(row=0, column=1)

    btn_deletar =Button(frame_btn, text="Deletar", width=10, height=2, bg=co11, fg=co5, font=("Ivy 10 bold"), relief=RAISED, overrelief=RIDGE, )
    btn_deletar.grid(row=0, column=2)

    btn_closed =Button(frame_btn, command=janela_bairros.destroy, text="Fechar", width=10, height=2, bg=co11, fg=co5, font=("Ivy 10 bold"), relief=RAISED, overrelief=RIDGE, )
    btn_closed.grid(row=0, column=3)
    
    ###################################################################################################################################################

    l_bairro = Label(frame_Baixo, text="Bairro", font=('Ivy 15 bold'), bg=co4, fg=co6)
    l_bairro.grid(row=0, column=0, padx=10, pady=10)
    e_bairro= Entry(frame_Baixo, width=15, justify=LEFT, font=('Ivy 10 bold'),  relief='solid')
    e_bairro.grid(row=0, column=1, padx=10, pady=10)


    #Tabela Alunos
    def mostrar_bairros():

        # Título
        app_nome = Label(frame_tabela, text="Registros de Bairros", height=1, pady=0, padx=0, relief="flat", anchor="center", font=('Ivy 10 bold'), bg=co4, fg=co6)
        app_nome.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")

        # Cabeçalhos da tabela
        list_header = ['id',  'Bairro']

        df_list = ver_bairro()

        global tree_bairros
        # Criando Treeview
        tree_bairros = ttk.Treeview(
            frame_tabela,
            selectmode="extended",
            columns=list_header,
            show="headings"
        )

        # Scrollbars
        vsb = ttk.Scrollbar(frame_tabela, orient="vertical", command=tree_bairros.yview)
        hsb = ttk.Scrollbar(frame_tabela, orient="horizontal", command=tree_bairros.xview)

        tree_bairros.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        tree_bairros.grid(column=0, row=1, sticky='nsew')
        vsb.grid(column=1, row=1, sticky='ns')
        hsb.grid(column=0, row=2, sticky='ew')

        frame_tabela.grid_rowconfigure(0, weight=20)

        # Ajuste das colunas
        hd = [ "center", "nw"]
        h =  [40, 100]

        for i, col in enumerate(list_header):
            tree_bairros.heading(col, text=col, anchor=NW)
            tree_bairros.column(col, width=h[i], anchor=hd[i])

        # Inserção dos registros — CORRETO
        for item in df_list:
            tree_bairros.insert("", "end", values=item)
    mostrar_bairros()

###############################################################################################################
# Cadastro de clientes
def cad_clientes():
    pass








janela.mainloop()