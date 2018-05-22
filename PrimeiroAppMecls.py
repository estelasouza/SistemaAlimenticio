from tkinter import *
#Aprender a colocar foto
#widgets --> elementos na tela !
def entrarLogin():
    dicionario={'mecls':('123','Estela','19','1')}
                ##LOGIN:(SENHA,NOME,IDADE,NIVEL)##
    if eLogin.get() in dicionario and eSenha.get() == dicionario[eLogin.get()][0]:
        i2=Tk()
        textoResposta1=Label(i2,text='Seja Bem vindo !')
        textoResposta1.pack()
        i2.mainloop()
    else:
        textoResposta['text']='Senha ou login invalidos'
    return dicionario

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
    if not eEmail in dicionarioNome:
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

texto = Label (i1,text='Seja bem vindo ao OnFood!!',fg='blue',font='14')
texto.pack()

login= Label(i1,text='Login')
login.place(x=50,y=100)
eLogin=Entry(i1)
eLogin.place(x=50,y=120)

senha=Label(i1,text='Senha')
senha.place(x=50,y=145)
eSenha=Entry(i1)
eSenha.place(x=50,y=165)


bEntrar= Button(i1,text='Entrar',command=entrarLogin,width=10)
bEntrar.place(x=50,y=190)

bCriar=Button(i1,text='criar',command=novoCadastro,width=10)
bCriar.place(x=130,y=190)
textoResposta=Label(i1,text='')
textoResposta.place(x=70,y=230)




##COMMAND --> DA UM PARAMETRO PRO BOTÃO 
#BACKGROUND ->bc = plano de fundo
#FORGROUND->fg= linha do texto

##SEMPRO COLOCAR ##PACK ##EM ALGUM ELEMENTO QUE EU QUERO MOSTRAR NA TELA 

i1.mainloop()
