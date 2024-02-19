def listaOrdenada(listaOrden):
    numero = len(listaOrden)
    for i in range(numero):
        for j in range(0,numero-i-1):
            if listaOrden[j] > listaOrden[j+1]:
                listaOrden[j], listaOrden[j+1] = listaOrden[j+1], listaOrden[j]
    return listaOrden


def mostrarlistaOrden():
    listaOrden = [8, 3, 1, 19, 14]
    return listaOrdenada(listaOrden)
if __name__ == "__main__":

    listas = mostrarlistaOrden()
    print("La lista ordenada: ", listas)