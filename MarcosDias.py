# Autor: Marcos Vinicius Dias Oliveira
# Componente Curricular: MI Algoritmos
# Concluído em: 11/09/2024
# Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
# trecho de código de outro colega ou de outro autor, tais como provindos de livros e
# apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
# de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
# do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.

# Variáveis vazias referentes a pontuação de cada equipe
pont_equipe_1 = int()
pont_equipe_2 = int()
pont_equipe_3 = int()
pont_equipe_4 = int()
pont_equipe_5 = int()

# Variáveis vazias referentes a tempo de cada equipe
tempo_equipe_1 = int()
tempo_equipe_2 = int()
tempo_equipe_3 = int()
tempo_equipe_4 = int()
tempo_equipe_5 = int()

# Contador de problemas da equipe 1
probs_1 = int()
probs_1_facil = int()
probs_1_medio = int()
probs_1_dificil = int()

# Contador de problemas da equipe 2
probs_2 = int()
probs_2_facil = int()
probs_2_medio = int()
probs_2_dificil = int()

# Contador de problemas da equipe 3
probs_3 = int()
probs_3_facil = int()
probs_3_medio = int()
probs_3_dificil = int()

# Contador de problemas da equipe 4
probs_4 = int()
probs_4_facil = int()
probs_4_medio = int()
probs_4_dificil = int()

# Contador de problemas da equipe 5
probs_5 = int()
probs_5_facil = int()
probs_5_medio = int()
probs_5_dificil = int()

print("!!! CONFIGURAÇÃO DE PONTUAÇÃO !!!")
print("!!! PARA NÚMEROS DECIMAIS UTILIZAR SEPARADOR \".\" !!!")

''' Configuração de pontuação de questões fáceis
Estava sendo utilizado Break, porém como não é permitido, tive que alterar a forma como funciona
Agora o loop fica ativo enquanto a variável "verificador" for falsa, caso o usuário digite um número inteiro
então entra na condicional e o verificador vira True, encerrando o loop
Utiliza uma condicional com a função isdigit para verificar se o que foi digitado é um número inteiro
Utiliza replace, para substituir o ponto do decimal por um espaço em branco, 
assim permitindo que o float seja lido como inteiro pelo isdigit
Caso o usário escreva qualquer coisa diferente de um número inteiro, uma mensagem de erro é apresentada e
o usuário precisa digitar novamente.'''
verificador = False
while verificador == False:
    facil = input("Qual será a pontuação das questões fáceis? ")
    facil_float = facil.replace(".", "", 1)
    if facil_float.isdigit():
        facil = float(facil)
        verificador = True
    else:
        print("ERRO! O que foi inserido não é um número válido, tente novamente.")

''' Configuração de pontuação de questões médias
Loop para verificação de entrada.
O loop roda enquanto verificador for false e utiliza isdigit para verificar se é inteiro.
Utiliza replace, para substituir o ponto do decimal por um espaço em branco, 
assim permitindo que o float seja lido como inteiro pelo isdigit
Há também uma condicional que verifica se o valor digitado é menor que o das fáceis
Caso seja menor é solicitado que digite novamente.'''
verificador = False
while verificador == False:
    medio = input("Qual será a pontuação das questões médias? ")
    medio_float = medio.replace(".", "", 1)
    if medio_float.isdigit():
        medio = float(medio)
        if medio <= facil:
            print("ERRO! Pontuação média menor ou igual que pontuação fácil, tente novamente.")
        else:
            verificador = True
    else:
        print("ERRO! O que foi inserido não é um número válido, tente novamente.")

''' Configuração de pontuação de questões difíceis
Loop para verificação de entrada.
O loop roda enquanto verificador for false e utiliza isdigit para verificar se é inteiro.
Utiliza replace, para substituir o ponto do decimal por um espaço em branco, 
assim permitindo que o float seja lido como inteiro pelo isdigit
Há também uma condicional que verifica se o valor digitado é menor que o das médias
Caso seja menor é solicitado que digite novamente.'''
verificador = False
while verificador == False:
    dificil = input("Qual será a pontuação das questões difíceis? ")
    dificil_float = dificil.replace(".", "", 1)
    if dificil_float.isdigit():
        dificil = float(dificil)
        if dificil <= medio:
            print("ERRO! Pontuação difícil menor ou igual que pontuação média, tente novamente.")
        else:
            verificador = True
    else:
        print("ERRO! O que foi inserido não é um número válido, tente novamente.")

# Solicita o nome das equipes para o usário
print("\n!!! CADASTRO DE EQUIPES !!!")
equipe_1 = input("Qual o nome da equipe 1? ")
equipe_2 = input("Qual o nome da equipe 2? ")
equipe_3 = input("Qual o nome da equipe 3? ")
equipe_4 = input("Qual o nome da equipe 4? ")
equipe_5 = input("Qual o nome da equipe 5? ")

# Explica ao usuário como funciona o cadastro de problemas
print("\n!!! CADASTRO DE PROBLEMAS RESOLVIDOS !!!")
print("Instruções: ")
print("1º O usuário deve informar quantos problemas resolvidos quer cadastrar.")
print("OBS: O número informado será o número TOTAL de problemas resolvidos cadastrados, incluindo TODAS as equipes.")
print("2º Na tela de cadastro de problemas será solicitado:")
print("1. Equipe (deve-se inserir um número de 1 a 5, cada número corresponde a uma equipe).")
print("2. Dificuldade do problema (deve-se inserir um número de 1 a 3, 1 sendo fácil, 2 médio e 3 difícil).")
print("3. Tempo de resolução (primeiro é solicitado horas, depois minutos, depois segundos).")
print("3º Após finalizar o cadastro de todos os problemas, será exibido o relatório final.\n")

''' Solicita ao usuário quantos problemas serão cadastrados
Loop para verificação de entrada.
O loop roda enquanto verificador for false e utiliza isdigit para verificar se é inteiro.'''
verificador = False
while verificador == False:
    num_prob = input("Quantas resoluções de problemas serão cadastradas? ")
    if num_prob.isdigit():
        num_prob = int(num_prob)
        verificador = True
    else:
        print("ERRO! O que foi inserido não é um número inteiro, tente novamente.")

# Loop que roda de 1 até o numéro informado pelo usuário para cadastro dos problemas
for x in range(1, num_prob+1):
    print(f"\n{x}º resolução de problema.")

    '''Solicita ao usuário qual equipe ele quer cadastrar
    Loop para verificação de entrada.
    O loop roda enquanto verificador for false e utiliza isdigit para verificar se é inteiro.
    Caso seja digitado um número diferente de 1 a 5 também solicita que digite de novo.'''
    verificador = False
    while verificador == False:
        equipe = input("Qual a equipe que resolveu o problema? (1 a 5) ")
        if equipe.isdigit():
            equipe = int(equipe)
            if equipe < 1 or equipe > 5:
                print("ERRO! Insira um número de 1 a 5. Tente novamente.")
            else:
                verificador = True
        else:
            print("ERRO! Insira um número de 1 a 5. Tente novamente.")
    
    # Match case que verifica qual foi o número digitado referente a equipe para poder prosseguir no código
    match equipe:
        case 1:
            # Aumenta em 1 o número de problemas resolvidos pela equipe
            probs_1 += 1

            '''Solicita ao usuário qual a dificuldade do problema.
            Loop para verificação de entrada.
            O loop roda enquanto verificador for false e utiliza isdigit para verificar se é inteiro.
            Caso seja digitado um número diferente de 1 a 3 também solicita que digite de novo.'''
            verificador = False
            while verificador == False:
                dif_prob = input("Qual a dificuldade do problema resolvido? (1 a 3) ")
                if dif_prob.isdigit():
                    dif_prob = int(dif_prob)
                    if dif_prob < 1 or dif_prob > 3:
                        print("ERRO! Insira um número de 1 a 3. Tente novamente.")
                    else:
                        verificador = True
                else:
                    print("ERRO! Insira um número de 1 a 3. Tente novamente.")
            
            ''' Match case para a dificuldade do problema
            Se for digitado 1, vai para fácil, então acrescenta a pontuação de problema fácil para a equipe
            e aumenta o contador de problemas faceis resolvidos.
            O mesmo vale para médio (2) e difícil (3)'''
            match dif_prob:
                case 1:
                    pont_equipe_1 += facil
                    probs_1_facil += 1
                case 2:
                    pont_equipe_1 += medio
                    probs_1_medio += 1
                case 3:
                    pont_equipe_1 += dificil
                    probs_1_dificil += 1
            
            # Loop com verificação de número inteiro
            # Solicita as horas, se for mais que 1, converte para segundos e armazena no tempo da equipe
            verificador = False
            while verificador == False:
                horas = input("Quantas horas o problema levou para ser resolvido? ")
                if horas.isdigit():
                    horas = int(horas)
                    if horas >= 1:
                        tempo_equipe_1 += (horas * 3600)
                    verificador = True
                else:
                    print("ERRO! Insira um número inteiro. Tente novamente.")

            # Loop com verificação de número inteiro
            # Solicita os minutos, se for mais que 1, converte para segundos e armazena no tempo da equipe
            verificador = False
            while verificador == False:
                minutos = input("Quantos minutos o problema levou para ser resolvido? ")
                if minutos.isdigit():
                    minutos = int(minutos)
                    if minutos >= 1:
                        tempo_equipe_1 += (minutos * 60)
                    verificador = True
                else:
                    print("ERRO! Insira um número inteiro. Tente novamente.")

            # Loop com verificação de número inteiro
            # Solicita os segundos e armazena no tempo da equipe
            verificador = False
            while verificador == False:
                segundos = input("Quantos segundos o problema levou para ser resolvido? ")
                if segundos.isdigit():
                    segundos = int(segundos)
                    if segundos >= 1:
                        tempo_equipe_1 += segundos
                    verificador = True
                else:
                    print("ERRO! Insira um número inteiro. Tente novamente.")
        case 2:
            # Aumenta em 1 o número de problemas resolvidos pela equipe
            probs_2 += 1

            '''Solicita ao usuário qual a dificuldade do problema.
            Loop para verificação de entrada.
            O loop roda enquanto verificador for false e utiliza isdigit para verificar se é inteiro.
            Caso seja digitado um número diferente de 1 a 3 também solicita que digite de novo.'''
            verificador = False
            while verificador == False:
                dif_prob = input("Qual a dificuldade do problema resolvido? (1 a 3) ")
                if dif_prob.isdigit():
                    dif_prob = int(dif_prob)
                    if dif_prob < 1 or dif_prob > 3:
                        print("ERRO! Insira um número de 1 a 3. Tente novamente.")
                    else:
                        verificador = True
                else:
                    print("ERRO! Insira um número de 1 a 3. Tente novamente.")
            
            ''' Match case para a dificuldade do problema
            Se for digitado 1, vai para fácil, então acrescenta a pontuação de problema fácil para a equipe
            e aumenta o contador de problemas faceis resolvidos.
            O mesmo vale para médio (2) e difícil (3)'''
            match dif_prob:
                case 1:
                    pont_equipe_2 += facil
                    probs_2_facil += 1
                case 2:
                    pont_equipe_2 += medio
                    probs_2_medio += 1
                case 3:
                    pont_equipe_2 += dificil
                    probs_2_dificil += 1
            
            # Loop com verificação de número inteiro
            # Solicita as horas, se for mais que 1, converte para segundos e armazena no tempo da equipe
            verificador = False
            while verificador == False:
                horas = input("Quantas horas o problema levou para ser resolvido?")
                if horas.isdigit():
                    horas = int(horas)
                    if horas >= 1:
                        tempo_equipe_2 += (horas * 3600)
                    verificador = True
                else:
                    print("ERRO! Insira um número inteiro. Tente novamente.")

            # Loop com verificação de número inteiro
            # Solicita os minutos, se for mais que 1, converte para segundos e armazena no tempo da equipe
            verificador = False
            while verificador == False:
                minutos = input("Quantos minutos o problema levou para ser resolvido?")
                if minutos.isdigit():
                    minutos = int(minutos)
                    if minutos >= 1:
                        tempo_equipe_2 += (minutos * 60)
                    verificador = True
                else:
                    print("ERRO! Insira um número inteiro. Tente novamente.")

            # Loop com verificação de número inteiro
            # Solicita os segundos e armazena no tempo da equipe
            verificador = False
            while verificador == False:
                segundos = input("Quantos segundos o problema levou para ser resolvido?")
                if segundos.isdigit():
                    segundos = int(segundos)
                    if segundos >= 1:
                        tempo_equipe_2 += segundos
                    verificador = True
                else:
                    print("ERRO! Insira um número inteiro. Tente novamente.")
        case 3:
            # Aumenta em 1 o número de problemas resolvidos pela equipe
            probs_3 += 1

            '''Solicita ao usuário qual a dificuldade do problema.
            Loop para verificação de entrada.
            O loop roda enquanto verificador for false e utiliza isdigit para verificar se é inteiro.
            Caso seja digitado um número diferente de 1 a 3 também solicita que digite de novo.'''
            verificador = False
            while verificador == False:
                dif_prob = input("Qual a dificuldade do problema resolvido? (1 a 3) ")
                if dif_prob.isdigit():
                    dif_prob = int(dif_prob)
                    if dif_prob < 1 or dif_prob > 3:
                        print("ERRO! Insira um número de 1 a 3. Tente novamente.")
                    else:
                        verificador = True
                else:
                    print("ERRO! Insira um número de 1 a 3. Tente novamente.")
            
            ''' Match case para a dificuldade do problema
            Se for digitado 1, vai para fácil, então acrescenta a pontuação de problema fácil para a equipe
            e aumenta o contador de problemas faceis resolvidos.
            O mesmo vale para médio (2) e difícil (3)'''
            match dif_prob:
                case 1:
                    pont_equipe_3 += facil
                    probs_3_facil += 1
                case 2:
                    pont_equipe_3 += medio
                    probs_3_medio += 1
                case 3:
                    pont_equipe_3 += dificil
                    probs_3_dificil += 1
            
            # Loop com verificação de número inteiro
            # Solicita as horas, se for mais que 1, converte para segundos e armazena no tempo da equipe
            verificador = False
            while verificador == False:
                horas = input("Quantas horas o problema levou para ser resolvido?")
                if horas.isdigit():
                    horas = int(horas)
                    if horas >= 1:
                        tempo_equipe_3 += (horas * 3600)
                    verificador = True
                else:
                    print("ERRO! Insira um número inteiro. Tente novamente.")

            # Loop com verificação de número inteiro
            # Solicita os minutos, se for mais que 1, converte para segundos e armazena no tempo da equipe
            verificador = False
            while verificador == False:
                minutos = input("Quantos minutos o problema levou para ser resolvido?")
                if minutos.isdigit():
                    minutos = int(minutos)
                    if minutos >= 1:
                        tempo_equipe_3 += (minutos * 60)
                    verificador = True
                else:
                    print("ERRO! Insira um número inteiro. Tente novamente.")

            # Loop com verificação de número inteiro
            # Solicita os segundos e armazena no tempo da equipe
            verificador = False
            while verificador == False:
                segundos = input("Quantos segundos o problema levou para ser resolvido?")
                if segundos.isdigit():
                    segundos = int(segundos)
                    if segundos >= 1:
                        tempo_equipe_3 += segundos
                    verificador = True
                else:
                    print("ERRO! Insira um número inteiro. Tente novamente.")
        case 4:
            # Aumenta em 1 o número de problemas resolvidos pela equipe
            probs_4 += 1

            '''Solicita ao usuário qual a dificuldade do problema.
            Loop para verificação de entrada.
            O loop roda enquanto verificador for false e utiliza isdigit para verificar se é inteiro.
            Caso seja digitado um número diferente de 1 a 3 também solicita que digite de novo.'''
            verificador = False
            while verificador == False:
                dif_prob = input("Qual a dificuldade do problema resolvido? (1 a 3) ")
                if dif_prob.isdigit():
                    dif_prob = int(dif_prob)
                    if dif_prob < 1 or dif_prob > 3:
                        print("ERRO! Insira um número de 1 a 3. Tente novamente.")
                    else:
                        verificador = True
                else:
                    print("ERRO! Insira um número de 1 a 3. Tente novamente.")
            
            ''' Match case para a dificuldade do problema
            Se for digitado 1, vai para fácil, então acrescenta a pontuação de problema fácil para a equipe
            e aumenta o contador de problemas faceis resolvidos.
            O mesmo vale para médio (2) e difícil (3)'''
            match dif_prob:
                case 1:
                    pont_equipe_4 += facil
                    probs_4_facil += 1
                case 2:
                    pont_equipe_4 += medio
                    probs_4_medio += 1
                case 3:
                    pont_equipe_4 += dificil
                    probs_4_dificil += 1
            
            # Loop com verificação de número inteiro
            # Solicita as horas, se for mais que 1, converte para segundos e armazena no tempo da equipe
            verificador = False
            while verificador == False:
                horas = input("Quantas horas o problema levou para ser resolvido?")
                if horas.isdigit():
                    horas = int(horas)
                    if horas >= 1:
                        tempo_equipe_4 += (horas * 3600)
                    verificador = True
                else:
                    print("ERRO! Insira um número inteiro. Tente novamente.")

            # Loop com verificação de número inteiro
            # Solicita os minutos, se for mais que 1, converte para segundos e armazena no tempo da equipe
            verificador = False
            while verificador == False:
                minutos = input("Quantos minutos o problema levou para ser resolvido?")
                if minutos.isdigit():
                    minutos = int(minutos)
                    if minutos >= 1:
                        tempo_equipe_4 += (minutos * 60)
                    verificador = True
                else:
                    print("ERRO! Insira um número inteiro. Tente novamente.")

            # Loop com verificação de número inteiro
            # Solicita os segundos e armazena no tempo da equipe
            verificador = False
            while verificador == False:
                segundos = input("Quantos segundos o problema levou para ser resolvido?")
                if segundos.isdigit():
                    segundos = int(segundos)
                    if segundos >= 1:
                        tempo_equipe_4 += segundos
                    verificador = True
                else:
                    print("ERRO! Insira um número inteiro. Tente novamente.")
        case 5:
            # Aumenta em 1 o número de problemas resolvidos pela equipe
            probs_5 += 1

            '''Solicita ao usuário qual a dificuldade do problema.
            Loop para verificação de entrada.
            O loop roda enquanto verificador for false e utiliza isdigit para verificar se é inteiro.
            Caso seja digitado um número diferente de 1 a 3 também solicita que digite de novo.'''
            verificador = False
            while verificador == False:
                dif_prob = input("Qual a dificuldade do problema resolvido? (1 a 3) ")
                if dif_prob.isdigit():
                    dif_prob = int(dif_prob)
                    if dif_prob < 1 or dif_prob > 3:
                        print("ERRO! Insira um número de 1 a 3. Tente novamente.")
                    else:
                        verificador = True
                else:
                    print("ERRO! Insira um número de 1 a 3. Tente novamente.")
            
            ''' Match case para a dificuldade do problema
            Se for digitado 1, vai para fácil, então acrescenta a pontuação de problema fácil para a equipe
            e aumenta o contador de problemas faceis resolvidos.
            O mesmo vale para médio (2) e difícil (3)'''
            match dif_prob:
                case 1:
                    pont_equipe_5 += facil
                    probs_5_facil += 1
                case 2:
                    pont_equipe_5 += medio
                    probs_5_medio += 1
                case 3:
                    pont_equipe_5 += dificil
                    probs_5_dificil += 1
            
            # Loop com verificação de número inteiro
            # Solicita as horas, se for mais que 1, converte para segundos e armazena no tempo da equipe
            verificador = False
            while verificador == False:
                horas = input("Quantas horas o problema levou para ser resolvido?")
                if horas.isdigit():
                    horas = int(horas)
                    if horas >= 1:
                        tempo_equipe_5 += (horas * 3600)
                    verificador = True
                else:
                    print("ERRO! Insira um número inteiro. Tente novamente.")

            # Loop com verificação de número inteiro
            # Solicita os minutos, se for mais que 1, converte para segundos e armazena no tempo da equipe
            verificador = False
            while verificador == False:
                minutos = input("Quantos minutos o problema levou para ser resolvido?")
                if minutos.isdigit():
                    minutos = int(minutos)
                    if minutos >= 1:
                        tempo_equipe_5 += (minutos * 60)
                    verificador = True
                else:
                    print("ERRO! Insira um número inteiro. Tente novamente.")

            # Loop com verificação de número inteiro
            # Solicita os segundos e armazena no tempo da equipe
            verificador = False
            while verificador == False:
                segundos = input("Quantos segundos o problema levou para ser resolvido?")
                if segundos.isdigit():
                    segundos = int(segundos)
                    if segundos >= 1:
                        tempo_equipe_5 += segundos
                    verificador = True
                else:
                    print("ERRO! Insira um número inteiro. Tente novamente.")

print("\n!!! EXIBIÇÃO DE RELATÓRIO !!!\n")

print("1. Ranking das equipes:")
primeiro_lugar, segundo_lugar, terceiro_lugar, quarto_lugar, quinto_lugar = None, None, None, None, None
pos1, pos2, pos3, pos4, pos5 = 0, 0, 0, 0, 0
pont_primeiro, pont_segundo, pont_terceiro, pont_quarto, pont_quinto = 0, 0, 0, 0, 0

''' Para definir a posição das equipes foram criadas uma série de condicionais que verificam:
1 - A pontuação
2 - Caso a pontuação seja igual, os problemas difíceis
3 - Caso os problemas dificieis sejam iguais, o tempo
Cada equipe é comparada individualmente com outra, e caso a equipe x ganhe da y em algum critério
na ordem de prioridade definida acima, ela ganha +1 em sua variável que vai determinar a posição posteriormente
'''
if pont_equipe_1 > pont_equipe_2:
    pos1+=1
elif pont_equipe_1 < pont_equipe_2:
    pos2+=1
elif pont_equipe_1 == pont_equipe_2:
    if probs_1_dificil > probs_2_dificil:
        pos1+=1
    elif probs_1_dificil < probs_2_dificil:
        pos2+=1
    elif probs_1_dificil == probs_2_dificil:
        if tempo_equipe_1 < tempo_equipe_2:
            pos1+=1
        elif tempo_equipe_1 > tempo_equipe_2:
            pos2+=1
        elif tempo_equipe_1 == tempo_equipe_2:
            pos1+=1
            pos2+=1

if pont_equipe_1 > pont_equipe_3:
    pos1 += 1
elif pont_equipe_1 < pont_equipe_3:
    pos3 += 1
elif pont_equipe_1 == pont_equipe_3:
    if probs_1_dificil > probs_3_dificil:
        pos1 += 1
    elif probs_1_dificil < probs_3_dificil:
        pos3 += 1
    elif probs_1_dificil == probs_3_dificil:
        if tempo_equipe_1 < tempo_equipe_3:
            pos1 += 1
        elif tempo_equipe_1 > tempo_equipe_3:
            pos3 += 1
        elif tempo_equipe_1 == tempo_equipe_3:
            pos1 += 1
            pos3 += 1

if pont_equipe_1 > pont_equipe_4:
    pos1 += 1
elif pont_equipe_1 < pont_equipe_4:
    pos4 += 1
elif pont_equipe_1 == pont_equipe_4:
    if probs_1_dificil > probs_4_dificil:
        pos1 += 1
    elif probs_1_dificil < probs_4_dificil:
        pos4 += 1
    elif probs_1_dificil == probs_4_dificil:
        if tempo_equipe_1 < tempo_equipe_4:
            pos1 += 1
        elif tempo_equipe_1 > tempo_equipe_4:
            pos4 += 1
        elif tempo_equipe_1 == tempo_equipe_4:
            pos1 += 1
            pos4 += 1

if pont_equipe_1 > pont_equipe_5:
    pos1 += 1
elif pont_equipe_1 < pont_equipe_5:
    pos5 += 1
elif pont_equipe_1 == pont_equipe_5:
    if probs_1_dificil > probs_5_dificil:
        pos1 += 1
    elif probs_1_dificil < probs_5_dificil:
        pos5 += 1
    elif probs_1_dificil == probs_5_dificil:
        if tempo_equipe_1 < tempo_equipe_5:
            pos1 += 1
        elif tempo_equipe_1 > tempo_equipe_5:
            pos5 += 1
        elif tempo_equipe_1 == tempo_equipe_5:
            pos1 += 1
            pos5 += 1

if pont_equipe_2 > pont_equipe_3:
    pos2 += 1
elif pont_equipe_2 < pont_equipe_3:
    pos3 += 1
elif pont_equipe_2 == pont_equipe_3:
    if probs_2_dificil > probs_3_dificil:
        pos2 += 1
    elif probs_2_dificil < probs_3_dificil:
        pos3 += 1
    elif probs_2_dificil == probs_3_dificil:
        if tempo_equipe_2 < tempo_equipe_3:
            pos2 += 1
        elif tempo_equipe_2 > tempo_equipe_3:
            pos3 += 1
        elif tempo_equipe_2 == tempo_equipe_3:
            pos2 += 1
            pos3 += 1

if pont_equipe_2 > pont_equipe_4:
    pos2 += 1
elif pont_equipe_2 < pont_equipe_4:
    pos4 += 1
elif pont_equipe_2 == pont_equipe_4:
    if probs_2_dificil > probs_4_dificil:
        pos2 += 1
    elif probs_2_dificil < probs_4_dificil:
        pos4 += 1
    elif probs_2_dificil == probs_4_dificil:
        if tempo_equipe_2 < tempo_equipe_4:
            pos2 += 1
        elif tempo_equipe_2 > tempo_equipe_4:
            pos4 += 1
        elif tempo_equipe_2 == tempo_equipe_4:
            pos2 += 1
            pos4 += 1

if pont_equipe_2 > pont_equipe_5:
    pos2 += 1
elif pont_equipe_2 < pont_equipe_5:
    pos5 += 1
elif pont_equipe_2 == pont_equipe_5:
    if probs_2_dificil > probs_5_dificil:
        pos2 += 1
    elif probs_2_dificil < probs_5_dificil:
        pos5 += 1
    elif probs_2_dificil == probs_5_dificil:
        if tempo_equipe_2 < tempo_equipe_5:
            pos2 += 1
        elif tempo_equipe_2 > tempo_equipe_5:
            pos5 += 1
        elif tempo_equipe_2 == tempo_equipe_5:
            pos2 += 1
            pos5 += 1

if pont_equipe_3 > pont_equipe_4:
    pos3 += 1
elif pont_equipe_3 < pont_equipe_4:
    pos4 += 1
elif pont_equipe_3 == pont_equipe_4:
    if probs_3_dificil > probs_4_dificil:
        pos3 += 1
    elif probs_3_dificil < probs_4_dificil:
        pos4 += 1
    elif probs_3_dificil == probs_4_dificil:
        if tempo_equipe_3 < tempo_equipe_4:
            pos3 += 1
        elif tempo_equipe_3 > tempo_equipe_4:
            pos4 += 1
        elif tempo_equipe_3 == tempo_equipe_4:
            pos3 += 1
            pos4 += 1

if pont_equipe_3 > pont_equipe_5:
    pos3 += 1
elif pont_equipe_3 < pont_equipe_5:
    pos5 += 1
elif pont_equipe_3 == pont_equipe_5:
    if probs_3_dificil > probs_5_dificil:
        pos3 += 1
    elif probs_3_dificil < probs_5_dificil:
        pos5 += 1
    elif probs_3_dificil == probs_5_dificil:
        if tempo_equipe_3 < tempo_equipe_5:
            pos3 += 1
        elif tempo_equipe_3 > tempo_equipe_5:
            pos5 += 1
        elif tempo_equipe_3 == tempo_equipe_5:
            pos3 += 1
            pos5 += 1

if pont_equipe_4 > pont_equipe_5:
    pos4 += 1
elif pont_equipe_4 < pont_equipe_5:
    pos5 += 1
elif pont_equipe_4 == pont_equipe_5:
    if probs_4_dificil > probs_5_dificil:
        pos4 += 1
    elif probs_4_dificil < probs_5_dificil:
        pos5 += 1
    elif probs_4_dificil == probs_5_dificil:
        if tempo_equipe_4 < tempo_equipe_5:
            pos4 += 1
        elif tempo_equipe_4 > tempo_equipe_5:
            pos5 += 1
        elif tempo_equipe_4 == tempo_equipe_5:
            pos4 += 1
            pos5 += 1

'''
Essa série de condicionais verifica as variáveis "pos" criadas anteriormente, as comparando para definir
o ranking. Os "pos" são ordenados de forma decrescente, assim as equipes com os maiores "pos" ficam acima no ranking.
Simultaneamente a definição das posições finais no ranking, também é armazenado a pontuação da equipe que ficou
em cada posição em uma variável diferente, referente a pontuação da posição, para poder exibir no ranking.
'''
if pos1 >= pos2 and pos1 >= pos3 and pos1 >= pos4 and pos1 >= pos5:
    primeiro_lugar = 1
    pont_primeiro = pont_equipe_1
    if pos2 >= pos3 and pos2 >= pos4 and pos2 >= pos5:
        segundo_lugar = 2
        pont_segundo = pont_equipe_2
        if pos3 >= pos4 and pos3 >= pos5:
            terceiro_lugar = 3
            pont_terceiro = pont_equipe_3
            if pos4 >= pos5:
                quarto_lugar = 4
                quinto_lugar = 5
                pont_quarto = pont_equipe_4
                pont_quinto = pont_equipe_5
            elif pos5 >= pos4:
                quarto_lugar = 5
                quinto_lugar = 4
                pont_quarto = pont_equipe_5
                pont_quinto = pont_equipe_4
        elif pos4 >= pos3 and pos4 >= pos5:
            terceiro_lugar = 4
            pont_terceiro = pont_equipe_4
            if pos3 >= pos5:
                quarto_lugar = 3
                quinto_lugar = 5
                pont_quarto = pont_equipe_3
                pont_quinto = pont_equipe_5
            elif pos5 >= pos3:
                quarto_lugar = 5
                quinto_lugar = 3
                pont_quarto = pont_equipe_5
                pont_quinto = pont_equipe_3
        elif pos5 >= pos3 and pos5 >= pos4:
            terceiro_lugar = 5
            pont_terceiro = pont_equipe_5
            if pos3 >= pos4:
                quarto_lugar = 3
                quinto_lugar = 4
                pont_quarto = pont_equipe_3
                pont_quinto = pont_equipe_4
            elif pos4 >= pos3:
                quarto_lugar = 4
                quinto_lugar = 3
                pont_quarto = pont_equipe_4
                pont_quinto = pont_equipe_3
    elif pos3 >= pos2 and pos3 >= pos4 and pos3 >= pos5:
        segundo_lugar = 3
        pont_segundo = pont_equipe_3
        if pos2 >= pos4 and pos2 >= pos5:
            terceiro_lugar = 2
            pont_terceiro = pont_equipe_2
            if pos4 >= pos5:
                quarto_lugar = 4
                quinto_lugar = 5
                pont_quarto = pont_equipe_4
                pont_quinto = pont_equipe_5
            elif pos5 >= pos4:
                quarto_lugar = 5
                quinto_lugar = 4
                pont_quarto = pont_equipe_5
                pont_quinto = pont_equipe_4
        elif pos4 >= pos2 and pos4 >= pos5:
            terceiro_lugar = 4
            pont_terceiro = pont_equipe_4
            if pos2 >= pos5:
                quarto_lugar = 2
                quinto_lugar = 5
                pont_quarto = pont_equipe_2
                pont_quinto = pont_equipe_5
            elif pos5 >= pos2:
                quarto_lugar = 5
                quinto_lugar = 2
                pont_quarto = pont_equipe_5
                pont_quinto = pont_equipe_2
        elif pos5 >= pos2 and pos5 >= pos4:
            terceiro_lugar = 5
            pont_terceiro = pont_equipe_5
            if pos2 >= pos4:
                quarto_lugar = 2
                quinto_lugar = 4
                pont_quarto = pont_equipe_2
                pont_quinto = pont_equipe_4
            elif pos4 >= pos2:
                quarto_lugar = 4
                quinto_lugar = 2
                pont_quarto = pont_equipe_4
                pont_quinto = pont_equipe_2
    elif pos4 >= pos2 and pos4 >= pos3 and pos4 >= pos5:
        segundo_lugar = 4
        pont_segundo = pont_equipe_4
        if pos3 >= pos2 and pos3 >= pos5:
            terceiro_lugar = 3
            pont_terceiro = pont_equipe_3
            if pos2 >= pos5:
                quarto_lugar = 2
                quinto_lugar = 5
                pont_quarto = pont_equipe_2
                pont_quinto = pont_equipe_5
            elif pos5 >= pos2:
                quarto_lugar = 5
                quinto_lugar = 2
                pont_quarto = pont_equipe_5
                pont_quinto = pont_equipe_2
        elif pos2 >= pos3 and pos2 >= pos5:
            terceiro_lugar = 2
            pont_terceiro = pont_equipe_2
            if pos3 >= pos5:
                quarto_lugar = 3
                quinto_lugar = 5
                pont_quarto = pont_equipe_3
                pont_quinto = pont_equipe_5
            elif pos5 >= pos3:
                quarto_lugar = 5
                quinto_lugar = 3
                pont_quarto = pont_equipe_5
                pont_quinto = pont_equipe_3
        elif pos5 >= pos3 and pos5 >= pos2:
            terceiro_lugar = 5
            pont_terceiro = pont_equipe_5
            if pos3 >= pos2:
                quarto_lugar = 3
                quinto_lugar = 2
                pont_quarto = pont_equipe_3
                pont_quinto = pont_equipe_2
            elif pos2 >= pos3:
                quarto_lugar = 2
                quinto_lugar = 3
                pont_quarto = pont_equipe_2
                pont_quinto = pont_equipe_3
    elif pos5 >= pos2 and pos5 >= pos4 and pos5 >= pos3:
        segundo_lugar = 5
        pont_segundo = pont_equipe_5
        if pos3 >= pos4 and pos3 >= pos2:
            terceiro_lugar = 3
            pont_terceiro = pont_equipe_3
            if pos4 >= pos2:
                quarto_lugar = 4
                quinto_lugar = 2
                pont_quarto = pont_equipe_4
                pont_quinto = pont_equipe_2
            elif pos2 >= pos4:
                quarto_lugar = 2
                quinto_lugar = 4
                pont_quarto = pont_equipe_2
                pont_quinto = pont_equipe_4
        elif pos4 >= pos3 and pos4 >= pos2:
            terceiro_lugar = 4
            pont_terceiro = pont_equipe_4
            if pos3 >= pos2:
                quarto_lugar = 3
                quinto_lugar = 2
                pont_quarto = pont_equipe_3
                pont_quinto = pont_equipe_2
            elif pos2 >= pos3:
                quarto_lugar = 2
                quinto_lugar = 3
                pont_quarto = pont_equipe_2
                pont_quinto = pont_equipe_3
        elif pos2 >= pos3 and pos2 >= pos4:
            terceiro_lugar = 2
            pont_terceiro = pont_equipe_2
            if pos3 >= pos4:
                quarto_lugar = 3
                quinto_lugar = 4
                pont_quarto = pont_equipe_3
                pont_quinto = pont_equipe_4
            elif pos4 >= pos3:
                quarto_lugar = 4
                quinto_lugar = 3
                pont_quarto = pont_equipe_4
                pont_quinto = pont_equipe_3
elif pos2 >= pos1 and pos2 >= pos3 and pos2 >= pos4 and pos2 >= pos5:
    primeiro_lugar = 2
    pont_primeiro = pont_equipe_2
    if pos1 >= pos3 and pos1 >= pos4 and pos1 >= pos5:
        segundo_lugar = 1
        pont_segundo = pont_equipe_1
        if pos3 >= pos4 and pos3 >= pos5:
            terceiro_lugar = 3
            pont_terceiro = pont_equipe_3
            if pos4 >= pos5:
                quarto_lugar = 4
                quinto_lugar = 5
                pont_quarto = pont_equipe_4
                pont_quinto = pont_equipe_5
            elif pos5 >= pos4:
                quarto_lugar = 5
                quinto_lugar = 4
                pont_quarto = pont_equipe_5
                pont_quinto = pont_equipe_4
        elif pos4 >= pos3 and pos4 >= pos5:
            terceiro_lugar = 4
            pont_terceiro = pont_equipe_4
            if pos3 >= pos5:
                quarto_lugar = 3
                quinto_lugar = 5
                pont_quarto = pont_equipe_3
                pont_quinto = pont_equipe_5
            elif pos5 >= pos3:
                quarto_lugar = 5
                quinto_lugar = 3
                pont_quarto = pont_equipe_5
                pont_quinto = pont_equipe_3
        elif pos5 >= pos3 and pos5 >= pos4:
            terceiro_lugar = 5
            pont_terceiro = pont_equipe_5
            if pos3 >= pos4:
                quarto_lugar = 3
                quinto_lugar = 4
                pont_quarto = pont_equipe_3
                pont_quinto = pont_equipe_4
            elif pos4 >= pos3:
                quarto_lugar = 4
                quinto_lugar = 3
                pont_quarto = pont_equipe_4
                pont_quinto = pont_equipe_3
    elif pos3 >= pos1 and pos3 >= pos4 and pos3 >= pos5:
        segundo_lugar = 3
        pont_segundo = pont_equipe_3
        if pos1 >= pos4 and pos1 >= pos5:
            terceiro_lugar = 1
            pont_terceiro = pont_equipe_1
            if pos4 >= pos5:
                quarto_lugar = 4
                quinto_lugar = 5
                pont_quarto = pont_equipe_4
                pont_quinto = pont_equipe_5
            elif pos5 >= pos4:
                quarto_lugar = 5
                quinto_lugar = 4
                pont_quarto = pont_equipe_5
                pont_quinto = pont_equipe_4
        elif pos4 >= pos1 and pos4 >= pos5:
            terceiro_lugar = 4
            pont_terceiro = pont_equipe_4
            if pos1 >= pos5:
                quarto_lugar = 1
                quinto_lugar = 5
                pont_quarto = pont_equipe_1
                pont_quinto = pont_equipe_5
            elif pos5 >= pos1:
                quarto_lugar = 5
                quinto_lugar = 1
                pont_quarto = pont_equipe_5
                pont_quinto = pont_equipe_1
        elif pos5 >= pos1 and pos5 >= pos4:
            terceiro_lugar = 5
            pont_terceiro = pont_equipe_5
            if pos1 >= pos4:
                quarto_lugar = 1
                quinto_lugar = 4
                pont_quarto = pont_equipe_1
                pont_quinto = pont_equipe_4
            elif pos4 >= pos1:
                quarto_lugar = 4
                quinto_lugar = 1
                pont_quarto = pont_equipe_4
                pont_quinto = pont_equipe_1
    elif pos4 >= pos1 and pos4 >= pos3 and pos4 >= pos5:
        segundo_lugar = 4
        pont_segundo = pont_equipe_4
        if pos3 >= pos1 and pos3 >= pos5:
            terceiro_lugar = 3
            pont_terceiro = pont_equipe_3
            if pos1 >= pos5:
                quarto_lugar = 1
                quinto_lugar = 5
                pont_quarto = pont_equipe_1
                pont_quinto = pont_equipe_5
            elif pos5 >= pos1:
                quarto_lugar = 5
                quinto_lugar = 1
                pont_quarto = pont_equipe_5
                pont_quinto = pont_equipe_1
        elif pos1 >= pos3 and pos1 >= pos5:
            terceiro_lugar = 1
            pont_terceiro = pont_equipe_1
            if pos3 >= pos5:
                quarto_lugar = 3
                quinto_lugar = 5
                pont_quarto = pont_equipe_3
                pont_quinto = pont_equipe_5
            elif pos5 >= pos3:
                quarto_lugar = 5
                quinto_lugar = 3
                pont_quarto = pont_equipe_5
                pont_quinto = pont_equipe_3
        elif pos5 >= pos3 and pos5 >= pos1:
            terceiro_lugar = 5
            pont_terceiro = pont_equipe_5
            if pos3 >= pos1:
                quarto_lugar = 3
                quinto_lugar = 1
                pont_quarto = pont_equipe_3
                pont_quinto = pont_equipe_1
            elif pos1 >= pos3:
                quarto_lugar = 1
                quinto_lugar = 3
                pont_quarto = pont_equipe_1
                pont_quinto = pont_equipe_3
    elif pos5 >= pos1 and pos5 >= pos4 and pos5 >= pos3:
        segundo_lugar = 5
        pont_segundo = pont_equipe_5
        if pos3 >= pos4 and pos3 >= pos1:
            terceiro_lugar = 3
            pont_terceiro = pont_equipe_3
            if pos4 >= pos1:
                quarto_lugar = 4
                quinto_lugar = 1
                pont_quarto = pont_equipe_4
                pont_quinto = pont_equipe_1
            elif pos1 >= pos4:
                quarto_lugar = 1
                quinto_lugar = 4
                pont_quarto = pont_equipe_1
                pont_quinto = pont_equipe_4
        elif pos4 >= pos3 and pos4 >= pos1:
            terceiro_lugar = 4
            pont_terceiro = pont_equipe_4
            if pos3 >= pos1:
                quarto_lugar = 3
                quinto_lugar = 1
                pont_quarto = pont_equipe_3
                pont_quinto = pont_equipe_1
            elif pos1 >= pos3:
                quarto_lugar = 1
                quinto_lugar = 3
                pont_quarto = pont_equipe_1
                pont_quinto = pont_equipe_3
        elif pos1 >= pos3 and pos1 >= pos4:
            terceiro_lugar = 1
            pont_terceiro = pont_equipe_1
            if pos3 >= pos4:
                quarto_lugar = 3
                quinto_lugar = 4
                pont_quarto = pont_equipe_3
                pont_quinto = pont_equipe_4
            elif pos4 >= pos3:
                quarto_lugar = 4
                quinto_lugar = 3
                pont_quarto = pont_equipe_4
                pont_quinto = pont_equipe_3
elif pos3 >= pos2 and pos3 >= pos1 and pos3 >= pos4 and pos3 >= pos5:
    primeiro_lugar = 3
    pont_primeiro = pont_equipe_3
    if pos2 >= pos1 and pos2 >= pos4 and pos2 >= pos5:
        segundo_lugar = 2
        pont_segundo = pont_equipe_2
        if pos1 >= pos4 and pos1 >= pos5:
            terceiro_lugar = 1
            pont_terceiro = pont_equipe_1
            if pos4 >= pos5:
                quarto_lugar = 4
                quinto_lugar = 5
                pont_quarto = pont_equipe_4
                pont_quinto = pont_equipe_5
            elif pos5 >= pos4:
                quarto_lugar = 5
                quinto_lugar = 4
                pont_quarto = pont_equipe_5
                pont_quinto = pont_equipe_4
        elif pos4 >= pos1 and pos4 >= pos5:
            terceiro_lugar = 4
            pont_terceiro = pont_equipe_4
            if pos1 >= pos5:
                quarto_lugar = 1
                quinto_lugar = 5
                pont_quarto = pont_equipe_1
                pont_quinto = pont_equipe_5
            elif pos5 >= pos1:
                quarto_lugar = 5
                quinto_lugar = 1
                pont_quarto = pont_equipe_5
                pont_quinto = pont_equipe_1
        elif pos5 >= pos1 and pos5 >= pos4:
            terceiro_lugar = 5
            pont_terceiro = pont_equipe_5
            if pos1 >= pos4:
                quarto_lugar = 1
                quinto_lugar = 4
                pont_quarto = pont_equipe_1
                pont_quinto = pont_equipe_4
            elif pos4 >= pos1:
                quarto_lugar = 4
                quinto_lugar = 1
                pont_quarto = pont_equipe_4
                pont_quinto = pont_equipe_1
    elif pos1 >= pos2 and pos1 >= pos4 and pos1 >= pos5:
        segundo_lugar = 1
        pont_segundo = pont_equipe_1
        if pos2 >= pos4 and pos2 >= pos5:
            terceiro_lugar = 2
            pont_terceiro = pont_equipe_2
            if pos4 >= pos5:
                quarto_lugar = 4
                quinto_lugar = 5
                pont_quarto = pont_equipe_4
                pont_quinto = pont_equipe_5
            elif pos5 >= pos4:
                quarto_lugar = 5
                quinto_lugar = 4
                pont_quarto = pont_equipe_5
                pont_quinto = pont_equipe_4
        elif pos4 >= pos2 and pos4 >= pos5:
            terceiro_lugar = 4
            pont_terceiro = pont_equipe_4
            if pos2 >= pos5:
                quarto_lugar = 2
                quinto_lugar = 5
                pont_quarto = pont_equipe_2
                pont_quinto = pont_equipe_5
            elif pos5 >= pos2:
                quarto_lugar = 5
                quinto_lugar = 2
                pont_quarto = pont_equipe_5
                pont_quinto = pont_equipe_2
        elif pos5 >= pos2 and pos5 >= pos4:
            terceiro_lugar = 5
            pont_terceiro = pont_equipe_5
            if pos2 >= pos4:
                quarto_lugar = 2
                quinto_lugar = 4
                pont_quarto = pont_equipe_2
                pont_quinto = pont_equipe_4
            elif pos4 >= pos2:
                quarto_lugar = 4
                quinto_lugar = 2
                pont_quarto = pont_equipe_4
                pont_quinto = pont_equipe_2
    elif pos4 >= pos2 and pos4 >= pos1 and pos4 >= pos5:
        segundo_lugar = 4
        pont_segundo = pont_equipe_4
        if pos1 >= pos2 and pos1 >= pos5:
            terceiro_lugar = 1
            pont_terceiro = pont_equipe_1
            if pos2 >= pos5:
                quarto_lugar = 2
                quinto_lugar = 5
                pont_quarto = pont_equipe_2
                pont_quinto = pont_equipe_5
            elif pos5 >= pos2:
                quarto_lugar = 5
                quinto_lugar = 2
                pont_quarto = pont_equipe_5
                pont_quinto = pont_equipe_2
        elif pos2 >= pos1 and pos2 >= pos5:
            terceiro_lugar = 2
            pont_terceiro = pont_equipe_2
            if pos1 >= pos5:
                quarto_lugar = 1
                quinto_lugar = 5
                pont_quarto = pont_equipe_1
                pont_quinto = pont_equipe_5
            elif pos5 >= pos1:
                quarto_lugar = 5
                quinto_lugar = 1
                pont_quarto = pont_equipe_5
                pont_quinto = pont_equipe_1
        elif pos5 >= pos1 and pos5 >= pos2:
            terceiro_lugar = 5
            pont_terceiro = pont_equipe_5
            if pos1 >= pos2:
                quarto_lugar = 1
                quinto_lugar = 2
                pont_quarto = pont_equipe_1
                pont_quinto = pont_equipe_2
            elif pos2 >= pos1:
                quarto_lugar = 2
                quinto_lugar = 1
                pont_quarto = pont_equipe_2
                pont_quinto = pont_equipe_1
    elif pos5 >= pos2 and pos5 >= pos4 and pos5 >= pos1:
        segundo_lugar = 5
        pont_segundo = pont_equipe_5
        if pos1 >= pos4 and pos1 >= pos2:
            terceiro_lugar = 1
            pont_terceiro = pont_equipe_1
            if pos4 >= pos2:
                quarto_lugar = 4
                quinto_lugar = 2
                pont_quarto = pont_equipe_4
                pont_quinto = pont_equipe_2
            elif pos2 >= pos4:
                quarto_lugar = 2
                quinto_lugar = 4
                pont_quarto = pont_equipe_2
                pont_quinto = pont_equipe_4
        elif pos4 >= pos1 and pos4 >= pos2:
            terceiro_lugar = 4
            pont_terceiro = pont_equipe_4
            if pos1 >= pos2:
                quarto_lugar = 1
                quinto_lugar = 2
                pont_quarto = pont_equipe_1
                pont_quinto = pont_equipe_2
            elif pos2 >= pos1:
                quarto_lugar = 2
                quinto_lugar = 1
                pont_quarto = pont_equipe_2
                pont_quinto = pont_equipe_1
        elif pos2 >= pos1 and pos2 >= pos4:
            terceiro_lugar = 2
            pont_terceiro = pont_equipe_2
            if pos1 >= pos4:
                quarto_lugar = 1
                quinto_lugar = 4
                pont_quarto = pont_equipe_1
                pont_quinto = pont_equipe_4
            elif pos4 >= pos1:
                quarto_lugar = 4
                quinto_lugar = 1
                pont_quarto = pont_equipe_4
                pont_quinto = pont_equipe_1
elif pos4 >= pos2 and pos4 >= pos3 and pos4 >= pos1 and pos4 >= pos5:
    primeiro_lugar = 4
    pont_primeiro = pont_equipe_4
    if pos2 >= pos1 and pos2 >= pos3 and pos2 >= pos5:
        segundo_lugar = 2
        pont_segundo = pont_equipe_2
        if pos1 >= pos3 and pos1 >= pos5:
            terceiro_lugar = 1
            pont_terceiro = pont_equipe_1
            if pos3 >= pos5:
                quarto_lugar = 3
                quinto_lugar = 5
                pont_quarto = pont_equipe_3
                pont_quinto = pont_equipe_5
            elif pos5 >= pos3:
                quarto_lugar = 5
                quinto_lugar = 3
                pont_quarto = pont_equipe_5
                pont_quinto = pont_equipe_3
        elif pos3 >= pos1 and pos3 >= pos5:
            terceiro_lugar = 3
            pont_terceiro = pont_equipe_3
            if pos1 >= pos5:
                quarto_lugar = 1
                quinto_lugar = 5
                pont_quarto = pont_equipe_1
                pont_quinto = pont_equipe_5
            elif pos5 >= pos1:
                quarto_lugar = 5
                quinto_lugar = 1
                pont_quarto = pont_equipe_5
                pont_quinto = pont_equipe_1
        elif pos5 >= pos1 and pos5 >= pos3:
            terceiro_lugar = 5
            pont_terceiro = pont_equipe_5
            if pos1 >= pos3:
                quarto_lugar = 1
                quinto_lugar = 3
                pont_quarto = pont_equipe_1
                pont_quinto = pont_equipe_3
            elif pos3 >= pos1:
                quarto_lugar = 3
                quinto_lugar = 1
                pont_quarto = pont_equipe_3
                pont_quinto = pont_equipe_1
    elif pos1 >= pos2 and pos1 >= pos3 and pos1 >= pos5:
        segundo_lugar = 1
        pont_segundo = pont_equipe_1
        if pos2 >= pos3 and pos2 >= pos5:
            terceiro_lugar = 2
            pont_terceiro = pont_equipe_2
            if pos3 >= pos5:
                quarto_lugar = 3
                quinto_lugar = 5
                pont_quarto = pont_equipe_3
                pont_quinto = pont_equipe_5
            elif pos5 >= pos3:
                quarto_lugar = 5
                quinto_lugar = 3
                pont_quarto = pont_equipe_5
                pont_quinto = pont_equipe_3
        elif pos3 >= pos2 and pos3 >= pos5:
            terceiro_lugar = 3
            pont_terceiro = pont_equipe_3
            if pos2 >= pos5:
                quarto_lugar = 2
                quinto_lugar = 5
                pont_quarto = pont_equipe_2
                pont_quinto = pont_equipe_5
            elif pos5 >= pos2:
                quarto_lugar = 5
                quinto_lugar = 2
                pont_quarto = pont_equipe_5
                pont_quinto = pont_equipe_2
        elif pos5 >= pos2 and pos5 >= pos3:
            terceiro_lugar = 5
            pont_terceiro = pont_equipe_5
            if pos2 >= pos3:
                quarto_lugar = 2
                quinto_lugar = 3
                pont_quarto = pont_equipe_2
                pont_quinto = pont_equipe_3
            elif pos3 >= pos2:
                quarto_lugar = 3
                quinto_lugar = 2
                pont_quarto = pont_equipe_3
                pont_quinto = pont_equipe_2
    elif pos3 >= pos2 and pos3 >= pos1 and pos3 >= pos5:
        segundo_lugar = 3
        pont_segundo = pont_equipe_3
        if pos1 >= pos2 and pos1 >= pos5:
            terceiro_lugar = 1
            pont_terceiro = pont_equipe_1
            if pos2 >= pos5:
                quarto_lugar = 2
                quinto_lugar = 5
                pont_quarto = pont_equipe_2
                pont_quinto = pont_equipe_5
            elif pos5 >= pos2:
                quarto_lugar = 5
                quinto_lugar = 2
                pont_quarto = pont_equipe_5
                pont_quinto = pont_equipe_2
        elif pos2 >= pos1 and pos2 >= pos5:
            terceiro_lugar = 2
            pont_terceiro = pont_equipe_2
            if pos1 >= pos5:
                quarto_lugar = 1
                quinto_lugar = 5
                pont_quarto = pont_equipe_1
                pont_quinto = pont_equipe_5
            elif pos5 >= pos1:
                quarto_lugar = 5
                quinto_lugar = 1
                pont_quarto = pont_equipe_5
                pont_quinto = pont_equipe_1
        elif pos5 >= pos1 and pos5 >= pos2:
            terceiro_lugar = 5
            pont_terceiro = pont_equipe_5
            if pos1 >= pos2:
                quarto_lugar = 1
                quinto_lugar = 2
                pont_quarto = pont_equipe_1
                pont_quinto = pont_equipe_2
            elif pos2 >= pos1:
                quarto_lugar = 2
                quinto_lugar = 1
                pont_quarto = pont_equipe_2
                pont_quinto = pont_equipe_1
    elif pos5 >= pos2 and pos5 >= pos3 and pos5 >= pos1:
        segundo_lugar = 5
        pont_segundo = pont_equipe_5
        if pos1 >= pos3 and pos1 >= pos2:
            terceiro_lugar = 1
            pont_terceiro = pont_equipe_1
            if pos3 >= pos2:
                quarto_lugar = 3
                quinto_lugar = 2
                pont_quarto = pont_equipe_3
                pont_quinto = pont_equipe_2
            elif pos2 >= pos3:
                quarto_lugar = 2
                quinto_lugar = 3
                pont_quarto = pont_equipe_2
                pont_quinto = pont_equipe_3
        elif pos3 >= pos1 and pos3 >= pos2:
            terceiro_lugar = 3
            pont_terceiro = pont_equipe_3
            if pos1 >= pos2:
                quarto_lugar = 1
                quinto_lugar = 2
                pont_quarto = pont_equipe_1
                pont_quinto = pont_equipe_2
            elif pos2 >= pos1:
                quarto_lugar = 2
                quinto_lugar = 1
                pont_quarto = pont_equipe_2
                pont_quinto = pont_equipe_1
        elif pos2 >= pos1 and pos2 >= pos3:
            terceiro_lugar = 2
            pont_terceiro = pont_equipe_2
            if pos1 >= pos3:
                quarto_lugar = 1
                quinto_lugar = 3
                pont_quarto = pont_equipe_1
                pont_quinto = pont_equipe_3
            elif pos3 >= pos1:
                quarto_lugar = 3
                quinto_lugar = 1
                pont_quarto = pont_equipe_3
                pont_quinto = pont_equipe_1
elif pos5 >= pos2 and pos5 >= pos3 and pos5 >= pos4 and pos5 >= pos1:
    primeiro_lugar = 5
    pont_primeiro = pont_equipe_5
    if pos2 >= pos1 and pos2 >= pos3 and pos2 >= pos4:
        segundo_lugar = 2
        pont_segundo = pont_equipe_2
        if pos1 >= pos3 and pos1 >= pos4:
            terceiro_lugar = 1
            pont_terceiro = pont_equipe_1
            if pos3 >= pos4:
                quarto_lugar = 3
                quinto_lugar = 4
                pont_quarto = pont_equipe_3
                pont_quinto = pont_equipe_4
            elif pos4 >= pos3:
                quarto_lugar = 4
                quinto_lugar = 3
                pont_quarto = pont_equipe_4
                pont_quinto = pont_equipe_3
        elif pos3 >= pos1 and pos3 >= pos4:
            terceiro_lugar = 3
            pont_terceiro = pont_equipe_3
            if pos1 >= pos4:
                quarto_lugar = 1
                quinto_lugar = 4
                pont_quarto = pont_equipe_1
                pont_quinto = pont_equipe_4
            elif pos4 >= pos1:
                quarto_lugar = 4
                quinto_lugar = 1
                pont_quarto = pont_equipe_4
                pont_quinto = pont_equipe_1
        elif pos4 >= pos1 and pos4 >= pos3:
            terceiro_lugar = 4
            pont_terceiro = pont_equipe_4
            if pos1 >= pos3:
                quarto_lugar = 1
                quinto_lugar = 3
                pont_quarto = pont_equipe_1
                pont_quinto = pont_equipe_3
            elif pos3 >= pos1:
                quarto_lugar = 3
                quinto_lugar = 1
                pont_quarto = pont_equipe_3
                pont_quinto = pont_equipe_1
    elif pos1 >= pos2 and pos1 >= pos3 and pos1 >= pos4:
        segundo_lugar = 1
        pont_segundo = pont_equipe_1
        if pos2 >= pos3 and pos2 >= pos4:
            terceiro_lugar = 2
            pont_terceiro = pont_equipe_2
            if pos3 >= pos4:
                quarto_lugar = 3
                quinto_lugar = 4
                pont_quarto = pont_equipe_3
                pont_quinto = pont_equipe_4
            elif pos4 >= pos3:
                quarto_lugar = 4
                quinto_lugar = 3
                pont_quarto = pont_equipe_4
                pont_quinto = pont_equipe_3
        elif pos3 >= pos2 and pos3 >= pos4:
            terceiro_lugar = 3
            pont_terceiro = pont_equipe_3
            if pos2 >= pos4:
                quarto_lugar = 2
                quinto_lugar = 4
                pont_quarto = pont_equipe_2
                pont_quinto = pont_equipe_4
            elif pos4 >= pos2:
                quarto_lugar = 4
                quinto_lugar = 2
                pont_quarto = pont_equipe_4
                pont_quinto = pont_equipe_2
        elif pos4 >= pos2 and pos4 >= pos3:
            terceiro_lugar = 4
            pont_terceiro = pont_equipe_4
            if pos2 >= pos3:
                quarto_lugar = 2
                quinto_lugar = 3
                pont_quarto = pont_equipe_2
                pont_quinto = pont_equipe_3
            elif pos3 >= pos2:
                quarto_lugar = 3
                quinto_lugar = 2
                pont_quarto = pont_equipe_3
                pont_quinto = pont_equipe_2
    elif pos3 >= pos2 and pos3 >= pos1 and pos3 >= pos4:
        segundo_lugar = 3
        pont_segundo = pont_equipe_3
        if pos1 >= pos2 and pos1 >= pos4:
            terceiro_lugar = 1
            pont_terceiro = pont_equipe_1
            if pos2 >= pos4:
                quarto_lugar = 2
                quinto_lugar = 4
                pont_quarto = pont_equipe_2
                pont_quinto = pont_equipe_4
            elif pos4 >= pos2:
                quarto_lugar = 4
                quinto_lugar = 2
                pont_quarto = pont_equipe_4
                pont_quinto = pont_equipe_2
        elif pos2 >= pos1 and pos2 >= pos4:
            terceiro_lugar = 2
            pont_terceiro = pont_equipe_2
            if pos1 >= pos4:
                quarto_lugar = 1
                quinto_lugar = 4
                pont_quarto = pont_equipe_1
                pont_quinto = pont_equipe_4
            elif pos4 >= pos1:
                quarto_lugar = 4
                quinto_lugar = 1
                pont_quarto = pont_equipe_4
                pont_quinto = pont_equipe_1
        elif pos4 >= pos1 and pos4 >= pos2:
            terceiro_lugar = 4
            pont_terceiro = pont_equipe_4
            if pos1 >= pos2:
                quarto_lugar = 1
                quinto_lugar = 2
                pont_quarto = pont_equipe_1
                pont_quinto = pont_equipe_2
            elif pos2 >= pos1:
                quarto_lugar = 2
                quinto_lugar = 1
                pont_quarto = pont_equipe_2
                pont_quinto = pont_equipe_1
    elif pos4 >= pos2 and pos4 >= pos3 and pos4 >= pos1:
        segundo_lugar = 4
        pont_segundo = pont_equipe_4
        if pos1 >= pos3 and pos1 >= pos2:
            terceiro_lugar = 1
            pont_terceiro = pont_equipe_1
            if pos3 >= pos2:
                quarto_lugar = 3
                quinto_lugar = 2
                pont_quarto = pont_equipe_3
                pont_quinto = pont_equipe_2
            elif pos2 >= pos3:
                quarto_lugar = 2
                quinto_lugar = 3
                pont_quarto = pont_equipe_2
                pont_quinto = pont_equipe_3
        elif pos3 >= pos1 and pos3 >= pos2:
            terceiro_lugar = 3
            pont_terceiro = pont_equipe_3
            if pos1 >= pos2:
                quarto_lugar = 1
                quinto_lugar = 2
                pont_quarto = pont_equipe_1
                pont_quinto = pont_equipe_2
            elif pos2 >= pos1:
                quarto_lugar = 2
                quinto_lugar = 1
                pont_quarto = pont_equipe_2
                pont_quinto = pont_equipe_1
        elif pos2 >= pos1 and pos2 >= pos3:
            terceiro_lugar = 2
            pont_terceiro = pont_equipe_2
            if pos1 >= pos3:
                quarto_lugar = 1
                quinto_lugar = 3
                pont_quarto = pont_equipe_1
                pont_quinto = pont_equipe_3
            elif pos3 >= pos1:
                quarto_lugar = 3
                quinto_lugar = 1
                pont_quarto = pont_equipe_3
                pont_quinto = pont_equipe_1

# Exibição do ranking
print(f"Primeiro lugar: Equipe {primeiro_lugar} com {pont_primeiro} pontos")
print(f"Segundo lugar: Equipe {segundo_lugar} com {pont_segundo} pontos")
print(f"Terceiro lugar: Equipe {terceiro_lugar} com {pont_terceiro} pontos")
print(f"Quarto lugar: Equipe {quarto_lugar} com {pont_quarto} pontos")
print(f"Quinto lugar: Equipe {quinto_lugar} com {pont_quinto} pontos\n")

# Exibição da quantidade de problemas resolvidos, separado por dificuldade para cada equipe
print("2. Quantidade de problemas resolvidos por cada equipe:")
print(f"Equipe 1 ({equipe_1}):")
print(f"Número de problemas resolvidos: {probs_1}")
print(f"Número de problemas fáceis resolvidos: {probs_1_facil}")
print(f"Número de problemas médios resolvidos: {probs_1_medio}")
print(f"Número de problemas difíceis resolvidos: {probs_1_dificil}\n")

print(f"Equipe 2 ({equipe_2}):")
print(f"Número de problemas resolvidos: {probs_2}")
print(f"Número de problemas fáceis resolvidos: {probs_2_facil}")
print(f"Número de problemas médios resolvidos: {probs_2_medio}")
print(f"Número de problemas difíceis resolvidos: {probs_2_dificil}\n")

print(f"Equipe 3 ({equipe_3}):")
print(f"Número de problemas resolvidos: {probs_3}")
print(f"Número de problemas fáceis resolvidos: {probs_3_facil}")
print(f"Número de problemas médios resolvidos: {probs_3_medio}")
print(f"Número de problemas difíceis resolvidos: {probs_3_dificil}\n")

print(f"Equipe 4 ({equipe_4}):")
print(f"Número de problemas resolvidos: {probs_4}")
print(f"Número de problemas fáceis resolvidos: {probs_4_facil}")
print(f"Número de problemas médios resolvidos: {probs_4_medio}")
print(f"Número de problemas difíceis resolvidos: {probs_4_dificil}\n")

print(f"Equipe 5 ({equipe_5}):")
print(f"Número de problemas resolvidos: {probs_5}")
print(f"Número de problemas fáceis resolvidos: {probs_5_facil}")
print(f"Número de problemas médios resolvidos: {probs_5_medio}")
print(f"Número do problemas difíceis resolvidos: {probs_5_dificil}\n")

# Verifica qual equipe ocupa a variável primeiro_lugar e exibe seu nome e pontuação
print("3. Equipe vencedora e sua pontuação total:")
if primeiro_lugar == 1:
    print(f"A equipe vencedora foi a Equipe 1 ({equipe_1}) com {pont_equipe_1} pontos!")
elif primeiro_lugar == 2:
    print(f"A equipe vencedora foi a Equipe 2 ({equipe_2}) com {pont_equipe_2} pontos!")
elif primeiro_lugar == 3:
    print(f"A equipe vencedora foi a Equipe 3 ({equipe_3}) com {pont_equipe_3} pontos!")
elif primeiro_lugar == 4:
    print(f"A equipe vencedora foi a Equipe 4 ({equipe_4}) com {pont_equipe_4} pontos!")
elif primeiro_lugar == 5:
    print(f"A equipe vencedora foi a Equipe 5 ({equipe_5}) com {pont_equipe_5} pontos!")
print()

# Série de condicionais que verifica e compara o número de questões difíceis resolvidas para exibir quem resolveu mais
print("4. Equipe que resolveu o maior número de problemas difíceis:")
if probs_1_dificil >= probs_2_dificil and probs_1_dificil >= probs_3_dificil and probs_1_dificil >= probs_4_dificil and probs_1_dificil >= probs_5_dificil:
    if probs_1_dificil == probs_2_dificil and probs_1_dificil == probs_3_dificil and probs_1_dificil == probs_4_dificil and probs_1_dificil == probs_5_dificil:
        print(f"Todas as equipes resolveram o mesmo número de problemas difíceis.")
    elif probs_1_dificil == probs_2_dificil and probs_1_dificil == probs_3_dificil and probs_1_dificil == probs_4_dificil:
        print("As equipes 1, 2, 3 e 4 foram as que resolveram mais problemas difíceis.")
    elif probs_1_dificil == probs_2_dificil and probs_1_dificil == probs_3_dificil and probs_1_dificil == probs_5_dificil:
        print("As equipes 1, 2, 3 e 5 foram as que resolveram mais problemas difíceis.")
    elif probs_1_dificil == probs_2_dificil and probs_1_dificil == probs_5_dificil and probs_1_dificil == probs_4_dificil:
        print("As equipes 1, 2, 4 e 5 foram as que resolveram mais problemas difíceis.")
    elif probs_1_dificil == probs_5_dificil and probs_1_dificil == probs_3_dificil and probs_1_dificil == probs_4_dificil:
        print("As equipes 1, 3, 4 e 5 foram as que resolveram mais problemas difíceis.")
    elif probs_1_dificil == probs_2_dificil and probs_1_dificil == probs_3_dificil:
        print("As equipes 1, 2 e 3 foram as que resolveram mais problemas difíceis.")
    elif probs_1_dificil == probs_2_dificil and probs_1_dificil == probs_4_dificil:
        print("As equipes 1, 2 e 4 foram as que resolveram mais problemas difíceis.")
    elif probs_1_dificil == probs_2_dificil and probs_1_dificil == probs_5_dificil:
        print("As equipes 1, 2 e 5 foram as que resolveram mais problemas difíceis.")
    elif probs_1_dificil == probs_4_dificil and probs_1_dificil == probs_3_dificil:
        print("As equipes 1, 3 e 4 foram as que resolveram mais problemas difíceis.")
    elif probs_1_dificil == probs_5_dificil and probs_1_dificil == probs_3_dificil:
        print("As equipes 1, 3 e 5 foram as que resolveram mais problemas difíceis.")
    elif probs_1_dificil == probs_4_dificil and probs_1_dificil == probs_5_dificil:
        print("As equipes 1, 4 e 5 foram as que resolveram mais problemas difíceis.")
    elif probs_1_dificil == probs_2_dificil:
        print("As equipes 1 e 2 foram as que resolveram mais problemas difíceis.")
    elif probs_1_dificil == probs_3_dificil:
        print("As equipes 1 e 3 foram as que resolveram mais problemas difíceis.")
    elif probs_1_dificil == probs_4_dificil:
        print("As equipes 1 e 4 foram as que resolveram mais problemas difíceis.")
    elif probs_1_dificil == probs_5_dificil:
        print("As equipes 1 e 5 foram as que resolveram mais problemas difíceis.")
    else:
        print("A equipe 1 foi a que resolveu mais problemas difíceis.")
elif probs_2_dificil >= probs_1_dificil and probs_2_dificil >= probs_3_dificil and probs_2_dificil >= probs_4_dificil and probs_2_dificil >= probs_5_dificil:
    if probs_2_dificil == probs_5_dificil and probs_2_dificil == probs_3_dificil and probs_2_dificil == probs_4_dificil:
        print("As equipes 2, 3, 4 e 5 foram as que resolveram mais problemas difíceis.")
    elif probs_2_dificil == probs_3_dificil and probs_2_dificil == probs_4_dificil:
        print("As equipes 2, 3 e 4 foram as que resolveram mais problemas difíceis.")
    elif probs_2_dificil == probs_3_dificil and probs_2_dificil == probs_5_dificil:
        print("As equipes 2, 3 e 5 foram as que resolveram mais problemas difíceis.")
    elif probs_2_dificil == probs_4_dificil and probs_2_dificil == probs_4_dificil:
        print("As equipes 2, 4 e 5 foram as que resolveram mais problemas difíceis.")
    elif probs_2_dificil == probs_3_dificil:
        print("As equipes 2 e 3 foram as que resolveram mais problemas difíceis.")
    elif probs_2_dificil == probs_4_dificil:
        print("As equipes 2 e 4 foram as que resolveram mais problemas difíceis.")
    elif probs_2_dificil == probs_5_dificil:
        print("As equipes 2 e 5 foram as que resolveram mais problemas difíceis.")
    else:
        print("A equipe 2 foi a que resolveu mais problemas difíceis.")
elif probs_3_dificil >= probs_2_dificil and probs_3_dificil >= probs_1_dificil and probs_3_dificil >= probs_4_dificil and probs_3_dificil >= probs_5_dificil:
    if probs_3_dificil == probs_5_dificil and probs_3_dificil == probs_4_dificil:
        print("As equipes 3, 4 e 5 foram as que resolveram mais problemas difíceis.")
    elif probs_3_dificil == probs_4_dificil:
        print("As equipes 3 e 4 foram as que resolveram mais problemas difíceis.")
    elif probs_3_dificil == probs_5_dificil:
        print("As equipes 3 e 5 foram as que resolveram mais problemas difíceis.")
    else:
        print("A equipe 3 foi a que resolveu mais problemas difíceis.")
elif probs_4_dificil >= probs_2_dificil and probs_4_dificil >= probs_3_dificil and probs_4_dificil >= probs_1_dificil and probs_4_dificil >= probs_5_dificil:
    if probs_4_dificil == probs_5_dificil:
        print("As equipes 4 e 5 foram as que resolveram mais problemas difíceis.")
    else:
        print("A equipe 4 foi a que resolveu mais problemas difíceis.")
elif probs_5_dificil >= probs_2_dificil and probs_5_dificil >= probs_3_dificil and probs_5_dificil >= probs_4_dificil and probs_5_dificil >= probs_1_dificil:
    print("A equipe 5 foi a que resolveu mais problemas difíceis.")
print()

# Calcula a média das equipes dividindo a pontuação pelo número de problemas resolvidos
# Verifica se há 0 problemas, para não bugar com divisão por 0
print("5. Média de pontos por equipe:")
if probs_1 >= 1:
    print("Média equipe 1:", pont_equipe_1 / probs_1)
else:
    print("Equipe 1 não resolveu problemas.")
if probs_2 >= 1:
    print("Média equipe 2:", pont_equipe_2 / probs_2)
else:
    print("Equipe 2 não resolveu problemas.")
if probs_3 >= 1:
    print("Média equipe 3:", pont_equipe_3 / probs_3)
else:
    print("Equipe 3 não resolveu problemas.")
if probs_4 >= 1:
    print("Média equipe 4:", pont_equipe_4 / probs_4)
else:
    print("Equipe 4 não resolveu problemas.")
if probs_5 >= 1:
    print("Média equipe 5:", pont_equipe_5 / probs_5)
else:
    print("Equipe 5 não resolveu problemas.")
print()

# Converte individulamente o tempo de cada equipe para horas, minutos e segundos para melhor exibição.
if tempo_equipe_1 >= 3600:
    horas1 = tempo_equipe_1 // 3600
    minutos1 = tempo_equipe_1 % 3600
    segundos1 = minutos1 % 60
    minutos1 = minutos1 // 60
elif tempo_equipe_1 >= 60:
    horas1 = 0
    minutos1 = tempo_equipe_1 // 60
    segundos1 = tempo_equipe_1 % 60
elif tempo_equipe_1 >= 0:
    horas1 = 0
    minutos1 = 0
    segundos1 = tempo_equipe_1

if tempo_equipe_2 >= 3600:
    horas2 = tempo_equipe_2 // 3600
    minutos2 = tempo_equipe_2 % 3600
    segundos2 = minutos2 % 60
    minutos2 = minutos2 // 60
elif tempo_equipe_2 >= 60:
    horas2 = 0
    minutos2 = tempo_equipe_2 // 60
    segundos2 = tempo_equipe_2 % 60
elif tempo_equipe_2 >= 0:
    horas2 = 0
    minutos2 = 0
    segundos2 = tempo_equipe_2

if tempo_equipe_3 >= 3600:
    horas3 = tempo_equipe_3 // 3600
    minutos3 = tempo_equipe_3 % 3600
    segundos3 = minutos3 % 60
    minutos3 = minutos3 // 60
elif tempo_equipe_3 >= 60:
    horas3 = 0
    minutos3 = tempo_equipe_3 // 60
    segundos3 = tempo_equipe_3 % 60
elif tempo_equipe_3 >= 0:
    horas3 = 0
    minutos3 = 0
    segundos3 = tempo_equipe_3

if tempo_equipe_4 >= 3600:
    horas4 = tempo_equipe_4 // 3600
    minutos4 = tempo_equipe_4 % 3600
    segundos4 = minutos4 % 60
    minutos4 = minutos4 // 60
elif tempo_equipe_4 >= 60:
    horas4 = 0
    minutos4 = tempo_equipe_4 // 60
    segundos4 = tempo_equipe_4 % 60
elif tempo_equipe_4 >= 0:
    horas4 = 0
    minutos4 = 0
    segundos4 = tempo_equipe_4

if tempo_equipe_5 >= 3600:
    horas5 = tempo_equipe_5 // 3600
    minutos5 = tempo_equipe_5 % 3600
    segundos5 = minutos5 % 60
    minutos5 = minutos5 // 60
elif tempo_equipe_5 >= 60:
    horas5 = 0
    minutos5 = tempo_equipe_5 // 60
    segundos5 = tempo_equipe_5 % 60
elif tempo_equipe_5 >= 0:
    horas5 = 0
    minutos5 = 0
    segundos5 = tempo_equipe_5

# Verifica o primeiro lugar e então exibe o tempo gasto por essa equipe
print("6. Tempo total gasto pela equipe vencedora:")
if primeiro_lugar == 1:
    print(f"Equipe 1 - {equipe_1}: {horas1} horas, {minutos1} minutos e {segundos1} segundos")
elif primeiro_lugar == 2:
    print(f"Equipe 2 - {equipe_2}: {horas2} horas, {minutos2} minutos e {segundos2} segundos")
elif primeiro_lugar == 3:
    print(f"Equipe 3 - {equipe_3}: {horas3} horas, {minutos3} minutos e {segundos3} segundos")
elif primeiro_lugar == 4:
    print(f"Equipe 4 - {equipe_4}: {horas4} horas, {minutos4} minutos e {segundos4} segundos")
elif primeiro_lugar == 5:
    print(f"Equipe 5 - {equipe_5}: {horas5} horas, {minutos5} minutos e {segundos5} segundos")