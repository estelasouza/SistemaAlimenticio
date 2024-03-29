

""" Universidade federal de Pernambuco (UFPE),
Centro de informatica (CIn)
Graduando em Gestão da informação
Programação 1, IF968
Discente: Maria Estela da Costa e Lima Souza (mecls)
Email: mecls@cin.ufpe.br
Data: 24/05/2018"""

from datetime import datetime
from tkinter import *
import random


#Aprender a colocar foto


'---------- criptografia-------------'


def guardarArqCrip(x):

    ''' função de guardar o eleemnto criptografado no arquivo '''
    
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
    '''função de criptografar a string '''
    
    y=''
    numerosY=''
    lista=lerChave('chavePublica.txt')
    for x in string:
        y=ord(x)**lista[0]
        numerosY+=str(y)+' '
    return (numerosY)


def descriptografarArq(stringCrip):
    '''função de descriptografar a string '''
    
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

'--------- RECUPERAR A SENHA ------------'

def recuperarSenha():
    def sair():
        i4.destroy()
        

    def acharUsuario():
        def salvar():
            lista=[]
            if eNovaSenha.get() == eConfirmaSenha.get():
                for x in dicionarioLogin[sLogin.get()]:
                    lista.append(x)
                dicionarioLogin[sLogin.get()]=lista
                dicionarioLogin[sLogin.get()][2]=eNovaSenha.get()
                dicionarioLogin[sLogin.get()]=tuple(lista)
                texto['text']='Senha cadastrada'
            else:
                texto['text']='A senha não está igual'
                
                
        if sLogin.get() in dicionarioLogin and dicionarioLogin[sLogin.get()][2]== sChave.get():
            frame1=Frame(i4)
            novaSenha=Label(frame1,text='Digite a nova senha ')
            eNovaSenha= Entry(frame1)
            confirmaSenha=Label(frame1,text='digite novamente')
            eConfirmaSenha=Entry(frame1)
            bSalvar= Button(frame1,text='salvar',command=salvar)

            texto=Label(frame1,text='')
            texto.pack()

            novaSenha.pack()
            eNovaSenha.pack()
            confirmaSenha.pack()
            eConfirmaSenha.pack()
            bSalvar.pack()
            frame1.pack()
        else:
            aviso['text']='Login ou chave passe chave errados'
            
    i4=Tk()
    i4.title('OnFood')
    i4.geometry('350x350')

    login=Label(i4,text='Login')
    sLogin=Entry(i4)

    login.pack()
    sLogin.pack()

    chave=Label(i4,text='palavra chave')
    sChave=Entry(i4)

    chave.pack()
    sChave.pack()

    bSalvar= Button (i4,text='Entrar',command=acharUsuario)
    bSalvar.pack()

    bSair= Button(i4,text='sair',command=sair)
    bSair.pack()

    aviso= Label(i4,text='')
    aviso.pack()

    
    i4.mainloop()
    
    

'--------- DICIONARIOS---------------'

###OS DICIONARIOS ESTÃO SENDO USADAS COMO GLOBAL ###
####

dicionarioLogin=reescreverElementosDict('usuarios.txt')
dicionarioAlimento=reescreverElementosDict('alimentosTotais.txt')

####
'----------- entrar no login ---------------------'

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
        cadastroChave=Label(i3,text='palavra chave',font=14,bg='white')
        cadastroChave.pack()
        eChave=Entry(i3)
        eChave.pack()
        cadastroNivel=Label(i3,text='Nivel',font=14,bg='white')
        cadastroNivel.pack()
        eNivel=Entry(i3)
        eNivel.pack()
            
        def criarPessoas():
            
            '''Analisa se o login é existente no dict,caso ele seja adiciona no arquivo o novo usuario, caso o usuario já exista, ele avisa na interface!
                Também tem a função de sair, caso o usuario não queira mais cadastrar algum usuario novo'''
            novoUsuario={}
            if not eEmail.get() in dicionarioLogin:
                dicionarioLogin[eEmail.get()]=(eSenha.get(),eNome.get(),eChave.get(),eNivel.get())
                
                novoUsuario[eEmail.get()]=(eSenha.get(),eNome.get(),eChave.get(),eNivel.get())
                guardarElementosArq('usuarios.txt',novoUsuario)
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

    '------------ PRODUTOS UTILIZADOS NO DIA -----------'

    def produtosUtilizados():
        def salvar():
            valor=''
            novo=''
            qnt=int(eQntProduto.get())
            if eProduto.get() in dicionarioAlimento:
                valor=int(dicionarioAlimento[eProduto.get()][0])
                novo= valor-qnt
                dicionarioAlimento[eProduto.get()][0]=str(novo)
            elif eProduto.get() not in dicionarioAlimento:
                aviso['text']='Alimento não cadastrado'
                
        def sair():
            i3.destroy()
            
        
        i3= Frame(i2, bg = 'white' )
        produto= Label (i3, text='Digite o nome do produtos ',font=13,bg='white')
        eProduto=Entry(i3)
        qntProduto=Label(i3,text='Quantida de produto utilizado', font= 13,bg='white')
        eQntProduto= Entry(i3)
        produto.pack()
        eProduto.pack()
        qntProduto.pack()
        eQntProduto.pack()
        salvar = Button(i3, text='Salvar', command= salvar,bg='white')
        sair = Button(i3, text='Sair',command= sair )
        aviso = Label(i3,text='',bg='white')
        aviso.pack()
        salvar.pack()
        sair.pack()
        i3.pack()
        
    '-------- CADASTRO ALIMENTOS---------'
    def cadastroAlimentos(): 
        ''' É possivel cadastrar um novo alimento '''

        i3=Frame(i2,bg='white')
        #dictAlimento={alimento:(qnt,validade,tipo,preço)}
        alimento=Label(i3,text='Alimento',bg='white',font=15)
        alimentoE=Entry(i3)
        alimento.pack()
        alimentoE.pack()

        qntAlimento=Label(i3,text='Quantidade de produtos disponiveis',bg='white',font=15)
        qntAlimentoE=Entry(i3)
        qntAlimento.pack()
        qntAlimentoE.pack()

        validadeProdutos=Label(i3,text='Data de validade',bg='white',font=15)
        validadeProdutosE=Entry(i3)
        validadeProdutos.pack()
        validadeProdutosE.pack()

        tipoProduto= Label(i3,text='Tipo de produto',bg='white',font=15)
        tipoProdutoE=Entry(i3)
        tipoProduto.pack()
        tipoProdutoE.pack()

            
        precoProduto=Label(i3,text='Valor do produto',bg='white',font=15)
        precoProdutoE=Entry(i3)
        precoProduto.pack()
        precoProdutoE.pack()
        def SalvarCadastro():
            novoAlimento={}
            if not alimentoE.get() in dicionarioAlimento:
                dicionarioAlimento[alimentoE.get()]=(qntAlimentoE.get(),validadeProdutosE.get(),tipoProdutoE.get(),precoProdutoE.get())
                novoAlimento[alimentoE.get()]=(qntAlimentoE.get(),validadeProdutosE.get(),tipoProdutoE.get(),precoProdutoE.get())
                guardarElementosArq('alimentosTotais.txt',novoAlimento)
                aviso=Label(i3,text='Alimento cadastrado! ', font=14, bg= 'white')
                aviso.pack()
        def sair():
            i3.destroy()
                
            
        bCadastro=Button(i3,text='Salvar',command=SalvarCadastro)
        bSair=Button(i3,text='Sair',command=sair)
        bCadastro.pack()
        bSair.pack()
        i3.pack()




    '------------CARDAPIO DO DIA -------------'
    def cardarpioDia():
        def lanche():
            listaAlimento=[]
            listaBebida=[]
            
            for y in dicionarioAlimento:
                if dicionarioAlimento[y][2]=='bebida' :
                    listaBebida.append(y)
                if dicionarioAlimento[y][2]== 'lanche' :
                    listaAlimento.append(y)
            a=random.choice(listaBebida)
            b=random.choice(listaAlimento)

            def escolha():
                now = datetime.now()
                hora=str(now)
                arq= open('alimentoMensal.txt','a')
                arq.writelines(a)
                arq.write('--')
                arq.writelines(b)
                arq.write('--')
                arq.writelines(hora)
                arq.write('\n')

                i3.destroy()
                arq.close()


                     
            material=Label(i3,text='O cardapio será:',bg='white',fg='black',font=13)
            receitaBebida=Label(i3,text=a,bg='white',fg='black',font=13)
            receitaComida=Label(i3,text=b,bg='white',fg='black',font=13)
            Salvar= Button(i3,text='Salvar', command=escolha)
            
            material.pack()
            receitaComida.pack()
            receitaBebida.pack()
            Salvar.pack()
            

            
        def Almoco():

            listaAlimento=[]
            listaBebida=[]
            listaCarne=[]
            for x in dicionarioAlimento:
                if dicionarioAlimento[x][2]=='bebida' :
                    listaBebida.append(x)
                if dicionarioAlimento[x][2]== 'almoco' :
                    listaAlimento.append(x)
                if dicionarioAlimento[x][2] =='carne' :
                    listaCarne.append(x)
            
            a=random.choice(listaBebida)
            b=random.choice(listaAlimento)
            c=random.choice(listaCarne)
            d=random.choice(listaAlimento)
            
            def escolha():
                now = datetime.now()
                hora=str(now)
                arq= open('alimentoMensal.txt','a')
                arq.writelines(a)
                arq.write('--')
                arq.writelines(b)
                arq.write('--')
                arq.writelines(c)
                arq.write('--')
                arq.writelines(d)
                arq.writelines('--')
                arq.writelines(hora)
                arq.write('\n')

                
                aviso= Label(i3,text='Salvo')
                aviso.pack()
                i3.destroy()
                arq.close()
                
            material=Label(i3,text='O Almoço  será:',bg='white',fg='black',font=13)
            receitaBebida=Label(i3,text=a ,bg='white',fg='black',font=13)
            receitaComida=Label(i3,text=b ,bg='white',fg='black',font=13)
            receitaComida2=Label(i3,text=d ,bg='white',fg='black',font=13)
            receitaCarne= Label(i3,text=c ,bg='white',fg='black',font=13)
            Salvar= Button(i3,text='Salvar', command=escolha)

            
            material.pack()
            receitaComida.pack()
            receitaBebida.pack()
            receitaCarne.pack()
            Salvar.pack()

            
        def jantar():
            listaAlimento=[]
            listaBebida=[]
            listaCarne=[]
            for x in dicionarioAlimento:
                if dicionarioAlimento[x][2]=='bebida' :
                    listaBebida.append(x)
                if dicionarioAlimento[x][2]== 'jantar' :
                    listaAlimento.append(x)
                if dicionarioAlimento[x][2] =='carne' :
                    listaCarne.append(x)

                      
            a= random.choice(listaBebida)
            b= random.choice(listaAlimento)
            c= random.choice(listaCarne)

            def escolha():
                now = datetime.now()
                hora=str(now)
                arq= open('alimentoMensal.txt','a')
                arq.writelines(a)
                arq.write('--')
                arq.writelines(b)
                arq.write('--')
                arq.writelines(c)
                arq.write('--')
                arq.writelines(hora)
                arq.write('\n')

                i3.destroy()
                arq.close()
       
            material=Label(i3,text='O Jantar será:',bg='white',fg='black',font=13)
            receitaBebida=Label(i3,text=a ,bg='white',fg='black',font=13)
            receitaComida=Label(i3,text=b ,bg='white',fg='black',font=13)
            receitaCarne= Label(i3,text=c ,bg='white',fg='black',font=13)
            Salvar= Button(i3,text='Salvar', command=escolha)
                        
            material.pack()
            receitaComida.pack()
            receitaBebida.pack()
            receitaCarne.pack()
            Salvar.pack()
            
        def sair():
            i3.destroy()
        
            

                           
        i3 = Frame(i2,bg='white')
        bCafe= Button(i3,text='Café da manha ',command=lanche)
        bAlmoco= Button(i3,text='Almoço', command=Almoco)
        bJantar= Button(i3,text='Jantar',command=jantar)
        bLanche= Button(i3,text='Lanche',command=lanche)
        bSair= Button(i3,text='Sair',command=sair)
        
        bCafe.pack()
        bJantar.pack()
        bLanche.pack()
        bAlmoco.pack()
        bSair.pack()
        i3.pack()


    '------ ANALISA LISTA PRODUTOS--------'
    def listaProdutos():
        lerProdutos('alimentosTotais.txt')

        
    '----LER ARQUIVO DOS PRODUTOS---------'
    def lerProdutos(arq):
        arquivo= open(arq,'r')
        i3= Frame(i2,bg='white')
        for elemento in arquivo:
            nomeAlimento=Label(i3,text=elemento,bg='white',font=14)
            nomeAlimento.pack()

        def sair():
            i3.destroy()
            
        fechar= Button(i3,text='Sair',command=sair)
        fechar.pack()
        arquivo.close()
        i3.pack()
        
    '--------- ANALISA LISTA DO MES------'
    def mostrarListaMes():
        lerProdutos('AlimentoMensal.txt')



    '--------- REMOVER ELEMENTOS DO DICIONARIO------------'#NAO ESQUECER #######
    def removerElementoDict(dicionario,elemento): ##NAO ESQUECER#################
        def fechar():
            janela.destroy()

        if elemento in dicionario:
            del dicionario[elemento]
            janela=Tk()
            janela.title('OnFood')
            aviso= Label(janela, text='Elemento removido')
            bOk=Button(janela,text='ok',command=fechar)
            aviso.pack()
            bOk.pack()
            janela.mainloop()
        else:
            janela=Tk()
            janela.title('OnFood')
            aviso= Label(janela, text='Elemento não existe no dicionario')
            bOk=Button(janela,text='ok',command=fechar)
            aviso.pack()
            bOk.pack()
            janela.mainloop()


    '--------- REMOVER ALIMENTO -----------'    
    def removerAlimento():
        def sair():
            i3.destroy()
        def play():
            removerElementoDict(dicionarioAlimento,eAlimento.get())
            
        i3=Frame(i2,bg='white')

        alimento=Label(i3,text='Digite o alimento que você deseja remover', font=13)
        eAlimento= Entry(i3)
        alimento.pack()
        eAlimento.pack()

        
        bLogin=Button(i3,text='Deletar',command=play)
        bLogin.pack()

        
        bSair=Button(i3,text='Sair',command=sair)
        bSair.pack()

        i3.pack()


    '--------- NIVEL DO USUARIO -------------'
    def mudarNivel():
        def salvar():
            lista=[]
            
            if usuarioE.get() in dicionarioLogin :
                for x in dicionarioLogin[usuarioE.get()]:
                    lista.append(x)
                dicionarioLogin[usuarioE.get()]=lista 
                dicionarioLogin[usuarioE.get()][3]= nivelE.get()
                dicionarioLogin[usuarioE.get()]=tuple(lista)
                resposta['text']='Novo nivel salvo!'
                

            elif usuarioE.get() not in dicionarioLogin:
                resposta['text']='Usuario não encotrado'
                
        def sair():
            i3.destroy()

                
        i3= Frame(i2)
        usuario = Label(i3, text='Digite o usuario', bg= 'white',font=14)
        usuarioE= Entry(i3)
    
        usuario.pack()
        usuarioE.pack()

        nivel= Label(i3, text= 'Digite o novo nivel', bg= 'white',font=14)
        nivelE=Entry(i3)

        nivel.pack()
        nivelE.pack()

        salvar= Button(i3,text='Salvar',command=salvar)
        salvar.pack()

        sair= Button(i3,text='sair',command=sair)
        sair.pack()

        resposta=Label(i3,text='',bg='white',font=14)
        resposta.pack()
        i3.pack()
        
        
     

    '----------- REMOVER USUARIO -------------'
    def removerUsuario():
        def sair():
            i3.destroy()

        def play():
            removerElementoDict(dicionarioLogin,eLogin.get())
            
        i3=Frame(i2,bg='white')

        login=Label(i3,text='Digite o email do usuario que você deseja remover', font=13)
        eLogin= Entry(i3)
        login.pack()
        eLogin.pack()
        bLogin=Button(i3,text='Deletar',command=play)
        bLogin.pack()
        bSair=Button(i3,text='Sair',command=sair)
        bSair.pack()
        
        i3.pack()
        
      


    '------------------ XXX-----------'

    
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

        bCriarCardapio= Button(frameI2, text = 'Cardapio do dia',command=cardarpioDia) 
        bCriarCardapio.pack(side= LEFT,padx= 2,pady=2)

        bVerCardapio= Button(frameI2, text= 'Cardapio mensal',command=mostrarListaMes)
        bVerCardapio.pack(side= LEFT,padx= 2,pady=3)

        bListaProdutos =Button(frameI2, text= 'Lista de produtos ',command=listaProdutos) 
        bListaProdutos.pack(side= LEFT,padx= 2,pady=4)


        bAdicionarProdutos= Button(frameI2,text= 'Cadastro de Alimentos',command=cadastroAlimentos) 
        bAdicionarProdutos.pack(side= LEFT,padx= 1,pady=6)

        bRemoverAlimento= Button(frameI2, text= 'Remover alimentos da lista',command=removerAlimento) 
        bRemoverAlimento.pack(side=LEFT,padx=2,pady=5)

        bRemoverUsuario= Button(frameI2,text='Remover usuario',command=removerUsuario) 
        bRemoverUsuario.pack(side=LEFT,padx=2,pady=7)

        bProdutosUtilizados= Button(frameI2,text='Produtos utilizados no dia ',command=produtosUtilizados) ####FALTA###### #TODOS OS NIVEIS## ### FALTA REMOVER DA LISTA .TXT### 
        bProdutosUtilizados.pack(side=LEFT,padx=2,pady=9)

        bNivelUsuario=Button(frameI2,text='Mudar o nivel do usuario',command=mudarNivel) #####FALTA #######
        bNivelUsuario.pack(side=LEFT,padx=2,pady=8)

        
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

        bCriarCardapio= Button(frameI2, text = 'Cardapio do dia',command=cardarpioDia) 
        bCriarCardapio.pack(side= LEFT,padx= 2,pady=2)

        bVerCardapio= Button(frameI2, text= 'Cardapio mensal',command=mostrarListaMes)
        bVerCardapio.pack(side= LEFT,padx= 2,pady=3)

        bListaProdutos =Button(frameI2, text= 'Lista de produtos ',command=listaProdutos)
        bListaProdutos.pack(side= LEFT,padx= 2,pady=4)

        bAdicionarProdutos= Button(frameI2,text= 'Cadastro de Alimentos',command=cadastroAlimentos) 
        bAdicionarProdutos.pack(side= LEFT,padx= 1,pady=6)

        bRemoverAlimento= Button(frameI2, text= 'Remover alimentos da lista',command=removerAlimento)
        bRemoverAlimento.pack(side=LEFT,padx=2,pady=5)

        bProdutosUtilizados= Button(frameI2,text='Produtos utilizados no dia ',command=produtosUtilizados) ####FALTA###### #TODOS OS NIVEIS## ### FALTA REMOVER DA LISTA .TXT### 
        bProdutosUtilizados.pack(side=LEFT,padx=2,pady=9)

        frameI2.pack(side= TOP, fill=X)
        subMenu= Menu(i2)
        i2.mainloop()


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

        bCriarCardapio= Button(frameI2, text = 'Cardapio do dia',command=cardarpioDia) 
        bCriarCardapio.pack(side= LEFT,padx= 2,pady=2)

        bListaProdutos =Button(frameI2, text= 'Lista de produtos ',command=listaProdutos)
        bListaProdutos.pack(side= LEFT,padx= 2,pady=4)

        bProdutosUtilizados= Button(frameI2,text='Produtos utilizados no dia ',command=produtosUtilizados) ####FALTA###### #TODOS OS NIVEIS## ### FALTA REMOVER DA LISTA .TXT### 
        bProdutosUtilizados.pack(side=LEFT,padx=2,pady=9)

        frameI2.pack(side= TOP, fill=X)
        subMenu= Menu(i2)
        i2.mainloop()

    
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
subMenu.add_command(label='recuperar a senha',command=recuperarSenha) 
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



