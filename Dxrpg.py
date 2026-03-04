import random

import os

import sys


global resposta, classe, idade, nome, weapon, resistence, strength, agility, intelligence


def Fucntion_Start():
    print("Olá seja bem vindo. Digiite sim para começar o jogo ou não para sair")
    resposta = input("")
    if resposta.strip().lower() in ["sim", "s"]:
        return True
    else:
        print("Ok, jogo encerrado. Até mais!")
        sys.exit()

def Function_CreatePlayer():
    print("Vamos criar seu personagem. Qual é o nome do seu personagem?")
    nome = input("Nome: ")
    print(f"Olá, {nome}! Vamos começar a sua jornada!")
    print("Digite sua idade?")
    idade = input("Idade: ")
    print(f"Você tem {idade} anos. Isso é incrível!")
    print("Agora, escolha a classe do seu personagem: Guerreiro, Mago ou Arqueiro")
    classe = input("Classe: ")
    print(f"Você escolheu a classe {classe}. Isso é incrível!")
    if classe.strip().lower() == "guerreiro":
        print("Você é um guerreiro forte e corajoso!")
        weapon = "Espada"
    elif classe.strip().lower() == "mago":
        print("Você é um mago sábio e poderoso!")
        weapon = "Cajado"
    elif classe.strip().lower() == "arqueiro":
        print("Você é um arqueiro ágil e preciso!")
        weapon = "Arco"
    else:
        print("Classe inválida. Por favor, escolha entre Guerreiro, Mago ou Arqueiro.")
        return Function_CreatePlayer()
    return nome, idade, classe, weapon

def Function_Props():
    print("Agora, vamos definir os atributos do seu personagem.")
       
    resistence = random.randint(1, 10)
    print("Resistência:", resistence)
    print("Deseja girar os dados novamente para redefinir seus atributos? (sim/não)")  
    resposta = input("Girando os dados...")
    if resposta.strip().lower() in ["sim", "s"]:
        resistence = random.randint(1, 10)
        print("Resistência redefinida:", resistence)
        
    else:
        print("Atributos mantidos.", resistence)
        
         
    strength = random.randint(1, 10)
    print("Força:", strength)
    print("Deseja girar os dados novamente para redefinir seus atributos? (sim/não)")  
    resposta = input("Girando os dados...")
    if resposta.strip().lower() in ["sim", "s"]:
        strength = random.randint(1, 10)
        print("Força redefinida:", strength)
        
    else:
        print("Atributos mantidos.", strength)
        
    
    
    agility = random.randint(1, 10)
    print("Agilidade:", agility)
    print("Deseja girar os dados novamente para redefinir seus atributos? (sim/não)")
    resposta = input("Girando os dados...")
    if resposta.strip().lower() in ["sim", "s"]:
        agility = random.randint(1, 10)
        print("Agilidade redefinida:", agility)
        
    else:
        print("Atributos mantidos.", agility)
       

    intelligence = random.randint(1, 10)
    print("Inteligência:", intelligence)
    print("Deseja girar os dados novamente para redefinir seus atributos? (sim/não)")
    resposta = input("Girando os dados...")
    if resposta.strip().lower() in ["sim", "s"]:
        intelligence = random.randint(1, 10)
        print("Inteligência redefinida:", intelligence)
       
    else:
        print("Atributos mantidos.", intelligence)
        
    print("Seus atributos finais são:")
    print("{nome}, Resistência: {resistence}, Força: {strength}, Agilidade: {agility}, Inteligência: {intelligence}")

    return resistence, strength, agility, intelligence

def function_Historia(nome, classe, strength, agility, intelligence, resistence):
    print("\n" + "="*60)
    print("INICIANDO SUA JORNADA ÉPICA...")
    print("="*60 + "\n")
    
    if classe.strip().lower() == "guerreiro":
        print(f"🗡️  {nome}, o Guerreiro Lendário")
        print("-" * 60)
        print(f"\nVocê acordou em uma floresta escura e misteriosa.")
        print(f"Com sua força de {strength}, você avança confiante entre as árvores.")
        print(f"De repente, um rugido ensurdecedor ecoa pela floresta!")
        print(f"\nUm Orc gigante aparece à sua frente, bloqueando seu caminho.")
        print(f"Você empunha sua espada com determinação, pronto para o combate!")
        print(f"\n⚔️  BATALHA ÉPICA!")
        print(f"Sua força ({strength}) vs Força do Orc (15)")
        
        if strength >= 12:
            print(f"\nCom um golpe poderoso, você derrota o Orc!")
            print(f"O monstro cai ao chão, derrotado por sua bravura.")
        else:
            print(f"\nApós uma batalha feroz, você consegue vencer o Orc!")
            print(f"Sua determinação foi mais forte que a dor.")
        
    elif classe.strip().lower() == "mago":
        print(f"✨ {nome}, o Mago Sábio")
        print("-" * 60)
        print(f"\nVocê aparece em uma torre antiga, envolta em magia arcana.")
        print(f"Com sua inteligência de {intelligence}, você sente as energias mágicas ao redor.")
        print(f"Na sala ao fundo, você vê um fogo ardente e incontrolável!")
        print(f"\nUm espírito de fogo bloqueia seu acesso à saída.")
        print(f"Você levanta seu cajado, canalizando toda sua magia!")
        print(f"\n🔥 DUELO MÁGICO!")
        print(f"Sua inteligência ({intelligence}) vs Poder do Espírito (15)")
        
        if intelligence >= 12:
            print(f"\nCom um feitiço devastador, você dissipa o espírito!")
            print(f"A magia negra se desvanece pela torre.")
        else:
            print(f"\nApós um intenso duelo mágico, você vence o espírito!")
            print(f"Sua sabedoria superou a fúria das chamas.")
        
    elif classe.strip().lower() == "arqueiro":
        print(f"🏹 {nome}, o Arqueiro Lendário")
        print("-" * 60)
        print(f"\nVocê se vê em um vale profundo, cercado por penhascos íngremes.")
        print(f"Com sua agilidade de {agility}, você se move silenciosamente pelas sombras.")
        print(f"De súbito, você avista uma criatura alada no céu!")
        print(f"\nUm Grifo feroz desce em sua direção, pronto para atacar.")
        print(f"Você prepara seu arco com precisão mortal!")
        print(f"\n🦅 CAÇADA ÉPICA!")
        print(f"Sua agilidade ({agility}) vs Velocidade do Grifo (15)")
        
        if agility >= 12:
            print(f"\nCom flechas precisas, você derrota o Grifo!")
            print(f"O monstro alado cai do céu, vencido por sua precisão.")
        else:
            print(f"\nApós uma perseguição tensa, você consegue derrotar o Grifo!")
            print(f"Sua destreza foi o diferencial nessa batalha.")
        
    
    # escolha de sobrevivência
    print("\nVocê está cansado e faminto após o confronto.")
    escolha = input("Deseja caçar (c) ou beber água (b)? ").strip().lower()
    if escolha not in ['c', 'b']:
        print("Você hesita, mas acaba colhendo frutas silvestres para se manter.")
        resistence += 1
        print("(+1 de resistência pelas vitaminas)")
    else:
        if escolha == 'c':
            print("Você sai em busca de caça e consegue abater um pequeno animal.")
            strength += 1
            print("(+1 de força pela refeição nutritiva)")
        else:
            print("Você encontra um riacho cristalino e bebe água fresca.")
            agility += 1
            print("(+1 de agilidade por estar bem hidratado)")
    
    # resolução final com possível morte
    print("\nUm último desafio surge... role os dados para ver seu destino.")
    dice = random.randint(1, 20)
    print(f"Você rolou {dice}!")
    total = dice + (strength + agility + intelligence + resistence) // 4
    if total < 15:
        print("\n💀 O destino foi cruel...")
        print("Você sucumbiu às feridas e ao cansaço. Sua história termina aqui.")
        print("FIM DE JOGO")
        return
    
    print("\n🌟 O destino sorri para você...")
    print("Você supera o último obstáculo e emerge vitorioso!")
    
    print("\n" + "="*60)
    print("O DESTINO FINAL SE REVELA...")
    print("="*60)
    
    print(f"\nDepois de sua vitória, você sente uma energia estranha.")
    print(f"O chão começou a brilhar com runas antigos...")
    print(f"\nUma voz etérea ecoa:")
    print(f"'Aquele que venceu a besta da floresta/torre/vale'")
    print(f"'Você provou ser digno do poder supremo!'")
    
    print(f"\n✨ Uma luz cegante envolve você...")
    print(f"Seus atributos se potencializam!")
    print(f"Força: {strength} → {strength + 5}")
    print(f"Agilidade: {agility} → {agility + 5}")
    print(f"Inteligência: {intelligence} → {intelligence + 5}")
    print(f"Resistência: {resistence} → {resistence + 5}")
    
    print(f"\nVocê é transportado para um reino celestial...")
    print(f"Lá, você encontra o Grande Dragão Ancião.")
    print(f"\nO Dragão fala: 'Bem-vindo, {nome}!'")
    print(f"'Com sua bravura, você conquistou o direito'")
    print(f"'de ser o Guardião do Reino das Sombras!'")
    
    print(f"\n🐛 O Dragão coloca uma coroa em sua cabeça...")
    print(f"A magia flui por todo seu corpo!")
    print(f"Você se torna imortal e poderoso além da medida!")
    
    print(f"\n" + "="*60)
    print(f"🎭 PARABÉNS, {nome.upper()}!")
    print(f"VOCÊ COMPLETOU SUA JORNADA E SE TORNOU UMA LENDA!")
    print(f"="*60 + "\n")
    print("A história do seu personagem começa aqui...")




def main():
    # inicia jogo e gera personagem
    Fucntion_Start()
    nome, idade, classe, weapon = Function_CreatePlayer()
    resistence, strength, agility, intelligence = Function_Props()

    # executa a história com os atributos gerados
    function_Historia(nome, classe, strength, agility, intelligence, resistence)


if __name__ == "__main__":
    main()