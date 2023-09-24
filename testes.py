import seed, iterativo, recursivo
import time

def testes_iterativos():
    inicio_tempo = time.perf_counter()
    for _ in range(n_execucoes):
        iterativo.contador_iterativo(V)
    fim_tempo = time.perf_counter()
    delta_tempo = fim_tempo - inicio_tempo
    print(f'Total iterativo: {delta_tempo:.6f} segundos |'
            + f' Media iterativo: {delta_tempo/n_execucoes:.10f} segundos')

def testes_recursivos():
    inicio_tempo = time.perf_counter()
    for _ in range(n_execucoes):
        recursivo.contador_recursivo(V)
    fim_tempo = time.perf_counter()
    delta_tempo = fim_tempo - inicio_tempo

    print(f'Total recursivo: {delta_tempo:.6f} segundos | ' + 
            f'Media recursivo: {delta_tempo/n_execucoes:.10f} segundos')
    
if __name__ == '__main__':
    n_execucoes = 250
    V = seed.V
    testes_recursivos()
    testes_iterativos() 
    
