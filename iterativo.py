import seed

def contador_iterativo(V):  
    contagem_valor_D = 0
    for valor in V:
        if valor == 'D':
            contagem_valor_D += 1
        
    return contagem_valor_D;

if __name__ == '__main__':
    V = seed.V; print(V)
    print(contador_iterativo(V))

