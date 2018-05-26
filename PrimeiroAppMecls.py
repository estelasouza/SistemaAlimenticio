""" Universidade federal de Pernambuco (UFPE),
Centro de informatica (CIn)
Graduando em Gestão da informação
Programação 1, IF968
Discente: Maria Estela da Costa e Lima Souza (mecls)
Email: mecls@cin.ufpe.br
Data: 24/05/2018"""

from tkinter import *
import random
#Aprender a colocar foto
'---------- criptografia-------------'
def guardarArqCrip(x):
    arquivo=open('criptografia.txt','w')
    
    for elemento in x:
        if elemento != ' ' :
            arquivo.write(elemento)
        else :
            arquivo.write('\n')
    arquivo.close()

def lerChave(arq):
    arq=open(arq,'r')
    armazena= ''
    listaElementos=[]
    for elemento in arq.read():
        if elemento != ' ':
            armazena+=elemento
        else:
            listaElementos.append(int(armazena))
            armazena=''
    listaElementos.append(int(armazena))
    return listaElementos

def criptografarArq(string):
    y=''
    numerosY=''
    lista=lerChave('chavePublica.txt')
    for x in string:
        y=ord(x)**lista[0]
        numerosY+=str(y)+' '
    return (numerosY)


def descriptografarArq(stringCrip):
    textoNovo=''
    lista=lerChave('chavePrivada.txt')
    n=''
    for x in stringCrip:
        if x != ' ':
            textoNovo+=x
        else:
            n+=chr((int(textoNovo)**lista[0])%lista[1])
            textoNovo=''
    return n


def guardarArqEmStr(arq):
    arquivo=open(arq,'r')
    stringElementos= arquivo.read()
    arquivo.close()
    return stringElementos
    
'------------ GUARDAR ELEMENTOS NO ARQ----------------'


def guardarElementosArq(arq,dicionario):
    
    arquivo=open(arq,'a')
    for chaves in dicionario:     
        arquivo.writelines(chaves)
        arquivo.write('-')
        arquivo.writelines(dicionario[chaves][0])
        arquivo.write('-')
        arquivo.writelines(dicionario[chaves][1])
        arquivo.write('-')
        arquivo.writelines(dicionario[chaves][2])
        arquivo.write('-')
        arquivo.writelines(dicionario[chaves][3])
        
        arquivo.write('\n')
    arquivo.close()

    
'----------REESCREVER OS ELEMENTOS NO DICT --------------'
def reescreverElementosDict(arq):
    arquivo = open(arq,'r')
    dicionario={}
    nome=''
    lista=[]
    for elemento in arquivo.read():
        if elemento != '-' and elemento != '\n':
            nome+=elemento
        elif elemento == '-':
            lista.append(nome)
            nome=''
        elif elemento == '\n':
            lista.append(nome)
            dicionario[lista[0]]=tuple(lista[1::])
            lista=[]
            nome=''
    arquivo.close()
    return dicionario


    
'--------- DICIONARIOS---------------'

###OS DICIONARIOS ESTÃO SENDO USADAS COMO GLOBAL ###
####

dicionarioLogin={'adm':('adm','Estela','19','1')}
dicionarioAlimento=reescreverElementosDict('alimentos.txt')

####
'----------- entrar no login ---------------------'
#####falta analisar os niveis##########

def entrarLogin():
    '---------CADASTRO PESSOAS---------------'
    ##LOGIN:(SENHA,NOME,IDADE,NIVEL)##
    def novoCadastro():   
        '''nessa função é possivel cadastrar um novo usuario'''

        i3=Frame(i2,bg='white')
          
        cadastroEmail=Label(i3,text='Login',font=14,bg='white')
        cadastroEmail.pack()
        eEmail=Entry(i3)
        eEmail.pack()
        cadastroSenha=Label(i3,text='Senha',font=14,bg='white')
        cadastroSenha.pack()
        eSenha=Entry(i3)
        eSenha.pack()
        cadastroNome= Label(i3,text='Nome',font=14,bg='white')
        cadastroNome.pack()
        eNome=Entry(i3)
        eNome.pack()
        cadastroIdade=Label(i3,text='Idade',font=14,bg='white')
        cadastroIdade.pack()
        eIdade=Entry(i3)
        eIdade.pack()
        cadastroNivel=Label(i3,text='Nivel',font=14,bg='white')
        cadastroNivel.pack()
        eNivel=Entry(i3)
        eNivel.pack()
            
        def criarPessoas():
            '''Analisa se o login é existente no dict '''
            if not eEmail.get() in dicionarioLogin:
                dicionarioLogin[eEmail.get()]=(eSenha.get(),eNome.get(),eIdade.get(),eNivel.get())
                
                guardarElementosArq('usuarios.txt',dicionarioLogin)
                x=Label(i3,text='Usuario Salvo !',bg='white',font=10)
                x.pack()
                  
            else:
                resposta= Label(i3,text='Email já existente,tente mais uma vez  ',font=10,bg='white')
                resposta.pack()
                
        def sair():
            i3.destroy()
               
            
        bSalvar= Button(i3,text='Salvar',command=criarPessoas)
        bSalvar.pack()
        bSair =Button(i3,text='Sair',command=sair)
        bSair.pack()
         
        i3.pack()
            
    '-------- CADASTRO ALIMENTOS---------'
    def cadastroAlimentos():
        ''' É possivel cadastrar um novo elemento '''

        i4=Frame(i2,bg='white')
        #dictAlimento={alimento:(qnt,validade,tipo,preço)}
        alimento=Label(i4,text='Alimento',bg='white',font=15)
        alimentoE=Entry(i4)
        alimento.pack()
        alimentoE.pack()

        qntAlimento=Label(i4,text='Quantidade de produtos disponiveis',bg='white',font=15)
        qntAlimentoE=Entry(i4)
        qntAlimento.pack()
        qntAlimentoE.pack()

        validadeProdutos=Label(i4,text='Data de validade',bg='white',font=15)
        validadeProdutosE=Entry(i4)
        validadeProdutos.pack()
        validadeProdutosE.pack()

        tipoProduto= Label(i4,text='Tipo de produto',bg='white',font=15)
        tipoProdutoE=Entry(i4)
        tipoProduto.pack()
        tipoProdutoE.pack()

            
        precoProduto=Label(i4,text='Valor do produto',bg='white',font=15)
        precoProdutoE=Entry(i4)
        precoProduto.pack()
        precoProdutoE.pack()
        def SalvarCadastro():
            if not alimentoE.get() in dicionarioAlimento:
                dicionarioAlimento[alimentoE.get()]=(qntAlimentoE.get(),validadeProdutosE.get(),tipoProdutoE.get(),precoProdutoE.get())
                guardarElementosArq('alimentos.txt',dicionarioAlimento)
                i4.destroy()
                
            
        bCadastro=Button(i4,text='Salvar',command=SalvarCadastro)
        bCadastro.pack()
        i4.pack()

    '------------CARDAPIO DO DIA -------------'
    def cardarpioDia():
        def lanche():
            listaAlimento=[]
            listaBebida=[]
            for bebida in dicionarioAlimento:
                if dicionarioAlimento[bebida][2]=='bebida' :
                    listaBebida.append(bebida)
            for alimento in dicionarioAlimento:
                if dicionarioAlimento[alimento][2]== 'lanche' :
                    listaAlimento.append(alimento)

                     
            material=Label(i5,text='O cardapio será:',bg='white',fg='black',font=13)
            receitaBebida=Label(i5,text=random.choice(listaBebida),bg='white',fg='black')
            receitaComida=Label(i5,text=random.choice(listaAlimento),bg='white',fg='black')
            Salvar= Button(i5,text='Salvar', command=guardarElementoArq('alimento.txt',dicionarioAlimento))
            
            material.pack()
            receitaComida.pack()
            receitaBebida.pack()
            Salvar.pack()
        def Almoco():
            print(dicionarioAlimento)
            
            listaAlimento=[]
            listaBebida=[]
            listaCarne=[]
            for bebida in dicionarioAlimento:
                if dicionarioAlimento[bebida][2]=='bebida' :
                    listaBebida.append(bebida)
            for alimento in dicionarioAlimento:
                if dicionarioAlimento[alimento][2]== 'almoco' :
                    listaAlimento.append(alimento)
            for carne in dicionarioAlimento:
                if dicionarioAlimento[carne][2] =='carne' :
                    listaCarne.append(carne)
            print(listaBebida,listaAlimento,listaCarne)
            a=random.choice(listaBebida)
            b=random.choice(listaAlimento)
            c=random.choice(listaCarne)
            def escolha():
                guardarElementoArq('alimentoMensal.txt',dicionarioAlimento)
                
            material=Label(i5,text='O Almoço  será:',bg='white',fg='black',font=13)
            receitaBebida=Label(i5,text=a ,bg='white',fg='black',font=13)
            receitaComida=Label(i5,text=b ,bg='white',fg='black',font=13)
            receitaCarne= Label(i5,text=c ,bg='white',fg='black',font=13)
            Salvar= Button(i5,text='Salvar', command=escolha)
            material.pack()
            receitaComida.pack()
            receitaBebida.pack()
            receitaCarne.pack()
            Salvar.pack()
        def jantar():
            listaAlimento=[]
            listaBebida=[]
            listaCarne=[]
            for bebida in dicionarioAlimento:
                if dicionarioAlimento[bebida][2]=='bebidas' :
                    listaBebida.append(bebida)
            for alimento in dicionarioAlimento:
                if dicionarioAlimento[alimento][2]== 'jantar' :
                    listaAlimento.append(alimento)
            for carne in dicionarioAlimento:
                if dicionarioAlimento[carne][2] =='carne' :
                    listaCarne.append(carne)

                                 
            material=Label(i5,text='O Jantar será:',bg='white',fg='black',font=13)
            receitaBebida=Label(i5,text=random.choice(listaBebida),bg='white',fg='black',font=13)
            receitaComida=Label(i5,text=random.choice(listaAlimento),bg='white',fg='black',font=13)
            receitaCarne= Label(i5,text=random.choice(listaCarne),bg='white',fg='black',font=13)
            Salvar= Button(i5,text='Salvar', command=guardarElementoArq('alimento.txt',dicionarioAlimento))
            
        
            

                           
        i5 = Frame(i2,bg='white')
        bCafe= Button(i5,text='Café da manha ',command=lanche)
        bAlmoco= Button(i5,text='Almoço', command=Almoco)
        bJantar= Button(i5,text='Jantar',command=jantar)
        bLanche= Button(i5,text='Lanche',command=lanche)
        bCafe.pack()
        bJantar.pack()
        bLanche.pack()
        bAlmoco.pack()
        i5.pack()

        
   
    def listaProdutos():
        arquivo= open('alimentos.txt','r')
        i6= Frame(i2,bg='white')
        for elemento in arquivo:
            nomeAlimento=Label(i6,text=elemento,bg='white')
            pularLinha=Label(i6,text='\n',bg='white')
            nomeAlimento.pack()
            pularLinha.pack()
        arquivo.close()
        i6.pack()
        



        
    if eLogin.get() in dicionarioLogin and eSenha.get() == dicionarioLogin[eLogin.get()][0] and dicionarioLogin[eLogin.get()][3]=='1':

        i2=Tk()
        i2.configure(bg='white')
        i2.title('OnFood')
        i2.geometry('800x600')
        textoResposta1=Label(i2,text='Seja Bem vindo !',font=20,bg='white')
        textoResposta1.pack()
        frameI2= Frame(i2, bg= 'blue')
        menu = Menu(i2)

        i2.config(menu = menu)

        subMenu= Menu(menu)

        menu.add_cascade(label= 'Opções ', menu = subMenu) 
        subMenu.add_command(label= 'salvar')
        subMenu.add_separator()     
        
        bCriarUsuario=Button(frameI2,text='Cadastrar usuario',command=novoCadastro)
        bCriarUsuario.pack(side= LEFT,padx= 2,pady=1)

        bCriarCardapio= Button(frameI2, text = 'Cardapio do dia',command=cardarpioDia)  #FALTA
        bCriarCardapio.pack(side= LEFT,padx= 2,pady=2)

        bVerCardapio= Button(frameI2, text= 'Cardapio mensal')#FALTA
        bVerCardapio.pack(side= LEFT,padx= 2,pady=3)

        bListaProdutos =Button(frameI2, text= 'Lista de produtos ')#FALTA
        bListaProdutos.pack(side= LEFT,padx= 2,pady=4)

        bProdutosUtilizados= Button(frameI2,text= 'Produtos utilizados' )#FALTA
        bProdutosUtilizados.pack(side= LEFT,padx= 2,pady=5)

        bAdicionarProdutos= Button(frameI2,text= 'Cadastro de Alimentos',command=cadastroAlimentos)
        bAdicionarProdutos.pack(side= LEFT,padx= 1,pady=6)

        bProdDisponiveis= Button(frameI2,text= 'Produtos disponiveis ')#FALTA
        bProdDisponiveis.pack(side= LEFT,padx= 1,pady=7)

        frameI2.pack(side= TOP, fill=X)
        subMenu= Menu(i2)
        i2.mainloop()
    elif eLogin.get() in dicionarioLogin and eSenha.get() == dicionarioLogin[eLogin.get()][0] and dicionarioLogin[eLogin.get()][3]=='2':
        i2=Tk()
        i2.configure(bg='white')
        i2.title('OnFood')
        i2.geometry('800x600')
        textoResposta1=Label(i2,text='Seja Bem vindo !',font=20,bg='white')
        textoResposta1.pack()
        frameI2= Frame(i2, bg= 'blue')
        menu = Menu(i2)

        i2.config(menu = menu)

        subMenu= Menu(menu)

        menu.add_cascade(label= 'Opções ', menu = subMenu) 
        subMenu.add_command(label= 'salvar')
        subMenu.add_separator()


    elif eLogin.get() in dicionarioLogin and eSenha.get() == dicionarioLogin[eLogin.get()][0] and dicionarioLogin[eLogin.get()][3]=='3':
        i2=Tk()
        i2.configure(bg='white')
        i2.title('OnFood')
        i2.geometry('800x600')
        textoResposta1=Label(i2,text='Seja Bem vindo !',font=20,bg='white')
        textoResposta1.pack()
        frameI2= Frame(i2, bg= 'blue')
        menu = Menu(i2)

        i2.config(menu = menu)

        subMenu= Menu(menu)

        menu.add_cascade(label= 'Opções ', menu = subMenu) 
        subMenu.add_command(label= 'salvar')
        subMenu.add_separator()

    
    else:
        textoResposta['text']='Senha ou login invalidos'
    return dicionarioLogin


'======== CODIGO INICIAL ============='        
        

i1= Tk()
i1.geometry('500x400')
i1.title('OnFood')
i1.configure(bg='yellow')
fontePadrao=('Arial','10')


##NAÕ ESQUECER DESSA PARTE!!
menu = Menu(i1)

i1.config(menu = menu)

subMenu= Menu(menu)

menu.add_cascade(label= 'Opções ', menu = subMenu)
subMenu.add_command(label='recuperar a senha') 
subMenu.add_separator()
#######


texto = Label (i1,text='Seja bem vindo ao OnFood!!',fg='blue',font='14',bg='yellow')
texto.pack()

login= Label(i1,text='Login',bg='yellow')
login.place(x=50,y=100)
eLogin=Entry(i1)
eLogin.place(x=50,y=120)

senha=Label(i1,text='Senha',font =fontePadrao,bg='yellow')
senha.place(x=50,y=145)
eSenha=Entry(i1)
eSenha.place(x=50,y=165)
eSenha["font"] = fontePadrao
eSenha["show"] = "*"




bEntrar= Button(i1,text='Entrar',command=entrarLogin,width=10)
bEntrar.place(x=50,y=190)

##tentar!!!
#fotoInicio= PhotoImage(file='C:Users\br\Desktop\projetoMecls\food.png')
#labelImg= Label(i1,image = fotoInicio,text='aq')
#labelImg.pack()
## É A IMAGEM


textoResposta=Label(i1,text='',bg='yellow')
textoResposta.place(x=70,y=230)

i1.mainloop()

'--------criptografia------------'
stringArq=guardarArqEmStr('usuarios.txt')
x=criptografarArq(stringArq)
guardarArqCrip(x)
