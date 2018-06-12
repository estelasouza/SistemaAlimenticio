

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

#FALTA O LOG##


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


'--------- DICIONARIOS---------------'

###OS DICIONARIOS ESTÃO SENDO USADAS COMO GLOBAL ###
####

dicionarioLogin=reescreverElementosDict('usuarios.txt')
dicionarioAlimento=reescreverElementosDict('alimentosTotais.txt')

####
'-------- REESCREVER DICT-----------'

def reescreverDict(arq,dicionario):
    
    arquivo=open(arq,'w')
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

'--------- ordenar elemento ------------------'
def ordenarElemento():
    arq= open('listaOrd.txt','a')
    lista=sorted(dicionarioLogin)
    for x in lista:
        if x in dicionarioLogin:
            arq.readlines(x)
            arq.readlines('--')
            arq.readlines(dicionarioLogin[x][0])
            arq.readlines('--')
            arq.readlines(dicionarioLogin[x][1])
            arq.readlines('--')
            arq.readlines(dicionarioLogin[x][2])
            arq.readlines('--')
            arq.readlines(dicionarioLogin[x][3])

            arq.readlines('\n')
    arq.close()
'----------- entrar no login ---------------------'

def entrarLogin():
    def loginLogout(string):

        now= datetime.now()
        hora=str(now)
        login=dicionarioLogin[eLogin.get()][0]
        arq= open('loginLogout.txt','a')
        arq.writelines(string)
        arq.writelines('--------')
        arq.writelines(login)
        arq.writelines('--------')
        arq.writelines(hora)
        arq.writelines('\n')
        
        arq.close()


    '---------CADASTRO PESSOAS---------------'
    ##LOGIN:(SENHA,NOME,IDADE,NIVEL)##
    def novoCadastro():   
        '''nessa função é possivel cadastrar um novo usuario'''
        
        i3=Frame(i2,bg='white')
        fonte=('Arial','10')
        cadastroEmail=Label(i3,text='Login',font=14,bg='white')
        cadastroEmail.pack()
        eEmail=Entry(i3)
        eEmail.pack()
        cadastroSenha=Label(i3,text='Senha',font=14,bg='white')
        cadastroSenha.pack()
        eSenha=Entry(i3)
        eSenha['font']=fonte
        eSenha['show']='*'
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
               
            
        bSalvar= Button(i3,text='Salvar',command=criarPessoas,width=5,height=1)
        bSalvar.pack(side=LEFT,fill=X)
        espaco=Label(i3,text='            ',bg='white',fg='white')
        espaco.pack(side=LEFT,fill=X)
        bSair =Button(i3,text='Sair',command=sair,width=5,height=1)
        bSair.pack(side=LEFT,fill=X)
         
        i3.pack()

    '------------ PRODUTOS UTILIZADOS NO DIA -----------'

    def produtosUtilizados():
        def salvar():
            valor=''
            novo=''
            qnt=int(eQntProduto.get())
            lista=[]
            if eProduto.get() in dicionarioAlimento:
                valor=int(dicionarioAlimento[eProduto.get()][0])
                novo= valor-qnt
                for x in dicionarioAlimento[eProduto.get()]:
                    lista.append(x)
                dicionarioAlimento[eProduto.get()]=lista
                dicionarioAlimento[eProduto.get()][0]=str(novo)
                dicionarioAlimento[eProduto.get()]=tuple(lista)
                reescreverDict
                ('alimentosTotais.txt',dicionarioAlimento)
                aviso['text']='Alimento cadastrado'

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
        salvar = Button(i3, text='Salvar', command= salvar,bg='white',width=5,height=2)
        sair = Button(i3, text='Sair',command= sair ,width=5,height=2)
        aviso = Label(i3,text='',bg='white')
        aviso.pack()
        salvar.pack()
        sair.pack()
        i3.pack(fill= BOTH)
        
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
                
            
        bCadastro=Button(i3,text='Salvar',command=SalvarCadastro,width=5,height=2)
        bSair=Button(i3,text='Sair',command=sair,width=5,height=2)
        bCadastro.pack()
        bSair.pack()
        i3.pack(fill= BOTH)




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
            Salvar= Button(i3,text='Salvar', command=escolha,width=5,height=2)
            
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
            Salvar= Button(i3,text='Salvar', command=escolha,width=5,height=2)

            
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
            Salvar= Button(i3,text='Salvar', command=escolha,width=5,height=2)
                        
            material.pack()
            receitaComida.pack()
            receitaBebida.pack()
            receitaCarne.pack()
            Salvar.pack()
            
        def sair():
            i3.destroy()
        
            

                           
        i3 = Frame(i2,bg='white')
        bCafe= Button(i3,text='Café da manha ',command=lanche,width=15,height=2)
        bAlmoco= Button(i3,text='Almoço', command=Almoco,width=10,height=2)
        bJantar= Button(i3,text='Jantar',command=jantar,width=10,height=2)
        bLanche= Button(i3,text='Lanche',command=lanche,width=10,height=2)
        bSair= Button(i3,text='Sair',command=sair,width=10,height=2)
        bCafe.pack(side=LEFT)
        bJantar.pack(side=LEFT)
        bLanche.pack(side=LEFT)
        bAlmoco.pack(side=LEFT)
        bSair.pack(side=LEFT)
        i3.pack(fill= BOTH)


    '------ ANALISA LISTA PRODUTOS--------'
    def listaProdutos():
        lerProdutos('alimentosTotais.txt')

        
    '----LER ARQUIVO DOS PRODUTOS---------'
    def lerProdutos(arq):
        arquivo= open(arq,'r')
        i3= Frame(i2,bg='grey')
        fontPadrao=('arial','14')
        for elemento in arquivo:
            nomeAlimento=Label(i3,text=elemento,bg='grey',fg='white',font=fontPadrao)
            nomeAlimento.pack()

        def sair():
            i3.destroy()
            
        fechar= Button(i3,text='Sair',command=sair,width=5,height=2)
        fechar.pack()
        arquivo.close()
        i3.pack(fill =Y)
        
    '--------- ANALISA LISTA DO MES------'
    def mostrarListaMes():
        lerProdutos('AlimentoMensal.txt')



    '--------- REMOVER ELEMENTOS DO DICIONARIO------------'
    def removerElementoDict(dicionario,elemento): 
        def fechar():
            janela.destroy()

        if elemento in dicionario:
            del dicionario[elemento]

            reescreverDict('usuarios.txt',dicionarioLogin)
            reescreverDict('alimentosTotais.txt',dicionarioAlimento)
            janela=Tk()
            janela.title('OnFood')
            aviso= Label(janela, text='Elemento removido')
            bOk=Button(janela,text='ok',command=fechar,width=5,height=2)
            aviso.pack()
            bOk.pack()
            janela.mainloop()
        else:
            janela=Tk()
            janela.title('OnFood')
            aviso= Label(janela, text='Elemento não existe no dicionario')
            bOk=Button(janela,text='ok',command=fechar,width=5,height=2)
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

        
        bLogin=Button(i3,text='Deletar',command=play,width=5,height=2)
        bLogin.pack()

        
        bSair=Button(i3,text='Sair',command=sair,width=5,height=2)
        bSair.pack()

        i3.pack(fill= BOTH)


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
                reescreverDict('usuarios.txt',dicionarioLogin)
                

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

        salvar= Button(i3,text='salvar',command=salvar,width=5,height=2)
        salvar.pack()

        sair= Button(i3,text='sair',command=sair,width=5,height=2)
        sair.pack()

        resposta=Label(i3,text='',bg='white',font=14)
        resposta.pack()
        i3.pack(fill= BOTH)
        
        
     

    '----------- REMOVER USUARIO -------------'
    def removerUsuario():
        def sair():
            i3.destroy()

        def play():
            removerElementoDict(dicionarioLogin,eLogin.get())
            
        i3=Frame(frameI2,bg='white')

        login=Label(i3,text='Digite o email do usuario que você deseja remover', font=13)
        eLogin= Entry(i3)
        login.pack()
        eLogin.pack()
        bLogin=Button(i3,text='Deletar',command=play,width=5,height=2)
        bLogin.pack()
        bSair=Button(i3,text='Sair',command=sair,width=5,height=2)
        bSair.pack()
        
        i3.pack(fill= BOTH)
        
    '---------- sair-------------'
    def sair():
        i2.destroy()
        loginLogout('Logout')

    '------------------ BUSCAR PRODUTO -------'
    def buscarProduto():
        def sair():
            i3.destroy()
            
        def achar():
            if eProduto.get() in dicionarioAlimento:
                mostrar['text']=dicionarioAlimento[eProduto.get()]
            else:
                mostrar['text']='produto não cadastrado'
                
        i3=Frame(i2,bg='white')
        
        produto=Label(i3,text='Digite o produto que deseja encontrar',font=15)
        eProduto=Entry(i3)
        
        bAchar=Button(i3,text='Procurar',command=achar,width=5,height=2)
        sair=Button(i3,text='sair',command=sair,width=5,height=2)

        mostrar=Label(i3,text='',font=19,bg='white')

        produto.pack()
        eProduto.pack()

        bAchar.pack()
        sair.pack()

        mostrar.pack()

        i3.pack(fill= BOTH)
    '------------------ XXX-----------'

    
    if eLogin.get() in dicionarioLogin and eSenha.get() == dicionarioLogin[eLogin.get()][0] and dicionarioLogin[eLogin.get()][3]=='1':
        loginLogout('Login')

        i2=Tk()
        i2.configure(bg='white')
        i2.title('OnFood')
        i2.geometry('800x600')
        fontPadrao=('arial','17')
        textoResposta1=Label(i2,text='Seja Bem vindo !',font=fontPadrao,bg='blue',fg='white')
        textoResposta1.pack(fill=X)
        frameI2= Frame(i2, bg= 'blue')
     
        menu = Menu(i2)

        i2.config(menu = menu)

        subMenu= Menu(menu)

        menu.add_cascade(label= 'Opções ', menu = subMenu) 
        subMenu.add_command(label= 'sair',command=sair)
        subMenu.add_separator()     
        
        bCriarUsuario=Button(frameI2,text='Cadastrar usuario',command=novoCadastro, width=25, height=2,font=17)
        bCriarUsuario.pack()

        bCriarCardapio= Button(frameI2, text = 'Cardapio do dia',command=cardarpioDia, width=25, height=2,font=17) 
        bCriarCardapio.pack()

        bVerCardapio= Button(frameI2, text= 'Cardapio mensal',command=mostrarListaMes, width=25, height=2,font=17)
        bVerCardapio.pack()

        bListaProdutos =Button(frameI2, text= 'Lista de produtos ',command=listaProdutos, width=25, height=2,font=17) 
        bListaProdutos.pack()

        bBuscarProdutos =Button(frameI2, text= 'Encontrar produto ',command=buscarProduto, width=25, height=2,font=17) 
        bBuscarProdutos.pack()


        bAdicionarProdutos= Button(frameI2,text= 'Cadastro de Alimentos',command=cadastroAlimentos, width=25, height=2,font=17) 
        bAdicionarProdutos.pack()

        bRemoverAlimento= Button(frameI2, text= 'Remover alimentos da lista',command=removerAlimento, width=25, height=2,font=17) 
        bRemoverAlimento.pack()

        bRemoverUsuario= Button(frameI2,text='Remover usuario',command=removerUsuario, width=25, height=2,font=17) 
        bRemoverUsuario.pack()

        bProdutosUtilizados= Button(frameI2,text='Produtos utilizados no dia ',command=produtosUtilizados, width=25, height=2,font=17) 
        bProdutosUtilizados.pack()

        bNivelUsuario=Button(frameI2,text='Mudar o nivel do usuario',command=mudarNivel, width=25, height=2,font=17) 
        bNivelUsuario.pack()

        
        frameI2.pack(side=LEFT,fill=Y)
        subMenu= Menu(i2)
        i2.mainloop()

        
    elif eLogin.get() in dicionarioLogin and eSenha.get() == dicionarioLogin[eLogin.get()][0] and dicionarioLogin[eLogin.get()][3]=='2':

        
        loginLogout('Login')
        i2=Tk()
        i2.configure(bg='white')
        i2.title('OnFood')
        i2.geometry('400x500')
        fontPadrao=('arial','17')
        textoResposta1=Label(i2,text='Seja Bem vindo !',font=fontPadrao,bg='white')
        textoResposta1.pack()
        frameI2= Frame(i2, bg= 'blue')
        menu = Menu(i2)

        i2.config(menu = menu)

        subMenu= Menu(menu)

        menu.add_cascade(label= 'Opções ', menu = subMenu) 
        subMenu.add_command(label= 'sair',command=sair)
        subMenu.add_separator()

        bCriarCardapio= Button(frameI2, text = 'Cardapio do dia',command=cardarpioDia, width=25, height=2,font=17) 
        bCriarCardapio.pack()

        bVerCardapio= Button(frameI2, text= 'Cardapio mensal',command=mostrarListaMes, width=25, height=2,font=17)
        bVerCardapio.pack()

        bListaProdutos =Button(frameI2, text= 'Lista de produtos ',command=listaProdutos, width=25, height=2,font=17)
        bListaProdutos.pack()

        bAdicionarProdutos= Button(frameI2,text= 'Cadastro de Alimentos',command=cadastroAlimentos, width=25, height=2,font=17) 
        bAdicionarProdutos.pack()

        bRemoverAlimento= Button(frameI2, text= 'Remover alimentos da lista',command=removerAlimento, width=25, height=2,font=17)
        bRemoverAlimento.pack()

        bProdutosUtilizados= Button(frameI2,text='Produtos utilizados no dia ',command=produtosUtilizados, width=25, height=2,font=17) 
        bProdutosUtilizados.pack()

        frameI2.pack(side= LEFT,fill=Y)
        subMenu= Menu(i2)
        i2.mainloop()


    elif eLogin.get() in dicionarioLogin and eSenha.get() == dicionarioLogin[eLogin.get()][0] and dicionarioLogin[eLogin.get()][3]=='3':
        
        loginLogout('Login')
        i2=Tk()
        i2.configure(bg='white')
        i2.title('OnFood')
        i2.geometry('400x500')
        fontPadrao=('arial','17')
        textoResposta1=Label(i2,text='Seja Bem vindo !',font=fontPadrao,bg='white')
        textoResposta1.pack()
        frameI2= Frame(i2, bg= 'blue')
        menu = Menu(i2)

        i2.config(menu = menu)

        subMenu= Menu(menu)

        menu.add_cascade(label= 'Opções ', menu = subMenu) 
        subMenu.add_command(label= 'sair',command=sair)
        subMenu.add_separator()

        bCriarCardapio= Button(frameI2, text = 'Cardapio do dia',command=cardarpioDia, width=25, height=2,font=17) 
        bCriarCardapio.pack()

        bListaProdutos =Button(frameI2, text= 'Lista de produtos ',command=listaProdutos, width=25, height=2,font=17)
        bListaProdutos.pack()

        bProdutosUtilizados= Button(frameI2,text='Produtos utilizados no dia ',command=produtosUtilizados, width=25, height=2,font=17)
        bProdutosUtilizados.pack()

        frameI2.pack(side= LEFT)
        subMenu= Menu(i2)
        i2.mainloop()

    
    else:
        textoResposta['text']='Senha ou login invalidos'
    return dicionarioLogin

'------------ RECUPERAR A SENHA -------------'

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
                dicionarioLogin[sLogin.get()][0]=eNovaSenha.get()
                dicionarioLogin[sLogin.get()]=tuple(lista)
                texto['text']='Senha cadastrada'
                reescreverDict('usuarios.txt',dicionarioLogin)
            else:
                texto['text']='A senha não está igual'
                
                
        if sLogin.get() in dicionarioLogin and dicionarioLogin[sLogin.get()][2]== sChave.get():

        
            frame1=Frame(i4)
            fontePadrao=('Arial','10')
            novaSenha=Label(frame1,text='Digite a nova senha ')
            eNovaSenha= Entry(frame1)
            eNovaSenha['font']=fontePadrao
            eNovaSenha['show']='*'
            confirmaSenha=Label(frame1,text='digite novamente')
            eConfirmaSenha=Entry(frame1)
            eConfirmaSenha['font']=fontePadrao
            eConfirmaSenha['show']='*'
            bSalvar= Button(frame1,text='salvar',command=salvar,width=5,height=2)

            texto=Label(frame1,text='')
            texto.pack()

            novaSenha.pack()
            eNovaSenha.pack()
            confirmaSenha.pack()
            eConfirmaSenha.pack()
            bSalvar.pack()
            frame1.pack(fill=BOTH)
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

    bSalvar= Button (i4,text='Entrar',command=acharUsuario,width=5,height=2)
    bSalvar.pack()

    bSair= Button(i4,text='sair',command=sair,width=5,height=2)
    bSair.pack()

    aviso= Label(i4,text='')
    aviso.pack()

    
    i4.mainloop()
    
    

'======== CODIGO INICIAL ============='        
        

i1= Tk()
i1.geometry('500x400')
i1.title('OnFood')
i1.configure(bg='yellow')
fontePadrao=('Arial','10')


menu = Menu(i1)

i1.config(menu = menu)

subMenu= Menu(menu)

menu.add_cascade(label= 'Opções ', menu = subMenu)
subMenu.add_command(label='recuperar a senha',command=recuperarSenha) 
subMenu.add_separator()


texto = Label (i1,text='Seja bem vindo ao OnFood!!',fg='blue',font='23',bg='yellow')
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


textoResposta=Label(i1,text='',bg='yellow')
textoResposta.place(x=70,y=230)

i1.mainloop()

'--------criptografia------------'
stringArq=guardarArqEmStr('usuarios.txt')
x=criptografarArq(stringArq)
guardarArqCrip(x)



