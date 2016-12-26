def VectorizarBinario():
    VolcadoBinario=open('',"rb")
    ruta= ''
    tamano= os.path.getsize(ruta)
    byte=VolcadoBinario.read(tamano)
    posicion=VolcadoBinario.seek(1,1)
    datos=binascii.b2a_hex (byte)
    archi=open('Vector.txt','a')
    archi.write('Vector: '+ datos)
    archi.close()
