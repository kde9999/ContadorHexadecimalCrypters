import time
import os
import binascii

VolcadoBinario=''
def VectorizarBinario():
    VolcadoBinario=open('C:\Users\Thanos\Documents\GitHub\VectorBinario\jbb66.exe',"rb")
    ruta= 'C:\Users\Thanos\Documents\GitHub\VectorBinario\jbb66.exe'
    tamano= os.path.getsize(ruta)
    time.sleep(5)
    byte=VolcadoBinario.read(tamano)
    posicion=VolcadoBinario.seek(1,1)
    datos=binascii.b2a_hex (byte)
    archi=open('Vector.txt','a')
    archi.write(datos)
    archi.close()

def ContadorCaracteres():
    a=0
    b=0
    c=0
    d=0
    e=0
    f=0
    cero=0
    uno=0
    dos=0
    tres=0
    cuatro=0
    cinco=0
    seis=0
    siete=0
    ocho=0
    nueve=0

    archivoVector=open('Vector.txt','r')
    for line in archivoVector:
        for caracter in line:
            # print(caracter)
            if caracter=="a":
                a=a+1
            if caracter=="b":
                b=b+1
            if caracter=="c":
                c=c+1
            if caracter=="d":
                d=d+1
            if caracter=="e":
                e=e+1
            if caracter=="f":
                f=f+1
            if caracter=="0":
                cero=cero+1
            if caracter=="1":
                uno=uno+1
            if caracter=="2":
                dos=dos+1
            if caracter=="3":
                tres=tres+1
            if caracter=="4":
                cuatro=cuatro+1
            if caracter=="5":
                cinco=cinco+1
            if caracter=="6":
                seis=seis+1
            if caracter=="7":
                siete=siete+1
            if caracter=="8":
                ocho=ocho+1
            if caracter=="9":
                nueve=nueve+1




    archivoVector.close()
    archivoContador=open('Contador.txt','a')
    archivoContador.write('La cantidad de A es: '+ str(a)+'\n')
    archivoContador.write('La cantidad de B es: '+ str(b)+'\n')
    archivoContador.write('La cantidad de C es: '+ str(c)+'\n')
    archivoContador.write('La cantidad de D es: '+ str(d)+'\n')
    archivoContador.write('La cantidad de E es: '+ str(e)+'\n')
    archivoContador.write('La cantidad de F es: '+ str(f)+'\n')
    archivoContador.write('La cantidad de 0 es: '+ str(cero)+'\n')
    archivoContador.write('La cantidad de 1 es: '+ str(uno)+'\n')
    archivoContador.write('La cantidad de 2 es: '+ str(dos)+'\n')
    archivoContador.write('La cantidad de 3 es: '+ str(tres)+'\n')
    archivoContador.write('La cantidad de 4 es: '+ str(cuatro)+'\n')
    archivoContador.write('La cantidad de 5 es: '+ str(cinco)+'\n')
    archivoContador.write('La cantidad de 6 es: '+ str(seis)+'\n')
    archivoContador.write('La cantidad de 7 es: '+ str(siete)+'\n')
    archivoContador.write('La cantidad de 8 es: '+ str(ocho)+'\n')
    archivoContador.write('La cantidad de 9 es: '+ str(nueve)+'\n')



    print a
    print b
    print c
    print d
    print e
    print f
    print cero
    print uno
    print dos
    print tres
    print cuatro
    print cinco
    print seis
    print siete
    print ocho
    print nueve


VectorizarBinario()
ContadorCaracteres()
