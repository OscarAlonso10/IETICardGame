# imports
import xml.etree.ElementTree as ETree
import random

parser = ETree.XMLParser(encoding="utf-8")
enemyTree = None
tree = None
baraja = []

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
    cards = []
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

        cards.append(card)
    mostrarCartasAliadas(cards)


def mostrarCartasAliadas(cards):
    for i in range(len(cards)):
        print(cards[i])


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
    cards = []
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

        cards.append(card)
    mostrarCartasEnemigas(cards)


def mostrarCartasEnemigas(cards):
    for i in range(len(cards)):
        print(cards[i])


"<=====================================================   END Cartas Enemigo Aleatorio FUNCTION    ======================================>"
"<=====================================================   START Cartas Aliado Equilibrado FUNCTION    ======================================>"


def cartaEquilibradaAliada():
    cards = []
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
        cards.append(card)
    listaOrdenada = sorted(cards, key=lambda card: card['Media'])
    barajaEquilibradaOrdenada = []
    for j in range(0, 10):
        del listaOrdenada[j]["Media"]
        barajaEquilibradaOrdenada.append(listaOrdenada[j])
    mostrarCartasEquilibradasAliadas(barajaEquilibradaOrdenada)


def mostrarCartasEquilibradasAliadas(barajaEquilibradaOrdenada):
    for i in range(len(barajaEquilibradaOrdenada)):
        print(barajaEquilibradaOrdenada[i])


"<=====================================================   END Cartas Aliado Equilibrado FUNCTION    ======================================>"

"<=====================================================   START Cartas Enemigo Equilibrado FUNCTION    ======================================>"


def cartaEquilibradaEnemiga():

    cards = []
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
        cards.append(card)
    listaOrdenada = sorted(cards, key=lambda card: card['Media'])
    barajaEquilibradaOrdenada = []
    for j in range(0, 10):
        del listaOrdenada[j]["Media"]
        barajaEquilibradaOrdenada.append(listaOrdenada[j])
    mostrarCartasEquilibradasAliadas(barajaEquilibradaOrdenada)


def mostrarCartasEquilibradasEnemiga(barajaEquilibradaOrdenada):
    for i in range(len(barajaEquilibradaOrdenada)):
        print(barajaEquilibradaOrdenada[i])


"<=====================================================   END Cartas Enemigo Equilibrado FUNCTION    ======================================>"


def barajaOfensivaEnemigo():


    baraja = []
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
        baraja.append(carta)
    baraja.sort(reverse=True)

    # Ordenamos la variable barajaordatt y le decimos que comienze desde la posición de la lista 4
    # En este caso será la puntuación más alta de ataque que será la primera del mazo en generar
    barajaordatt = sorted(baraja, key=lambda h: h[4])
    barajaordatt.reverse()

    # Creamos un for de manera que añadimos a la lista barajaAtaque la variable que guardará la otra lista barajaordatt
    for i in range(0, 10):
        barajaAtaque.append(barajaordatt[i])
    print(barajaAtaque)


def barajaOfensiva():

    baraja = []
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
        baraja.append(carta)
    baraja.sort(reverse=True)

    # Ordenamos la variable barajaordatt y le decimos que comienze desde la posición de la lista 4
    # En este caso será la puntuación más alta de ataque que será la primera del mazo en generar
    barajaordatt = sorted(baraja, key=lambda h: h[4])
    barajaordatt.reverse()

    # Creamos un for de manera que añadimos a la lista barajaAtaque la variable que guardará la otra lista barajaordatt
    for i in range(0, 10):
        barajaAtaque.append(barajaordatt[i])
    print(barajaAtaque)


def barajaDefensiva():

    baraja = []
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
        baraja.append(carta)
    baraja.sort(reverse=True)

    # Ordenamos la variable barajaordedef y le decimos que comienze desde la posición de la lista 5
    # En este caso será la puntuación más alta de defensa la primera del mazo en generar
    barajaorddef = sorted(baraja, key=lambda h: h[5])
    barajaorddef.reverse()

    # Creamos un for de manera que añadimos a la lista barajaDefensa la variable que guardará la otra lista barajaordedef
    for i in range(0, 10):
        barajaDefensa.append(barajaorddef[i])
    print(barajaDefensa)


def barajaDefensivaEnemigo():


    baraja = []

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
        minaAtaque = 0
        carta.append(summonPoints)
        carta.append(tipo)
        carta.append(nombre)
        carta.append(descripcion)
        carta.append(ataque)
        carta.append(defensa)
        baraja.append(carta)
    baraja.sort(reverse=True)

    # Ordenamos la variable barajaordedef y le decimos que comienze desde la posición de la lista 5
    # En este caso será la puntuación más alta de defensa la primera del mazo en generar
    barajaorddef = sorted(baraja, key=lambda h: h[5])
    barajaorddef.reverse()

    # Creamos un for de manera que añadimos a la lista barajaDefensa la variable que guardará la otra lista barajaordedef
    for i in range(0, 10):
        barajaDefensa.append(barajaorddef[i])
    print(barajaDefensa)


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
                status = False
            elif option == 2:
                print("Creando mazo ofensivo...")
                status = False
                barajaOfensiva()
            elif option == 3:
                print("Creando mazo defensivo...")
                status = False
                barajaDefensiva()
            elif option == 4:
                print("Creando mazo equilibrado")
                cartaEquilibradaAliada()
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
                status = False
            elif option == 2:
                print("Creando mazo ofensivo...")
                status = False
                barajaOfensiva()
            elif option == 3:
                print("Creando mazo defensivo...")
                status = False
                barajaDefensiva()
            elif option == 4:
                print("Creando mazo equilibrado")
                cartaEquilibradaAliada()
                status = False
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
                randomPosAliada()
                print("Creando mazo aleatorio...")

                status = False
            elif option == 2:
                print("Creando mazo ofensivo...")
                status = False
                barajaOfensiva()
            elif option == 3:
                print("Creando mazo defensivo...")
                status = False
                barajaDefensiva()
            elif option == 4:
                print("Creando mazo equilibrado")
                cartaEquilibradaAliada()
                status = False
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
