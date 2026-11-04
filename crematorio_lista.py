lista_fallecidos = []

print("-- REGISTRO CREMATORIO --")

while len(lista_fallecidos) < 5:
    nombre = input("Ingrese el nombre completo de la persona: ").lower().strip()
    edad = int(input("Ingrese la edad: "))

    if edad >= 3:
        lista_fallecidos.append(f"{nombre} {edad} años")
        print(f"Ingresado. Espacio actual en la lista: {len(lista_fallecidos)}/5")
    else:
        print("Error: Edad menor a los 3 años.")

print("Horno lleno. Personas ingresadas:")
for persona in lista_fallecidos:
    print(f"- {persona}")