coca_cola = 1500
inca_cola = 1000
piri= 500

bistec_con_pure = 3500
lasagna = 4000
sopa_de_almeja_con_leche = 7500

jalea = 800
torta = 1500
brownie = 2000

lista_rut=[]

def opcion():

    while True:
        try:
          opcion = int(input("Ingrese opcion: "))
          if opcion in(1,2,3,4,5,6):
             return opcion 
          else:
                    print("ERROR! debe ingresar una opcion correcta")    
        except:
            print("ERROR! debe ingresar un numero entero!") 

def carta():
    while True:
        carta = int(input("Ingrese opcion de carta que desea: "))
        if carta in(1,2,3,4,5):
            print("""Carta
            1. Bebidas
            2. Platos
            3. Postres
            4. Pedir
            5. Pagar""")

def reserva():
    rut = validar_rut
    nombre = validar_nombre
    correo = validar_correo
    cantidad = validar_reserva

def validar_rut():
    while True:
        try:
            rut = int(input("Ingrese su rut sin puntos ni digito verificador: "))
            if rut>= 1000000 and rut <=99999999:
                lista_rut rut.append[rut]
                return rut
            else:
                print("ERROR! debe ingresar numeros enteros!") 
        except:
            print("ERROR! rut ingresado no valido!")          

def validar_nombre():
    while True:
        nombre=input("Ingrese su nombre: ")
        if len(nombre.isalpha()) >=3:
            return nombre

def validar_correo():
    while True:
        correo=input("Ingrese su correo: ")
        if "@" in correo:
            return correo

def validar_reserva():
    while True:
        try:
            cantidad = int(input("Ingrese cantidad de personas para la mesa: "))
            if cantidad >=1 and cantidad <=6:
                return cantidad
            else:
                print("ERROR! debe ingresar un numero entero!")
        except:
            print("ERROR! excedio numero de asistentes!")            

def validar_carta():
    rut = validar_rut
    for x in lista_rut:
        for x in range (len(lista_rut)):
            if rut == lista_rut:
                return rut
            else:
                print("ERROR! rut no encontrado!")    

while True:
    print("""Menu
    1. Ver restaurant
    2. Reservar mesa
    3. Carta
    4. Pagar
    5. Cancelar
    6. Salir""")


    
