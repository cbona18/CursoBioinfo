import sys
import numpy as np
import matplotlib.pyplot

def main_orig():
    script = sys.argv[0]
    filename = sys.argv[1]
    #filename = "data/inflammation-01.csv"
    data = numpy.loadtxt(filename, delimiter=',')
    for row_mean in numpy.mean(data, axis=1):
        print(row_mean)

def main():
    filename = "data/inflammation-01.csv"
    data = np.loadtxt(filename, delimiter=',')
    imprimir_data(data)
    suma_todos_los_valores_por_dia_de_todos_los_pacientes(data)
    suma_todos_los_valores_por_paciente(data)
    media_todos_los_valores_por_dia_de_todos_los_pacientes(data)
    media_todos_los_valores_por_paciente(data)
    maximo_valor_todos_los_valores_por_dia_de_todos_los_pacientes(data)
    minimo_valor_todos_los_valores_por_paciente(data)


def suma_todos_los_valores_por_dia_de_todos_los_pacientes(data):
    suma=np.sum(data, axis=0)
    print("\nSuma todos los valores por día de todos los pacientes:\n"+str(suma))
    sumplot=matplotlib.pyplot.plot(suma)
    matplotlib.pyplot.show()

def suma_todos_los_valores_por_paciente(data):
    suma=np.sum(data, axis=1)
    print("\nSuma todos los valores por paciente:\n"+str(suma))
    sumplot=matplotlib.pyplot.plot(suma)
    matplotlib.pyplot.show()

def media_todos_los_valores_por_dia_de_todos_los_pacientes(data):
    mean=np.mean(data, axis=0)
    print(mean)
    print("\nMedia todos los valores por día de todos los pacientes:\n"+str(mean))
    sumplot=matplotlib.pyplot.plot(mean)
    matplotlib.pyplot.show()
 
def media_todos_los_valores_por_paciente(data):
    mean=np.mean(data, axis=1)
    print(mean)
    print("\nMedia todos los valores por paciente:\n"+str(mean))
    sumplot=matplotlib.pyplot.plot(mean)
    matplotlib.pyplot.show()

def imprimir_data(data):
    imprimir_tabla(data.tolist())  # Convertir el arreglo a una lista de listas

def maximo_valor_todos_los_valores_por_dia_de_todos_los_pacientes(data):
    maximo_valor=np.amax(data, axis=0)
    print("\nMáximo valor de todos los valores por día de todos los pacientes:\n"+str(maximo_valor))
    sumplot=matplotlib.pyplot.plot(maximo_valor)
    matplotlib.pyplot.show()

def minimo_valor_todos_los_valores_por_paciente(data):
    minimo_valor=np.amin(data, axis=1)
    print("\nMínimo valor de todos los valores por paciente:\n"+str(minimo_valor))
    sumplot=matplotlib.pyplot.plot(minimo_valor)
    matplotlib.pyplot.show()


def imprimir_tabla(arreglo):
    if not arreglo:
        print("El arreglo está vacío")
        return
    print("***************\nTabla original:\n****************")
    # Obtener la longitud de la lista más larga para determinar el ancho de cada columna
    anchos = [max(len(str(elemento)) for elemento in columna) for columna in zip(*arreglo)]

    # Imprimir encabezado
    separadores = ['-' * ancho for ancho in anchos]
    encabezado = '|'.join(f'{elemento:^{ancho}}' for elemento, ancho in zip(arreglo[0], anchos))
    print(encabezado)
    print('|'.join(separadores))

    # Imprimir filas
    for fila in arreglo[1:]:
        fila_formateada = '|'.join(f'{elemento:<{ancho}}' for elemento, ancho in zip(fila, anchos))
        print(fila_formateada)


if __name__ == "__main__":
    main()
       
