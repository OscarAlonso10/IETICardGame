#imports
import xml.etree.ElementTree as ETree
parser = ETree.XMLParser(encoding="utf-8")
barajaEnemigo = None
MyBaraja = None
baraja = []

#Creación menu
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

subMenuBarajaEnemigoCargada='''
====================================
1.  Crear mazo aleatorio Enemigo
2.  Crear mazo ofensivo Enemigo
3.  Crear mazo defensivo Enemigo
4.  Crear mazo equilibrado Enemigo
5.  Volver al menu anterior
0.  Salir Menu
====================================
'''
#Cargar xml
def barajaAleatoria():
    print("hola")

def barajaOfensivaEnemigo():
    tree = ETree.parse("Enemigo.xml")
    root = tree.getroot()

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

def barajaOfensiva():
    tree = ETree.parse("myBaraja.xml")
    root = tree.getroot()

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
    tree = ETree.parse("myBaraja.xml")
    root = tree.getroot()
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
    tree = ETree.parse("Enemigo.xml")
    root = tree.getroot()

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
    while option<1 or option>3:
        option = int(input("Selecciona una opcion: "))

    if option == 1:
        MyBaraja = ETree.parse("myBaraja.xml")
        print(ETree.tostring(MyBaraja.getroot()))
        if MyBaraja != None and barajaEnemigo == None:
            print("Baraja Cargada Correctamente")
            print(subMenuMyBarajaCargada)
            option = int(input("Selecciona una opcion: "))
            while option < 0 or option > 5:
                option = int(input("Selecciona una opcion: "))
            if  option == 1:
                print("Creando mazo aleatorio...")
                barajaAleatoria()
                status = False
            elif option == 2:
                print("Creando mazo ofensivo...")
                status= False
                barajaOfensiva()
            elif option == 3:
                print("Creando mazo defensivo...")
                status = False
                barajaDefensiva()
            elif option ==4:
                print("Creando mazo equilibrado")
                status = False
            elif option == 5:
                status = True
            elif option == 0:
                print("Final del juego")
                status = False
        elif MyBaraja != None and barajaEnemigo != None:
            print(subMenu)
            option = int(input("Selecciona una opcion: "))
            while option < 0 or option > 11:
                option = int(input("Selecciona una opcion: "))
            if option == 1:
                print("Creando mazo aleatorio...")
                barajaAleatoria()
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
                status = False
            elif option == 5:
                print("Creando mazo del enemigo aleatorio...")
                status = False
            elif option == 6:
                print("Creando mazo del enemigo ofensivo...")
                status = False
            elif option == 7:
                print("Creando mazo del enemigo defensivo...")
                status = False
            elif option == 8:
                print("Creando mazo del enemigo equilibrado...")
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
        barajaEnemigo = ETree.parse("Enemigo.xml")
        print(ETree.tostring(barajaEnemigo.getroot()))
        if barajaEnemigo != None and MyBaraja == None:
            print("Baraja Enemigo Cargada Correctamente")
            print(subMenuBarajaEnemigoCargada)
            option = int(input("Selecciona una opcion: "))
            while option < 0 or option > 5:
                option = int(input("Selecciona una opcion: "))
            if  option == 1:
                print("Creando mazo del enemigo aleatorio...")
                status = False
            elif option == 2:
                print("Creando mazo del enemigo ofensivo...")
                status= False
                barajaOfensivaEnemigo()
            elif option == 3:
                print("Creando mazo del enemigo defensivo...")
                status = False
                barajaDefensivaEnemigo()
            elif option ==4:
                print("Creando mazo del enemigo equilibrado")
                status = False
            elif option == 5:
                status = True
            elif option == 0:
                print("Final del juego")
                status = False
        elif MyBaraja != None and barajaEnemigo != None:
            print(subMenu)
            option = int(input("Selecciona una opcion: "))
            while option < 0 or option > 11:
                option = int(input("Selecciona una opcion: "))
            if option == 1:
                print("Creando mazo aleatorio...")
                status = False
            elif option == 2:
                print("Creando mazo ofensivo...")
                status = False
                barajaOfensivaEnemigo()
            elif option == 3:
                print("Creando mazo defensivo...")
                status = False
                barajaDefensivaEnemigo()
            elif option == 4:
                print("Creando mazo equilibrado")
                status = False
            elif option == 5:
                print("Creando mazo del enemigo aleatorio...")
                status = False
            elif option == 6:
                print("Creando mazo del enemigo ofensivo...")
                status = False
            elif option == 7:
                print("Creando mazo del enemigo defensivo...")
                status = False
            elif option == 8:
                print("Creando mazo del enemigo equilibrado...")
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
