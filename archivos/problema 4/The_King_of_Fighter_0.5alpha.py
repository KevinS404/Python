#PROYECTO: "SISTEMA DE COMBATE ENTRE PERSONAJES (ATB)" 
#RAMO: FUNDAMENTOS DE COMPUTACIÓN Y PROGRAMACIÓN 
#SECCIÓN DE LABORATORIO: 1-G-3
#PROFESOR DE LABORATORIO: LUIS RÍOS SEPÚLVEDA
#PROFESOR DE TEORÍA: ALEJANDRO CISTERNA VILLALOBOS
#Integrantes:
#1.
#NOMBRE: IGNACIO ANDRÉS ARAYA VENEGAS
#RUT: 20.296.492-3
#CARRERA: INGENIERÍA CIVIL EN ELECTRICIDAD 
#2.
#NOMBRE: JHOEL ÁNGEL GENERAL SOTO
#RUT: 20.450.177-7
#CARRERA: INGENIERÍA CIVIL EN INFORMÁTICA
#3.
#NOMBRE: ISIDORA ANAÍS ROJAS ALVARADO
#RUT: 20.581.478-7
#CARRERA: INGENIERÍA DE EJECUCIÓN EN COMPUTACIÓN E INFORMÁTICA

#DESCRIPCIÓN DEL PROGRAMA

#BLOQUE DE IMPORTACIONES 
from random import choice , randint
from time import sleep

#BLOQUE DE DEFINICIÓN DE VARIABLES Y CONSTANTES

#STATS
#Realizamos una lista con las estadísticas de los personajes ya que en el código de el programa las necesitaremos. 
############### hp  spd - atk - def - U.H - %.H.A. - %.H.D. - %.H.C. - D.Min. - D.max - DHmin - DHmax         
statsFighter = [12,  3,    5,   14,   20,    0,         0,       0,       2,       8,     0,       0, 0, 0]
statsWizard =  [6,   2,    2,   12,   10,    20,       40,       0,       1,       4,     4,      12, 0, 0]
statsCleric =  [8,   2,    4,   12,   12,    0,        20,      40,       1,       6,     0,       0, 0, 0]

statsJugador = []

condicion = True

statsOponente = 0

ganador = 0

tipoCrecimiento = -1

rondas = -1

i = 0
#BLOQUE DE DEFINICIÓN DE FUNCIONES

#Esta función define al oponente contra el que luchara el jugador.
#Se utiliza el choice ya que la selección enemiga es aleatoria y esta variable nos permite realizar esa acción.
#También se utiliza el if y elif para la selección de solo un enemigo dependiendo de el número seleccionado por choice.
def establecerOponente(nivelJugador):
   
   #STATS OPONENTES
    #               hp  spd - atk - def - U.H - %.H.A. - %.H.D. - %.H.C. - D.Min. - D.max - DHmin - DHmax 

    statsKobold =  [4,   2,    2,   12,   20,     0,        0,       4,       1,       6,     0,       0, "kobold"]
    statsGoblin =  [6,   4,    1,   12,    0,     0,        0,       0,       1,       4,     0,       0, "goblin"]
    statsOrco =   [12,   2,    5,   14,    0,     0,        0,       0,       1,       8,     0,       0, "orco"]
    
    listaOponentes = [0,1,2]
    numeroOponentes = [1,2,3]
    oponentes = choice(numeroOponentes)
    
    limiteSuperiorNivel = nivelJugador + 3
    limiteInferiorNivel = nivelJugador - 3
    if limiteInferiorNivel<=0:
        limiteInferiorNivel = 1
    nivelEnemigos = limiteSuperiorNivel//oponentes

    statsKoboldCalculadas =  []
    statsGoblinCalculadas =  []
    statsOrcoCalculadas =   []
    
    
    #Se calculan las stats para el nuevo nivel de los enemigos
    
    i=0
    while i<12:
        statsKoboldCalculadas.append(statsKobold[i])
        j = 1
        while j<nivelEnemigos:
            statsKoboldCalculadas[i] = statsKoboldCalculadas[i] + (statsKobold[i]*800000)/1000000
            statsKoboldCalculadas[i] = statsKoboldCalculadas[i]//1
            j = j + 1
        i = i + 1
    i=0
    statsKoboldCalculadas.append(0)
    statsKoboldCalculadas.append(0)
    while i<12:
        statsGoblinCalculadas.append(statsGoblin[i])
        j = 1
        while j<nivelEnemigos:
            statsGoblinCalculadas[i] = statsGoblinCalculadas[i] + (statsGoblin[i]*1000000)/1000000
            statsGoblinCalculadas[i] = statsGoblinCalculadas[i]//1
            j = j + 1
        i = i + 1
    i=0
    statsGoblinCalculadas.append(0)
    statsGoblinCalculadas.append(0)
    while i<12:
        statsOrcoCalculadas.append(statsOrco[i])
        j = 1
        while j<nivelEnemigos:
            statsOrcoCalculadas[i] = statsOrcoCalculadas[i] + (statsOrco[i]*1250000)/1000000
            statsOrcoCalculadas[i] = statsOrcoCalculadas[i]//1
            j = j + 1
        i = i + 1
    
    statsOrcoCalculadas.append(0)
    statsOrcoCalculadas.append(0)
    statsOponentes = []
    
    i = 1
    while i<=oponentes:
        oponente = choice(listaOponentes)
        listaOponentes.remove(oponente)
        if oponente == 0:
            statsOponentes.append(statsKoboldCalculadas)
            print(" ---------------------------")
            print("| Lucharás contra un Kobold |")
            print(" ---------------------------")
            print("")
        elif oponente == 1:
            statsOponentes.append(statsGoblinCalculadas)
            print(" ---------------------------")
            print("| Lucharás contra un Goblin |")
            print(" ---------------------------")
            print("")
        elif oponente == 2:
            statsOponentes.append(statsOrcoCalculadas)
            print(" -------------------------")
            print("| Lucharás contra un Orco |")
            print(" -------------------------")
            print("")
        i = i + 1
    return statsOponentes, oponentes, nivelEnemigos

def establecerBoss(nivelJugador):
    statsBoss1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,"boss"]
    crecimientoBoss1 = "lento"
    statsBossElegido = []
    i = 0
    j = 0
    #ir añadiendo mas bosses, el while es igual para todos(excepto cambiando los nombres de variables)
    eleccion =int(input("ingrese el boss con el que quiera luchar: (1,2,3, etc)"))
    if eleccion==1:
        while i<12:
            statsBossElegido.append(statsBoss1[i])
            j = 1
            while j<nivelJugador:
                statsBossElegido[i] = statsBossElegido[i] + (statsBoss1[i]*1000000)/1000000
                statsBossElegido[i] = statsBossElegido[i]//1
                j = j + 1
            i = i + 1
        return statsBossElegido
    
#Esta función define el daño inflingido por el jugador u oponente en su respectivo turno.
#Utilizamos choice tambien por las probabilidades de las habilidades y criticos dados.
#Creamos una lista para el daño segun las instrucciones.
#El randint se utiliza para la selección de una estadística aleatoria entre las anteriormente dadas.
#Utilizamos print para darle al jugador los datos de avance de su personaje y le quede claro lo que pasó mientras avanza la pelea. 
def ataque(statsJugador,statsOponente):
    
    lista = list(range(0,21))
    valorAleatorio = choice(lista)
    
    if valorAleatorio + statsJugador[4] >= statsOponente[3]:
            
        daño = randint(statsJugador[8],statsJugador[9])
#Aquí colocamos un if nuevamente por que hay un caso especifico en donde si el valor aleatorio es 20 ocurre el "Daño Crítico".            
        if valorAleatorio == 20:
            
            print("CRÍTICO. Duplica el daño.")
            daño = daño * 2
            print("Inflige", daño, "puntos de daño.")
            print("==================================================================")
            print("==================================================================")
            print("")
            statsJugador[12] = statsJugador[12] + 1
            statsOponente[0] = statsOponente[0] - daño
            #return statsJugador,statsOponente

#Luego colocamos un elif, ya que en el caso que el valor aleatorio sea 0 ocurre un "Fallo".                         
        elif valorAleatorio == 0:
          
            daño = randint(1,4)
            print("FALLA, se hace", daño, "puntos de daño a sí mismo.")
            print("==================================================================")
            print("==================================================================")
            print("")
            statsJugador[13] = statsJugador[13] + 1
            statsJugador[0] = statsJugador[0] - daño
            #return statsJugador,statsOponente

#Sigue un else, ya que en el caso de que no ocurra ninguno de los anteriores el personaje atacará normalmente.                         
        else:    
            print("Inflige", daño, "puntos de daño.")
            print("==================================================================")
            print("==================================================================")
            print("")
            statsOponente[0] = statsOponente[0] - daño
            #return statsJugador, statsOponente

#Por último este else en el caso que el ataque no supere la defensa del oponente. 
    else:
        print("No supera la defensa del contrario. Inflige 0 pts de daño.")
        print("==================================================================")
        print("==================================================================")
        print("")
        #return(statsJugador,statsOponente)

#Ésta función define la cantidad de daño causada al oponente u jugador por el hechizo de ataque.
#También se define una lista y choice para la selección de un valor aleatorio.
#Casi al igual que en la definición de ataque ocurren varios casos en el cual utilizamos if, elif y else para cada caso.
def hechizoAtaque(statsJugador,statsOponente):
    
    lista = list(range(0,21))
    valorAleatorio = choice(lista)

#Aquí el valor aleatorio entregado debe superar el "Umbral de Hechizo" del jugador para poder seguir.    
    if valorAleatorio > statsJugador[4]:

#La condición se cumplirá sí la suma entre el valor aleatorio y el "Umbral de Hechizo" es superior o igual a la defensa del oponente.
        if valorAleatorio + statsJugador[4] >= statsOponente[3]:
            
            daño = randint(statsJugador[10],statsJugador[11])
            
            if valorAleatorio == 20:
                print("CRÍTICO. Daño x 1.5.")
                daño = daño * 1.5
                print("Inflige", daño, "puntos de daño.")
                print("==================================================================")
                print("==================================================================")
                print("")
                statsJugador[12] = statsJugador[12] + 1
                statsOponente[0] = statsOponente[0] - daño
                return statsJugador,statsOponente
            
            elif valorAleatorio == 0:
                print("FALLA, tus puntos de vida se reducen a la mitad")
                statsJugador[0] = statsJugador[0]/2
                print("Queda con", statsJugador[0], "puntos de vida.")
                print("==================================================================")
                print("==================================================================")
                print("")
                statsJugador[13] = statsJugador[13] + 1
                return statsJugador,statsOponente
            
            else:    
                print("Inflige", daño, "puntos de daño.")
                print("==================================================================")
                print("==================================================================")
                print("")
                statsOponente[0] = statsOponente[0] - daño
                return statsJugador, statsOponente

#Esta función define la cantidad de defensa que aumenta el hechizo de defensa al jugador u oponente
def hechizoDefensa(statsJugador,statsOponente):
    
    lista = list(range(0,21))
    valorAleatorio = choice(lista)

#Aquí el valor aleatorio entregado debe superar el "Umbral de Hechizo" del jugador para poder seguir.       
    if valorAleatorio > statsJugador[4]:
          
        if valorAleatorio == 20:
            print("CRÍTICO. Aumenta 2 puntos de defensa.")
            print("==================================================================")
            print("==================================================================")
            print("")
            statsJugador[12] = statsJugador[12] + 1
            statsJugador[3] = statsJugador[3] + 2
            return statsJugador, statsOponente
            
        elif valorAleatorio == 0:
            print("FALLA. Aumenta 1 punto de defensa al oponente.")
            print("==================================================================")
            print("==================================================================")
            print("")
            statsJugador[13] = statsJugador[13] + 1
            statsOponente[3] = statsOponente[3] + 1
            return statsJugador,statsOponente
            
        else:
            print("Aumenta 1 punto de defensa")
            print("==================================================================")
            print("==================================================================")
            print("")
            statsJugador[3] = statsJugador[3] + 1

#Esta función determina si el jugador u oponente realiza un hechizo de curación y el valor de la misma
def hechizoCuración(statsJugador,statsOponente,vidaOriginalJugador,vidaOriginalOponente):

    lista = list(range(0,21))
    valorAleatorio = choice(lista)

   
#Aquí el valor aleatorio entregado debe superar el "Umbral de Hechizo" del jugador para poder seguir.
    if valorAleatorio > statsJugador[4]:
            
        if valorAleatorio == 20:
            print("CRÍTICO. 4 puntos de curación extra.")
            print("==================================================================")
            print("==================================================================")
            print("")
            statsJugador[12] = statsJugador[12] + 1
            valor = randint(1,9)
            valor = valor + 4
            if statsJugador[0] + valor > vidaOriginalJugador:
                statsJugador[0] = vidaOriginalJugador
            else:
                statsJugador[0] = statsJugador[0] + valor
            return statsJugador, statsOponente
            
        elif valorAleatorio == 0:
            print("FALLA, cura 4 puntos de vida al contrario.")
            print("==================================================================")
            print("==================================================================")
            print("")
            statsJugador[13] = statsJugador[13] + 1
            if statsOponente[0] + 4 > vidaOriginalOponente:
                statsOponente[0] = vidaOriginalOponente
            else:
                statsOponente[0] = statsOponente + 4
            return statsJugador, statsOponente   
        
        else:
            valor = randint(1,9)
            print("Se cura", valor, "puntos de vida.")
            print("==================================================================")
            print("==================================================================")
            print("")
            if valor + statsJugador[0] > vidaOriginalJugador:
                statsJugador[0] = vidaOriginalJugador
            else:
                statsJugador[0] = statsJugador[0] + valor
            return statsJugador, statsOponente

#Esta función determina que es lo que hace el jugador o el oponente en su respectivo turno
def turno(statsJugador,statsOponente, vidaOriginalJugador, vidaOriginalOponente):
    
    lista = list(range(0,101))
    accion = choice(lista)
    
    if accion < statsJugador[5]:
        print("Lanza un hechizo de ataque.")
        #statsJugador = 
        hechizoAtaque(statsJugador, statsOponente)
        return statsJugador, statsOponente    
    
    elif accion >= statsJugador[5] and accion < statsJugador[6]:
        print("Lanza un hechizo de defensa.")
        #statsJugador = 
        hechizoDefensa(statsJugador, statsOponente)
        return statsJugador, statsOponente
    
    elif accion>=statsJugador[6] and accion <statsJugador[7]:
        print("Lanza un hechizo de curación.")
        #statsJugador = 
        hechizoCuración(statsJugador, statsOponente, vidaOriginalJugador, vidaOriginalOponente)
        return statsJugador, statsOponente
    
    else:
        print("Ataca.")
        #statsJugador = 
        ataque(statsJugador,statsOponente)
        return statsJugador, statsOponente

def determinarTurnos(statsJugador,statsOponente, numeroOponentes):
#Definimos el gauge del jugador y del oponente.
#Definimos la vida del jugador y del oponente igualando a la lista de estadísticas de cada uno.
    #ESTA FUNCION ES LA CUAL EL JUEGO QUEDA EN CICLO HASTA QUE LA VIDA DE EL JUGADOR O EL OPONENTE CAE A 0 (O NEGATIVA)
    #caso solo 1 oponente
    if numeroOponentes == 1:
        gaugeJugador = 0
        gaugeOponente = 0
        vidaOriginalJugador = statsJugador[0]
        vidaOriginalOponente = statsOponente[0][0]

        #La condición que se presenta es que la vida de uno de los combatientes debe llegue a cero antes de terminar el ciclo.

        while (statsJugador[0] > 0) and (statsOponente[0][0] > 0):

            print(" --------------------")
            print(" Tu salud:", statsJugador[0])
        
            #Aquí sumamos el gauge a la velocidad de ataque del correspondiente al personaje.
            #Cuando uno de los dos, ya sea el jugador o el oponente llegue a 10 atacará.
            #Agregamos una barra de progreso para que el jugador sepa como avanza su gauge y el del oponente.
        
            gaugeJugador = gaugeJugador + statsJugador[1]
            print(" progreso jug:",gaugeJugador)
            print(" --------------------")
            print("")

        
            print(" --------------------")
            print(" Salud oponente:", statsOponente[0][0])
            gaugeOponente = gaugeOponente + statsOponente[0][1]
            print(" progreso op:",gaugeOponente)
            print(" -------------------")
            print("")
            print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")
            #print("hp: ",statsJugador[0])

            #Utilizamos éste if para cuando el gauge del jugador llegue a 10 o más(dependiendo de las estadísticas del personaje) proceda a la "Acción".                 
            if gaugeJugador>10:
                print("==================================================================")
                print("Tu turno")
                #statsJugador, statsOponente = 
                turno(statsJugador,statsOponente[0], vidaOriginalJugador, vidaOriginalOponente)
                gaugeJugador = 0
        
            if statsOponente[0][0]<=0:
                return 0

            #Utilizamos éste if para cuando el gauge del oponente llegue a 10 o más(dependiendo de las estadísticas del personaje) proceda a la "Acción".                  
            if gaugeOponente>10:
                print("==================================================================")
                print("Turno del oponente")
                #statsOponente, statsJugador = 
                turno(statsOponente[0],statsJugador,vidaOriginalOponente,vidaOriginalJugador)
                gaugeOponente = 0
            
            if statsJugador[0] <= 0:
                return 1
        
            sleep(3)
    #caso 2 oponentes
    elif numeroOponentes == 2:
        gaugeJugador = 0
        gaugeOponente1 = 0
        gaugeOponente2 = 0
        vidaOriginalJugador = statsJugador[0]
        vidaOriginalOponente1 = statsOponente[0][0]
        vidaOriginalOponente2 = statsOponente[1][0]

        while (statsJugador[0] > 0) and ((statsOponente[0][0] > 0) or (statsOponente[1][0]>0)):

            print(" --------------------")
            print(" Tu salud:", statsJugador[0])
        
        
            gaugeJugador = gaugeJugador + statsJugador[1]
            print(" progreso jugador:",gaugeJugador)
            print(" --------------------")
            print("")

        
            print(" --------------------")
            print(" Salud oponente 1:", statsOponente[0][0])
            gaugeOponente1 = gaugeOponente1 + statsOponente[0][1]
            print(" progreso oponente 1:",gaugeOponente1)
            print(" -------------------")
            print("")
            
            print(" --------------------")
            print(" Salud oponente 2:", statsOponente[1][0])
            gaugeOponente2 = gaugeOponente2 + statsOponente[1][1]
            print(" progreso oponente 2:",gaugeOponente2)
            print(" -------------------")
            print("")
            
            print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")
            #print("hp: ",statsJugador[0])

        #Utilizamos éste if para cuando el gauge del jugador llegue a 10 o más(dependiendo de las estadísticas del personaje) proceda a la "Acción".                 
            if gaugeJugador>10:
                print("==================================================================")
                print("Tu turno")
                enemigos = [0,1]
                cualAtacar = choice(enemigos)
                if cualAtacar == 0:
                    turno(statsJugador,statsOponente[cualAtacar], vidaOriginalJugador, vidaOriginalOponente1)
                elif cualAtacar==1:
                    turno(statsJugador,statsOponente[cualAtacar], vidaOriginalJugador, vidaOriginalOponente2)
                gaugeJugador = 0
            
            if statsOponente[0][0] == 0 and statsOponente[1][0]==0:
                return 0
          #Utilizamos estos if para cuando el gauge de los oponentes lleguen a 10 o más(dependiendo de las estadísticas del personaje) proceda a la "Acción".                  
           
           #TURNO OPONENTE 1
            if gaugeOponente1>10 and statsOponente[0][0]>0:
                print("==================================================================")
                print("Turno del oponente 1")
                #statsOponente, statsJugador = 
                turno(statsOponente[0], statsJugador, vidaOriginalOponente1, vidaOriginalJugador)
                gaugeOponente1 = 0
            
            if statsJugador[0] <= 0:
                return 1
            
            #TURNO OPONENTE 2
            if gaugeOponente2>10 and statsOponente[1][0]>0:
                print("==================================================================")
                print("Turno del oponente 2")
                turno(statsOponente[1], statsJugador, vidaOriginalOponente2, vidaOriginalJugador)
                gaugeOponente2 = 0
                
            if statsJugador[0] <= 0:
                return 1
        
            sleep(3)  
    #caso 3 oponentes
    elif numeroOponentes == 3:
        gaugeJugador = 0
        gaugeOponente1 = 0
        gaugeOponente2 = 0
        gaugeOponente3 = 0
        vidaOriginalJugador = statsJugador[0]
        vidaOriginalOponente1 = statsOponente[0][0]
        vidaOriginalOponente2 = statsOponente[1][0]
        vidaOriginalOponente3 = statsOponente[2][0]



        while (statsJugador[0] > 0) and ((statsOponente[0][0] > 0) or (statsOponente[1][0]>0) or (statsOponente[2][0]>0)):

            print(" --------------------")
            print(" Tu salud:", statsJugador[0])
        
        
            gaugeJugador = gaugeJugador + statsJugador[1]
            print(" progreso jugador:",gaugeJugador)
            print(" --------------------")
            print("")

        
            print(" --------------------")
            print(" Salud oponente 1:", statsOponente[0][0])
            gaugeOponente1 = gaugeOponente1 + statsOponente[0][1]
            print(" progreso oponente 1:",gaugeOponente1)
            print(" -------------------")
            print("")
            
            print(" --------------------")
            print(" Salud oponente 2:", statsOponente[1][0])
            gaugeOponente2 = gaugeOponente2 + statsOponente[1][1]
            print(" progreso oponente 2:",gaugeOponente2)
            print(" -------------------")
            print("")
            
            print(" --------------------")
            print(" Salud oponente 3:", statsOponente[2][0])
            gaugeOponente3 = gaugeOponente3 + statsOponente[2][1]
            print(" progreso oponente 3:",gaugeOponente3)
            print(" -------------------")
            print("")
            
            print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")

        #Utilizamos éste if para cuando el gauge del jugador llegue a 10 o más(dependiendo de las estadísticas del personaje) proceda a la "Acción".                 
            if gaugeJugador>10:
                print("==================================================================")
                print("Tu turno")
                enemigos = [0,1,2]
                cualAtacar = choice(enemigos)
                if cualAtacar == 0:
                    turno(statsJugador,statsOponente[cualAtacar], vidaOriginalJugador, vidaOriginalOponente1)
                elif cualAtacar==1:
                    turno(statsJugador,statsOponente[cualAtacar], vidaOriginalJugador, vidaOriginalOponente2)
                elif cualAtacar==2:
                    turno(statsJugador,statsOponente[cualAtacar], vidaOriginalJugador, vidaOriginalOponente3)
                gaugeJugador = 0
        
            if statsOponente[0][0] == 0 and statsOponente[1][0]==0 and statsOponente[2][0]==0:
                return 0
          #Utilizamos estos if para cuando el gauge de los oponentes lleguen a 10 o más(dependiendo de las estadísticas del personaje) proceda a la "Acción".                  
           
           #TURNO OPONENTE 1
            if gaugeOponente1>10 and statsOponente[0][0]>0:
                print("==================================================================")
                print("Turno del oponente 1")
                #statsOponente, statsJugador = 
                turno(statsOponente[0], statsJugador, vidaOriginalOponente1, vidaOriginalJugador)
                gaugeOponente1 = 0
            
            if statsJugador[0] <= 0:
                return 1
            
            #TURNO OPONENTE 2
            if gaugeOponente2>10 and statsOponente[1][0]>0:
                print("==================================================================")
                print("Turno del oponente 2")
                turno(statsOponente[1], statsJugador, vidaOriginalOponente2, vidaOriginalJugador)
                gaugeOponente2 = 0
                
            if statsJugador[0] <= 0:
                return 1
            
            if gaugeOponente3>10 and statsOponente[2][0]>0:
                print("==================================================================")
                print("Turno del oponente 3")
                turno(statsOponente[2], statsJugador, vidaOriginalOponente3, vidaOriginalJugador)
                gaugeOponente3 = 0
                
            if statsJugador[0] <= 0:
                return 1
            
            sleep(3)

def determinarTurnosBoss(statsJugador, statsOponente):
    gaugeJugador = 0
    gaugeOponente = 0
    vidaOriginalJugador = statsJugador[0]
    vidaOriginalOponente = statsOponente[0]

        #La condición que se presenta es que la vida de uno de los combatientes debe llegue a cero antes de terminar el ciclo.

    while (statsJugador[0] > 0) and (statsOponente[0] > 0):

        print(" --------------------")
        print(" Tu salud:", statsJugador[0])
      
        #Aquí sumamos el gauge a la velocidad de ataque del correspondiente al personaje.
        #Cuando uno de los dos, ya sea el jugador o el oponente llegue a 10 atacará.
        #Agregamos una barra de progreso para que el jugador sepa como avanza su gauge y el del oponente.
        
        gaugeJugador = gaugeJugador + statsJugador[1]
        print(" progreso jug:",gaugeJugador)
        print(" --------------------")
        print("")

        
        print(" --------------------")
        print(" Salud oponente:", statsOponente[0])
        gaugeOponente = gaugeOponente + statsOponente[1]
        print(" progreso op:",gaugeOponente)
        print(" -------------------")
        print("")
        print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")
        #print("hp: ",statsJugador[0])

        #Utilizamos éste if para cuando el gauge del jugador llegue a 10 o más(dependiendo de las estadísticas del personaje) proceda a la "Acción".                 
        if gaugeJugador>10:
            print("==================================================================")
            print("Tu turno")
            #statsJugador, statsOponente = 
            turno(statsJugador,statsOponente, vidaOriginalJugador, vidaOriginalOponente)
            gaugeJugador = 0
        
        if statsOponente[0]<=0:
            return 0

            #Utilizamos éste if para cuando el gauge del oponente llegue a 10 o más(dependiendo de las estadísticas del personaje) proceda a la "Acción".                  
        if gaugeOponente>10:
            print("==================================================================")
            print("Turno del oponente")
            #statsOponente, statsJugador = 
            turno(statsOponente,statsJugador,vidaOriginalOponente,vidaOriginalJugador)
            gaugeOponente = 0
            
        if statsJugador[0] <= 0:
            return 1
        
        sleep(3)
def crecimiento(personaje, statsJugador, nivelJugador, expJugador, statsOponentes, nivelOponentes, numeroOponentes, tipoCrecimiento, vidaOriginal):
    
    statsFighter = [12,  3,    5,   14,   20,    0,         0,       0,       2,       8,     0,       0]
    statsWizard =  [6,   2,    2,   12,   10,    20,       40,       0,       1,       4,     4,      12]
    statsCleric =  [8,   2,    4,   12,   12,    0,        20,      40,       1,       6,     0,       0]
    
    sumExpOp = 0
    nivOP = numeroOponentes*nivelOponentes
    factorCrit = statsJugador[12]-statsJugador[13]
    factorDaño = vidaOriginal - statsJugador[0]
    
    if factorCrit>0:
        factorCrit = 1.5
    elif factorCrit==0:
        factorCrit = 1
    elif factorCrit<0:
        factorCrit = 0.75
        
    i=0
    while i<numeroOponentes:
        if statsOponentes[i][12] == "kobold":
            sumExpOp = sumExpOp + (4*(nivelOponentes**3))/5
            i = i + 1
        elif statsOponentes[i][12] == "goblin":
            sumExpOp = sumExpOp + nivelOponentes**3
            i = i + 1
        elif statsOponentes[i][12] == "orco":
            sumExpOp = sumExpOp(5*(nivelOponentes**3))/4  
            i = i + 1
    
    experienciaGanada = (sumExpOp*(nivOP/nivelJugador)*factorCrit*(1+factorDaño))/7
    experienciaTotal = expJugador + experienciaGanada
    
    
    
    
    if tipoCrecimiento=="lento":
     
        nuevoNivel = ((4/5)*experienciaTotal)**(1/3)
        nuevoNivel = nuevoNivel//1
        difNivel = nuevoNivel-nivelJugador
        if difNivel>0:
            i = 0
            if personajeJugador == 0:
                while i<12:
                    statsJugador[i] = (statsFighter[i]*1250000)/1000000
                    statsJugador[i] = statsJugador[i]//1
                    i = i + 1
             
            elif personajeJugador == 2:
                while i <12:
                    statsJugador[i] = (statsFighter[i]*1250000)/1000000
                    statsJugador[i] = statsJugador[i]//1
                    i = i + 1
                
        else:
            statsJugador[0] = vidaOriginal
            statsJugador[12] = 0
            statsJugador[13] = 0
        
        
    elif tipoCrecimiento=="ultralento":
        nuevoNivel = ((4/7)*experienciaTotal)**(1/3)
        nuevoNivel = nuevoNivel//1
        difNivel = nuevoNivel-nivelJugador
        if difNivel>0:
            i = 0
            if personajeJugador == 1:
                while i<12:
                    statsJugador[i] = (statsFighter[i]*1750000)/1000000
                    statsJugador[i] = statsJugador[i]//1
                statsJugador[12] = 0
                statsJugador[13] = 0
        else:
            statsJugador[0] = vidaOriginal
            statsJugador[12] = 0
            statsJugador[13] = 0
    return

#BLOQUE PRINCIPAL

#Esta parte esta escrita e impresa de esta forma, para que el jugador vea de manera visual, las estadísticas de los arquetipos de personaje a elegir 
print("==================================================================")
print("Bienvenido a THE KING OF FIGHTER 0.5 (ALPHA)")
print("Escoja el personaje a utilizar \n")

print("|---------------------------------------------------------------|")
print("|       CARACTERÍSTICA          | FIGTHER |  WIZARD  |   CLERIC  |")
print("|-------------------------------|---------|----------|--- -------|")
print("| Puntos de Vida                |    12   |     6    |     8     |") 
print("| Velocidad                     |     3   |     2    |     2     |") 
print("| Ataque                        |     5   |     2    |     4     |") 
print("| Defensa                       |    14   |    12    |    12     |") 
print("| Umbral de hechizo             |    20   |    10    |    12     |")  
print("| Prob. de hechizo de ataque    |     0   |    20    |     0     |")
print("| Prob. de hechizo de defensa   |     0   |    40    |    20     |")
print("| Prob. de hechizo de curación  |     0   |     0    |    40     |")
print("| Daño mínimo                   |     2   |     1    |     1     |")
print("| Daño máximo                   |     8   |     4    |     6     |")
print("| Daño de hechizo mínimo        |     0   |     4    |     0     |")
print("| Daño de hechizo máximo        |     0   |    12    |     0     |")
print("| Crecimiento                   |  Lento  |Ultralento|   Lento   |")
print("|----------------------------------------------------------------|")
print("                                                                 ")

#esta es al funcion que te entrega los datos de el jugador que seleccionaras, se repite hasta que se ingrese uno de los 3 valores indicados.
#utilizamos un while para que al seleccionar un jugador le muestre la lista de estadisticas
#y los if y elif definiendo el case de que eligiera un personaje u otro

while condicion:
    
    #ENTRADA DE DATOS
    personajeJugador = input("Ingrese 0 para Fighter, 1 para Wizard, 2 para Cleric: ")
    print(" ")
    print("==================================================================")
    if (personajeJugador) == "0":
        i = 0
        while i<14:
            statsJugador.append(statsFighter[i])
            i = i + 1
        print(" ----------------------")    
        print("| Jugarás como FIGHTER |")
        print(" ----------------------")
        print(" ")
        condicion = False
        tipoCrecimiento = "lento"
        
    elif (personajeJugador) == "1":
        i = 0
        while i<14:
            statsJugador.append(statsWizard[i])
            i = i + 1
        print(" ---------------------")    
        print("| Jugarás como WIZARD |")
        print(" ---------------------")
        print(" ")
        condicion = False
        tipoCrecimiento = "ultralento"
        
    elif (personajeJugador) == "2":
        i = 0
        while i<14:
            statsJugador.append(statsCleric[i])
            i = i + 1
        print(" ---------------------")
        print("| Jugarás como CLERIC |")
        print(" ---------------------")
        print(" ")
        condicion = False
        tipoCrecimiento = "lento"
        
    else:
        print("Personaje Inválido")


condicion = True

while condicion:
    rondas = int(input("Ingrese el numero de rondas a jugar: "))
    if (rondas)>=1:
        condicion = False
    else:
        print("Numero de rondas invalido")
####################
nivelJugador = 1   ##CAMBIAR ESTO
expJugador = 0
rondasPasadas = 10
###################
i = 1
while i<=rondas:
    #En esta parte se define al oponente y al ganador mediante las funciones colocadas en cada variable
    vidaOriginal = statsJugador[0]
    
    if rondasPasadas%10!=0:
        statsOponente, oponentes, nivelEnemigos = establecerOponente(nivelJugador)
        print("Te enfrentaras a", oponentes, "oponentes de niveles", nivelEnemigos)
        ganador = determinarTurnos(statsJugador, statsOponente, oponentes)
        #Aquí se muestra el resultado final
        if ganador == 0:
            print("Has ganado")
            crecimiento(personajeJugador, statsJugador, nivelJugador, expJugador, statsOponente, nivelEnemigos, oponentes, tipoCrecimiento, vidaOriginal)
        else:
            print("Has perdido")
            statsJugador[0] = vidaOriginal
            statsJugador[12] = 0
            statsJugador[13] = 0 
    
    elif rondasPasadas%10==0:
        statsOponente = establecerBoss(nivelJugador)
        ganador = determinarTurnosBoss(statsJugador, statsOponente)
        
        if ganador == 0:
            print("Has ganado al boss")
            
        else:
            print("has perdido contra el boss")
            statsJugador[0] = vidaOriginal
            statsJugador[12] = 0
            statsJugador[13] = 0 
    i = i + 1
    rondasPasadas = rondasPasadas + 1
#variable para guardar en un archivo los datos del jugador
guardarStats = open('datosJugador.txt','w')
#se le pregunta al jugador si quiere guardar los datos
print('1)Guardar Datos\n2)Terminar el juego')
verificador = int(input('ingrese la opcion que desea: '))
if(verificador == 1):
    convertidor = str(statsJugador)
    print('Sus estadisticas son: ',statsJugador)
    guardarStats.write(convertidor)
elif verificador == 2:
    print('Fin del juego')

guardarStats.close()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
