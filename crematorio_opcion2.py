# Un crematorio universitario requiere revisar un sistema para gestionar los pacientes que fallecieron y llegaron a su crematorio 

#primeras 2 opciones:

#1) Un registro en una lista donde pueden ingresar máximo 5 ingresos al horno como tope (nombres completos)
#   preguntar cuántos ingresos se hacen*
#   solo se puede ingresar edades >= 3.

#2) Va a hacer registro de insumos que se necesita para cremar a una persona, máximo 15 (también un listado de nombres solamente, productos)

#3) Debe mostrar un número aleatorio del 1 a 50, el cual va a representar los días de licencia que tiene el crematorio
#  Ej: ¿Cuántos días de licencia tengo para el crematorio? 
#	Respuesta: 1

#4) Opción 4 = Salir (Se tiene que repetir todas las veces que quiera)

#Regla1: Cada integrante del grupo debe tener su propia rama por separado.
#Regla 2: Cada grupo va a hacer solamente 1 repositorio. 
#Regla 3: Debe usar la misma estructura en términos de variable e identacion.

#1 archivo que tenga todo el código de los 3 

lista_insumos = []
cantidad_insumos = 0

def opcion_2 ():
    global cantidad_insumos
    while cantidad_insumos <= 0 or cantidad_insumos > 15:
        try:
                cantidad_insumos = int(input("Ingrese la cantidad de insumos que desea registrar en la lista (Máximo 15): "))
                if cantidad_insumos > 15:
                                    print("La cantidad de insumos a registrar no puede ser mayor a 15.")
                elif cantidad_insumos <=0: 
                    print("La cantidad de insumos no puede ser menor o igual 0.")       
        except:
            print("Error: Solo ingrese números enteros")
    
    for insumos in range (cantidad_insumos):
        insumos = input("Ingrese el nombre del producto para agregar a la lista de insumos: ")
        lista_insumos.append (insumos)

    print("La lista de insumos registrados es:", lista_insumos)

opcion_2 ()