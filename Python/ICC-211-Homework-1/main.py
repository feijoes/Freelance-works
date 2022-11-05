

## 2 Máximo Producto Dos Números

def max_pair_product(dataset):
    index = 0
    for i,data in enumerate(dataset):
        if dataset[index] < data:
          index = i 
    temp = dataset[-1]
    dataset[-1] = dataset[index]
    dataset[index] = temp   
    index = 0
    for i, data in enumerate(dataset[:-1]):
    	if dataset[index] < data:
    		index = i
    
    temp = dataset[-2]
    dataset[-2] = dataset[index]
    dataset[index] = temp   
    return dataset[-1] * dataset[-2]

print(max_pair_product([1,2,3,4,5,6]))
print(max_pair_product([4,2,5,1]))

## 3  Índice de Elemento en Arreglo (Permutación)

## 4. Algoritmo de Ordenamiento
def swapSort(L):
    print("Original L: ", L)
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if L[j] < L[i]:
                L[j], L[i] = L[i], L[j]
 	
    print("Final L: ", L)	
"""   
1. ¿Este algoritmo ordena la lista en orden ascendente o descendente?
	a. Ascendente.
2. ¿Cuál es el peor caso de complejidad de este algoritmo?
a. O(n2)
b. O(n)
c. O(n lg n)
d. O(1)
3. ¿Cuál es el mejor caso de complejidad de este algoritmo?
a. O(n2)
b. O(n)
c. O(n lg n)
d. O(1)
""" 
def modSwapSort(L):
    """ L is a list on integers """
    print("Original L: ", L)
    for i in range(len(L)):
       for j in range(len(L)):
           if L[j] < L[i]:
                L[j], L[i] = L[i], L[j]
    print("Final L: ", L)
"""
4. ¿Qué pasa con el comportamiento del algoritmo con este nuevo código?
	b. El algoritmo ahora ordena la lista en orden descendente.
"""