import os
#acima a importação de uma biblioteca que nos permite usar algumas funções 

restaurantes = [{'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}, 
                {'nome':'Praça', 'categoria':'Japonesa', 'ativo':False},
                {'nome':'Pizza Suprema', 'categoria':'Pizza', 'ativo':True},]

#variável global referente a lista de restaurantes cadastrados através do app.py
#A estrutura de dados dicionário nos permite manter dentro da chaves, todas as 
#Innformações do restaurante cadastrado, se tornando mais interessante que a lista
#Para este projeto.

def exibir_nome_do_programa():
#Esta função serve para exibir o nome do programa
    print('SABOR EXPRESS\n  ')

def exibir_opcoes():
#Esta função serve para listar um menu de opções para o usuário
    print('1.Cadastrar restaurante')
    print('2.Listar restaurantes')
    print('3.Alternar estado do restaurante')
    print('4.Sair') 

def finalizar_app():
#Esta função serve para finalizar o app.
    exibir_subtitulo ('Finalizando o app\n')

def voltar_ao_menu_principal():
#esta função serve para retornar ao menu principal após o usuário digitar uma tecla
#Input - tecla digitada pelo usuário
    input('\nDigite uma tecla para voltar ao menu principal')
    main() 

def exibir_subtitulo(texto):
#Esta função serve para apresentar o subtitulo das demais funções quando forem acionadas.
#pode ser usada sempre que houver informações repetidas dentro de diferentes funções.
    os.system('cls')
    linha = '*' *(len(texto)) #len indica que a quantidade de asteristicos deve ser proporcional a quantidade de letras do texto
    print(linha)
    print(texto)
    print(linha) 
  
def opcao_invalida():
#Esta função é acionada quando o usuário escolhe um opção que não existe. 
    exibir_subtitulo('Opção inválida!\n')
    voltar_ao_menu_principal()  

def cadastrar_restaurante(): 
#Esta função serve para cadastrar um restaurante
#Input - nome do restaurante, categoria e status
#Output - Restaurante cadastrado com sucesso
    exibir_subtitulo('Cadastro de novos restaurantes\n')
    nome_do_restaurante=input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria=input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante={'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    #abaixo as instruções para inserir o restaurante na lista(variáve gobal criada antes das funções)
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()
    
def listar_restaurantes():
#Esta função imprime uma lista com os dados dos restaurantes cadastrados
    exibir_subtitulo('Listando restaurantes')

    print(f"{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status")
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
        voltar_ao_menu_principal()

def alternar_estado_restaurante():
#Esta função serve para alternar o status do restaurante
#Input - nome do restaurante que irá alternar status
    exibir_subtitulo('Alternando o Estado do Restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante ['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante ['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante ['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado.')
        voltar_ao_menu_principal()
   
def escolher_opcao():
#Esta função serve para o usuário escolher uma das opções apresentadas no inicio do código.
#Input - opção digitada pelo usuário
#Output - Roda a função correspondente a opção escolhida pelo usuário
    try:
        Opcao = int(input('Escolha uma opção: '))
        #Opcao = int(Opcao)
        #print (f'A opção escohida é: {Opcao}')
        #Acima, um exemplo de interpolação de variáveis
        #Este exemplo também permite que o terminal imprima a opção escolhida no input
        if Opcao == 1:
            #iniciar o cadastro do restaurante com a função
            cadastrar_restaurante()
        #elife = else + if em python
        elif Opcao == 2:
            listar_restaurantes()
        elif Opcao == 3:
            alternar_estado_restaurante()
        elif Opcao == 4:
            finalizar_app()
        #Se escolher outra opção além das sugeridas o programa pode encerrar conforme abaixo.
        else: 
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

    #abaixo o caminho para dizer que o app.py é o arquivo principal do programa
    #ou seja, so roda o que for chamado dentro dele
if __name__ == '__main__':  
    main()

