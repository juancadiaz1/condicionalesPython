
def calcularDescuento(precio, dia):

    precioTotal = 0

    if (dia) == 'l':
        precioTotal = precio - (precio * 0.10)


    print("El precio final de su compra es de: ", precioTotal)
    return precioTotal

def main():

    precio=int(input("Ingrese el precio del producto: "))
    dia=input("Ingrese el dia de la semana: Lunes(l), Martes(m), Miercoles(M), Jueves(j), Viernes(v), Sabado(s), Domingo(d)  ")

    calcularDescuento(precio, dia)

if __name__ == '__main__':
    main()

