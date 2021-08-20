import math
def main():
    #escribe tu código abajo de esta línea
    pass
    r = float(input('Dame el valor del radio: '))

    a = (4 * math.pi * r ** 2)
    v = ((4 * math.pi * r ** 3) / 3)

    print('Area: '+str(a))
    print('Volumen: '+str(v))

if __name__=='__main__':
    main()
