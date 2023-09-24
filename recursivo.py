import seed

def contador_recursivo(lista):    
    if not lista:
        return 0    
    if lista[0] == 'D':
        return 1 + contador_recursivo(lista[1:])
    return contador_recursivo(lista[1:])

def recursividade(V):
    print(V)
    print('D ocorre', contador_recursivo(V), 'vezes na lista V.')

if __name__ == '__main__':
    recursividade(seed.V)

