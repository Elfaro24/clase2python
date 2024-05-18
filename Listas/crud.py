

animales = ["perro","gato","leon","jirafa"]

running = True

while running:

    print("mi zoologico \n")
    print("Opciones: ")
    opciones = int(input("Ingresa una opcion \n1: Agregar\n2: Mostrar\n3: Eliminar por indice \n4: Eliminar por nombre \n5: Salir"))

    if opciones==1:
        animal = input("Ingrese un animal: ")
        animales.append(animal)
    
    if opciones==2:
        print(animales)
    
    if opciones==3:
        eliminar_index=int(input("Ingrese indice"))
        animales.pop(eliminar_index)

    if opciones==4:
        elimina_palabra = input("Ingrese animal a eliminar: ")
        animales.remove(elimina_palabra)

    if opciones==5:
        running = False