#imports
import xml.etree.ElementTree as ETree
parser = ETree.XMLParser(encoding="utf-8")
barajaEnemigo = None
MyBaraja = None

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
                status = False
            elif option == 2:
                print("Creando mazo ofensivo...")
                status= False
            elif option == 3:
                print("Creando mazo defensivo...")
                status = False
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
                status = False
            elif option == 2:
                print("Creando mazo ofensivo...")
                status = False
            elif option == 3:
                print("Creando mazo defensivo...")
                status = False
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
            elif option == 3:
                print("Creando mazo del enemigo defensivo...")
                status = False
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
            elif option == 3:
                print("Creando mazo defensivo...")
                status = False
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
