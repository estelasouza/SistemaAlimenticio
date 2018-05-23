from tkinter import *
#Aprender a colocar foto
#widgets --> elementos na tela !
def entrarLogin():
    dicionarioLogin={'adm':('adm','Estela','19','1')}
                ##LOGIN:(SENHA,NOME,IDADE,NIVEL)##
    if eLogin.get() in dicionarioLogin and eSenha.get() == dicionarioLogin[eLogin.get()][0]:
        i2=Tk()
        i2.title('OnFood')
        i2.geometry('800x600')
        textoResposta1=Label(i2,text='Seja Bem vindo !')
        textoResposta1.pack()
        frameI2= Frame(i2, bg= 'blue')
        
        bCriarUsuario=Button(frameI2,text='Cadastrar usuario',command=novoCadastro)
        bCriarUsuario.pack(side= LEFT,padx= 2,pady=1)

        bCriarCardapio= Button(frameI2, text = 'Cardapio do dia')
        bCriarCardapio.pack(side= LEFT,padx= 2,pady=2)

        bVerCardapio= Button(frameI2, text= 'Cardapio mensal')
        bVerCardapio.pack(side= LEFT,padx= 2,pady=3)

        bListaProdutos =Button(frameI2, text= 'Lista de produtos ')
        bListaProdutos.pack(side= LEFT,padx= 2,pady=4)

        bProdutosUtilizados= Button(frameI2,text= 'Produtos utilizados' )
        bProdutosUtilizados.pack(side= LEFT,padx= 2,pady=5)

        bAdicionarProdutos= Button(frameI2,text= 'Adicionar novos produtos')
        bAdicionarProdutos.pack(side= LEFT,padx= 1,pady=6)

        frameI2.pack(side= TOP, fill=X)
        subMenu= Menu(i2)
        i2.mainloop()
    else:
        textoResposta['text']='Senha ou login invalidos'
    return dicionarioLogin

def guardarElementosArq(arq):
    dicElementos=criarPessoas()
    arquivo=open(arq,'w')
    for chaves,elementos in dicElementos:
        arquivo.writelines(chaves)
        arquivo.writelines(elementos)
        arquivo.write('\n')
    arquivo.close()
    
def criarPessoas():
    dicionarioNome=criarPessoa()
    if not eEmail.get() in dicionarioNome:
        dicionarioNome[eEmail.get()]=(eSenha.get(),eNome.get(),eIdade.get(),eNivel.get())
    else:
        resposta= Label(i3,text='Email já existente ')
        resposta.pack()
    print(dicionarioNome)
    i3.mainloop()
    
def novoCadastro():
    i3=Tk()
    cadastroEmail=Label(i3,text='Login')
    cadastroEmail.pack()
    eEmail=Entry(i3)
    eEmail.pack()
    cadastroSenha=Label(i3,text='Senha')
    cadastroSenha.pack()
    eSenha=Entry(i3)
    eSenha.pack()
    cadastroNome= Label(i3,text='Nome')
    cadastroNome.pack()
    eNome=Entry(i3)
    eNome.pack()
    cadastroIdade=Label(i3,text='Idade')
    cadastroIdade.pack()
    eIdade=Entry(i3)
    eIdade.pack()
    cadastroNivel=Label(i3,text='Nivel')
    cadastroNivel.pack()
    eNivel=Entry(i3)
    eNivel.pack()
    def criarPessoas():
        dicionarioNome=entrarLogin()
        if not eEmail in dicionarioNome:
            dicionarioNome[eEmail.get()]=(eSenha.get(),eNome.get(),eIdade.get(),eNivel.get())
        else:
            resposta= Label(i3,text='Email já existente ')
            resposta.pack()
        print(dicionarioNome)
        return dicionarioNome
    bSalvar= Button(i3,text='Salvar',command=criarPessoas)
    bSalvar.pack()
 
    i3.mainloop()
    i3.mainloop()
        
        

i1= Tk()
i1.geometry('500x400')
i1.title('OnFood')

fontePadrao=('Arial','10')
##NAÕ ESQUECER DESSA PARTE!!
menu = Menu(i1)

i1.config(menu = menu)

subMenu= Menu(menu)

menu.add_cascade(label= 'Opções ', menu = subMenu)
subMenu.add_command(label='configurações')
subMenu.add_command(label='recuperar a senha') 
subMenu.add_command(label= 'salvar')
subMenu.add_separator()
#""""!!! a
texto = Label (i1,text='Seja bem vindo ao OnFood!!',fg='blue',font='14')
texto.pack()

login= Label(i1,text='Login')
login.place(x=50,y=100)
eLogin=Entry(i1)
eLogin.place(x=50,y=120)

senha=Label(i1,text='Senha',font =fontePadrao)
senha.place(x=50,y=145)
eSenha=Entry(i1)
eSenha.place(x=50,y=165)
eSenha["font"] = fontePadrao
eSenha["show"] = "*"




bEntrar= Button(i1,text='Entrar',command=entrarLogin,width=10)
bEntrar.place(x=50,y=190)

##tentar!!!
fotoInicio= PhotoImage(file='C:Users\br\Desktop\projetoMecls\food.png')

labelImg= Label(i1,image = fotoInicio,text='aq')
labelImg.pack()

## É A IMAGEM


textoResposta=Label(i1,text='')
textoResposta.place(x=70,y=230)




##COMMAND --> DA UM PARAMETRO PRO BOTÃO 
#BACKGROUND ->bc = plano de fundo
#FORGROUND->fg= linha do texto

##SEMPRO COLOCAR ##PACK ##EM ALGUM ELEMENTO QUE EU QUERO MOSTRAR NA TELA 

i1.mainloop()

