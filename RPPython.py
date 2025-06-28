import os, time, random, sys

condicao_while = True     
atributos_contagem = 5

#Atributos do personagem
Name = 0
Health = 5  #Altera a vida do personagem
Health_combat = Health #Para o combate nn afetar a vida principal diretamente
HpMAX = 0
Defense = 2  #Altera a quantidade de dano recebido
Energy = 3 #Altera a energia para realizar tarefas secundárias
Dexterity = 3 #altera a chance de fugir de um combate
Strength = 4 #Altera o dano causado
Intelligence = 4 #Altera a chance de investigação
Gold = 0

equipamento = [
    "Espada de ferro enferrujada", "Armadura de combate desgastada", "Botas velhas"
]

inventario = {
    "curativo" : 1,

}

dic_nivel = {
    "Nível 1": {
        "nivel_atual" : 1,
        "xp_inicial" : 0,
        "xp_limite" : 100,
        "pontos_ganhos" : 5,
    },

    "Nível 2": {
        "nivel_atual" : 2,
        "xp_inicial" : 0,
        "xp_limite" : 125,
        "pontos_ganhos" : 5,
    },
    "Nível 3": {
        "nivel_atual" : 3,
        "xp_inicial" : 0,
        "xp_limite" : 150,
        "pontos_ganhos" : 5,
    },
    "Nível 4": {
        "nivel_atual" : 4,
        "xp_inicial" : 0,
        "xp_limite" : 175,
        "pontos_ganhos" : 5,
    },
    "Nível 5": {
        "nivel_atual" : 5,
        "xp_inicial" : 0,
        "xp_limite" : 200,
        "pontos_ganhos" : 5,
    },
    "Nível 6": {
        "nivel_atual" : 6,
        "xp_inicial" : 0,
        "xp_limite" : 225,
        "pontos_ganhos" : 5,
    },
    "Nível 7": {
        "nivel_atual" : 7,
        "xp_inicial" : 0,
        "xp_limite" : 250,
        "pontos_ganhos" : 5,
    },
    "Nível 8": {
        "nivel_atual" : 8,
        "xp_inicial" : 0,
        "xp_limite" : 275,
        "pontos_ganhos" : 5,
    },
    "Nível 9": {
        "nivel_atual" : 9,
        "xp_inicial" : 0,
        "xp_limite" : 300,
        "pontos_ganhos" : 5,
    },
    "Nível 10": {
        "nivel_atual" : 10,
        "xp_inicial" : 0,
        "xp_limite" : 325,
        "pontos_ganhos" : 5,
    },
    "Nível 11": {
        "nivel_atual" : 11,
        "xp_inicial" : 0,
        "xp_limite" : 350,
        "pontos_ganhos" : 5,
    },
    "Nível 12": {
        "nivel_atual" : 12,
        "xp_inicial" : 0,
        "xp_limite" : 375,
        "pontos_ganhos" : 5,
    },
    "Nível 13": {
        "nivel_atual" : 13,
        "xp_inicial" : 0,
        "xp_limite" : 400,
        "pontos_ganhos" : 5,
    },
    "Nível 14": {
        "nivel_atual" : 14,
        "xp_inicial" : 0,
        "xp_limite" : 425,
        "pontos_ganhos" : 5,
    },
    "Nível 15": {
        "nivel_atual" : 15,
        "xp_inicial" : 0,
        "xp_limite" : 450,
        "pontos_ganhos" : 5,
    },
    "Nível 16": {
        "nivel_atual" : "MAX",
        "xp_inicial" : 0,
        "xp_limite" : 475,
        "pontos_ganhos" : 0,
    },
}

contador_xp = 0

Level = dic_nivel["Nível 1"]["nivel_atual"]

x = 0
y = 0

        # x = 0        # x = 1      # x = 2         # x = 3        # x = 4
Map = [["Acampamento", "Floresta", "Floresta Negra", "Rio Verde", "Acampamentos dos bandidos"],      # y = 0
       ["Planície","Floresta", "Planícies Verdejantes", "Cidade Alta", "Posto de Mineração"],        # y = 1
       ["Floresta Funge", "Rio Funge", "Lago", "Cidade Baixa","Floresta"],                            # y = 2
       ["Montanhas", "Vilarejo das montanhas", "Depressão", "Caverna", "Floresta"],                   # y = 3
       ["Montanha do Dragão","Posto Comercial", "Montanhas", "Ponte", "Vale da Perdição"],]                      # y = 4

y_len = len(Map) - 1
x_len = len(Map[0]) - 1

painel_atual = Map[y][x]   #Demonstra qual é o meu painel atual no mapa
print(painel_atual) 


enemies_list = ["Soldado caído", "Saqueador", "Javali"]

mobs_loot = {
    "Soldado caído": [
        "Espada Quebrada", "Elmo perfurado"
    ],

    "Saqueador": [
        "Botas sujas", "Panos Rasgados"
    ],

    "Javali": [
        "Presas de Javali", "Carne de Porco"
    ],
}

# Mobs Temporários
mobs = {
    "Soldado caído": {
        "hp": 20,
        "str": 5,
        "defen": 2,
        "go":  10,
        "xp": 20,
    },

    "Saqueador": {
        "hp": 25,
        "str": 6,
        "defen":  1,
        "go":  15,
        "xp": 25,
    },

    "Javali": {
         "hp": 15,
        "str":  4,
        "defen":  1,
        "go":   5,
        "xp": 15,
    },
}

#Alternação das levas de dialogos
dialogo_1 = True


biom_description = {
    "Acampamento" : {
        "contador" : 0,
        "description_1" : [#"No meio da grama amassada e das cinzas quentes da fogueira, o seu acampamento parece um refúgio simples.",
                           #"De vez em quando dá pra ouvir o barulho de uma armadura ou das folhas balançando. O cheiro de couro ",
                           #"e chá de ervas enche o ar. É um lugar pequeno, mas seguro."
                           ],

        "description_2" : [#"O acampamento fica debaixo de árvores altas, onde a sombra é fresca e o som da fogueira é tranquilo.",
                           #"Um pedaço de pão está em cima de um tronco que serve de mesa, e uma brisa leve balança os panos das tendas.",
                           #"Aqui, tudo é calmo, um bom lugar para descansar."
                           ],

        "description_3" : ["Você está em seu acampamento."]
    },
    "Floresta" : {
        "contador" : 1,
        "description_1" : [#"A floresta fica mais fechada conforme se caminha. Galhos secos arranham os ombros e a luz do dia fica ",
                           #"fraca entre as folhas. Um cheiro forte de madeira e musgo toma conta do ar. Tudo parece calmo, mas há algo ",
                           #"estranho no silêncio."
                           ],

        "description_2" : [#"A cada passo, o chão úmido afunda um pouco, e raízes grossas cruzam o caminho. O vento sopra entre as ",
                           #"árvores e faz um assobio leve, quase como se a floresta sussurrasse algo. ",
                           #"É fácil se perder aqui — tanto nos caminhos quanto nos pensamentos."
                           ],

        "description_3" : ["Você está no meio de uma floresta"]
    },
    "Floresta Negra" : {
        "contador" : 1,
        "description_1" : ["....."],
        "description_2" : ["....."],
        "description_3" : ["....."]
    },
    "Rio Verde" : {
        "contador" : 1,
        "description_1" : ["....."],
        "description_2" : ["....."],
        "description_3" : ["....."]
    },
    "Acampamentos dos bandidos" : {
        "contador" : 1,
        "description_1" : ["....."],
        "description_2" : ["....."],
        "description_3" : ["....."]
    },
    "Planície" : {
        "contador" : 1,
        "description_1" : ["....."],
        "description_2" : ["....."],
        "description_3" : ["....."]
    },
    "Planícies Verdejantes" : {
        "contador" : 1,
        "description_1" : ["....."],
        "description_2" : ["....."],
        "description_3" : ["....."]
    },
    "Cidade Alta" : {
        "contador" : 1,
        "description_1" : ["....."],
        "description_2" : ["....."],
        "description_3" : ["....."]
    },
    "Cidade Baixa" : {
        "contador" : 1,
        "description_1" : ["....."],
        "description_2" : ["....."],
        "description_3" : ["....."]
    },
    "Posto de Mineração" : {
        "contador" : 1,
        "description_1" : ["....."],
        "description_2" : ["....."],
        "description_3" : ["....."]
    },
    "Floresta Funge" : {
        "contador" : 1,
        "description_1" : ["....."],
        "description_2" : ["....."],
        "description_3" : ["....."]
    },
     "Rio Funge" : {
        "contador" : 1,
        "description_1" : ["....."],
        "description_2" : ["....."],
        "description_3" : ["....."]
    },
     "Lago" : {
        "contador" : 1,
        "description_1" : ["....."],
        "description_2" : ["....."],
        "description_3" : ["....."]
    },
    "Montanhas" : {
        "contador" : 1,
        "description_1" : ["....."],
        "description_2" : ["....."],
        "description_3" : ["....."]
    },
    "Vilarejo das montanhas" : {
        "contador" : 1,
        "description_1" : ["....."],
        "description_2" : ["....."],
        "description_3" : ["....."]
    },
    "Depressão" : {
        "contador" : 1,
        "description_1" : ["....."],
        "description_2" : ["....."],
        "description_3" : ["....."]
    },
    "Caverna" : {
        "contador" : 1,
        "description_1" : ["....."],
        "description_2" : ["....."],
        "description_3" : ["....."]
    },
    "Montanha do Dragão" : {
        "contador" : 1,
        "description_1" : ["....."],
        "description_2" : ["....."],
        "description_3" : ["....."]
    },
    "Vale da Perdição" : {
        "contador" : 1,
        "description_1" : ["....."],
        "description_2" : ["....."],
        "description_3" : ["....."]
    },
    "Ponte" : {
        "contador" : 1,
        "description_1" : ["....."],
        "description_2" : ["....."],
        "description_3" : ["....."]
    },
    "Posto Comercial" : {
        "contador" : 1,
        "description_1" : ["....."],
        "description_2" : ["....."],
        "description_3" : ["....."]
    },
}
#Status dos biomas
biom = {
    "Acampamento": {
        "text" : "ACAMPAMENTO",
        "enemies" : False},

    "Floresta": {
        "text" : "FLORESTA",
        "enemies" : True},
    
    "Floresta Negra": {
        "text" : "FLORESTA NEGRA",
        "enemies" : True},

    "Rio Verde": {
        "text" : "RIO VERDE",
        "enemies" : False},

    "Acampamentos dos bandidos": {
        "text" : "ACAMPAMENTO DOS BANDIDOS",
        "enemies" : True},

    "Planície": {
        "text" : "PLANÍCIE",
        "enemies" : True},

    "Planícies Verdejantes": {
        "text" : "PLANÍCIES VERDEJANTES",
        "enemies" : False},

    "Cidade Alta": {
        "text" : "CIDADE ALTA",
        "enemies" : False},

    "Posto de Mineração": {
        "text" : "POSTO DE MINERAÇÃO",
        "enemies" : False},

    "Floresta Funge": {
        "text" : "FLORESTA FUNGE",
        "enemies" : True},
    
    "Rio Funge": {
        "text" : "RIO FUNGE",
        "enemies" : False},
    
    "Lago": {
        "text" : "LAGO",
        "enemies" : True},

    "Cidade Baixa": {
        "text" : "CIDADE BAIXA",
        "enemies" : True},

    "Montanhas": {
        "text" : "MONTANHAS",
        "enemies" : True},
    
    "Vilarejo das montanhas": {
        "text" : "VILAREJO DAS MONTANHAS",
        "enemies" : False},

    "Depressão": {
        "text" : "DEPRESSÃO",
        "enemies" : True},

    "Caverna": {
        "text" : "CAVERNA",
        "enemies" : True},

    "Montanha do Dragão": {
        "text" : "MONTANHA DO DRAGÃO",
        "enemies" : False},

    "Vale da Perdição": {
        "text" : "VALE DA PERDIÇÃO",
        "enemies" : True},
    
    "Ponte": {
        "text" : "PONTE",
        "enemies" : False},

    "Posto Comercial": {
        "text" : "POSTO COMERCIAL",
        "enemies" : False},
}
def parar_loop():  #Função para parar o while quando precisar
    global condicao_while
    condicao_while = False

def clear(): #Função para limpar o terminal
    os.system("cls")

def linhas(): #Função para aparecer as linhas de demarcação
    print("xX=================================Xx")

def contagem_pontos(a): #Função que checa a contagem de pontos que sera adicionado aos atributos do personagem
    global atributos_contagem

    if atributos_contagem >= a and a <= atributos_contagem:
            atributos_contagem = atributos_contagem - a
            print(f"\n# Pontos restantes: {atributos_contagem}")
            parar_loop()
            return a
    else:
        print("Pontos insuficiêntes, tente novamente")
        return "none"

def fronteira(): #Função que mostra mensagem ao chegar na fronteira do mapa
    clear()
    linhas()
    print("Existem dragões além das fronteiras, é perigoso ir para la!")
    linhas()
    print("- Digite qualquer tecla para continuar")
    input("\n#>")

def batalha(): #Função que define o funcionamento das batalhas
    global fight, play, Gold, Dressing, Health, Health_combat, y, x, Defense

    Health_combat = Health
    enemy = random.choice(enemies_list)
    hp = mobs[enemy]["hp"]
    hpmax = hp
    stren = mobs[enemy]["str"]
    defen = mobs[enemy]["defen"]
    g = mobs[enemy]["go"]

    while fight:
        clear()
        linhas()
        print("Enquanto andava você encontrou um(a) " + enemy + "!")
        print("Derrote ele(a) e ganhe recompensas!")
        linhas()
        print(enemy + ":  Vida: " + str(hp) + "/" + str(hpmax))
        print(Name + ":  Vida: " + str(Health_combat) + "/" + str(HpMAX))
        linhas()
        print("1 - Ataque")
        if "curativo" in inventario:
            print("2 - Usar curativo (20HP)")
        print("3 - Fuja")
        linhas()

        choice = input("#>")

        if choice =="1":
            dano_personagem = random.randint(Strength - 2, Strength + 3) - defen
            hp -=  dano_personagem #Mudar para o dano random (Esta random, altere se quiser)
            print(f"{Name} causou {str(dano_personagem)} de dano em {enemy}.")
            if hp > 0:
                dano_entidade = random.randint(stren - 2, stren + 3) - Defense
                Health_combat -= dano_entidade
                print(f"{enemy} causou {str(dano_entidade)} de dano em {Name}.")
            input("#>")

        elif choice =="2": 
            if "curativo" in inventario:
                cura_batalha(20)
                remover_item(inventario, "curativo", 1)
                dano_entidade = random.randint(stren - 2, stren + 3) - Defense
                Health_combat -= dano_entidade
                print(f"{enemy} causou {str(dano_entidade)} de dano em {Name}.")
            else:
                print("Você esta sem curativos!")
            input("#>")

        elif choice =="3":

            chance_fuga_batalha = fugir()

            if chance_fuga_batalha >= 11:
                print("\nVocê escapou da batalha com sucesso!")
                input("#>")
                clear()
                break
            
            else:
                print("\nVocê não conseguiu escapar da batalha...")

                dano_entidade = random.randint(stren - 2, stren + 3) - Defense
                Health_combat -= dano_entidade

                print(f"\n{enemy} causou {str(dano_entidade)} de dano em {Name}.")
                input("#>")



        if Health_combat <= 0:
            print(f"{enemy} derrotou {Name}...") 
            linhas()
            if Health <= 0:  #Por enquanto não é possivel zerar a vida, manter os codigos caso mude de ideia
                print("Você foi derrotado, fique mais forte para a próxima batalha.")
                y = 0
                x = 0
                Health = HpMAX / 2
            
            if Health - 5 > 15:
                Health -= 5
                print("Você perdeu essa luta, fique mais forte para as próximas!")
            
            input("#>")
            clear()
            break

        if hp <= 0:
            print(f"{Name} derrotou {enemy}!!!")
            Gold += g
            print(f"Você ganhou {g} moedas de prata!")
            print(f"Você ganhou {mobs[enemy]["xp"]} de experiência!")
            if random.randint(0, 100) <= 80:
                loot_ganho = random.choice(mobs_loot[enemy])
                print(f"Você ganhou {loot_ganho}")
                adicionar_item(inventario, loot_ganho)
            level_up(mobs[enemy]["xp"])
            Health = Health - 5
            input("#>")
            clear()
            break

def cura_menu(amount): #Função que faz o personagem utilizar um item de cura e aumentar seu HP no menu de jogo
    global Health
    if Health + amount < HpMAX:
        Health += amount
    else:
        Health = HpMAX

    print("Você se curou com sucesso!")

def cura_batalha(amount): #Função que faz o personagem utilizar um item de cura e aumentar seu HP no menu de batalha
    global Health_combat
    if Health_combat + amount < HpMAX:
        Health_combat += amount
    else:
        Health_combat = HpMAX

    print("Você se curou com sucesso!")

def mostrador_xp():
    return f"{contador_xp}/{dic_nivel[f'Nível {Level}']['xp_limite']}"

def level_up(xp):
    global Level, mostrador_xp, contador_xp, atributos_contagem

    contador_xp = contador_xp + xp
    if Level == "MAX":
        print("Você chegou ao nível máximo!")
        
    if contador_xp >= dic_nivel[f"Nível {Level}"]["xp_limite"]:
        atributos_contagem += dic_nivel[f"Nível {Level}"]["pontos_ganhos"]
        print(f"Você subiu de nivel! - {atributos_contagem} pontos de atributos disponiveis")
        Level = dic_nivel[f"Nível {Level + 1}"]["nivel_atual"]
        contador_xp = dic_nivel[f'Nível {Level}']['xp_limite'] - contador_xp 

def adicionar_item(inventario, item, quantidade=1):
    if item in inventario:
        inventario[item] += quantidade
    else:
        inventario[item] = quantidade

def remover_item(inventario, item, quantidade=1):
    if item in inventario:
        inventario[item] -= quantidade
        if inventario[item] <= 0:
            del inventario[item]

def mostrar_inventario():
    global inventario

    if not inventario:
            print("  (vazio)  ")
    else:  
        for item, qtd in inventario.items():
                print(f"- {item}: {qtd}")

def exibidor_texto_rpg(texto_lista, delay):
    for linha in texto_lista:
        for char in linha:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)

        print()

def escolha_exibidor_descricao():

    if biom_description[Map[y][x]]["contador"] == 0:
        biom_description[Map[y][x]]["contador"] += 1
        

    elif biom_description[Map[y][x]]["contador"] == 1:
        biom_description[Map[y][x]]["contador"] += 1
        print("======================================================================================================")
        exibidor_texto_rpg(biom_description[Map[y][x]]["description_1"], 0.01)
        print("======================================================================================================")
        input("\n#>")
    
    elif biom_description[Map[y][x]]["contador"] == 2:
        biom_description[Map[y][x]]["contador"] += 1
        print("======================================================================================================")
        exibidor_texto_rpg(biom_description[Map[y][x]]["description_2"], 0.01)
        print("======================================================================================================")
        input("\n#>")

    else:
        print("============================================")
        exibidor_texto_rpg(biom_description[Map[y][x]]["description_3"], 0.01)
        print("============================================")
        input("\n#>")

def fugir():
    global Dexterity

    chance_fuga = 4 * Dexterity

    return random.randint(0, chance_fuga)

def marcacao_dialogo():
    print("======================================================================================================")

def descansar_acampamento(cura):
    global Health
    if Health + cura < HpMAX:
        Health += cura
    else:
        Health = HpMAX
    clear()
    marcacao_dialogo()
    print(" O aventureiro(a) adormece na barraca do acampamento. Ao acordar você se sente mais forte")
    marcacao_dialogo()
    input("#>")

#Menus interativos
run = True
menu = True
play = False
status = False
fight = False
menu_game = True  #Define se não vai aparecer batalhas quando voltar de algum menu
status_points = False
inv = False
description = True
inside_region = False

#Menu dentro das regiões
Acampamento = False
Floresta = False
Floresta_Negra = False
Rio_Verde = False
Acampamento_Dos_Bandidos = False
Planicie = False
Planicie_Verdejantes = False
Cidade_Alta = False
Posto_De_Mineracao = False
Floresta_Funge = False
Rio_Funge = False
Lago = False
Cidade_Baixa = False
Montanhas = False
Vilarejo_Das_Montanhas = False
Depressao = False
Caverna = False
Montanha_Do_Dragao = False
Vale_Da_Perdicao = False
Ponte = False
Posto_Comercial = False

while run:
    while menu:
        clear()
        linhas()
        print(" - Bem vindo ao RPPython -")
        linhas()
        print("# Menu:")
        print("\n- Para começar o jogo digite 1")
        print("- Para sair do jogo digite 2")
        linhas()
        try:
            escolha_menu = int(input("#: "))
        except ValueError:
            print("Digite apenas numeros, tente novamente")
            time.sleep(1.5)
            continue
        if escolha_menu in [1,2]:
            if escolha_menu == 1:
                clear()
                Name = input("# Qual é o seu nome, heroi? > ")
                linhas()
                clear()

            
                linhas()
                print(" - Defina seus atributos -")
                linhas()
                print("\nVocê tem 5 pontos para distribuir em:")
                print('\n# Vida - possui "5" pontos')
                print('# Defesa - possui "2" pontos ')
                print('# Energia - possui "3" pontos')
                print('# Destreza - possui "3" pontos')
                print('# Força - possui "4" pontos')
                print('# Inteligência - possui "4" pontos')
                print('\nCaso não deseja aumentar nenhum atributo, digite 0')
                linhas()

                while condicao_while:
                    try:
                        vida = contagem_pontos(int(input("- Digite a quantidade de pontos extras para Vida:")))
                        if vida == 0:
                            parar_loop()
                        if vida == "none":
                            continue
                        Health = ((Health + vida) * 5) + 15
                        HpMAX = Health
                    except ValueError:
                        print("Digite apenas numeros, tente novamente.")
                        continue
                condicao_while = True
                while condicao_while:
                    try:
                        defesa = contagem_pontos(int(input("- Digite a quantidade de pontos extras para Defesa:")))
                        if defesa == 0:
                            parar_loop()
                        if defesa == "none":
                            continue
                        Defense = Defense + defesa
                    except ValueError:
                        print("Digite apenas numeros, tente novamente.")
                        continue
                condicao_while = True
                while condicao_while:
                    try:
                        energia = contagem_pontos(int(input("- Digite a quantidade de pontos extras para Energia:")))
                        if energia == 0:
                            parar_loop()
                        if energia == "none":
                            continue
                        Energy = Energy + energia
                    except ValueError:
                        print("Digite apenas numeros, tente novamente.")
                        continue
                condicao_while = True
                while condicao_while:
                    try:
                        destreza = contagem_pontos(int(input("- Digite a quantidade de pontos extras para Destreza:")))
                        if destreza == 0:
                            parar_loop()
                        if destreza == "none":
                            continue
                        Dexterity = Dexterity + destreza
                    except ValueError:
                        print("Digite apenas numeros, tente novamente.")
                        continue
                condicao_while = True
                while condicao_while:
                    try:
                        forca = contagem_pontos(int(input("- Digite a quantidade de pontos extras para Força:")))
                        if forca == 0:
                            parar_loop()
                        if forca == "none":
                            continue
                        Strength = Strength + forca
                    except ValueError:
                        print("Digite apenas numeros, tente novamente.")
                        continue
                condicao_while = True
                while condicao_while:
                    try:
                        inteligencia = contagem_pontos(int(input("- Digite a quantidade de pontos extras para Inteligência:")))
                        if inteligencia == 0:
                            parar_loop()
                        if inteligencia == "none":
                            continue
                        Intelligence = Intelligence + inteligencia
                    except ValueError:
                        print("Digite apenas numeros, tente novamente.")
                        continue
                menu = False
                Acampamento = True
                inside_region = True
            elif escolha_menu == 2:
                print("Saindo...")
                time.sleep(1)
                quit()
            else:
                print("Escolha apenas 1 ou 2, tente novamente")
                time.sleep(1.5)
                continue 


        #Dialogos do jogo, está aqui pois o mome só é salvo aqui em cima
        dialogo_acampamento_lista = {
        "dialogo_1" : ["Você está em seu acampamento, sentado perto da fogueira. A carne já está quase pronta, e o cheiro bom",
                       "preenche o ar. O dia de viagem foi longo, e finalmente tem um pouco de paz."],

        "dialogo_2" : ["De repente, um barulho estranho corta o som da noite. Passos rápidos... cascos?"],

        "dialogo_3" : [f"{Name}: Isso não é lobo. Alguém vem montado..."],

        "dialogo_4" : ["Você se levanta devagar, com a mão no cabo da espada. Fica parado, escutando. O som se aproxima."],

        "dialogo_5" : ["Um cavalo surge entre as árvores. O animal está ofegante, suado. Um homem pula de cima dele, quase",
                       "tropeçando. Ele está usando um manto da cidade Alta."],

        "dialogo_6" : ["Desconhecido: Você! Aventureiro(a)! Graças aos céus... achei você!"],

        "dialogo_7" : [f"{Name}: Quem é você? O que quer aqui?"],

        "dialogo_8" : ["Desconhecido: Sou Darrin, Mensageiro do Lorde Harwin. O lorde soube que você estava",
                        "chegando e me enviou para recruta-lo, estamos com problemas."],

        "dialogo_9" : [f"{Name}: O que o lorde quer de mim ?"],

        "dialogo_10" : [f"Darrin (Mensageiro do Lorde): Ultimamente estamos recebendo pedidos de ajuda de comerciantes por causa",
                       "de bandidos, eles estão atacando as caravanas que estão de viagem até a Cidade Alta. Nossos batedores",
                       "encontraram onde eles firmaram um acampamento."],

        "dialogo_11" : [f"{Name}: E o Lorde Harwin quer que eu vá até esse acampamento e faça o trabalho sujo por ele ?"],

        "dialogo_12" : ["Darrin (Mensageiro do Lorde): Basicamente sim aventureiro(a). Se você conseguir tal feito, o Lorde",
                       "vai te dar uma recompensa a altura."],

        "dialogo_13" : [f"{Name}: Eu aceito o contrato, onde posso achar esse Acampamento dos Bandidos ?"],

        "dialogo_14" : ["Darrin (Mensageiro do Lorde): Nossos batedores encontraram ele ao extremo leste, seguindo pela Floresta",
                         "Negra e ultrapassando o Rio Verde."],
        
        "dialogo_15" : [f"{Name}: Vou resolver isso, avise ao lorde que irei até a Cidade Alta para buscar minha recompensa",
                        "quando eu terminhar o trabalho."],

        "dialogo_16" : ["Darrin (Mensageiro do Lorde): Muito obrigado aventureiro(a), irei avisa-lo. Boa sorte na sua jornada e que",
                        "os ventos da Montanha do Dragão te ajudem."],

        "dialogo_17" : ["O mensageiro sobe em seu cavalo e parte de volta pela floresta."]


    }
    
    def dialogos_acampamento():
        global Name, dialogo_acampamento_lista, dialogo_1

        if dialogo_1:
            for i in dialogo_acampamento_lista:
                marcacao_dialogo()
                exibidor_texto_rpg(dialogo_acampamento_lista[f"{i}"], 0.01)
                marcacao_dialogo()
                input("\n#>")
                clear()
        dialogo_1 = False

    def stats_region():
        global status, Acampamento, Floresta, Floresta_Negra, Rio_Verde, Acampamento_Dos_Bandidos, Planicie, Planicie_Verdejantes, Cidade_Alta, Posto_De_Mineracao
        global Floresta_Funge, Rio_Funge, Lago, Cidade_Baixa, Montanhas, Vilarejo_Das_Montanhas, Depressao, Caverna, Montanha_Do_Dragao, Vale_Da_Perdicao, Ponte, Posto_Comercial

        if biom[Map[y][x]]["text"] == "ACAMPAMENTO":
            status = False
            Acampamento = True
        
        if biom[Map[y][x]]["text"] == "FLORESTA":
            status = False
            Floresta = True
        
        if biom[Map[y][x]]["text"] == "FLORESTA NEGRA":
            status = False
            Floresta_Negra = True
        
        if biom[Map[y][x]]["text"] == "RIO VERDE":
            status = False
            Rio_Verde = True
        
        if biom[Map[y][x]]["text"] == "ACAMPAMENTO DOS BANDIDOS":
            status = False
            Acampamento_Dos_Bandidos = True
        
        if biom[Map[y][x]]["text"] == "PLANÍCIE":
            status = False
            Planicie = True
        
        if biom[Map[y][x]]["text"] == "PLANÍCIES VERDEJANTES":
            status = False
            Planicie_Verdejantes = True
        
        if biom[Map[y][x]]["text"] == "CIDADE ALTA":
            status = False
            Cidade_Alta = True
        
        if biom[Map[y][x]]["text"] == "POSTO DE MINERAÇÃO":
            status = False
            Posto_De_Mineracao = True
        
        if biom[Map[y][x]]["text"] == "FLORESTA FUNGE":
            status = False
            Floresta_Funge = True
        
        if biom[Map[y][x]]["text"] == "RIO FUNGE":
            status = False
            Rio_Funge = True
        
        if biom[Map[y][x]]["text"] == "LAGO":
            status = False
            Lago = True
        
        if biom[Map[y][x]]["text"] == "CIDADE BAIXA":
            status = False
            Cidade_Baixa = True
        
        if biom[Map[y][x]]["text"] == "MONTANHAS":
            status = False
            Montanhas = True
        
        if biom[Map[y][x]]["text"] == "VILAREJO DAS MONTANHAS":
            status = False
            Vilarejo_Das_Montanhas = True
        
        if biom[Map[y][x]]["text"] == "DEPRESSÃO":
            status = False
            Depressao = True
        
        if biom[Map[y][x]]["text"] == "CAVERNA":
            status = False
            Caverna = True
        
        if biom[Map[y][x]]["text"] == "MONTANHA DO DRAGÃO":
            status = False
            Montanha_Do_Dragao = True
        
        if biom[Map[y][x]]["text"] == "VALE DA PERDIÇÃO":
            status = False
            Vale_Da_Perdicao = True
        
        if biom[Map[y][x]]["text"] == "PONTE":
            status = False
            Ponte = True
        
        if biom[Map[y][x]]["text"] == "POSTO COMERCIAL":
            status = False
            Posto_Comercial = True

    def inv_region():
        global inv, Acampamento, Floresta, Floresta_Negra, Rio_Verde, Acampamento_Dos_Bandidos, Planicie, Planicie_Verdejantes, Cidade_Alta, Posto_De_Mineracao
        global Floresta_Funge, Rio_Funge, Lago, Cidade_Baixa, Montanhas, Vilarejo_Das_Montanhas, Depressao, Caverna, Montanha_Do_Dragao, Vale_Da_Perdicao, Ponte, Posto_Comercial

        if biom[Map[y][x]]["text"] == "ACAMPAMENTO":
            inv = False
            Acampamento = True
        
        if biom[Map[y][x]]["text"] == "FLORESTA":
            inv = False
            Floresta = True
        
        if biom[Map[y][x]]["text"] == "FLORESTA NEGRA":
            inv = False
            Floresta_Negra = True
        
        if biom[Map[y][x]]["text"] == "RIO VERDE":
            inv = False
            Rio_Verde = True
        
        if biom[Map[y][x]]["text"] == "ACAMPAMENTO DOS BANDIDOS":
            inv = False
            Acampamento_Dos_Bandidos = True
        
        if biom[Map[y][x]]["text"] == "PLANÍCIE":
            inv = False
            Planicie = True
        
        if biom[Map[y][x]]["text"] == "PLANÍCIES VERDEJANTES":
            inv = False
            Planicie_Verdejantes = True
        
        if biom[Map[y][x]]["text"] == "CIDADE ALTA":
            inv = False
            Cidade_Alta = True
        
        if biom[Map[y][x]]["text"] == "POSTO DE MINERAÇÃO":
            inv = False
            Posto_De_Mineracao = True
        
        if biom[Map[y][x]]["text"] == "FLORESTA FUNGE":
            inv = False
            Floresta_Funge = True
        
        if biom[Map[y][x]]["text"] == "RIO FUNGE":
            inv = False
            Rio_Funge = True
        
        if biom[Map[y][x]]["text"] == "LAGO":
            inv = False
            Lago = True
        
        if biom[Map[y][x]]["text"] == "CIDADE BAIXA":
            inv = False
            Cidade_Baixa = True
        
        if biom[Map[y][x]]["text"] == "MONTANHAS":
            inv = False
            Montanhas = True
        
        if biom[Map[y][x]]["text"] == "VILAREJO DAS MONTANHAS":
            inv = False
            Vilarejo_Das_Montanhas = True
        
        if biom[Map[y][x]]["text"] == "DEPRESSÃO":
            inv = False
            Depressao = True
        
        if biom[Map[y][x]]["text"] == "CAVERNA":
            inv = False
            Caverna = True
        
        if biom[Map[y][x]]["text"] == "MONTANHA DO DRAGÃO":
            inv = False
            Montanha_Do_Dragao = True
        
        if biom[Map[y][x]]["text"] == "VALE DA PERDIÇÃO":
            inv = False
            Vale_Da_Perdicao = True
        
        if biom[Map[y][x]]["text"] == "PONTE":
            inv = False
            Ponte = True
        
        if biom[Map[y][x]]["text"] == "POSTO COMERCIAL":
            inv = False
            Posto_Comercial = True

    def entrar_regioes():
        if biom[Map[y][x]]["text"] == "ACAMPAMENTO":
                print("6 - Entrar no Acampamento")

        if biom[Map[y][x]]["text"] == "FLORESTA":
                print("6 - Entrar na Floresta")

            
        if biom[Map[y][x]]["text"] == "FLORESTA NEGRA":
                print("6 - Entrar na Floresta Negra")

            
        if biom[Map[y][x]]["text"] == "RIO VERDE":
                print("6 - Entrar no Rio Verde")

            
        if biom[Map[y][x]]["text"] == "ACAMPAMENTO DOS BANDIDOS":
                print("6 - Entrar no Acampamento dos Bandidos")

            
        if biom[Map[y][x]]["text"] == "PLANÍCIE":
                print("6 - Entrar na Planície")

            
        if biom[Map[y][x]]["text"] == "PLANÍCIES VERDEJANTES":
                print("6 - Entrar nas Planíes Verdejantes")

            
        if biom[Map[y][x]]["text"] == "CIDADE ALTA":
                print("6 - Entrar na Cidade Alta")

            
        if biom[Map[y][x]]["text"] == "POSTO DE MINERAÇÃO":
                print("6 - Entrar no POsto de Mineração")

            
        if biom[Map[y][x]]["text"] == "FLORESTA FUNGE":
                print("6 - Entrar na Floresta Funge")

            
        if biom[Map[y][x]]["text"] == "RIO FUNGE":
                print("6 - Entrar no Rio Funge")

            
        if biom[Map[y][x]]["text"] == "LAGO":
                print("6 - Entrar no Lago")

            
        if biom[Map[y][x]]["text"] == "CIDADE BAIXA":
                print("6 - Entrar na Cidade Baixa")

            
        if biom[Map[y][x]]["text"] == "MONTANHAS":
                print("6 - Entrar nas Montanhas")

            
        if biom[Map[y][x]]["text"] == "VILAREJO DAS MONTANHAS":
                print("6 - Entrar no Vilarejo das Montanhas")

            
        if biom[Map[y][x]]["text"] == "DEPRESSÃO":
                print("6 - Entrar na Depressão")

            
        if biom[Map[y][x]]["text"] == "CAVERNA":
                print("6 - Entrar na Caverna")

            
        if biom[Map[y][x]]["text"] == "MONTANHA DO DRAGÃO":
                print("6 - Entrar na Montanha do Dragão")

            
        if biom[Map[y][x]]["text"] == "VALE DA PERDIÇÃO":
                print("6 - Entrar no Vale da Perdição")

            
        if biom[Map[y][x]]["text"] == "PONTE":
                print("6 - Entrar na Ponte")

            
        if biom[Map[y][x]]["text"] == "POSTO COMERCIAL":
                print("6 - Entrar no Posto Comercial")

    while play:
        clear()
        if description:
            escolha_exibidor_descricao()
        clear()
        if not menu_game:
            if biom[Map[y][x]]["enemies"]:
                if random.randint(0, 100) <= 30:
                    fight = True
                    batalha()

        linhas()
        print("Localização:", biom[Map[y][x]]["text"])
        linhas()
        print(f"Nome: {Name}")
        print(f"Nivel de personagem: {Level}")
        print("Vida:" + str(Health) + "/" + str(HpMAX))
        print(f"Dinheiro: {Gold}")
        linhas()
        print("Equipamento:")
        for itens in equipamento:
            print(f"- {itens}")
        linhas()
        print("Comandos:")
        print("\n0 - Ver Atributos")
        print("1 - Ver inventário")
        if y > 0:
            print("2 - NORTE") 
        if x < x_len:
            print("3 - LESTE")
        if y < y_len:
            print("4 - SUL")
        if x > 0:
            print("5 - OESTE")
        entrar_regioes()
        linhas()
        dest = input("#>")

        if dest =="0":
            menu_game = True
            play = False
            status = True
            description = False

        if dest =="1":
            menu_game = True
            play = False
            inv = True
            description = False

        if dest == "2":   #Vai para o norte
            if y > 0:
                y -= 1
                menu_game = False
                description = True
            else:
                fronteira()
        elif dest == "3":   #Vai para o Leste
            if x < x_len:
                x += 1
                menu_game = False
                description = True
            else:
                fronteira()
        elif dest == "4":   #Vai para o Sul
            if y < y_len:
                y += 1
                menu_game = False
                description = True
            else:
                fronteira()
        elif dest == "5":   #Vai para o Oeste
            if x > 0:
                x -= 1
                menu_game = False
                description = True
            else:
                fronteira()

        if biom[Map[y][x]]["text"] == "ACAMPAMENTO":
            if dest == "6":
                clear()
                linhas()
                print("O aventureiro(a) entra em seu acampamento")
                linhas()
                input("#>")
                play = False
                Acampamento = True
                inside_region = True
                

            

    while status:
        clear()
        linhas()
        print(f"Atributos de {Name}")
        print(f"Nível de personagem: {Level} - Experiência: {mostrador_xp()}")
        print("\n- Vida:" + str(Health) + "/" + str(HpMAX))
        print("- Defesa:" + str(Defense))
        print("- Energia:" + str(Energy))
        print("- Destreza:" + str(Dexterity))
        print("- Força:" + str(Strength))
        print("- Inteligência:" + str(Intelligence))
        print("\n")
        linhas()
        print("Pontos disponíveis: ", atributos_contagem)
        linhas()
        print('Digite "0" para voltar')
        if atributos_contagem > 0:
            print('Digite "1" para distribuir os pontos')
        linhas()
        dest_status = input("#>")

        if dest_status == "0":
            if inside_region:
                stats_region()

            else:
                status = False
                play = True
        
        if  atributos_contagem > 0:
            if dest_status == "1":
                status = False
                status_points = True
    
    while status_points:
        clear()
        linhas()
        print(f"Você tem {atributos_contagem} pontos para distribuir entre os seus atributos!")
        linhas()
        print('\n - "1" para aumentar 1 ponto em Vida')
        print(' - "2" para aumentar 1 ponto em Defesa')
        print(' - "3" para aumentar 1 ponto em Energia')
        print(' - "4" para aumentar 1 ponto em Destreza')
        print(' - "5" para aumentar 1 ponto em Força')
        print(' - "6" para aumentar 1 ponto em Inteligência')
        print('\n - "0" para voltar')
        linhas()
        choice_points = input("#>")

        if choice_points == "1":
            if atributos_contagem > 0:
                atributos_contagem = atributos_contagem - 1
                Health = Health + 5
                HpMAX = HpMAX + 5
                print("\nPonto adicionado com sucesso!")
                input("#>")
            else:
                print("\nPontos insuficientes!")
                input("#>")
        if choice_points == "2":
            if atributos_contagem > 0:
                atributos_contagem = atributos_contagem - 1
                Defense = Defense + 1
                print("\nPonto adicionado com sucesso!")
                input("#>")
            else:
                print("\nPontos insuficientes!")
                input("#>")
        if choice_points == "3":
            if atributos_contagem > 0:
                atributos_contagem = atributos_contagem - 1
                Energy = Energy + 1
                print("\nPonto adicionado com sucesso!")
                input("#>")
            else:
                print("\nPontos insuficientes!")
                input("#>")
        if choice_points == "4":
            if atributos_contagem > 0:
                atributos_contagem = atributos_contagem - 1
                Dexterity = Dexterity + 1
                print("\nPonto adicionado com sucesso!")
                input("#>")
            else:
                print("\nPontos insuficientes!")
                input("#>")
        if choice_points == "5":
            if atributos_contagem > 0:
                atributos_contagem = atributos_contagem - 1
                Strength = Strength + 1
                print("\nPonto adicionado com sucesso!")
                input("#>")
            else:
                print("\nPontos insuficientes!")
                input("#>")
        if choice_points == "6":
            if atributos_contagem > 0:
                atributos_contagem = atributos_contagem - 1
                Intelligence = Intelligence + 1
                print("\nPonto adicionado com sucesso!")
                input("#>")
            else:
                print("\nPontos insuficientes!")
                input("#>")
        if choice_points == "0":
            status_points = False
            status = True

    while inv:
        clear()
        linhas()
        print(f"INVENTÁRIO DE {Name.upper()}")
        linhas()
        mostrar_inventario()
        linhas()
        print('Digite "0" para voltar')
        if "curativo" in inventario:
            print('Digite "1" para usar o curativo(20HP)')
        linhas()

        dest_inv = input("#>")

        if dest_inv == "0":
            if inside_region:
                inv_region()
            else:
                inv = False
                play = True

        if "curativo" in inventario:
            if dest_inv =="1":
                cura_menu(20)  
                remover_item(inventario, "curativo", 1)
                input("#>")

    while Acampamento:
        clear()
        dialogos_acampamento()
        clear()
        linhas()
        print("Localização:", biom[Map[y][x]]["text"])
        linhas()
        print(f"Nome: {Name}")
        print(f"Nivel de personagem: {Level}")
        print("Vida:" + str(Health) + "/" + str(HpMAX))
        print(f"Dinheiro: {Gold}")
        linhas()
        print("Equipamento:")
        for itens in equipamento:
            print(f"- {itens}")
        linhas()
        print("Comandos:")
        print("\n0 - Ver Atributos")
        print("1 - Ver inventário")
        print("2 - Descansar no acampamento")
        print("3 - Sair do acampamento")
        linhas()
        dest = input("#>")

        if dest =="0":
            menu_game = True
            Acampamento = False
            status = True

        if dest =="1":
            menu_game = True
            Acampamento = False
            inv = True

        if dest =="2":
            descansar_acampamento(25)
        
        if dest =="3":
            clear()
            marcacao_dialogo()
            print("O aventureiro(a) sai de seu acampamento e parte para a estrada")
            marcacao_dialogo()
            input("#>")
            Acampamento = False
            play = True
            inside_region = False



