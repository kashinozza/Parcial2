from pokemon import pokedex
from tree import BinaryTree
from typing import Any
from collections import Counter

class Pokedex(BinaryTree):
    #2
    def proximity_search_pokemon(self, value: Any) :
            def __search(root, value):
                if root is not None:
                    if value.lower() in root.value.lower():
                        print(root.other_values)
        
                    __search(root.left, value)
            
                    __search(root.right, value)

            aux = None
            if self.root is not None:
                aux = __search(self.root, value)
            return aux
    
    def buscar_datos(self, nombre):
        nodo = self.search(nombre)
        if nodo is not None:
            print(nodo.other_values)
        else:
            print('pokemon no encontrado')

    #3
def busqueda_tipo(self, nombre):
    pokemon_tipo = []

    def __busqueda_tipo(root, nombre):
        if root is not None:
            __busqueda_tipo(root.left, nombre)
            tipo = root.value
            if nombre.lower() in tipo.lower():
                pokemon_encontrado = root.other_values['nombre']
                pokemon_tipo.append(pokemon_encontrado)

            __busqueda_tipo(root.right, nombre)
    __busqueda_tipo(self.root, nombre)
    if len(pokemon_tipo) >= 1:
        return pokemon_tipo
    else:
        return f'No se ha encontrado ningún Pokémon del tipo {nombre}'
        
    #5
def busqueda_debilidad(self, nombre):
    pokemon_debiles = []
    pokemon = self.search(nombre)
    if pokemon is None:
        return f'No se ha encontrado el Pokémon {nombre}'
    oponente = pokemon.other_values['tipos']

    def __busqueda_debilidad(root, oponente):
        if root is not None:
            __busqueda_debilidad(root.left, oponente)

            debil = root.other_values['debilidades']

            for tiposoponente in oponente:
                if tiposoponente in debil:
                    pokemon_encontrado = root.value
                    if pokemon_encontrado not in pokemon_debiles:
                        pokemon_debiles.append(pokemon_encontrado)

                    break
            __busqueda_debilidad(root.right, oponente)
    __busqueda_debilidad(self.root, oponente)

    if len(pokemon_debiles) >= 1:
        return pokemon_debiles
    else:
        return f'No se ha encontrado ningún Pokémon débil frente a {nombre}'
  
    #6
def cantidad_tipos(self):
        tipos = []
        count = Counter()
        def __cantidad_tipos(root):
            if root is not None:
                __cantidad_tipos(root.left)
                pokemon_tipo = root.value
                for valor in pokemon_tipo:
                         count[valor]+=1
                         if not valor in tipos:
                            tipos.append(valor)
                    
                __cantidad_tipos(root.right)
        __cantidad_tipos(self.root)
        for valor in tipos:
            print(f'tipo {valor} : {count[valor]}')

    #7-8
def busqueda_info(self, nombre):
    pokemon_info = []

    def __busqueda_tipo(root, nombre):
        if root is not None:
            __busqueda_tipo(root.left, nombre)

            tipo = root.other_values[nombre]

            if tipo == True:
                pokemon_encontrado = root.other_values['nombre']
                pokemon_info.append(pokemon_encontrado)

            __busqueda_tipo(root.right, nombre)

    __busqueda_tipo(self.root, nombre)

    return len(pokemon_info)
        

         
            
                    


#1
nombre_pokedex = Pokedex()
numero_pokedex = Pokedex()
tipo_pokedex = Pokedex()

for pokemon in pokedex:
    nombre_pokedex.insert(pokemon['nombre'], pokemon)
    numero_pokedex.insert(pokemon['numero'], pokemon)
    tipo_pokedex.insert(pokemon['tipos'], pokemon)

#2
nombre_pokedex.proximity_search_pokemon('jol')
print()
numero_pokedex.buscar_datos(745)
print()

#3

info = tipo_pokedex.busqueda_tipo('fantasma')
print(f'pokemon tipo fantasma: {info}')

info = tipo_pokedex.busqueda_tipo('fuego')
print(f'pokemon tipo fuego: {info}')

info = tipo_pokedex.busqueda_tipo('acero')
print(f'pokemon tipo acero: {info}')

info = tipo_pokedex.busqueda_tipo('electrico')
print(f'pokemon tipo electrico: {info}')

#4
print()
print('orden por número')
numero_pokedex.in_order()
print()
print('orden por nombre')
nombre_pokedex.in_order()
print()
print('orden por nivel por nombre:')
nombre_pokedex.by_level()
print()

#5
info =nombre_pokedex.busqueda_debilidad('jolteon')
print(f'pokemon debiles ante jolteon:{info}')

info =nombre_pokedex.busqueda_debilidad('lycanroc')
print(f'pokemon debiles ante lycanroc:{info}')

info =nombre_pokedex.busqueda_debilidad('tyrantrum')
print(f'pokemon debiles ante tyrantrum:{info}')

#6
tipo_pokedex.cantidad_tipos()
print()

#7
info = nombre_pokedex.busqueda_info('megaevolucion')
print(f'pokemon con megaevolución: {info}')
#8
info = nombre_pokedex.busqueda_info('gigamax')
print(f'pokemon con gigamax: {info}')






