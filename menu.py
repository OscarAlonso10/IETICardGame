# imports
import xml.etree.ElementTree as ETree
import random


parser = ETree.XMLParser(encoding="utf-8")
enemyTree = None
tree = None

vidaAliada = ""
vidaEnemiga = ""

baraja = [{'Name': 'Tulip', 'Decription': 'Veterano francotirador que usa el rifle como bastón.', 'Attack': '2', 'Defense': '1', 'SummonPoints': '3', 'Type': 'lancer'},
{'Name': 'Buffalo', 'Decription': 'Gran y fuerte búfalo montado por un pequeño elfo estratega.', 'Attack': '1', 'Defense': '1', 'SummonPoints': '2', 'Type': 'chivalry'},
{'Name': 'Blade', 'Decription': 'Viejo y oxidado cañón que aún cuenta con alta precisión.', 'Attack': '3', 'Defense': '0', 'SummonPoints': '3', 'Type': 'lancer'},
{'Name': 'Bodhi', 'Decription': 'Osito de peluche que dispara un líquido blanco por sus ojos.', 'Attack': '1', 'Defense': '0', 'SummonPoints': '1', 'Type': 'lancer'},
{'Name': 'Imorgon', 'Decription': 'Ágil velociraptor que no verás venir y solo sentirás dolor.', 'Attack': '3', 'Defense': '0', 'SummonPoints': '3', 'Type': 'chivalry'},
{'Name': 'Phantom', 'Decription': 'Un gnomo a los mandos de un robot gigantesco y resistente.', 'Attack': '2', 'Defense': '3', 'SummonPoints': '5', 'Type': 'chivalry'},
{'Name': 'Tug', 'Decription': 'Cachalote gigante con capacidad para elvarse unos 30 metros.', 'Attack': '1', 'Defense': '2', 'SummonPoints': '3', 'Type': 'infantry'},
{'Name': 'Phoenix', 'Decription': 'Fénix ancestral escupe-fuego desde las alturas.', 'Attack': '3', 'Defense': '1', 'SummonPoints': '4', 'Type': 'lancer'},
{'Name': 'Nemesis', 'Decription': 'Caballero de la noche que posee un robusto mazo con pinchos.', 'Attack': '1', 'Defense': '1', 'SummonPoints': '2', 'Type': 'chivalry'},
{'Name': 'Technical', 'Decription': 'Dromedario africano armado hasta los dientes.', 'Attack': '1', 'Defense': '1', 'SummonPoints': '2', 'Type': 'infantry'}]
barajaEnemiga =[{'Name': 'Tulip', 'Decription': 'Veterano francotirador que usa el rifle como bastón.', 'Attack': '2', 'Defense': '1', 'SummonPoints': '3', 'Type': 'lancer'},
{'Name': 'Buffalo', 'Decription': 'Gran y fuerte búfalo montado por un pequeño elfo estratega.', 'Attack': '1', 'Defense': '1', 'SummonPoints': '2', 'Type': 'chivalry'},
{'Name': 'Blade', 'Decription': 'Viejo y oxidado cañón que aún cuenta con alta precisión.', 'Attack': '3', 'Defense': '0', 'SummonPoints': '3', 'Type': 'lancer'},
{'Name': 'Bodhi', 'Decription': 'Osito de peluche que dispara un líquido blanco por sus ojos.', 'Attack': '1', 'Defense': '0', 'SummonPoints': '1', 'Type': 'lancer'},
{'Name': 'Imorgon', 'Decription': 'Ágil velociraptor que no verás venir y solo sentirás dolor.', 'Attack': '3', 'Defense': '0', 'SummonPoints': '3', 'Type': 'chivalry'},
{'Name': 'Phantom', 'Decription': 'Un gnomo a los mandos de un robot gigantesco y resistente.', 'Attack': '2', 'Defense': '3', 'SummonPoints': '5', 'Type': 'chivalry'},
{'Name': 'Tug', 'Decription': 'Cachalote gigante con capacidad para elvarse unos 30 metros.', 'Attack': '1', 'Defense': '2', 'SummonPoints': '3', 'Type': 'infantry'},
{'Name': 'Phoenix', 'Decription': 'Fénix ancestral escupe-fuego desde las alturas.', 'Attack': '3', 'Defense': '1', 'SummonPoints': '4', 'Type': 'lancer'},
{'Name': 'Nemesis', 'Decription': 'Caballero de la noche que posee un robusto mazo con pinchos.', 'Attack': '1', 'Defense': '1', 'SummonPoints': '2', 'Type': 'chivalry'},
{'Name': 'Technical', 'Decription': 'Dromedario africano armado hasta los dientes.', 'Attack': '1', 'Defense': '1', 'SummonPoints': '2', 'Type': 'infantry'}]

cartasAliadasJugadas = []
cartasEnemigasJugadas = []

# Creación menu
showMenu = '''
====================================
1.  Cargar Cartas
2.  Cargar cartas enemigo
3.  Salir del juego
====================================
'''

subMenu = '''
====================================
1.  Crear mazo aleatorio
2.  Crear mazo ofensivo
3.  Crear mazo defensivo
4.  Crear mazo equilibrado
5.  Crear mazo aleatorio Enemigo
6.  Crear mazo ofensivo Enemigo
7.  Crear mazo defensivo Enemigo
8.  Crear mazo equilibrado Enemigo
9.  Luchar Jugador vs Jugador
10. Luchar Jugador vs Bot
11. Luchar Jugador vs Bot (liga)
0.  Salir Menu
====================================
'''

menuLucha = '''
====================================
1. Luchar Jugador vs Jugador
2. Luchar Jugador vs Bot
3. Luchar Jugador vs Bot (liga)
0.  Salir Menu
====================================
'''

subMenuMyBarajaCargada = '''
====================================
1.  Crear mazo aleatorio
2.  Crear mazo ofensivo
3.  Crear mazo defensivo
4.  Crear mazo equilibrado
5.  Volver al menu anterior
0.  Salir Menu
====================================
'''

subMenuBarajaEnemigoCargada = '''
====================================
1.  Crear mazo aleatorio Enemigo
2.  Crear mazo ofensivo Enemigo
3.  Crear mazo defensivo Enemigo
4.  Crear mazo equilibrado Enemigo
5.  Volver al menu anterior
0.  Salir Menu
====================================
'''
# Cargar xml

"<=====================================================   START Cartas Aliada Aleatorio FUNCTION    ======================================>"


def randomPosAliada():
    randomPos = []
    i = 0
    while i < 10:
        pos = random.randrange(1, 20)
        if pos not in randomPos:
            randomPos.append(pos)
            i += 1
    generarCartaAliada(randomPos)


def generarCartaAliada(randomPos):
    #cards = []
    for i in range(len(randomPos)):
        cardSumPoint = root.find('.//card[' + str(randomPos[i]) + ']').attrib['summonPoints']
        cardType = root.find('.//card[' + str(randomPos[i]) + ']').attrib['type']
        cardName = root.findtext('.//card[' + str(randomPos[i]) + ']/name')
        cardDesc = root.findtext('.//card[' + str(randomPos[i]) + ']/description')
        cardAtk = root.findtext('.//card[' + str(randomPos[i]) + ']/attack')
        cardDef = root.findtext('.//card[' + str(randomPos[i]) + ']/defense')

        card = {
            "Name": cardName,
            "Decription": cardDesc,
            "Attack": cardAtk,
            "Defense": cardDef,
            "SummonPoints": cardSumPoint,
            "Type": cardType
        }

        baraja.append(card)
    mostrarCartasAliadas(baraja)


def mostrarCartasAliadas(baraja):
    for i in range(len(baraja)):
        print(baraja[i])

"<=====================================================   END Cartas Aliada Aleatorio FUNCTION    ======================================>"
"<=====================================================   START Cartas Enemigo Aleatorio FUNCTION    ======================================>"


def randomPosEnemiga():
    randomPos = []
    i = 0
    while i < 10:
        pos = random.randrange(1, 20)
        if pos not in randomPos:
            randomPos.append(pos)
            i += 1
    generarCartaEnemigas(randomPos)


def generarCartaEnemigas(randomPos):
    #cards = []
    for i in range(len(randomPos)):
        cardSumPoint = enemyRoot.find('.//card[' + str(randomPos[i]) + ']').attrib['summonPoints']
        cardType = enemyRoot.find('.//card[' + str(randomPos[i]) + ']').attrib['type']
        cardName = enemyRoot.findtext('.//card[' + str(randomPos[i]) + ']/name')
        cardDesc = enemyRoot.findtext('.//card[' + str(randomPos[i]) + ']/description')
        cardAtk = enemyRoot.findtext('.//card[' + str(randomPos[i]) + ']/attack')
        cardDef = enemyRoot.findtext('.//card[' + str(randomPos[i]) + ']/defense')

        card = {
            "Name": cardName,
            "Decription": cardDesc,
            "Attack": cardAtk,
            "Defense": cardDef,
            "SummonPoints": cardSumPoint,
            "Type": cardType
        }

        barajaEnemiga.append(card)
    mostrarCartasEnemigas(barajaEnemiga)


def mostrarCartasEnemigas(barajaEnemiga):
    for i in range(len(barajaEnemiga)):
        print(barajaEnemiga[i])


"<=====================================================   END Cartas Enemigo Aleatorio FUNCTION    ======================================>"
"<=====================================================   START Cartas Aliado Equilibrado FUNCTION    ======================================>"


def cartaEquilibradaAliada():
    #cards = []
    for i in range(1, 20):
        cardSumPoint = root.find('.//card[' + str(i) + ']').attrib['summonPoints']
        cardType = root.find('.//card[' + str(i) + ']').attrib['type']
        cardName = root.findtext('.//card[' + str(i) + ']/name')
        cardDesc = root.findtext('.//card[' + str(i) + ']/description')
        cardAtk = root.findtext('.//card[' + str(i) + ']/attack')
        cardDef = root.findtext('.//card[' + str(i) + ']/defense')

        media = int(cardAtk) - int(cardDef)
        media = abs(media)

        card = {
            "Name": cardName,
            "Decription": cardDesc,
            "Attack": cardAtk,
            "Defense": cardDef,
            "SummonPoints": cardSumPoint,
            "Type": cardType,
            "Media": media
        }
        baraja.append(card)
    listaOrdenada = sorted(baraja, key=lambda card: card['Media'])
    #barajaEquilibradaOrdenada = []
    for j in range(0, 10):
        del listaOrdenada[j]["Media"]
        baraja.append(listaOrdenada[j])
    mostrarCartasEquilibradasAliadas(baraja)


def mostrarCartasEquilibradasAliadas(baraja):
    for i in range(len(baraja)):
        print(baraja[i])


"<=====================================================   END Cartas Aliado Equilibrado FUNCTION    ======================================>"

"<=====================================================   START Cartas Enemigo Equilibrado FUNCTION    ======================================>"


def cartaEquilibradaEnemiga():

    #cards = []
    for i in range(1, 20):
        cardSumPoint = enemyRoot.find('.//card[' + str(i) + ']').attrib['summonPoints']
        cardType = enemyRoot.find('.//card[' + str(i) + ']').attrib['type']
        cardName = enemyRoot.findtext('.//card[' + str(i) + ']/name')
        cardDesc = enemyRoot.findtext('.//card[' + str(i) + ']/description')
        cardAtk = enemyRoot.findtext('.//card[' + str(i) + ']/attack')
        cardDef = enemyRoot.findtext('.//card[' + str(i) + ']/defense')

        media = int(cardAtk) - int(cardDef)
        media = abs(media)

        card = {
            "Name": cardName,
            "Decription": cardDesc,
            "Attack": cardAtk,
            "Defense": cardDef,
            "SummonPoints": cardSumPoint,
            "Type": cardType,
            "Media": media
        }
        barajaEnemiga.append(card)
    listaOrdenada = sorted(barajaEnemiga, key=lambda card: card['Media'])
    #barajaEquilibradaOrdenada = []
    for j in range(0, 10):
        del listaOrdenada[j]["Media"]
        barajaEnemiga.append(listaOrdenada[j])
    mostrarCartasEquilibradasAliadas(barajaEnemiga)


def mostrarCartasEquilibradasEnemiga(barajaEnemiga):
    for i in range(len(barajaEnemiga)):
        print(barajaEnemiga[i])


"<=====================================================   END Cartas Enemigo Equilibrado FUNCTION    ======================================>"


def barajaOfensivaEnemigo():

    barajaAtaque = []

    # Creamos un for de manera que debemos de encontrar mediante el metodo findall los tags dentro de deck/card
    for card in enemyRoot.findall('deck/card'):
        carta = []
        summonPoints = int(card.attrib['summonPoints'])
        tipo = str(card.attrib['type'])
        nombre = str(card.find('name').text)
        descripcion = str(card.find('description').text)
        ataque = int(card.find('attack').text)
        defensa = int(card.find('defense').text)
        carta.append(summonPoints)
        carta.append(tipo)
        carta.append(nombre)
        carta.append(descripcion)
        carta.append(ataque)
        carta.append(defensa)
        barajaAtaque.append(carta)
    barajaAtaque.sort(reverse=True)

    # Ordenamos la variable barajaordatt y le decimos que comienze desde la posición de la lista 4
    # En este caso será la puntuación más alta de ataque que será la primera del mazo en generar
    barajaordatt = sorted(barajaAtaque, key=lambda h: h[4])
    barajaordatt.reverse()

    # Creamos un for de manera que añadimos a la lista barajaAtaque la variable que guardará la otra lista barajaordatt
    for i in range(0, 10):
        barajaEnemiga.append(barajaordatt[i])
    print(barajaEnemiga)


def barajaOfensiva():

    barajaAtaque = []

    # Creamos un for de manera que debemos de encontrar mediante el metodo findall los tags dentro de deck/card
    for card in root.findall('deck/card'):
        carta = []
        summonPoints = int(card.attrib['summonPoints'])
        tipo = str(card.attrib['type'])
        nombre = str(card.find('name').text)
        descripcion = str(card.find('description').text)
        ataque = int(card.find('attack').text)
        defensa = int(card.find('defense').text)

        carta.append(summonPoints)
        carta.append(tipo)
        carta.append(nombre)
        carta.append(descripcion)
        carta.append(ataque)
        carta.append(defensa)
        barajaAtaque.append(carta)
    barajaAtaque.sort(reverse=True)

    # Ordenamos la variable barajaordatt y le decimos que comienze desde la posición de la lista 4
    # En este caso será la puntuación más alta de ataque que será la primera del mazo en generar
    barajaordatt = sorted(barajaAtaque, key=lambda h: h[4])
    barajaordatt.reverse()

    # Creamos un for de manera que añadimos a la lista barajaAtaque la variable que guardará la otra lista barajaordatt
    for i in range(0, 10):
        baraja.append(barajaordatt[i])
    print(baraja)


def barajaDefensiva():

    barajaDefensa = []

    # Creamos un for de manera que debemos de encontrar mediante el metodo findall los tags dentro de deck/card
    for card in root.findall('deck/card'):
        carta = []
        summonPoints = int(card.attrib['summonPoints'])
        tipo = str(card.attrib['type'])
        nombre = str(card.find('name').text)
        descripcion = str(card.find('description').text)
        ataque = int(card.find('attack').text)
        defensa = int(card.find('defense').text)
        carta.append(summonPoints)
        carta.append(tipo)
        carta.append(nombre)
        carta.append(descripcion)
        carta.append(ataque)
        carta.append(defensa)
        barajaDefensa.append(carta)
    barajaDefensa.sort(reverse=True)

    # Ordenamos la variable barajaordedef y le decimos que comienze desde la posición de la lista 5
    # En este caso será la puntuación más alta de defensa la primera del mazo en generar
    barajaorddef = sorted(barajaDefensa, key=lambda h: h[5])
    barajaorddef.reverse()

    # Creamos un for de manera que añadimos a la lista barajaDefensa la variable que guardará la otra lista barajaordedef
    for i in range(0, 10):
        baraja.append(barajaorddef[i])
    print(baraja)


def barajaDefensivaEnemigo():


    barajaDefensa = []

    # Creamos un for de manera que debemos de encontrar mediante el metodo findall los tags dentro de deck/card
    for card in enemyRoot.findall('deck/card'):
        carta = []
        summonPoints = int(card.attrib['summonPoints'])
        tipo = str(card.attrib['type'])
        nombre = str(card.find('name').text)
        descripcion = str(card.find('description').text)
        ataque = int(card.find('attack').text)
        defensa = int(card.find('defense').text)

        carta.append(summonPoints)
        carta.append(tipo)
        carta.append(nombre)
        carta.append(descripcion)
        carta.append(ataque)
        carta.append(defensa)
        barajaDefensa.append(carta)
    barajaDefensa.sort(reverse=True)

    # Ordenamos la variable barajaordedef y le decimos que comienze desde la posición de la lista 5
    # En este caso será la puntuación más alta de defensa la primera del mazo en generar
    barajaorddef = sorted(barajaDefensa, key=lambda h: h[5])
    barajaorddef.reverse()

    # Creamos un for de manera que añadimos a la lista barajaDefensa la variable que guardará la otra lista barajaordedef
    for i in range(0, 10):
        barajaEnemiga.append(barajaorddef[i])
    print(barajaEnemiga)


def DecidirInicio():
    inicio = random.randrange(1, 3)
    return inicio

#vidaAliada = root.findtext('.//playerLife')
#vidaEnemiga = enemyRoot.findtext('.//playerLife')
def faseDeInvocacionAliada():
    print("Jugador 1")
    print("Vida: ", vidaAliada)
    cardSelection()

def cardSelection():
    print("Turno del Jugador 1.")
    summonPoints = root.findtext('.//summonPointsPlayer')
    print("Summon Points del Jugador 1:", summonPoints)
    chosenCard = random.choice(baraja)
    cardSummonPoints = chosenCard.get("SummonPoints")
    summonPoints = int(summonPoints) - int(cardSummonPoints)
    print(chosenCard)
    cartasAliadasJugadas.append(chosenCard)
    print("Los Summon Points actuales del Jugador 1: ", summonPoints)
    combatiente = 1
    faseDeCombate(combatiente)

def faseDeInvocacionEnemiga():
    print("Jugador 2")
    print("Vida: ", vidaEnemiga)
    cardEnemySelection()

vidaAliadaActual = ""
vidaEnemigaActual = ""
def cardEnemySelection():
    print("Turno del Jugador 2.")
    summonPointsEnemigo = enemyRoot.findtext('.//summonPointsPlayer')

    print("Summon Points del Jugador 2", summonPointsEnemigo)
    chosenEnemyCard = random.choice(barajaEnemiga)
    cardEnemySummonPoints = chosenEnemyCard.get("SummonPoints")
    summonPointsEnemigo = int(summonPointsEnemigo) - int(cardEnemySummonPoints)
    print(chosenEnemyCard)
    print("Sumon Points carta Jugador 2: ", cardEnemySummonPoints)
    cartasEnemigasJugadas.append(chosenEnemyCard)
    print("Los Summon Points actuales del Jugador 2: ", summonPointsEnemigo)
    combatiente = 2
    faseDeCombate(combatiente)

def faseDeCombate(combatiente):

    print("Cartas aliadas ", cartasAliadasJugadas)
    print("Cartas enemigas ", cartasEnemigasJugadas)
    if combatiente == 1:
        atkAlly = cartasAliadasJugadas[0].get("Attack")
        print("El ataque de la carta del Jugador 1: ", atkAlly)
        if cartasEnemigasJugadas:
            defEnemy = cartasEnemigasJugadas[0].get("Defense")
            print("La defensa de la carta del Jugador 2: ", defEnemy)
            enemyDamage = int(atkAlly) - int(defEnemy)
            if enemyDamage > 0:
                print("Daño de la carta del Jugador 1: ", enemyDamage)
                vidaEnemigaActual = int(vidaEnemiga) - int(enemyDamage)
                print("La vida del Jugador 2: ", vidaEnemigaActual)
                cartasEnemigasJugadas.pop(0)
            elif enemyDamage == 0:
                cartasEnemigasJugadas.pop(0)
            op = ""
            while op != "YES" or op != "NO":
                print("Juador 1 quieres terminar el turno? (yes/no)")
                op = input()
                op = op.upper()
                if op == "YES":
                    print("Final del turno del Jugador 1.")
                    cardEnemySelection()
                elif op == "NO":
                    cardSelection()

        else:
            op = ""
            while op != "YES" or op != "NO":
                print("Juador 1 quieres terminar el turno? (yes/no)")
                op = input()
                op = op.upper()
                if op == "YES":
                    print("Final del turno del Jugador 1.")
                    cardEnemySelection()
                elif op == "NO":
                    cardSelection()
    else:
        atkEnemy = cartasEnemigasJugadas[0].get("Attack")
        print("El ataque de l carta del Jugador 2: ", atkEnemy)
        if cartasAliadasJugadas :
            defAlly = cartasAliadasJugadas[0].get("Defense")
            print("La defensa de la carta del Jugador 1: ", defAlly)
            allyDamage = int(atkEnemy) - int(defAlly)
            if allyDamage > 0:
                print("Daño de la carta del Jugador 2: ", allyDamage)
                vidaAliadaActual = int(vidaAliada) - int(allyDamage)
                print("La vida del Jugador 1: ", vidaAliadaActual)
                cartasAliadasJugadas.pop(0)
            elif allyDamage == 0:
                cartasAliadasJugadas.pop(0)
            op = ""
            while op != "YES" or op != "NO":
                print("Jugador 2 quieres terminar el turno? (yes/no)")
                op = input()
                op = op.upper()
                if op == "YES":
                    print("Final del turno del Jugador 2.")
                    cardSelection()
                elif op == "NO":
                    cardEnemySelection()
        else:
            op = ""
            while op != "YES" or op != "NO":
                print("Jugador 2 quieres terminar el turno? (yes/no)")
                op = input()
                op = op.upper()
                if op == "YES":
                    print("Final del turno del Jugador 2.")
                    cardSelection()
                elif op == "NO":
                    cardEnemySelection()

def JugadorVsJugador():

    if DecidirInicio() ==1:
        print('empieza el jugador 1')
        faseDeInvocacionAliada()
    else:
        print('empieza el jugador 2')
        faseDeInvocacionEnemiga()


status = True
while status:
    print(showMenu)
    option = int(input("Selecciona una opcion: "))
    while option < 1 or option > 3:
        option = int(input("Selecciona una opcion: "))

    if option == 1:
        tree = ETree.parse("myBaraja.xml")
        root = tree.getroot()
        if tree != None and enemyTree == None:
            print("Baraja Cargada Correctamente")
            print(subMenuMyBarajaCargada)
            option = int(input("Selecciona una opcion: "))
            while option < 0 or option > 5:
                option = int(input("Selecciona una opcion: "))
            if option == 1:
                print("Creando mazo aleatorio...")
                randomPosAliada()
                print(menuLucha)
                lucha = int(input("Selecciona una opcion: "))
                while lucha < 0 or lucha > 3:
                    lucha = int(input("Selecciona una opcion: "))
                    print(lucha)
                    if lucha == 1:
                        print("Empieza lucha Jugador vs Jugador")
                        JugadorVsJugador()

            elif option == 2:
                print("Creando mazo ofensivo...")
                barajaOfensiva()
                print(menuLucha)
                status=False
                option = int(input("Selecciona una opcion: "))
                while option < 0 or option > 3:
                    option = int(input("Selecciona una opcion: "))
                    if option == 1:
                        print("Empieza lucha Jugador vs Jugador")
                        JugadorVsJugador()
            elif option == 3:
                print("Creando mazo defensivo...")
                barajaDefensiva()
                print(menuLucha)
                option = int(input("Selecciona una opcion: "))
                while option < 0 or option > 3:
                    option = int(input("Selecciona una opcion: "))
                    if option == 1:
                        print("Empieza lucha Jugador vs Jugador")
                        JugadorVsJugador()

            elif option == 4:
                print("Creando mazo equilibrado")
                cartaEquilibradaAliada()
                print(menuLucha)
                option = int(input("Selecciona una opcion: "))
                while option < 0 or option > 3:
                    option = int(input("Selecciona una opcion: "))
                    if option == 1:
                        print("Empieza lucha Jugador vs Jugador")
                        JugadorVsJugador()

            elif option == 5:
                status = True
            elif option == 0:
                print("Final del juego")
                status = False
        elif tree != None and enemyTree != None:
            print(subMenu)
            option = int(input("Selecciona una opcion: "))
            while option < 0 or option > 11:
                option = int(input("Selecciona una opcion: "))
            if option == 1:
                print("Creando mazo aleatorio...")
                randomPosAliada()
                print(menuLucha)
                option = int(input("Selecciona una opcion: "))
                while option < 0 or option > 3:
                    option = int(input("Selecciona una opcion: "))
                    if option==1:
                        print("Empieza lucha Jugador vs Jugador")
                        JugadorVsJugador()
            elif option == 2:
                print("Creando mazo ofensivo...")
                barajaOfensiva()
                print(menuLucha)
                option = int(input("Selecciona una opcion: "))
                while option < 0 or option > 3:
                    option = int(input("Selecciona una opcion: "))
                    if option == 1:
                        print("Empieza lucha Jugador vs Jugador")
                        JugadorVsJugador()
            elif option == 3:
                print("Creando mazo defensivo...")
                barajaDefensiva()
                print(menuLucha)
                option = int(input("Selecciona una opcion: "))
                while option < 0 or option > 3:
                    option = int(input("Selecciona una opcion: "))
                    if option == 1:
                        print("Empieza lucha Jugador vs Jugador")
                        JugadorVsJugador()
            elif option == 4:
                print("Creando mazo equilibrado")
                cartaEquilibradaAliada()
                print(menuLucha)
                option = int(input("Selecciona una opcion: "))
                while option < 0 or option > 3:
                    option = int(input("Selecciona una opcion: "))
                    if option == 1:
                        print("Empieza lucha Jugador vs Jugador")
                        JugadorVsJugador()
            elif option == 5:
                print("Creando mazo del enemigo aleatorio...")
                randomPosEnemiga()
                status = False
            elif option == 6:
                print("Creando mazo del enemigo ofensivo...")
                barajaOfensivaEnemigo()
                status = False
            elif option == 7:
                print("Creando mazo del enemigo defensivo...")
                barajaDefensivaEnemigo()
                status = False
            elif option == 8:
                print("Creando mazo del enemigo equilibrado...")
                cartaEquilibradaEnemiga()
                status = False
            elif option == 9:
                print("Preparando lucha Jugador vs Jugador...")
                JugadorVsJugador()
                print('Aun no teneis una baraja cargada')
                status = False

            elif option == 10:
                print("Preparando lucha Jugador vs Bot...")
                status = False
            elif option == 1:
                print("Preparando lucha Jugador vs Bot (modo liga)...")
                status = False
            elif option == 0:
                print("Final del juego")
                status = False
        else:
            print("No hay cartas")
    elif option == 2:
        enemyTree = ETree.parse("Enemigo.xml")
        enemyRoot = enemyTree.getroot()
        if enemyTree != None and tree == None:
            print("Baraja Enemigo Cargada Correctamente")
            print(subMenuBarajaEnemigoCargada)
            option = int(input("Selecciona una opcion: "))
            while option < 0 or option > 5:
                option = int(input("Selecciona una opcion: "))
            if option == 1:
                print("Creando mazo del enemigo aleatorio...")
                randomPosEnemiga()
                status = False
            elif option == 2:
                print("Creando mazo del enemigo ofensivo...")
                status = False
                barajaOfensivaEnemigo()
            elif option == 3:
                print("Creando mazo del enemigo defensivo...")
                status = False
                barajaDefensivaEnemigo()
            elif option == 4:
                print("Creando mazo del enemigo equilibrado")
                cartaEquilibradaEnemiga()
                status = False
            elif option == 5:
                status = True
            elif option == 0:
                print("Final del juego")
                status = False
        elif tree != None and enemyTree != None:
            print(subMenu)
            option = int(input("Selecciona una opcion: "))
            while option < 0 or option > 11:
                option = int(input("Selecciona una opcion: "))
            if option == 1:
                print("Creando mazo aleatorio...")
                randomPosAliada()
                print(menuLucha)
                option = int(input("Selecciona una opcion: "))
                while option < 0 or option > 3:
                    option = int(input("Selecciona una opcion: "))
                    if option == 1:
                        print("Empieza lucha Jugador vs Jugador")
                        JugadorVsJugador()
            elif option == 2:
                print("Creando mazo ofensivo...")
                barajaOfensiva()
                print(menuLucha)
                option = int(input("Selecciona una opcion: "))
                while option < 0 or option > 3:
                    option = int(input("Selecciona una opcion: "))
                    if option == 1:
                        print("Empieza lucha Jugador vs Jugador")
                        JugadorVsJugador()
            elif option == 3:
                print("Creando mazo defensivo...")
                barajaDefensiva()
                print(menuLucha)
                option = int(input("Selecciona una opcion: "))
                while option < 0 or option > 3:
                    option = int(input("Selecciona una opcion: "))
                    if option == 1:
                        print("Empieza lucha Jugador vs Jugador")
                        JugadorVsJugador()
            elif option == 4:
                print("Creando mazo equilibrado")
                cartaEquilibradaAliada()
                print(menuLucha)
                option = int(input("Selecciona una opcion: "))
                while option < 0 or option > 3:
                    option = int(input("Selecciona una opcion: "))
                    if option == 1:
                        print("Empieza lucha Jugador vs Jugador")
                        JugadorVsJugador()
            elif option == 5:
                print("Creando mazo del enemigo aleatorio...")
                randomPosEnemiga()
                status = False
            elif option == 6:
                print("Creando mazo del enemigo ofensivo...")
                barajaOfensivaEnemigo()
                status = False
            elif option == 7:
                print("Creando mazo del enemigo defensivo...")
                barajaDefensivaEnemigo()
                status = False
            elif option == 8:
                print("Creando mazo del enemigo equilibrado...")
                cartaEquilibradaEnemiga()
                status = False
            elif option == 9:
                print("Preparando lucha Jugador vs Jugador...")
                vidaAliada = root.findtext(".//playerLife")
                vidaEnemiga = enemyRoot.findtext(".//playerLife")
                JugadorVsJugador()
                print('Aun no teneis una baraja cargada')
                status = False
            elif option == 10:
                print("Preparando lucha Jugador vs Bot...")
                status = False
            elif option == 1:
                print("Preparando lucha Jugador vs Bot (modo liga)...")
                status = False
            elif option == 0:
                print("Final del juego")
                status = False
        else:
            print("No hay cartas")
    else:
        print("Final del juego")
        status = False