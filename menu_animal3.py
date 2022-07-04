import animales
menu = {
    '1':'1. Loro',
    '2':'2. Serpiente',
    '0':'0. Exit',
}
class Animal():
    def __init__(self, type):
        self.type = type

    def mostrar_animal(self):
        animal_art = getattr(animales, self.type) #paso dinamicamente diferentes propiedades acorde a lo que el usuario ingrese
        return animal_art

# Ejecución principal 
if __name__ == '__main__':
    for option in menu:    #para imprimir los valores de las llaves, el valor de cada key (un diccionario nos permite esto)
        print(menu.get(option))
  
    while True:
        user_input = input('Ingresa una opcion: ')
        if user_input == '0': #si el usuario me indica el 0 se rompe el loop
            # El usuario quiere dejar de jugar
            break
        elif user_input in menu: #si lo que el usuario coloca esta en el menu me imprima un animal
            # Imprimir animal
            menu_value = menu.get(user_input) #estoy buscando el animal y no el numero de la opcion en el menu
            #print(menu_value.split()) #consiguiendo el valor al numero que el usuario ingreso
            second_value = menu_value.split()[1]
            print(second_value)
            animal = Animal(second_value)
            print(getattr(animales,second_value))
          
        else: #si es distinto de lo que esta en el menu me muestra que es una opcion invalida
            # Opcion invalida
            print('Opcion invalida')
            pass

