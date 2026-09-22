import random

def crearEntrenador(tupla):
    nomEntrenador = input("Ingrese el nombre del entrenador:")
    nomPokemon = input("Ingrese el nombre del pokemon:")
    atkPokemon = random.randint(150, 250)
    hpPokemon = random.randint(500, 900)
    
    NuevoEntrenador = (nomEntrenador, nomPokemon, atkPokemon, hpPokemon)
    
    tupla.append(NuevoEntrenador)
    
def listaEntrenador(tupla):
    for entrenador in range(len(tupla)):
        for pokemon in range(len(tupla) - entrenador - 1):
            if(tupla[pokemon][2] > tupla[pokemon + 1][2]):
                tupla[pokemon], tupla[pokemon + 1] = tupla[pokemon + 1], tupla[pokemon]

    if(len(tupla) == 0):
        print("No hay entrenadores registrados.")
    else:
        print("===== LISTA DE ENTRENADORES =====")
        numero = 1
        for entrenador in tupla:
            print(f"{numero}. Nombre:{entrenador[0]} - Pokemon:{entrenador[1]} - Ataque:{entrenador[2]} - Vida:{entrenador[3]}")
            numero += 1

def borrarPorPokemon(tupla):
    borrarEntrenador = int(input("Ingrese un valor de vida del pokemon: "))
    
    for entrenador in range(len(tupla)):
        minVidaPKM = entrenador
        for pokemon in range(entrenador + 1, len(tupla)):
            if tupla[pokemon][3] < tupla[minVidaPKM][3]:
                minVidaPKM = pokemon

        # Si encontramos un número menor, los intercambiamos afuera del bucle
        if minVidaPKM != entrenador:
            tupla[entrenador], tupla[minVidaPKM] = tupla[minVidaPKM], tupla[entrenador]

    low = 0
    higher = len(tupla) - 1
    idxPokemon = -1
    while(higher - low > 1):
        mid = (higher + low)//2
        if(tupla[mid][3] == borrarEntrenador):
            idxPokemon = mid
        elif(tupla[mid][3] < borrarEntrenador):
            low = mid
        else:
            higher = mid

    if idxPokemon != -1:
        eliminado = tupla.pop(idxPokemon)
        print(f"Se eliminó a {eliminado[0]} y su pokemon {eliminado[1]} (vida: {eliminado[3]}).")
    else:
        print(f"No se encontró ningún pokemon con vida = {borrarEntrenador}.")
        
    
    
def peleaPokemon(lista):
    
    listaEntrenador(lista)

    if len(lista) < 2:
        print("No hay suficientes pokemones para pelear.\n")
        return

        num1 = int(input("Ingrese el número del primer pokemon: "))
    num2 = int(input("Ingrese el número del segundo pokemon: "))

    if (num1 < 1 or num1 > len(lista) or num2 < 1 or num2 > len(lista) or num1 == num2):
        print("Selección inválida.\n")
        return

    idx1 = num1 - 1
    idx2 = num2 - 1

    # Ordenamos los índices de mayor a menor (método de burbuja) para poder
    # eliminar ambos después sin que la lista se desfase al hacer pop()
    indiceMayor, indiceMenor = idx1, idx2
    if indiceMenor > indiceMayor:
        indiceMayor, indiceMenor = indiceMenor, indiceMayor

    entrenador1, pokemon1, ataque1, vida1 = lista[idx1]
    entrenador2, pokemon2, ataque2, vida2 = lista[idx2]

    multiplicador1 = random.randint(0, 5)
    multiplicador2 = random.randint(0, 5)

    danio1 = ataque1 * multiplicador1  # daño que pokemon1 hace a pokemon2
    danio2 = ataque2 * multiplicador2  # daño que pokemon2 hace a pokemon1

    vidaFinal1 = vida1 - danio2
    vidaFinal2 = vida2 - danio1

    print(f"\n⚔  ¡COMBATE! {pokemon1} ({entrenador1}) VS {pokemon2} ({entrenador2})")
    print(f"{pokemon1} ataca: {ataque1} x {multiplicador1} = {danio1} de daño a {pokemon2}")
    print(f"{pokemon2} ataca: {ataque2} x {multiplicador2} = {danio2} de daño a {pokemon1}")
    print(f"Vida restante de {pokemon1}: {max(vidaFinal1, 0)}")
    print(f"Vida restante de {pokemon2}: {max(vidaFinal2, 0)}")

    if vidaFinal1 <= 0 and vidaFinal2 <= 0:
        print(f"\n ¡Ambos pokemones quedaron sin vida! "
              f"{entrenador1} y {entrenador2} son eliminados.\n")
        lista.pop(indiceMayor)
        lista.pop(indiceMenor)
    elif vidaFinal1 == vidaFinal2:
        print(f"\n ¡Empate! Ambos entrenadores pierden y son eliminados.\n")
        lista.pop(indiceMayor)
        lista.pop(indiceMenor)
    elif vidaFinal1 > vidaFinal2:
        print(f"\n ¡Ganador: {entrenador1} con su pokemon {pokemon1}!\n")
        lista.pop(idx2)
    else:
        print(f"\n ¡Ganador: {entrenador2} con su pokemon {pokemon2}!\n")
        lista.pop(idx1)


def mostrarMenu():
    print("\n===== MENÚ POKEMON =====")
    print("1. Crear Entrenador")
    print("2. Listar Entrenadores")
    print("3. Borrar por Pokemon")
    print("4. Pelea Pokemon")
    print("5. Fin")
 
 
def main():
    entrenadores = []  # Lista de tuplas: (entrenador, pokemon, ataque, vida)
 
    while True:
        mostrarMenu()
        opcion = input("Seleccione una opción: ").strip()
 
        if opcion == "1":
            crearEntrenador(entrenadores)
        elif opcion == "2":
            listaEntrenador(entrenadores)
        elif opcion == "3":
            borrarPorPokemon(entrenadores)
        elif opcion == "4":
            peleaPokemon(entrenadores)
        elif opcion == "5":
            print("\n¡Gracias por jugar! Hasta pronto.\n")
            break
        else:
            print("\nOpción inválida, intente nuevamente.\n")
 
 
if __name__ == "__main__":
    main()

