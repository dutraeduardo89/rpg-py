#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

import os

import sys



response = ""
arma_caca = ""
meat = ""
intelligence = random.randint(7, 20)
calculo = ""
resistence = random.randint(7, 20)
money = 50              
money2 = 25
produto = ""
strenght = random.randint(7, 20)    
choice = ""
name2 = ""




def Function_CreatePlayer():
    resposta = input("Iniciar novo jogo? (Sim/Não): ").strip().lower()

    if resposta == 'sim':
        nome = input("Escreva seu nome: ")
        age = input("Escreve sua idade: ")
        class1 = input("Escreve sua classe: ")
        attack = 0
        heath = 100
        fear = 0
        dice = random.randint(0, 20)
        global response, arma_caca, meat, intelligence, calculo, resistence, strenght
        response = ""
        arma_caca = ""
        meat = ""
        intelligence = random.randint(7, 20)
        calculo = ""
        resistence = random.randint(7, 20)
        strenght = random.randint(7, 20)
        return nome, class1, age, attack, heath, fear, dice
    elif resposta == 'não':
        print("Ok, jogo encerrado. Até mais!")
        sys.exit()
    else:
        print("Resposta inválida. Digite 'Sim' ou 'Não'.")
        return Function_CreatePlayer()





def Function_PlayerStatus(strenght, dexterity, intelligence, resistence):
    print("")
    print('Sua força é:', strenght)
    response = input('Gostaria de mudar sua força? Sim ou Não: ')
    if response.strip().lower() in ['sim', 's']:
        strenght = random.randint(7, 20)
        print('Sua nova força:', strenght)
    else:
        print('Sua força:', strenght)

    print("")
    print('Sua destreza é:', dexterity)
    response = input('Gostaria de mudar sua destreza? Sim ou Não: ')
    if response.strip().lower() in ['sim', 's']:
        dexterity = random.randint(7, 20)
        print('Sua nova destreza:', dexterity)
    else:
        print('Sua destreza', dexterity)

    print("")
    print('Sua inteligência:', intelligence)
    response = input('Gostaria de mudar sua inteligência? Sim ou Não: ')
    if response.strip().lower() in ['sim', 's']:
        intelligence = random.randint(7, 20)
        print('Sua nova inteligência:', intelligence)
    else:
        print('Sua inteligência:', intelligence)

    print("")
    print('Sua resistência é:', resistence)
    response = input('Gostaria de mudar sua resistência? Sim ou Não: ')
    if response.strip().lower() in ['sim', 's']:
        resistence = random.randint(7, 20)
        print('Sua nova resistência:', resistence)
    else:
        print('Sua nova resistência:', resistence)


def Play_Dice():
    print("")
    print("Gostaria de lançar o dado? Sim ou Não")
    response = input("")
    if response.strip().lower() in ['sim', 's']:
        dice = random.randint(7, 20)
        print('Seu resultado:', dice)
        return dice
    else:
        dice = random.randint(0, 20)
        print('Seu resultado:', dice)
        return dice




def Function_MiniGame1(money):
    print("")
    print("04:00 am")
    print("")
    print('Sua tarefa: (8+4) x (5-2) / 2 + √9 \n A)21, B)23, C)27, D)31')
    calculo = 21  # resultado correto
    response = input("Sua resposta: ")
    print("O resultado correto é:", calculo)

    print("")
    if response.strip().lower() == '21' or response.strip().lower() == 'a':
        print('É a verdadeira máquina, certa reposta!:')
        money = 50
    else:
        money = 25
        print("Resposta errada, tente novamente outra hora!")
    print("Salário:", money)
    return money


def compra(money):
    print("")
    print("Após conseguir terminar os cálculos, você vai até o ferreiro que estava terminando de forjar um machado.")
    print("Ao perguntar o preço, ele sugere que o justo por aquele machado recém feito e impecável era 35$ eldores.")
    print("Sugerindo também uma opção mais barata, uma faca e um canivete por 15$ eldores.")
    print("Qual você gostaria levar? (machado / faca e canivete)")
    print("Seu saldo:", money)
    response = input().strip().lower()
    if response == 'machado':
        produto = "Machado"
        money = money - 35
        print("Seu novo armamento é um: Machado")
        print("Seu saldo restante:", money, '$')
    else:
        produto = "Faca e canivete"
        money = money - 15
        print('Seu novo produto é uma Faca e um canivete')
        print("Seu saldo restante:", money, '$')
    return money, produto



def Function_Sobrevivencia(response, arma_caca, produto, meat, nome, intelligence, dice, strenght):
    print("")
    print("Então sai da aldeia e segue o caminho pela selva que é mais rápido.")
    print("Então ele(a) busca recurso naturais pra sua sobrevivência")
    print("Então acha pedras, bromélias, bambu e madeiras")
    print("Então pensa em duas possibilidades de armas \n criar uma lança com madeira \n ou com caule de palmeira, bambu e madeira criaria um arco e flecha ")
    print("Então avalia as opções e acaba percebendo que o arco  é mais vantajoso porém mais demorado \n lança mais fácil porém não tão precisa")
    print("Arco e flecha ou Lança?")
    response = input()
    if response.lower() == 'arco e flecha' or response.lower() == 'arco':
        arma_caca = "Arco e flecha"
        print('Então', nome, "decide fazer o", arma_caca, "ele(a) reúne os materiais necessários e parte pra criação")
    else:
        arma_caca = "lança"
        print('Então', nome, "decide fazer a", arma_caca, "ele(a) reúne os materiais necessários e parte pra criação")

    print("Antes de ir caçar ele(a) decide fazer uma fogueira,")
    if produto == "Faca e canivete":
        print("Ele(a) decide usar uma técnica de refletir a luz do sol com seu canivete")
    elif produto == "Machado":
        print("decide usar uma técnica de fricção que exige muito habilidade e tempo")
    print("Após conseguir fazer fogo",nome, "decide ir caçar. Logo adentro da floresta ele avista um cervo e um javali")
    print("Cervo ou javali?")
    response = input()
    if response.lower() == 'cervo':
        meat = "cervo"
        print('Então com seu', arma_caca, "acerta ele e vai em busca da carne do", meat)
        print("Logo após pegar a carne ele(a) corta em pedaços e guarda alguns pra depois, e vai logo assar.")
    else:
        meat = "javali"
        print('Então com seu', arma_caca, "acerta ele e vai em busca da carne do", meat)
        print("Logo após pegar a carne ele(a) corta em pedaços e guarda alguns pra depois, e vai logo assar.")
    print("Após comer ele(a) esconde a carne debaixo da terra pra nenhum predador farejar.")
    print("Então começa a escutar rugidos e barulhos de gravetos quebrando.")
    print("Logo ele(a) tenta fugir pra cima da árvores mais algo agarra seu pé com força o puxando pra baixo")
    print("Era uma puma")

    dice = 0
    
    # Teste com o Puma
    dice = Play_Dice()
    if dice > 13:
        print("Consegue escapar e se arma rapidamente")
        heath = 100
        print("Sua saúde pós ataque", heath)
        print("")
        print("Ele(a) percebe que tem que fazer uma estratégia contra os predadores.")
        print("Então passa lama em todo o corpo pra disfarçar o seu cheiro.")
        print("logo desenterra sua carne a guarda em sua mochila, e pega um graveto com pedaço de pano e faz uma tocha")
        print("caminhando pela floresta adentro, ele (a) sempre esperto nos barulhos e predadores")
        print("Chegando na aldeia", nome, "para pra se hidratar e para pra  descansar e esquentar sua carne")
        print("Após comer", nome, "vai treinar")
        print("Sua força pós treino", strenght + 2)
    else:
        print("Escapou mas se feriu")
        heath = 100 - 20
        print("Então une forças e parte pra cima do puma e o abate.")
        heath = 80
        print("Percebendo se ferimento grave no seu pé o que te deixa manco")
        print("ele(a) que ir buscar ajuda mas percebe que sua lesão está impossibiltando sua missão e está muito cansado(a).")
        print("Então fica em dúvida se vai buscar ajuda ou se sobe na copa de uma árvore pra descansar e seguir o trecho no outro dia")
        print("Ir atrás de ajuda ou descansar?")
        response = input("")

        if  response.lower() == 'descansar' or response.lower() == 'Descansar':
            response = "Descansar"
            print("Então", nome, "sobe em cima da árvore e deita-se pra descansar e dorme até o outro dia")
            print("Ao acordar, ele retira sua carne enterrada no solo e a esquenta pra comer")
            print("Logo após comer, começa sua jornada.")
            print("ele(a) percebe que tem que fazer uma estratégia contra os predadores.")
            print("Então passa lama em todo o corpo pra disfarçar o seu cheiro e segue a caminhada.")
            print("Chegando na aldeia",nome, "para pra se hidratar e logo depois vai atrás de ajuda")
            print("Ele(a) acha a curandeira da aldeia e inicia o tratamento da lesão")
            heath = 100
            print("Sua saúde pós tratamento", heath)
            print("Sua saúde pós tratamento: ", heath)
            print("Após recuperação", nome, "vai treinar")
            print("Sua força pós treino", strenght + 2)

        else:

            response.lower() == 'ir atras de ajuda' or response.lower() == 'ir atrás de ajuda'
            response = "ir atrás de ajuda"
            print("Ele(a) percebe que tem que fazer uma estratégia contra os predadores.")
            print("Então passa lama em todo o corpo pra disfarçar o seu cheiro e segue a caminhada.")
            print("logo mais", nome, " caminha pela floresta adentro, sempre esperto nos barulhos e predadores")
            print("Chegando na aldeia", nome, "para pra se hidratar e logo depois vai atrás de ajuda")
            print("Ele(a) acha a curandeira da aldeia e inicia o tratamento da lesão")
            heath = 100
            print("Sua saúde pós tratamento", heath)
            print("Sua saúde pós tratamento: ", heath)
            print("Após recuperação", nome, "vai treinar")
            print("Sua força pós treino", strenght + 2)





def Option_01(response, resistence, dice, arma_caca, money, produto, nome):
    print("")
    print("Ataca o ladrão e o vence")



def Gameplay(nome, class1,age, strenght, calculo, money, response, heath, appearance, intelligence, dice, resistence):

    print("Dia 01")
    dice = 0
    print("")
    print("Em um reino distante chamado Eldor, um castelo majestoso erguido no alto de uma montanha.")
    print("")
    print("Dia 01")
    print("")
    print("04:00 am")
    print("No coração desse castelo, a Princesa Elara, herdeira do trono")
    print("Foi capturada por uma terrível criatura conhecida como a Sombra do Dragão.")
    print("Essa entidade sombria, um ser místico que se alimentava do medo, lançou uma maldição sobre o reino")
    print("Mergulhando-o em trevas e desespero.")
    print("")
    print("07:00 am")
    print("O rei, desesperado para salvar sua filha e libertar seu povo do jugo da Sombra do Dragão ")
    print("Convoca um(a) herói(na) destemido(a) de seu povo, um(a) moço(a) com uma beleza peculiar.")
    print("Esse(a)"" herói(na) chamado", nome, "um(a)",class1," jovem de", age, "anos corajoso(a)"", dotado(a)"" de habilidades e conhecimentos.")
    print("")
    print("10:00 am")
    print("Seu caminho começa na aldeia de Eldoria, pouco próximo da montanha que abriga o castelo.")
    print("")
    print("11:00 am")
    print("Parando pra se hidratar e percebendo não ter dinheiro", money, "suficiente pra comprar seu armamento")
    print("Ele(a) avista uma placa de contrata-se")
    print("Interresado(a) ele conversa com o dono do comércio e é contratado sendo sua única função realizar cálculos matemáticos")
    print("Então começa seu expediente")
    print("")
    print("11:30 am")
    money = Function_MiniGame1(money)
    print("")
    print("")
    print("13:00 pm")
    money, produto = compra(money)
    print("13:20")
    Function_Sobrevivencia(response, arma_caca, produto, meat, nome, intelligence, dice, strenght)
    print("")
    print("Dia 02")
    print("")
    print("02:30 am")
    print("")
    print("06:00 am")
    print("começa sua jornada após descansar ele(a) segue a subida na montanha.")
    print("lugar com clima muito frio")
    print("08:00 am")
    print("Então no meio do caminho é rendido por um assaltante, que queria todo seu dinheiro")
    print("")
    Option_01(response, resistence, dice, arma_caca, money, produto, nome)
    print("")
    print("14:00 pm")
    print("ele (a) chega no topo da montanha e percebe que tem uma muralha em volta ao castelo, protegida de guardiões")
    print("então percebe um ponto fraco, onde só tem um guarda defesa. O Ataca e rouba sua armadura")
    print("ele(a) vasculha o castelo inteiro atrás da princesa. Então a acha, muito triste em uma cela")
    print("Logo",nome,"diz os encantamentos e abre a fechadura")
    print("recebido com um abraço da princesa, logo eles tem que achar a saída")
    print("então vão andadando em marcha lenta e nocauteando todos os guardas do caminho")
    print("Até que a entidade sobra do dragão toma forma uma humana e te ataca")
    print("")
    dice = 0

    print("")
    print("16:00 pm")
    print("")

    dice = 0

    # Teste de ataque
    dice = Play_Dice()
    if dice < 13:
        print("foi acertado")
        heath = 90
        print("então levanta e continua")
    else:
        print("com sua destreza ele desvia facilmente")

    # Contra-ataque
    dice = Play_Dice()
    if dice > 13:
        print("feriu a entidade")
    else:
        print("acertou a entidade")

    print("")
    print("19:00 pm")
    print("")
    print("derrotando a entidade",nome,"percebe que tem que selar aquela entidade e teria que ter uma alma a mais de guardião do selo")
    print("Então pede pra princesa dizer os encantamentos e selá-los em um frasco")
    print("")
    print("Dia 03")
    print("")
    print("00:00 am")
    print("Ao chegar nas terras é dado a notícia do ocorrido")
    print("")
    print("00:00 am")
    print("Então o rei manda fazer uma homenagem em nome de",nome, "uma festa e decreta 7 dias de luto")
    print(nome,"fica marcado(a) na história")


    encerrar_programa()





def main():
    print("Bem-vindo ao RPG Eldor!")
    choice = input("Digite 'iniciar' Para começar ou 'sair' para sair: ").strip().lower()
    
    if choice in ['iniciar novo jogo', '1', 'iniciar']:
        # Cria o personagem
        nome, class1, age, attack, heath, fear, dice = Function_CreatePlayer()
        
        # Define os atributos
        strenght = random.randint(7, 20)
        intelligence = random.randint(7, 20)
        resistence = random.randint(7, 20)
        dexterity = random.randint(7, 20)
        
        # Exibe status
        Function_PlayerStatus(strenght, dexterity, intelligence, resistence)
        
        # Mini jogo de cálculo
        money = Function_MiniGame1(50)
        
        # Compra de arma
        money, produto = compra(money)
        
        # Sobrevivência na floresta
        Function_Sobrevivencia(produto, arma_caca, produto, meat, nome, intelligence, dice, strenght)
        
        # Gameplay principal
        Gameplay(nome, class1, age, strenght, calculo, money, response, heath, "", intelligence, dice, resistence)
        
    elif choice == 'sair':
        print("Saindo do jogo. Até a próxima!")
        sys.exit()
    else:
        print("Opção inválida. Por favor, escolha novamente.")
        main()



import sys

def encerrar_programa():
    print("Encerrando o programa...")

    sys.exit()



if __name__ == "__main__":
    main()









# In[ ]:




